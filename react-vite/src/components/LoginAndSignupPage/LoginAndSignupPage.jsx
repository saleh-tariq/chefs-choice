import React, { useState } from "react";
import "./LoginAndSignupPage.css";
import LoginFormPage from "../LoginFormPage";
import SignupFormPage from "../SignupFormPage";
import "./LoginAndSignupPage.css";

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
          <div className="signup-div login-signup-main">
            <p>already have an account?</p>
            <a onClick={signupToggle} className="dark-accent-text">
              login
            </a>
          </div>
        </>
      ) : (
        <>
          <LoginFormPage />
          <div className="login-div login-signup-main">
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
