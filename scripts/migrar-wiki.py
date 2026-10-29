#!/usr/bin/env python3
"""Converte a Wiki do Azure DevOps (pasta `documentacao/`) em páginas do Docusaurus.

Uso:
    python3 scripts/migrar-wiki.py <pasta-da-wiki> docs

O que a conversão faz:
- Proposta-de-Processo/<Secao>.md vira docs/<Secao>/index.md (página de abertura da categoria)
- A ordem das páginas vem dos arquivos .order da Wiki (sidebar_position)
- Blocos `::: mermaid ... :::` viram blocos ```mermaid
- Links absolutos da Wiki (/Proposta-de-Processo/...) viram links relativos para os .md
- Readme.md vira a página inicial (docs/index.md), com os integrantes da página Processo-de-Software
"""
import json
import os
import re
import sys
from pathlib import Path

WIKI_PREFIX = "/Proposta-de-Processo"


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8").replace("\r\n", "\n")


def read_order(folder: Path) -> list[str]:
    f = folder / ".order"
    if not f.exists():
        return []
    return [l.strip() for l in read(f).splitlines() if l.strip()]


def convert_mermaid(text: str) -> str:
    out, in_block = [], False
    for line in text.split("\n"):
        s = line.strip()
        if not in_block and re.fullmatch(r":::\s*mermaid", s):
            out.append("```mermaid")
            in_block = True
        elif in_block and s == ":::":
            out.append("```")
            in_block = False
        else:
            out.append(line)
    return "\n".join(out)


def first_h1(text: str) -> str | None:
    m = re.search(r"^# (.+)$", text, re.M)
    return m.group(1).strip() if m else None


class Migrator:
    def __init__(self, src: Path, dst: Path):
        self.src = src
        self.dst = dst
        self.base = src / "Proposta-de-Processo"
        # caminho da Wiki (sem prefixo) -> arquivo de destino
        self.targets: dict[str, Path] = {}
        self._index_targets()

    def _index_targets(self):
        for md in self.base.rglob("*.md"):
            rel = md.relative_to(self.base).with_suffix("")
            wiki_path = "/" + rel.as_posix()
            folder = md.with_suffix("")
            if folder.is_dir():
                target = self.dst / rel / "index.md"
            else:
                target = self.dst / rel.with_suffix(".md")
            self.targets[wiki_path] = target

    def fix_links(self, text: str, current: Path) -> str:
        def repl(m):
            label, url = m.group(1), m.group(2)
            if not url.startswith(WIKI_PREFIX):
                return m.group(0)
            path, _, anchor = url[len(WIKI_PREFIX):].partition("#")
            target = self.targets.get(path.rstrip("/"))
            if target is None:
                print(f"  aviso: link sem destino em {current.name}: {url}")
                return m.group(0)
            rel = os.path.relpath(target, current.parent).replace(os.sep, "/")
            if not rel.startswith("."):
                rel = "./" + rel
            return f"[{label}]({rel}{'#' + anchor if anchor else ''})"

        return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", repl, text)

    def write_page(self, src_md: Path, target: Path, position: int | None):
        text = convert_mermaid(read(src_md))
        text = self.fix_links(text, target)
        fm = ["---"]
        if position is not None:
            fm.append(f"sidebar_position: {position}")
        fm.append("---\n")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("\n".join(fm) + "\n" + text.strip() + "\n", encoding="utf-8")

    def walk(self, folder: Path):
        order = read_order(folder)
        names = {p.stem for p in folder.glob("*.md")}
        ordered = [n for n in order if n in names] + sorted(names - set(order))
        for pos, name in enumerate(ordered, start=1):
            md = folder / f"{name}.md"
            rel = md.relative_to(self.base).with_suffix("")
            target = self.targets["/" + rel.as_posix()]
            sub = folder / name
            if sub.is_dir():
                label = first_h1(read(md)) or name
                cat = self.dst / rel / "_category_.json"
                cat.parent.mkdir(parents=True, exist_ok=True)
                cat.write_text(json.dumps({"label": label, "position": pos}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                self.write_page(md, target, None)
                self.walk(sub)
            else:
                self.write_page(md, target, pos)

    def home(self):
        readme = convert_mermaid(read(self.src / "Readme.md"))
        readme = self.fix_links(readme, self.dst / "index.md")
        readme = readme.replace("Como esta Wiki está organizada", "Como este portal está organizado")
        equipe = ""
        pds = self.src / "Processo-de-Software.md"
        if pds.exists():
            t = read(pds)
            disc = re.search(r"^Ambiente para.*$", t, re.M)
            integ = re.search(r"\*\*Integrantes:\*\*\s*(.+?)\s*$", t, re.M)
            prof = re.search(r"\*\*Professor:\*\*\s*(.+?)\s*$", t, re.M)
            linhas = ["\n## Equipe\n"]
            if disc:
                linhas.append(disc.group(0) + "\n")
            if integ:
                nomes = re.sub(r"[¹²³]", "", integ.group(1)).strip()
                linhas.append(f"- **Integrantes:** {nomes}")
            if prof:
                linhas.append(f"- **Professor:** {prof.group(1).strip()}")
            equipe = "\n".join(linhas) + "\n"
        body = readme.strip() + "\n" + equipe
        fm = "---\nslug: /\nsidebar_position: 0\nsidebar_label: Início\n---\n\n"
        (self.dst / "index.md").write_text(fm + body, encoding="utf-8")


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, dst = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    dst.mkdir(parents=True, exist_ok=True)
    m = Migrator(src, dst)
    m.home()
    m.walk(m.base)
    print(f"{len(list(dst.rglob('*.md')))} páginas geradas em {dst}")


if __name__ == "__main__":
    main()
