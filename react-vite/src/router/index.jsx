import { createBrowserRouter, redirect } from "react-router-dom";
import LoginFormPage from "../components/LoginFormPage";
import SignupFormPage from "../components/SignupFormPage";
import IngredientsPage from "../components/IngredientsPage";
import HomePage from "../components/HomePage";
import Layout from "./Layout";
import RecipesPage from "../components/recipes";
import RecipeDetailsPage from "../components/RecipeDetails";
import RecipeEditAndDeletePage from "../components/RecipeEditAndDeletePage";

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <HomePage />,
        loader: async () => {
          const res1 = await fetch("/api/recipes/available");
          const res2 = await fetch("/api/ingredients");
          const data = { ...(await res1.json()), ...(await res2.json()) };
          if (res1.ok && res2.ok) return data;
          return null;
        },
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "recipes",
        element: <RecipesPage />,
        loader: async () => {
          const res = await fetch("/api/recipes");
          const data = await res.json();
          if (res.ok) {
            return {
              Recipes: data,
            };
          }
          return { Recipes: [] };
        },
      },
      {
        path: "recipes/:recipeId",
        element: <RecipeDetailsPage />,
        loader: async ({ params }) => {
          const res = await fetch("/api/recipes/" + params.recipeId);
          const data = await res.json();
          if (res.ok) return data;
          return null;
        },
        action: async ({ params }) => {
          const res = await fetch("/api/recipes/" + params.recipeId, {
            method: "DELETE",
          });
          redirect("/recipes");
          return null;
        },
      },
      {
        path: "recipes/new",
        element: <RecipeEditAndDeletePage />,
        loader: async () => {
          const res = await fetch("/api/ingredients");
          const data = await res.json();
          if (res.ok) return data;
          return null;
        },
        action: async ({ request: req }) => {
          const { Recipe, Steps } = await req.json();
          const res = await fetch(`/api/recipes`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              name: Recipe.name,
              description: Recipe.description,
            }),
          });
          const recipe = await res.json();

          console.log(recipe);

          for (let i = 0; i < Steps.length; i++) {
            let currStep = Steps[i];
            const res = await fetch(`/api/recipes/${recipe.id}/steps`, {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                description: currStep.description,
                seconds: currStep.seconds,
              }),
            });

            const step = await res.json();
            console.log(currStep.Ingredients);
            for (let j = 0; j < currStep.Ingredients.length; j++) {
              let ingredient = currStep.Ingredients[j];
              const res = await fetch(`/api/steps/${step.id}/ingredients`, {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({
                  ingredient_id: ingredient.ingredient.id,
                  amount_needed: ingredient.amountNeeded,
                }),
              });

              const newIngredient = await res.json();
              console.log(newIngredient);
            }
          }
          return null;
        },
      },
      {
        path: "ingredients",
        element: <IngredientsPage />,
        loader: async () => {
          const res = await fetch("/api/ingredients");
          const data = await res.json();
          if (res.ok) return data;
          return null;
        },
        action: async ({ request: req }) => {
          const data = await req.json();
          if (req.method.toUpperCase() === "PUT") {
            const ingredient = data;
            console.log({
              name: ingredient.name,
              price_per_unit: ingredient.price,
              img: ingredient.img,
              amount_available: ingredient.amountAvailable,
              unit_of_measurement: ingredient.unitsOfMeasurement,
            });
            const res = await fetch(`/api/ingredients/${ingredient.id}`, {
              method: "PUT",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                name: ingredient.name,
                price_per_unit: ingredient.price,
                img: ingredient.img,
                amount_available: ingredient.amountAvailable,
                unit_of_measurement: ingredient.unitsOfMeasurement,
              }),
            });
            return null;
          }
          if (req.method.toUpperCase() === "POST") {
            const ingredient = data;
            const res = await fetch(`/api/ingredients`, {
              method: "post",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                name: ingredient.name,
                price_per_unit: ingredient.price,
                img: ingredient.img,
                amount_available: ingredient.amountAvailable,
                unit_of_measurement: ingredient.unitsOfMeasurement,
              }),
            });
            return null;
          }
          if (req.method.toUpperCase() === "DELETE") {
            const { id } = data;
            const res = await fetch(`/api/ingredients/${id}`, {
              method: "DELETE",
            });
            return null;
          }
        },
      },
    ],
  },
]);
