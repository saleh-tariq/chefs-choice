import React, { useEffect, useState } from "react";
import { useLoaderData, useNavigate } from "react-router-dom";
import Recipe from "./Recipe";
import "./RecipesPage.css";
import formatDuration from "/utils/format-duration";

function RecipesPage() {
  const navigate = useNavigate();
  const data = useLoaderData();
  const [Recipes, setRecipes] = useState({
    Recipes: [],
    Available: [],
    Unavailable: [],
  });
  useEffect(() => {
    if (data) setRecipes(data.Recipes);
  }, data);
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
              key={i}
              className={!(i % 2) ? "dark-primary" : "dark-secondary"}
              recipeId={recipe.id}
              recipeName={recipe.name}
              otherData={formatDuration(recipe.total_seconds)}
            />
          )
        )}
        <button
          className="dark-accent"
          onClick={() => navigate("/recipes/new")}
        >
          Create a New Recipe
        </button>
      </table>
    </div>
  );
}

export default RecipesPage;
