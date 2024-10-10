import React from "react";
import { useLoaderData } from "react-router-dom";
import "./RecipeDetailsPage.css";

function RecipeDetailsPage() {
  const recipe = useLoaderData();
  console.log(recipe);
  return (
    <div className="recipe-details">
      <h2>{recipe.name}</h2>
      <h2>{recipe.description}</h2>
      <div
        className="recipe-image"
        style={{ backgroundImage: `url(${recipe.img})` }}
      >
        some text
      </div>
    </div>
  );
}

export default RecipeDetailsPage;
