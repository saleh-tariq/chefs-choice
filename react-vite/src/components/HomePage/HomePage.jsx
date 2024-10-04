import React from "react";
import { useLoaderData, useNavigate } from "react-router-dom";

function HomePage() {
  const { Recipes } = useLoaderData();
  const navigate = useNavigate();
  return (
    <>
      {Recipes.map((recipe) => (
        <div onClick={() => navigate("/recipes/" + recipe.id)}>
          <h3>{recipe.name}</h3>
        </div>
      ))}
    </>
  );
}

export default HomePage;
