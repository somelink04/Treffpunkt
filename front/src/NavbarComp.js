import React from "react";
import { Link } from "react-router-dom";

export default function NavigationBar() {

    return (
        <nav
            className="bg-blue w-100 border-0 d-flex justify-content-around align-items-center position-fixed bottom-0"
            style={{
                height: "76px",

            }}
        >
            <Link to="/" className=""><img src="plus.svg" width="20" height="20" alt=""/></Link>
            <Link to="/" className=""><img src="plus.svg" width="20" height="20" alt=""/></Link>
            <Link to="/" className=""><img src="plus.svg" width="20" height="20" alt=""/></Link>
            <Link to="/" className=""><img src="plus.svg" width="20" height="20" alt=""/></Link>
        </nav>
    );
}