import React, { useEffect, useState } from "react";
import { useSubmit } from "react-router-dom";

function Ingredient({ ingredient }) {
  const [name, setName] = useState(ingredient.name);
  const [amountAvailable, setAmountAvailable] = useState(
    ingredient.amount_available
  );
  const [price, setPrice] = useState(ingredient.price);
  const [edit, setEdit] = useState(false);
  const [unitsOfMeasurement, setUnitsOfMeasurement] = useState(
    ingredient.unit_of_measurement
  );

  const submit = useSubmit();

  useEffect(() => {
    setName(ingredient.name);
    setAmountAvailable(ingredient.amount_available);
    setPrice(ingredient.price);
    setUnitsOfMeasurement(ingredient.unit_of_measurement);
  }, [ingredient]);

  const put = () => {
    submit(
      { name, amountAvailable, price, unitsOfMeasurement, id: ingredient.id },
      { method: "PUT", encType: "application/json" }
    );
    setEdit(false);
  };

  const deleter = (ingredient) => {
    submit(ingredient, { method: "DELETE", encType: "application/json" });
  };
  return (
    <li className="ingredient-li">
      <form
        className="ingredient"
        action="PUT"
        onSubmit={async (e) => {
          e.preventDefault();
          put();
        }}
      >
        {edit ? (
          <>
            <div>
              <input
                className="dark-primary"
                value={name}
                onInput={(e) => setName(e.target.value)}
                placeholder="Ingredient Name"
              />
            </div>
            <div>
              $
              <input
                className="dark-primary"
                type="number"
                value={price}
                placeholder="price"
                onInput={(e) => setPrice(e.target.value)}
              />
              per unit
            </div>
            <div>
              <input
                className="dark-primary"
                type="number"
                placeholder="amount"
                value={amountAvailable}
                onInput={(e) => setAmountAvailable(e.target.value)}
              />
              <input
                className="dark-primary"
                type="text"
                placeholder="units"
                value={unitsOfMeasurement}
                onInput={(e) => setUnitsOfMeasurement(e.target.value)}
              />
              <button className="dark-secondary" type="submit">
                Save
              </button>
            </div>
          </>
        ) : (
          <>
            <div>
              <p className="ingredient-name">{ingredient.name}</p>
            </div>
            <div>
              <p>${ingredient.price} per unit</p>
            </div>
            <div>
              <p className="ingredient-amount">
                {`${ingredient.amount_available} ${ingredient.unit_of_measurement}`}
              </p>
              <button
                className="dark-secondary"
                onClick={(e) => {
                  e.preventDefault();
                  setEdit(true);
                }}
              >
                Edit
              </button>
              <button
                className="dark-accent"
                onClick={(e) => {
                  e.preventDefault();
                  if (window.confirm("You suck")) {
                    deleter(ingredient);
                  }
                }}
              >
                delete
              </button>
            </div>
          </>
        )}
      </form>
    </li>
  );
}

export default Ingredient;