import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { IoIosMenu } from "react-icons/io";
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
      {showMenu || !user || (
        <button onClick={toggleMenu} className="nav-button dark">
          <IoIosMenu />
        </button>
      )}
      {showMenu && (
        <div className={"side-bar dark"} ref={ulRef}>
          {user ? (
            <>
              <p>{user.username}</p>
              <p>{user.email}</p>
              <NavLink to="/">Home</NavLink>
              <NavLink to="/">Home</NavLink>
              <NavLink to="/">Home</NavLink>
              <NavLink to="/">Home</NavLink>
              <button onClick={logout} className="dark-secondary">
                Log Out
              </button>
            </>
          ) : (
            <></>
          )}
        </div>
      )}
    </>
  );
}

export default NavBar;
