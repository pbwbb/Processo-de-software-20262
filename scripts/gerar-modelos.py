#!/usr/bin/env python3
"""Gera static/modelos/modelos-pvd.zip a partir da página de Templates.

Cada seção "## Axx Nome" da página vira um arquivo Markdown no pacote, com o
cabeçalho comum já expandido. Roda automaticamente antes do build (prebuild).
"""
import re
import unicodedata
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "docs" / "04-Especificacao-do-Processo" / "Templates.md"
OUT = ROOT / "static" / "modelos" / "modelos-pvd.zip"


def slug(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main():
    text = PAGE.read_text(encoding="utf-8")
    header = re.search(r"## Cabeçalho comum.*?```markdown\n(.*?)```", text, re.S).group(1).strip()
    # Divide a página nas seções de nível 2, ignorando "## " dentro de blocos de código
    sections, current, in_code = [], None, False
    for line in text.split("\n"):
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and line.startswith("## "):
            m = re.match(r"## (A\d{2}) (.+)", line)
            current = [m.group(1), m.group(2).strip(), ""] if m else None
            if current:
                sections.append(current)
            continue
        if current:
            current[2] += line + "\n"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for art_id, name, body in sections:
            block = re.search(r"```markdown\n(.*?)```", body, re.S)
            if not block:
                continue
            content = block.group(1).replace("<cabeçalho comum>", header)
            z.writestr(f"{art_id}-{slug(name)}.md", content)
    print(f"{len(sections)} modelos em {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
