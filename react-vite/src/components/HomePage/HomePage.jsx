import React, { useState } from "react";
import { useLoaderData, useNavigate } from "react-router-dom";
import "./HomePage.css";
import { useSelector } from "react-redux";
import logo from "/pngwing.com.png";
import formatDuration from "/utils/format-duration";

function HomePage() {
  const user = useSelector((store) => store.session.user);
  if (!user || !logo) {
    return <h2>Loading...</h2>;
  }
  const { Recipes, Ingredients } = useLoaderData() || {
    Recipes: [],
    Ingredients: [],
  };

  const navigate = useNavigate();

  return (
    <div className="home-main">
      <div className="home-logo">
        <h2 className="logo ">
          <img className="logo-image" src={logo} />
          Chef's Choice
        </h2>
      </div>
      <div className="home-nav-buttons">
        <div
          onClick={() => navigate("/recipes")}
          className="cursive dark-secondary"
        >
          Recipes
        </div>
        <div
          onClick={() => navigate("/ingredients")}
          className="cursive dark-primary"
        >
          Ingredients
        </div>
      </div>
      <div className="inset home-table-main">
        <div className="home-recipes dark-secondary">
          <table className="home-recipes-table">
            <tr>
              <th className="col1" align="center">
                Recipe name
              </th>
              <th align="center">Time to make</th>
            </tr>
            {Recipes.sort((a, b) => a.total_seconds - b.total_seconds).map(
              (recipe, i) => (
                <tr className={i % 2 || "dark-primary"}>
                  <td className="col1" align="center">
                    <p onClick={() => navigate("/recipes/" + recipe.id)}>
                      {recipe.name}
                    </p>
                  </td>
                  <td align="center">
                    <p>{formatDuration(recipe.total_seconds)}</p>
                  </td>
                </tr>
              ),
            )}
          </table>
          <div
            onClick={() => navigate("/recipes/new")}
            className="dark home-recipe-button"
          >
            <h3>Create new recipe</h3>
          </div>
        </div>
        <div>
          {Ingredients.length ? (
            <div className="home-ingredients dark-secondary">
              <table className="">
                <tr>
                  <th className="col1" align="center">
                    Ingredient name
                  </th>
                  <th align="center">Amount available</th>
                </tr>
                {Ingredients.sort(
                  (a, b) => a.amount_available - b.amount_available,
                ).map((ingredient, i) => (
                  <tr className={i % 2 || "dark-primary"}>
                    <td className="col1" align="center">
                      <p>{ingredient.name}</p>
                    </td>
                    <td align="center">
                      <p>
                        {ingredient.amount_available}{" "}
                        {ingredient.unit_of_measurement}
                      </p>
                    </td>
                  </tr>
                ))}
              </table>
              <div
                onClick={() => navigate("/ingredients")}
                className="dark home-recipe-button"
              >
                <h3>View and create ingredients</h3>
              </div>
            </div>
          ) : (
            <></>
          )}
        </div>
      </div>
    </div>
  );
}

export default HomePage;
