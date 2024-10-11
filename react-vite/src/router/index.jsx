import { createBrowserRouter } from "react-router-dom";
import LoginFormPage from "../components/LoginFormPage";
import SignupFormPage from "../components/SignupFormPage";
import LoginAndSignupPage from "../components/LoginAndSignupPage";
import IngredientsPage from "../components/IngredientsPage";
import HomePage from "../components/HomePage";
import Layout from "./Layout";
import RecipesPage from "../components/recipes";
import RecipeDetailsPage from "../components/RecipeDetails";

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <HomePage />,
        loader: async () => {
          const res = await fetch("/api/recipes/available");
          const data = await res.json();
          if (res.ok) return data;
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
          const res = [
            await fetch("/api/recipes"),
            await fetch("/api/recipes/available"),
            await fetch("/api/recipes/unavailable"),
          ];
          const data = [];
          for (let i = 0; i < res.length; i++) {
            data[i] = await res[i].json();
          }
          if (!data.includes(false)) {
            return {
              Recipes: data[0],
              Available: data[1],
              Unavailable: data[2],
            };
          }
          return null;
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
