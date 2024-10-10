import React from "react";
import { useNavigate } from "react-router-dom";

function Recipe({ recipe }) {
  const navigate = useNavigate();
  return (
    <div className="recipe" onClick={() => navigate("/recipes/" + recipe.id)}>
      <h3>{recipe.name}</h3>
      <p>{recipe.description}</p>
    </div>
  );
}

export default Recipe;
