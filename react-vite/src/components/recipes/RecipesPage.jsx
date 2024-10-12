import React from "react";
import { useLoaderData } from "react-router-dom";
import Recipe from "./Recipe";
import "./RecipesPage.css";

function RecipesPage() {
  const { Recipes } = useLoaderData() || {
    Recipes: [],
    Available: [],
    Unavailable: [],
  };
  return (
    <div className="recipes-page">
      <h2>Recipes</h2>
      <table className="recipes-table dark-secondary">
        <tr>
          <th align="left">
            <h3>Recipe name</h3>
          </th>
          <th align="center">
            <h3>Time to make</h3>
          </th>
        </tr>
        {Recipes.Recipes.sort((a, b) => a.total_seconds - b.total_seconds).map(
          (recipe, i) => (
            <Recipe
              className={!(i % 2) ? "dark-primary" : "dark-secondary"}
              recipeId={recipe.id}
              recipeName={recipe.name}
              otherData={recipe.total_seconds}
            />
          )
        )}
      </table>
    </div>
  );
}

export default RecipesPage;
