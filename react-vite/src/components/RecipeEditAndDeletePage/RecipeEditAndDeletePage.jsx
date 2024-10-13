import React, { useEffect, useState } from "react";
import "./RecipeEditAndDeletePage.css";
import { FaRegPlusSquare } from "react-icons/fa";
import Step from "./Step";
import { useLoaderData } from "react-router-dom";

function RecipeEditAndDeletePage() {
  const [steps, setSteps] = useState([]);
  const { Ingredients } = useLoaderData();

  return (
    <div>
      <form action="post" className="recipe-form">
        <h2>New Recipe</h2>
        <input type="text" placeholder="name" className="dark-primary" />
        <textarea
          placeholder="description..."
          className="textarea recipe-description dark-primary"
        />
        <h3>Steps</h3>
        <div
          className="dark-accent-text recipe-form-add-step"
          onClick={async (e) => {
            e.preventDefault();
            steps.push(<Step Ingredients={Ingredients} />);
            setSteps([...steps]);
          }}
        >
          Add new Step
          <FaRegPlusSquare />
        </div>
        {steps}
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default RecipeEditAndDeletePage;
