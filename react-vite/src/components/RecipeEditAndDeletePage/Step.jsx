import React, { useEffect, useState } from "react";

function Step({ Ingredients }) {
  const [description, setDescription] = useState("");
  return (
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
        <p>Time to complete</p>
        <input className="dark-secondary" type="number" placeholder="minutes" />
        <input className="dark-secondary" type="number" placeholder="seconds" />
      </div>

      <div>
        <select>
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
        />
        <button>Add ingredient</button>
      </div>
    </div>
  );
}

export default Step;
