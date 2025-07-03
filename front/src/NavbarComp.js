import React from "react";
import { Link } from "react-router-dom";


export default function NavigationBar() {
    return (

        <nav
            className="bg-blue w-100 border-0 d-flex justify-content-around align-items-center fixed-bottom" //position-fixed bottom-0
            style={{
                height: "76px",
                borderRadius: '16px 16px 0 0',
            }}>
            <Link to="/dashboard" className=""><img src="clipboard.svg" width="40" height="40" alt=""/></Link>
            <Link to="/accepted" className=""><img src="bell.svg" width="40" height="40" alt=""/></Link>
            <Link to="/profil" className=""><img src="profile.svg" width="38" height="38" alt=""/></Link>
        </nav>
    );
}