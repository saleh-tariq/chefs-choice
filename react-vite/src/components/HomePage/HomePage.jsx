import React, { useState } from "react";
import { useLoaderData, useNavigate } from "react-router-dom";
import "./HomePage.css";

function HomePage() {
  const { Recipes } = useLoaderData();
  const navigate = useNavigate();
  const colSetter = {};
  [colSetter.col1, colSetter.setCol1] = useState(false);
  [colSetter.col2, colSetter.setCol2] = useState(false);
  [colSetter.col3, colSetter.setCol3] = useState(true);

  function changeOrderBy(col) {
    const letters = col.split("");
    const setter = `set${letters[0].toUpperCase() + letters.slice(1).join("")}`;
    colSetter.setCol1(false);
    colSetter.setCol2(false);
    colSetter.setCol3(false);
    colSetter[setter](true);
  }

  function formatDuration(seconds) {
    if (!seconds) return "instant";
    let secs = seconds % 60;
    let mins = Math.floor(seconds / 60) % 60;
    let hours = Math.floor(seconds / (60 * 60)) % 24;
    let days = Math.floor(seconds / (24 * 60 * 60)) % 365;
    let years = Math.floor(seconds / (365 * 24 * 60 * 60));

    let time = [secs, mins, hours, days, years];
    for (let i = time.length - 1; i >= 0; i--) {
      if (time[i]) break;
      time.splice(i, 1);
    }
    const words = [" second", " minute", " hour", " day", " year"];
    for (let i = 0; i < time.length; i++) {
      if (time[i] > 1) {
        time[i] += words[i];
        time[i] += "s";
      } else {
        time[i] += words[i];
      }
    }
    time = time.filter((el) => +el[0]);
    return time.length > 2
      ? time
          .slice(2)
          .reverse()
          .map((el) => el + ", ")
          .join("") + time.slice(0, 2).reverse().join(" and ")
      : time.reverse().join(" and ");
  }
  console.log(Recipes);
  return (
    <>
      <h2>Whats on the menu today?</h2>
      {Recipes.length ? (
        <table className="home-recipes">
          <tr>
            <th
              className={"col1" + (colSetter.col1 ? " selected-header" : "")}
              onClick={() => changeOrderBy("col1")}
            >
              Recipe name
            </th>
            <th
              className={"col2" + (colSetter.col2 ? " selected-header" : "")}
              onClick={() => changeOrderBy("col2")}
            >
              No. of steps
            </th>
            <th
              className={"col3" + (colSetter.col3 ? " selected-header" : "")}
              onClick={() => changeOrderBy("col3")}
            >
              Time to make
            </th>
          </tr>
          {Recipes.sort((a, b) => a.steps.length - b.steps.length).map(
            (recipe) => (
              <tr>
                <td className="col1">
                  <h3 onClick={() => navigate("/recipes/" + recipe.id)}>
                    {recipe.name}
                  </h3>
                </td>
                <td className="col2" align="center">
                  <p>{recipe.steps.length}</p>
                </td>
                <td className="col3" align="right">
                  <p>{formatDuration(recipe.total_seconds)}</p>
                </td>
              </tr>
            )
          )}
        </table>
      ) : (
        <>
          <h3>No recipes available</h3>
          <button onClick={showUnavailable}>Show unavailable recipes</button>
          <button onClick={() => navigate("/recipes")}>
            Create new recipes
          </button>
        </>
      )}
    </>
  );
}

export default HomePage;
