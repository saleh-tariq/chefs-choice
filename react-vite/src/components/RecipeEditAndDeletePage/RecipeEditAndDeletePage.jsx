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
            ingredients: step.Ingredients.map((ingredient) => {
              return { ...ingredient, amountNeeded: ingredient.amount_needed };
            }),
            seconds: step.seconds,
          };
        })
      : []
  );
  const [image, setImage] = useState("");
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
    } else if (recipeName.length > 40) {
      return "Recipe name cannot exceed 40 characters";
    }
  };

  const post = async () => {
    const recipeErr = validate_recipe();
    errors.recipe = null;
    setErrors({ ...errors });
    if (recipeErr) {
      return setErrors({ ...errors, recipe: recipeErr });
    }
    const form = new FormData();
    if (image) {
      // const reader = new FileReader();
      // reader.readAsDataURL(image);
      // reader.onload = (e) => {
      form.append("img", image);
      // };
    }
    form.append("name", recipeName);
    form.append("description", recipeDescription);
    const stepString = JSON.stringify(
      committedSteps.map((step) => {
        return {
          Ingredients: step.ingredients,
          description: step.description,
          seconds: step.seconds,
        };
      })
    );
    form.append("steps", stepString);
    submit(form, { method: "post", encType: "multipart/form-data" });
  };
  useEffect(() => {}, [image]);
  return (
    <div>
      <form
        action="post"
        className="recipe-form"
        onSubmit={(e) => {
          e.preventDefault();
          post();
        }}
        encType="multipart/form-data"
      >
        <h2>{edit ? "Edit Recipe" : "New Recipe"}</h2>
        {errors.recipe}
        <div className="recipe-input-area">
          <div className="recipe-name-disc">
            <input
              type="text"
              placeholder="name"
              className="dark-primary recipe-name"
              value={recipeName}
              onInput={(e) => setRecipeName(e.target.value)}
            />
            <textarea
              placeholder="description..."
              className="textarea recipe-description dark-primary"
              value={recipeDescription}
              onInput={(e) => setRecipeDescription(e.target.value)}
            />
            <input type="file" onInput={(e) => setImage(e.target.files[0])} />
          </div>

          <div className="recipe-form-step dark-primary">
            <div className="recipe-form-step-only">
              <h3>Add a Step</h3>
              <textarea
                value={description}
                onInput={(e) => {
                  e.preventDefault();
                  setDescription(e.target.value);
                }}
                placeholder="description..."
                className="textarea recipe-form-step-description dark-secondary"
              />
              <div className="recipe-form-step-seconds">
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
                      ingredients: [...ingredients],
                      seconds: seconds + minutes * 60,
                    });
                    setCommittedSteps([...committedSteps]);
                  }}
                >
                  Add Step
                  <FaRegPlusSquare />
                </button>
              </div>
            </div>
            <div className="recipe-form-ingredient-container">
              <div>
                <select
                  className="dark-secondary recipe-form-ingredient-select"
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
                <div className="recipe-form-step-ingredient-form">
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
                </div>
                <button
                  className="dark-accent"
                  onClick={(e) => {
                    e.preventDefault();
                    errors.ingredient = null;
                    setErrors({ ...errors });
                    const ingredErr = validate_ingredient();
                    if (ingredErr) {
                      return setErrors({ ...errors, ingredient: ingredErr });
                    }
                    const existing = ingredients.find(
                      (i) => i.id === selected.id
                    );
                    if (existing) {
                      existing.amountNeeded += amountNeeded;
                      return;
                    }
                    setIngredients([
                      ...ingredients,
                      { ...selected, amountNeeded },
                    ]);
                  }}
                >
                  Add ingredient to step
                </button>
                {errors.ingredient ? errors.ingredient : null}
              </div>
              <div>
                <p>Ingredients added to step (scrollable):</p>
                <div className="recipe-form-step-ingredients">
                  {ingredients.map((i, idx) => {
                    return (
                      <div
                        className={
                          idx % 2
                            ? "recipe-form-step-ingredient dark-primary"
                            : "recipe-form-step-ingredient dark-secondary"
                        }
                      >
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
                      </div>
                    );
                  })}
                </div>
              </div>
              {errors.step ? errors.step : null}
            </div>
          </div>
        </div>
        <h3>Added Steps</h3>
        <div className="">
          {committedSteps.map((step, i) => {
            return (
              <div>
                <p>{`Step #${i + 1}`}</p>
                <p>{step.description}</p>
                <p>{formatDuration(step.seconds)}</p>
                {!!step.ingredients.length && <p>Ingredients used:</p>}
                {step.ingredients.map((i) => {
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
        </div>
        <button type="submit" className="dark-accent">
          Submit
        </button>
      </form>
    </div>
  );
}

export default RecipeEditAndDeletePage;
