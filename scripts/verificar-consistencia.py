#!/usr/bin/env python3
"""Verifica a consistência interna da especificação do processo.

Roda no pipeline antes do build. Falha (código 1) se encontrar:
- atividade sem algum dos campos obrigatórios
- atividade sem exatamente um papel com A (responde)
- artefato do catálogo sem atividade que o produza ou sem template
- problema do diagnóstico sem nenhuma atividade que o atenda
- atividade no catálogo que não está especificada, ou o contrário
- checklist citado que não existe

Uso: python3 scripts/verificar-consistencia.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "docs" / "04-Especificacao-do-Processo"
CAMPOS = [
    "Propósito", "Categorias", "Gatilho", "Entradas", "Saídas", "Papéis",
    "Ferramentas", "Instrumento de apoio", "Critério de conclusão", "Problemas atendidos",
]
ARTEFATOS = [f"A{i:02d}" for i in range(1, 19)]
PROBLEMAS = [f"P{i:02d}" for i in range(1, 12)]

erros: list[str] = []


def campo(secao: str, nome: str) -> str | None:
    m = re.search(rf"^\| {re.escape(nome)} \| (.+) \|$", secao, re.M)
    return m.group(1) if m else None


def papeis_com_a(texto: str) -> list[str]:
    texto = texto.split(". ")[0]
    responsaveis = []
    for trecho in texto.split(", "):
        m = re.match(r"^((?:[RACI](?: e )?)+)\s+(.+)$", trecho.strip())
        if m and "A" in m.group(1).split():
            responsaveis += re.split(r"\s+e\s+", m.group(2).strip())
    return responsaveis


def main():
    atividades: dict[str, str] = {}
    for pagina in sorted((SPEC / "Atividades").glob("*.md")):
        if pagina.name == "index.md":
            continue
        for secao in re.split(r"^## ", pagina.read_text(encoding="utf-8"), flags=re.M)[1:]:
            titulo = secao.split("\n", 1)[0]
            if re.match(r"AT\d{2} ", titulo):
                atividades[titulo[:4]] = secao

    produzidos: set[str] = set()
    atendidos: set[str] = set()
    for at, secao in sorted(atividades.items()):
        for nome in CAMPOS:
            if campo(secao, nome) is None:
                erros.append(f"{at}: campo '{nome}' ausente")
        papeis = campo(secao, "Papéis") or ""
        resp = papeis_com_a(papeis)
        if len(resp) != 1:
            erros.append(f"{at}: deveria ter exatamente um A, encontrado {resp or 'nenhum'} em '{papeis}'")
        produzidos |= set(re.findall(r"A\d{2}", campo(secao, "Saídas") or ""))
        atendidos |= set(re.findall(r"P\d{2}", campo(secao, "Problemas atendidos") or ""))
        if "### Passos" not in secao:
            erros.append(f"{at}: sem passos")

    templates = (SPEC / "Templates.md").read_text(encoding="utf-8")
    for a in ARTEFATOS:
        if a not in produzidos:
            erros.append(f"{a}: nenhuma atividade o produz")
        if not re.search(rf"^## {a} ", templates, re.M):
            erros.append(f"{a}: sem template")
    for p in PROBLEMAS:
        if p not in atendidos:
            erros.append(f"{p}: nenhuma atividade o atende")

    catalogo = set(re.findall(r"^\| (AT\d{2}) \|", (SPEC / "Atividades" / "index.md").read_text(encoding="utf-8"), re.M))
    for at in sorted(catalogo ^ set(atividades)):
        erros.append(f"{at}: presente só no catálogo ou só nas páginas de fase")

    checklists = (SPEC / "Checklists.md").read_text(encoding="utf-8")
    existentes = set(re.findall(r"^## (CL\d{2}) ", checklists, re.M))
    citados = set()
    for pagina in SPEC.rglob("*.md"):
        citados |= set(re.findall(r"\bCL\d{2}\b", pagina.read_text(encoding="utf-8")))
    for cl in sorted(citados - existentes):
        erros.append(f"{cl}: citado mas não definido em Checklists")

    print(f"{len(atividades)} atividades, {len(ARTEFATOS)} artefatos, {len(PROBLEMAS)} problemas, {len(existentes)} checklists verificados")
    if erros:
        print("\nInconsistências encontradas:")
        for e in erros:
            print(f"  - {e}")
        sys.exit(1)
    print("Nenhuma inconsistência encontrada")


if __name__ == "__main__":
    main()
