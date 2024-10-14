import React, { useEffect, useState } from "react";
import "./RecipeEditAndDeletePage.css";
import { FaRegPlusSquare } from "react-icons/fa";
import { useLoaderData, useNavigate, useSubmit } from "react-router-dom";
import formatDuration from "/utils/format-duration";

function RecipeEditAndDeletePage({ edit }) {
  const navigate = useNavigate();
  const submit = useSubmit();
  const data = useLoaderData();
  const { Ingredients } = data;
  if (!Ingredients.length) {
    Ingredients[0] = { name: "No valid Ingredients" };
  }
  const { Recipe } = edit ? data : { Recipe: {} };
  const [committedSteps, setCommittedSteps] = useState(
    edit
      ? Recipe.steps.map((step) => {
          return {
            description: step.description,
            ingredients: step.Ingredients,
            seconds: step.seconds,
          };
        })
      : []
  );
  const [description, setDescription] = useState("");
  const [ingredients, setIngredients] = useState([]);
  const [seconds, setSeconds] = useState(0);
  const [minutes, setMinutes] = useState(0);
  const [selected, setSelected] = useState(Ingredients[0]);
  const [amountNeeded, setAmountNeeded] = useState(0);
  const [recipeDescription, setRecipeDescription] = useState(
    edit ? Recipe.description : ""
  );
  const [recipeName, setRecipeName] = useState(edit ? Recipe.name : "");
  const [errors, setErrors] = useState({});

  const validate_ingredient = () => {
    if (!selected?.id || amountNeeded <= 0) {
      return "Please use an amount greater than 0.";
    }
  };

  const validate_step = () => {
    if (!description) {
      return "Step description is required";
    }
  };

  const validate_recipe = () => {
    if (!recipeDescription || !recipeName) {
      return "Recipe name and description are required";
    }
  };

  const post = async () => {
    const recipeErr = validate_recipe();
    errors.recipe = null;
    setErrors({ ...errors });
    if (recipeErr) {
      return setErrors({ ...errors, recipe: recipeErr });
    }
    submit(
      {
        Recipe: { name: recipeName, description: recipeDescription },
        Steps: committedSteps.map((step) => {
          return {
            Ingredients: step.ingredients,
            description: step.description,
            seconds: step.seconds,
          };
        }),
      },
      { method: "post", encType: "application/json" }
    );
  };

  return (
    <div>
      <form
        action="post"
        className="recipe-form"
        onSubmit={(e) => {
          e.preventDefault();
          post();
        }}
      >
        <h2>{edit ? "Edit Recipe" : "New Recipe"}</h2>
        {errors.recipe}
        <input
          type="text"
          placeholder="name"
          className="dark-primary"
          value={recipeName}
          onInput={(e) => setRecipeName(e.target.value)}
        />
        <textarea
          placeholder="description..."
          className="textarea recipe-description dark-primary"
          value={recipeDescription}
          onInput={(e) => setRecipeDescription(e.target.value)}
        />
        <h3>Steps</h3>
        {committedSteps.map((step, i) => {
          return (
            <div>
              <p>{`Step #${i + 1}`}</p>
              <p>{step.description}</p>
              <p>{formatDuration(step.seconds)}</p>
              {!!step.ingredients.length && <p>Ingredients used:</p>}
              {step.ingredients.map((i) => {
                console.log(i);
                return (
                  <>
                    <p>{i.name}</p>
                    <p>{i.amountNeeded}</p>
                  </>
                );
              })}
              <button
                className="dark-accent"
                onClick={(e) => {
                  e.preventDefault();
                  committedSteps.splice(i, 1);
                  setCommittedSteps([...committedSteps]);
                }}
              >
                Remove step
              </button>
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
                    {i.name} | {i.amountNeeded}
                  </p>
                  <button
                    className="dark-accent"
                    onClick={(e) => {
                      e.preventDefault();
                      ingredients.splice(i, 1);
                      setIngredients([...ingredients]);
                    }}
                  >
                    Remove ingredient
                  </button>
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
              value={amountNeeded || ""}
              onInput={(e) => {
                e.preventDefault();
                setAmountNeeded(Number(e.target.value));
              }}
            />
            <p>{selected?.unit_of_measurement || "units"}</p>
            <button
              className="dark-secondary"
              onClick={(e) => {
                e.preventDefault();
                errors.ingredient = null;
                setErrors({ ...errors });
                const ingredErr = validate_ingredient();
                if (ingredErr) {
                  return setErrors({ ...errors, ingredient: ingredErr });
                }
                setIngredients([...ingredients, { ...selected, amountNeeded }]);
              }}
            >
              Add ingredient
            </button>
            {errors.ingredient ? errors.ingredient : null}
          </div>
          <div>
            <p>Time to complete</p>
            <input
              className="dark-secondary"
              type="number"
              placeholder="minutes"
              value={minutes || ""}
              onInput={(e) => setMinutes(Number(e.target.value))}
            />
            <input
              className="dark-secondary"
              type="number"
              placeholder="seconds"
              value={seconds || ""}
              onInput={(e) => setSeconds(Number(e.target.value))}
            />
          </div>
          <button
            className="dark-accent recipe-form-add-step"
            onClick={(e) => {
              e.preventDefault();
              errors.step = null;
              setErrors({ ...errors });
              const stepErr = validate_step();
              if (stepErr) {
                return setErrors({ ...errors, step: stepErr });
              }
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
          {errors.step ? errors.step : null}
        </div>
        <button type="submit" className="dark-accent">
          Submit
        </button>
      </form>
    </div>
  );
}

export default RecipeEditAndDeletePage;
