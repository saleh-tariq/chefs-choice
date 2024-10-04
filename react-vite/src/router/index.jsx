import { createBrowserRouter } from "react-router-dom";
import LoginFormPage from "../components/LoginFormPage";
import SignupFormPage from "../components/SignupFormPage";
import LoginAndSignupPage from "../components/LoginAndSignupPage";
import HomePage from "../components/HomePage";
import Layout from "./Layout";

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <HomePage />,
        loader: async () => {
          const res = await fetch("/api/recipes");
          const data = await res.json();
          if (res.ok) return data;
          return false;
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
    ],
  },
]);
