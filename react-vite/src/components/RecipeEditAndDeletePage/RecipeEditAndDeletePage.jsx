import React, { useEffect, useState } from "react";
import "./RecipeEditAndDeletePage.css";
import { FaRegPlusSquare } from "react-icons/fa";
import { useLoaderData } from "react-router-dom";

function RecipeEditAndDeletePage() {
  const [description, setDescription] = useState("");
  const { Ingredients } = useLoaderData();
  const [committedSteps, setCommittedSteps] = useState([]);
  const [ingredients, setIngredients] = useState([]);
  const [seconds, setSeconds] = useState(0);
  const [minutes, setMinutes] = useState(0);
  const [selected, setSelected] = useState(Ingredients[0]);
  const [amountNeeded, setAmountNeeded] = useState(0);

  return (
    <div>
      <form
        action="post"
        className="recipe-form"
        onSubmit={(e) => {
          e.preventDefault();
        }}
      >
        <h2>New Recipe</h2>
        <input type="text" placeholder="name" className="dark-primary" />
        <textarea
          placeholder="description..."
          className="textarea recipe-description dark-primary"
        />
        <h3>Steps</h3>
        {committedSteps.map((step, i) => {
          return (
            <div>
              <p>{`Step #${i + 1}`}</p>
              <p>{step.description}</p>
              {!!step.ingredients.length && <p>Ingredients used</p>}
              {step.ingredients.map((i) => {
                return (
                  <>
                    <p>{i.ingredient.name}</p>
                    <p>{i.amountNeeded}</p>
                  </>
                );
              })}
            </div>
          );
        })}

        <div className="recipe-form-step dark-primary">
          <textarea
            value={description}
            onInput={(e) => {
              e.preventDefault();
              setDescription(e.target.value);
            }}
            placeholder="description..."
            className="textarea recipe-step-description dark-secondary"
          />
          <div>
            <p>Ingredients</p>
            {ingredients.map((i) => {
              return (
                <>
                  <p>
                    {i.ingredient.name} | {i.amountNeeded}
                  </p>
                </>
              );
            })}
          </div>

          <div>
            <select
              className="dark-secondary"
              onChange={(e) => {
                setSelected(
                  Ingredients.find(
                    (b) =>
                      b.id ===
                      Number(e.target.options[e.target.selectedIndex].id)
                  )
                );
              }}
            >
              {Ingredients.map((e) => {
                return (
                  <option id={e.id}>
                    <p>{e.name}</p>
                  </option>
                );
              })}
            </select>
            <input
              className="dark-secondary"
              type="number"
              placeholder="amount needed"
              value={amountNeeded}
              onInput={(e) => {
                e.preventDefault();
                setAmountNeeded(Number(e.target.value));
              }}
            />
            <p>{selected.unit_of_measurement}</p>
            <button
              className="dark-secondary"
              onClick={(e) => {
                e.preventDefault();
                setIngredients([
                  ...ingredients,
                  { ingredient: selected, amountNeeded },
                ]);
              }}
            >
              Add ingredient
            </button>
          </div>

          <div>
            <p>Time to complete</p>
            <input
              className="dark-secondary"
              type="number"
              placeholder="minutes"
              value={minutes}
              onInput={(e) => setMinutes(Number(e.target.value))}
            />
            <input
              className="dark-secondary"
              type="number"
              placeholder="seconds"
              value={seconds}
              onInput={(e) => setSeconds(Number(e.target.value))}
            />
          </div>

          <button
            className="dark-accent recipe-form-add-step"
            onClick={(e) => {
              e.preventDefault();
              committedSteps.push({
                description,
                ingredients,
                seconds: seconds + minutes * 60,
              });
              setCommittedSteps([...committedSteps]);
            }}
          >
            Add Step
            <FaRegPlusSquare />
          </button>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default RecipeEditAndDeletePage;
