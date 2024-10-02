import React, { useState } from "react";
import "./LoginAndSignupPage.css";
import LoginFormPage from "../LoginFormPage";
import SignupFormPage from "../SignupFormPage";

function LoginAndSignupPage() {
  const [signup, setSignUp] = useState(false);
  const signupToggle = () => {
    setSignUp(!signup);
  };
  return (
    <div>
      {signup ? (
        <>
          <SignupFormPage />
          <div>
            <p>already have an account?</p>
            <a onClick={signupToggle} className="dark-accent-text">
              login
            </a>
          </div>
        </>
      ) : (
        <>
          <LoginFormPage />
          <div>
            <p>dont have an account?</p>
            <a onClick={signupToggle} className="dark-accent-text">
              sign up
            </a>
          </div>
        </>
      )}
    </div>
  );
}

export default LoginAndSignupPage;
