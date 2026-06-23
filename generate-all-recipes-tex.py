from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path


def find_recipe_pdf(recipe_dir: Path) -> Path | None:
    pdf_files = sorted(recipe_dir.glob("*.pdf"), key=lambda p: p.name.lower())
    if not pdf_files:
        return None

    exact_match = next((p for p in pdf_files if p.stem == recipe_dir.name), None)
    return exact_match or pdf_files[0]


def find_recipes(search_dir: Path) -> list[Path]:
    recipes: list[Path] = []
    for entry in sorted(search_dir.iterdir(), key=lambda p: p.name.lower()):
        if (
            not entry.is_dir()
            or entry.name.startswith('.')
            or entry.name.lower() == "archive"
        ):
            continue

        recipe_pdf = find_recipe_pdf(entry)
        if recipe_pdf is not None:
            recipes.append(recipe_pdf)

    return recipes


def build_tex(recipe_pdfs: list[Path], output_path: Path) -> str:
    lines = [
        r"\documentclass{article}",
        r"\usepackage{pdfpages}",
        r"\usepackage[paperwidth=8.5in, paperheight=11in, margin=0in]{geometry}",
        r"\begin{document}",
    ]

    for pdf_path in recipe_pdfs:
        relative_path = pdf_path.relative_to(output_path.parent).as_posix()
        lines.append(f"\\includepdf[pages=-]{{{relative_path}}}")

    lines.append(r"\end{document}")
    return "\n".join(lines) + "\n"


def main() -> None:
    script_dir = Path(__file__).resolve().parent

    parser = ArgumentParser(
        description="Generate all-recipes.tex from recipe folders containing PDF files."
    )
    parser.add_argument(
        "--root",
        help="Directory containing recipe folders. Defaults to the script directory.",
        default=None,
    )
    parser.add_argument(
        "--parent",
        action="store_true",
        help="Search the parent directory of the script instead of the script directory.",
    )
    parser.add_argument(
        "--output",
        help="Output TeX filename.",
        default=str(script_dir / "all-recipes.tex"),
    )

    args = parser.parse_args()
    search_dir = Path(args.root).expanduser().resolve() if args.root else (script_dir.parent if args.parent else script_dir)
    output_path = Path(args.output).expanduser().resolve()

    if not search_dir.exists() or not search_dir.is_dir():
        raise SystemExit(f"Recipe directory not found: {search_dir}")

    recipe_pdfs = find_recipes(search_dir)
    if not recipe_pdfs:
        raise SystemExit(f"No recipe PDFs found in: {search_dir}")

    output_path.write_text(build_tex(recipe_pdfs, output_path), encoding="utf-8")
    print(f"Wrote {output_path} with {len(recipe_pdfs)} recipes from {search_dir}")


if __name__ == "__main__":
    main()
