# My Food Recipes

A collection of personal cooking recipes, formatted in LaTeX for professional-looking PDFs.

## 📥 Download the PDFs

The latest compiled recipe PDFs are available from GitHub Actions.

1.  Click the **Actions** tab.
2.  Click on the most recent workflow run.
3.  Scroll down to the **Artifacts** section.
4.  Download the **Recipe-PDFs** ZIP archive.

## 📖 Recipe List

Here are the recipes currently in this collection:

### 🥩 Beef
*   **Asian Style Beef Strips**
*   **Carne Asada Tacos**
*   **Garlic Butter Steak Bites**

### 🍗 Chicken
*   **Butter Chicken**
*   **Creamy Tuscan Chicken**
*   **Lemon Pepper Wings**
*   **Mexican Chicken Marinade**
*   **Chipotle Meal Prep**

### 🥣 Soups, Sides & Others
*   **Charro Beans**
*   **Chicken Vegetable Stir-Fry**
*   **Egg Drop Soup**
*   **Korean Egg Rice**
*   **Picadillo**
*   **Potato Soup**
*   **Tomato Soup**
*   **Vegetable Soup**

## 🛠️ Building Locally

If you have LaTeX installed locally, you can generate or compile the collection locally.

Generate `all-recipes.tex` from current folders:

```bash
cd "c:\Users\ryanm\Documents\Knowledge\Diet & Lifestyle\Food Recipes"
python generate-all-recipes-tex.py
```

Compile the combined PDF:

```bash
pdflatex all-recipes.tex
```

Compile a single recipe:

```bash
cd "Korean Egg Rice"
pdflatex "Korean Egg Rice.tex"
```