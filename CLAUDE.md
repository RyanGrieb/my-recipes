# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repo is

A personal recipe collection. Each recipe is a standalone LaTeX document that compiles to a
1–2 page PDF meant to be printed or read on a phone while cooking. Every recipe shares one
preamble, so all PDFs look identical: same font, margins, bullets, and title treatment.

**The goal of this file is consistency.** A new recipe should be indistinguishable in layout
and voice from the existing sixteen.

## Layout

```
Recipe Name/
  Recipe Name.tex     <- the source (tracked)
  Recipe Name.pdf     <- the compiled output (tracked, committed alongside the .tex)
preamble.tex          <- shared styling; every recipe \input's it
all-recipes.tex       <- GENERATED, gitignored. Never hand-edit.
generate-all-recipes-tex.py
README.md
Archive/              <- legacy .docx/.pdf originals; do not add to it
```

Folder name, `.tex` basename, and `.pdf` basename must all be identical. The build script and
`generate-all-recipes-tex.py` both rely on this.

Recipe folders are also PDF-tracked: a recipe commit contains exactly two files, the `.tex`
and the `.pdf`. Build artifacts (`.aux`, `.log`, `.fls`, `.fdb_latexmk`, `.synctex.gz`) are
gitignored — never stage them.

## Adding a new recipe

1. Create `Recipe Name/Recipe Name.tex` from the template below.
2. Compile it: `cd "Recipe Name" && pdflatex "Recipe Name.tex"`.
3. Check the PDF is 1–2 pages and nothing overflows.
4. Add the recipe to the correct category list in `README.md` (Beef / Chicken / Soups, Sides
   & Others), keeping each list alphabetical.
5. Commit the `.tex` and `.pdf` with the message `Add Recipe Name`.

Do not regenerate or commit `all-recipes.tex` — it is gitignored and CI rebuilds it.

## The canonical template

This is the exact shape of the majority of recipes (e.g. `Creamy Tuscan Chicken`,
`Picadillo`, `Vegetable Soup`). Start here.

```latex
% !TEX root = Recipe Name.tex
\input{../preamble.tex}

\begin{document}

% ================= PAGE 1 =================
\makeRecipeTitle{Recipe Name}

\section*{Ingredients}

\begin{itemize}
      \item Ingredient Name – Quantity, prep note
      \item Ingredient Name – Quantity
\end{itemize}

\newpage
\makeRecipeTitle{Recipe Name}
\section*{Instructions}

\begin{enumerate}

      \item \textbf{Step Title} \\
            One to three sentences describing the step.

      \item \textbf{Step Title} \\
            One to three sentences describing the step.

\end{enumerate}

\end{document}
```

Fixed points, do not vary:

- `\input{../preamble.tex}` — never a `\documentclass`, never `\usepackage` in a recipe file.
  All styling lives in `preamble.tex`. If a recipe needs a package, add it to the preamble.
- The `% !TEX root =` line matches the file's own name.
- The `% ================= PAGE 1 =================` banner comment above the first title.
- Ingredients always come first; Instructions always start on a fresh `\newpage`.
- `\makeRecipeTitle{...}` is repeated on every page with the same text, so each printed page
  is self-identifying.
- On the instructions page the three lines `\newpage`, `\makeRecipeTitle{...}`,
  `\section*{Instructions}` are consecutive with no blank lines between them.
- A blank line after `\begin{enumerate}`, a blank line between steps, and a blank line before
  `\end{enumerate}`.

## Whitespace

- Indent `\item` by **6 spaces**.
- Indent an instruction's body text by **12 spaces**, aligned under the step title.
- Wrap body text only if it gets unwieldy; continuation lines keep the 12-space indent.
- File ends with `\end{document}` and a trailing newline.

Five older files (`Korean Egg Rice`, `Lemon Pepper Wings`, `Chipotle Meal Prep`,
`Chicken Vegetable Stir-Fry`, plus stray page banners elsewhere) use 4/10-space indents.
That is legacy — use 6/12 for anything new, and do not reflow those files just to match.

## Characters and escapes

