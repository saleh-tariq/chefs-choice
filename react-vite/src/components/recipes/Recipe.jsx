import React from "react";
import { useNavigate } from "react-router-dom";

function Recipe({ recipeName, otherData, recipeId, className }) {
  const navigate = useNavigate();
  return (
    <tr
      className={"recipe " + className}
      onClick={() => navigate("/recipes/" + recipeId)}
    >
      <td align="left">
        <h3>{recipeName}</h3>
      </td>
      <td align="center">
        <p>{otherData}</p>
      </td>
    </tr>
  );
}

export default Recipe;
