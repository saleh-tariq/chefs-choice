import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { IoIosMenu, IoIosClose } from "react-icons/io";
import { thunkLogout } from "../../redux/session";
import { NavLink } from "react-router-dom";

function NavBar() {
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const user = useSelector((store) => store.session.user);
  const ulRef = useRef();

  const toggleMenu = (e) => {
    e.stopPropagation(); // Keep from bubbling up to document and triggering closeMenu
    setShowMenu(!showMenu);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (ulRef.current && !ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const closeMenu = () => setShowMenu(false);

  const logout = (e) => {
    e.preventDefault();
    dispatch(thunkLogout());
    closeMenu();
  };

  return (
    <>
      {!user || (
        <button
          onClick={toggleMenu}
          className={
            showMenu ? "nav-button-open nav-button dark" : "nav-button dark"
          }
        >
          {showMenu ? <IoIosClose /> : <IoIosMenu />}
        </button>
      )}

      <div
        className={showMenu ? "side-bar side-bar-open dark" : "side-bar dark"}
        ref={ulRef}
      >
        {user ? (
          <>
            <p>{user.username}</p>
            <p>{user.email}</p>
            <NavLink to="/" className={"dark-accent-text"}>
              Home
            </NavLink>
            <NavLink to="/ingredients" className={"dark-accent-text"}>
              My Ingredients
            </NavLink>
            <NavLink to="/recipes" className={"dark-accent-text"}>
              Recipes
            </NavLink>
            <button onClick={logout} className="dark-secondary">
              Log Out
            </button>
          </>
        ) : (
          <></>
        )}
      </div>
    </>
  );
}

export default NavBar;