| Use | For | Example |
|---|---|---|
| `–` (en dash, U+2013) | the separator between ingredient and quantity | `Kosher Salt – 2 tsp` |
| `--` | numeric ranges in prose | `cook 10--15 minutes`, `3--4 small` |
| `\&` | ampersand anywhere in text | `Deglaze \& Combine` |
| `$^\circ$F` | temperatures | `Cook to 165$^\circ$F` |
| `½` `¼` `¾` | fractions, or plain `1/2` `1/3` | either, but be consistent per file |

`°` typed literally appears once in `Lemon Pepper Wings`; prefer `$^\circ$F`. Accented
characters (`Jalapeño`, `Sauté`) are typed directly — the preamble loads `utf8` inputenc, so
they compile fine.

## Ingredients section

Format each line as `Name – Quantity, prep note`:

```latex
\item Garlic Cloves – 6, minced
\item Yellow Potatoes – 8 ounces (about 3--4 small), diced
\item Chicken Broth – 4 cups (945ml)
\item Salt and Pepper – to taste
```

- Ingredient names in Title Case; prep notes in lowercase after the comma.
- Parentheses hold clarifications, brand hints, or metric equivalents: `– 1 lb (454g)`,
  `– 1 tsp (Kashmiri recommended)`.
- Pick abbreviated units (`tsp`, `tbsp`, `oz`) or spelled-out (`teaspoon`, `tablespoon`) and
  stay with that choice for the whole file.
- Ordering: lead with the star ingredient (the protein), then either alphabetize the rest or
  follow order of use — one or the other, consistently, within a recipe.
- An optional ingredient is marked in place: `– 1, minced (optional)` or
  `\item Thai chili and green beans (optional)`.

### Grouped ingredients

When a recipe has distinct components (marinade / sauce / finish), group them. Use a bold
line followed by its own `itemize` with tightened spacing:

```latex
\textbf{For the Beans}
\begin{itemize}[itemsep=0.1em, label={\raisebox{-0.1ex}{\large\textbullet}}]
      \item Dried Pinto Beans – 1 lb (454g), rinsed and sorted
\end{itemize}

\textbf{Charro Base \& Meats}
\begin{itemize}[itemsep=0.1em, label={\raisebox{-0.1ex}{\large\textbullet}}]
      \item Bacon – 8 oz, diced
\end{itemize}
```

Group headings are short noun phrases: `For the Beans`, `The Sauce`, `Vegetables \& Aromatics`,
`Seasonings \& Finishing`. `Butter Chicken` uses `\subsection*{For the Chicken Marinade:}`
instead — both render similarly, but prefer the bold-line form for new recipes.

## Notes section (optional)

Only when a recipe genuinely needs caveats. It sits on page 1, after Ingredients, before the
`\newpage`. Two established forms:

Footnote-style, keyed from asterisks in the ingredient lines (`Potato Soup`):

```latex
\section*{Notes}

\begin{itemize}
      \item[*] \textbf{Salt:} Start with 1 1/2 teaspoons, then taste and add more if needed.
      \item[**] \textbf{Ancho Chili Powder:} Start with 1/4 teaspoon and taste before adding more.
\end{itemize}
```

Plain topic bullets (`Vegetable Soup`):

```latex
\section*{Notes}

\begin{itemize}
      \item \textbf{Storage:} Leftovers keep for 4--5 days in a tightly sealed container.
\end{itemize}
```

Both lead with a bold topic label ending in a colon.

## Instructions section

```latex
      \item \textbf{Sauté Aromatics} \\
            Add the butter and chopped onion to the pot. Cook over medium heat, stirring
            occasionally, until the onions are tender (3--5 minutes).
```

**Step titles** — bold, Title Case, 2–4 words, no trailing period, followed by ` \\`:

- Prefer an imperative verb phrase naming the action: `Sear Chicken`, `Make the Roux`,
  `Brown the Beef`, `Blend Half the Soup`, `Marinate`, `Serve`.
- A `The ...` noun phrase is the accepted alternative for punchy technique steps:
  `The Sear`, `The Dredge`, `The Flip`, `The Finish`.
- `For the ...` / `To Assemble` is used only for component-based recipes where each step is a
  separate sub-recipe (`Chipotle Meal Prep`).
- Append a duration in parentheses when the step is long or timing-critical:
  `Cook the Beans (1.5--2 hours)`, `Sear the Chicken (5 minutes)`. Optional — most recipes
  omit it; use it throughout a recipe or not at all.
