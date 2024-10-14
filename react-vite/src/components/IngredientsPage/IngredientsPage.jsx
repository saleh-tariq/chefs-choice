import React, { useEffect, useState } from "react";
import "./IngredientsPage.css";
import { useLoaderData, useSubmit } from "react-router-dom";
import Ingredient from "./Ingredient";

function IngredientsPage() {
  const { Ingredients } = useLoaderData();
  const submit = useSubmit();
  const [name, setName] = useState("");
  const [amountAvailable, setAmountAvailable] = useState(0);
  const [unitsOfMeasurement, setUnitsOfMeasurement] = useState("units");

  useEffect(() => {}, [Ingredients]);
  const post = (e) => {
    e.preventDefault();
    submit(
      { name, amountAvailable, unitsOfMeasurement },
      { method: "post", encType: "application/json" }
    );
  };

  return (
    <div className="ingredients">
      <h2>My Ingredients</h2>
      <form
        action="POST"
        className="new-ingredient dark-primary"
        onSubmit={post}
      >
        <span className="ingredient-form-name">
          <h2>Create new ingredient</h2>
          <p>Name</p>
          <input
            className="dark-primary"
            type="text"
            onInput={(e) => setName(e.target.value)}
            value={name}
          />
        </span>
        <span className="ingredient-form-amount">
          <div>
            <p>Amount Available</p>

            <input
              className="dark-primary"
              type="number"
              onInput={(e) => setAmountAvailable(e.target.value)}
              value={amountAvailable}
            />
          </div>
          <div>
            <p>Units of Measurment</p>
            <input
              className="dark-primary"
              type="text"
              onInput={(e) => setUnitsOfMeasurement(e.target.value)}
              value={unitsOfMeasurement}
            />
          </div>
        </span>
        <button className="ingredient-submit dark-accent" type="submit">
          Create
        </button>
      </form>

      {Ingredients.map((e, i) => (
        <Ingredient ingredient={e} i={i} />
      ))}
    </div>
  );
}

export default IngredientsPage;
