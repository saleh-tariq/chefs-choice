import React from "react";
import { useLoaderData } from "react-router-dom";
import Recipe from "./Recipe";

function RecipesPage() {
  const { Recipes, Available, Unavailable } = useLoaderData();
  return (
    <div className="recipes-page">
      <h2>Ready to make</h2>
      {Available.Recipes.map((recipe) => (
        <Recipe recipe={recipe} />
      ))}
      <hr />
      <h2>Need ingredients to make</h2>
      {Unavailable.Recipes.map((recipe) => (
        <Recipe recipe={recipe} />
      ))}
      <hr />
      <h2>All Recipes</h2>
      {Recipes.Recipes.map((recipe) => (
        <Recipe recipe={recipe} />
      ))}
    </div>
  );
}

export default RecipesPage;