- The last step is almost always `Serve` or `The Finish`.

**Body text** — complete sentences, second person imperative, addressed to the cook:

- State the doneness cue, not just the clock: "until the whites are opaque and nearly set",
  "until the potatoes are tender when pierced with a fork", "until fragrant".
- Times go in parentheses at the end of a clause: `(3--5 minutes)`, `(30 seconds)`.
- Keep it warm but efficient. Occasional enthusiasm is in voice ("Enjoy!", "Try to get a nice
  char on the steak!"); flowery food writing is not.
- Bold inline labels split a step into branches or emphasize a warning:
  `\textbf{Option A (Air Fryer):}`, `\textbf{If using chorizo:}`,
  `\textbf{CRITICAL STEP:}`, `\textbf{Chef's Tip:}`.
- Use `\\` to break a step into paragraphs when it has distinct phases.
- Aim for 4–8 steps.

### Sub-bullets within a step

When a step is a list of discrete actions rather than a paragraph, nest an itemize with dash
labels. Note the step title then has **no** trailing `\\`:

```latex
      \item \textbf{The Dredge}
            \begin{itemize}[label=--]
                  \item In a large bowl, mix the flour, cornstarch, and baking powder.
                  \item Toss the oiled wings in the mixture.
                  \item \textbf{CRITICAL STEP:} Shake the wings to remove excess flour.
            \end{itemize}
```

Use this sparingly — the `\\`-and-paragraph form is the default and is more common.

## Page structure

- **Standard (almost all recipes):** page 1 Ingredients, page 2 Instructions.
- **Long ingredient lists:** continue onto extra pages with
  `\section*{Ingredients (Continued)}` after a `\newpage` and a repeated title, then put
  Instructions last (`Chipotle Meal Prep` is the only example, at 4 pages).
- Never let a section split awkwardly across a page break — if ingredients nearly fill page 1,
  either tighten with grouped `itemsep=0.1em` lists or add a continuation page.
- Older files carry `% ================= PAGE 2 =================` banners. Optional; the
  `PAGE 1` banner is the one that is always present.

## Titles

`\makeRecipeTitle{}` takes the dish's display name, which may be more descriptive than the
folder name: folder `Potato Soup` → title `Loaded Potato Soup`, folder `Lemon Pepper Wings` →
title `Air-Fryer Lemon Pepper Wings`, folder `Chipotle Meal Prep` → title
`Chipotle Meal Prep (Burrito Bowl)`. Keep the folder name the plain searchable one. Remember
`\&` if the title contains an ampersand.

Freezer-prep components — batch-cooked bases portioned into molds and frozen rather than
served straight away — are the one exception to the plain-folder-name rule. They take a
`Frozen ` prefix **everywhere**: folder, `.tex` and `.pdf` filenames, `\makeRecipeTitle{}`,
and the README entry, so they are never mistaken for a dish to eat now. They also end on a
`Portion and Freeze` step instead of `Serve`. Example: `Frozen Black Beans/Frozen Black Beans.tex`.

## Source credit (optional)

When a recipe comes from a video or website, credit it with `\recipeSource{}{}` (defined in
`preamble.tex`) as the last line before `\end{document}`. It pins a small "Source:" line and a
clickable link to the bottom of the final page:

```latex
\end{enumerate}

\recipeSource{Chef Jack Ovens -- 55g Protein Meal Prep That Doesn't Get Dry}{https://www.youtube.com/watch?v=vAsaq06wVDY}

\end{document}
```

First argument is `Creator -- Title` (use `--`; a literal `|` renders as a dash-like glyph in
this font setup, so drop it from video titles). For YouTube, get the exact creator and title from
`https://www.youtube.com/oembed?url=<video url>&format=json` rather than guessing.

## Building

Single recipe:

```bash
cd "Korean Egg Rice"
pdflatex "Korean Egg Rice.tex"
```

Whole collection (regenerates the gitignored merge file, then compiles it):

```bash
python generate-all-recipes-tex.py
pdflatex all-recipes.tex
```

CI (`.github/workflows/verify-recipes.yml`) runs `.github/scripts/build_all_recipes.sh`, which
compiles every `.tex` with `-halt-on-error` and merges the PDFs. **Every recipe must compile
standalone with zero errors** — a single broken file fails the build.
