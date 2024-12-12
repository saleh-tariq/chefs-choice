import React from "react";
import { useLoaderData, useNavigate, useSubmit } from "react-router-dom";
import "./RecipeDetailsPage.css";
import { FaTrash } from "react-icons/fa6";
import { CiEdit } from "react-icons/ci";

function RecipeDetailsPage() {
  const recipe = useLoaderData();
  const submit = useSubmit();
  const navigate = useNavigate();
  return (
    <div className="recipe-details">
      <div className="recipe-top">
        <h2>{recipe.name}</h2>
        <div className="recipe-buttons">
          <a onClick={() => navigate(`/recipes/${recipe.id}/edit`)}>
            <CiEdit className="recipe-edit" />
          </a>
          <form
            onSubmit={(e) => {
              e.preventDefault();
              const confirmDelete = window.confirm(
                "Are you sure you want to delete this Recipe?"
              );
              if (!confirmDelete) {
                return;
              }
              submit(
                { id: recipe.id },
                { method: "delete", encType: "application/json" }
              );
            }}
          >
            <button type="submit" className="dark-accent recipe-delete">
              <FaTrash />
            </button>
          </form>
        </div>
      </div>
      <img src={recipe.img} alt="Image" className="recipe-image" />
      <p>
        {recipe.is_available
          ? "ready to make"
          : `unavailable ingredients: ${recipe.missing_ingredients
              .map((e) => `${e.name}`)
              .join(", ")}`}
      </p>
      <p>{recipe.description}</p>
      <h3>Steps</h3>
      <div className="recipe-steps">
        {recipe.steps.map((step, i) => (
          <>
            <div className="recipe-step dark-secondary">
              <h4>{`Step #${i + 1}`}</h4>
              <p>{step.description}</p>
              <p>{`Ingredients used: ${step.Ingredients.map(
                (e) => `${e.name} | ${e.amount_needed}`
              ).join(", ")}`}</p>
            </div>
          </>
        ))}
      </div>
    </div>
  );
}

export default RecipeDetailsPage;
