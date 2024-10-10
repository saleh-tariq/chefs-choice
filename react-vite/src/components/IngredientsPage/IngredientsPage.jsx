import React, { useEffect, useState } from "react";
import "./IngredientsPage.css";
import { useLoaderData, useSubmit } from "react-router-dom";
import Ingredient from "./Ingredient";

function IngredientsPage() {
  const { Ingredients } = useLoaderData();
  const submit = useSubmit();
  const [name, setName] = useState("");
  const [amountAvailable, setAmountAvailable] = useState(0);
  const [price, setPrice] = useState(0);
  const [unitsOfMeasurement, setUnitsOfMeasurement] = useState("units");

  useEffect(() => {}, [Ingredients]);
  const post = (e) => {
    e.preventDefault();
    submit(
      { name, amountAvailable, price, unitsOfMeasurement },
      { method: "post", encType: "application/json" }
    );
  };

  return (
    <div className="ingredients">
      <h2>My Ingredients</h2>
      <form action="POST" className="new-ingredient" onSubmit={post}>
        <span>
          <p>Name</p>
          <input
            className="dark-primary"
            type="text"
            onInput={(e) => setName(e.target.value)}
            value={name}
          />
        </span>
        <span>
          <p>Price per unit</p>
          <input
            className="dark-primary"
            type="number"
            onInput={(e) => setPrice(e.target.value)}
            value={price}
          />
        </span>
        <span>
          <p>Amount Available</p>
          <input
            className="dark-primary"
            type="number"
            onInput={(e) => setAmountAvailable(e.target.value)}
            value={amountAvailable}
          />
        </span>
        <span>
          <p>Units of Measurment</p>
          <input
            className="dark-primary"
            type="text"
            onInput={(e) => setUnitsOfMeasurement(e.target.value)}
            value={unitsOfMeasurement}
          />
        </span>
        <button className="dark-secondary" type="submit">
          Create
        </button>
      </form>
      <ul>
        {Ingredients.map((e) => (
          <Ingredient ingredient={e} />
        ))}
      </ul>
    </div>
  );
}

export default IngredientsPage;
