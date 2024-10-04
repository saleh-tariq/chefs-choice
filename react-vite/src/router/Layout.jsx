import { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { ModalProvider, Modal } from "../context/Modal";
import { thunkAuthenticate } from "../redux/session";
import Navigation from "../components/Navigation/Navigation";
import LoginAndSignupPage from "../components/LoginAndSignupPage";

export default function Layout() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(thunkAuthenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  const user = useSelector((store) => store.session.user);

  return (
    <>
      <ModalProvider>
        <Navigation />
        {isLoaded && user ? <Outlet /> : <LoginAndSignupPage />}
        <Modal />
      </ModalProvider>
    </>
  );
}
