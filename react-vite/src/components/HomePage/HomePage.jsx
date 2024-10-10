import React from "react";
import { useLoaderData, useNavigate } from "react-router-dom";

function HomePage() {
  const { Recipes } = useLoaderData();
  const navigate = useNavigate();
  return (
    <>
      <h2>Whats on the menu today?</h2>
      {Recipes.length ? (
        Recipes.map((recipe) => (
          <div onClick={() => navigate("/recipes/" + recipe.id)}>
            <h3>{recipe.name}</h3>
          </div>
        ))
      ) : (
        <button onClick={() => navigate("/recipes")}>Create new recipes</button>
      )}
    </>
  );
}

export default HomePage;
