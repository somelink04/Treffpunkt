import React, { useState } from "react";
import {Link, Navigate, useNavigate} from 'react-router-dom';
import "./style/global.css";

export default function DashboardForm()
{


    return (
        <>
            <nav className="navbar navbar-light px-3 d-flex justify-content-between align-items-center"
                 style={{backgroundColor: "#546FF1", height: "60px", borderRadius: "0 0 12px 12px"}} >
                <h1 className="navbar-brand text-white mb-0 fw-bold"
                    style={{fontSize: "1.8rem"}}>Für dich!</h1>
                <div className="d-flex gap-3">
                    <Link className="nav-icon-small text-white" to="#">
                        <i className="fa-solid fa-calendar-days"></i>
                    </Link>
                    <Link className="nav-icon-small text-white" to="#">
                        <i className="fa-solid fa-filter"></i>
                    </Link>
                </div>
            </nav>
            <div className="container mt-4 text-white">

                <div id="slide-container" className="position-relative text-center mt-4">
                    <div id="arrow-controls" className="position-absolute w-100 d-flex justify-content-between">
                        <button id="prevBtn" className="btn btn-warning rounded-circle">&#8592;</button>
                        <button id="nextBtn" className="btn btn-warning rounded-circle">&#8594;</button>
                    </div>
                </div>

                <div className="text-center mt-4">
                    <button id="confirmBtn" className="btn btn-warning px-5 py-2 rounded-pill">✔</button>
                </div>
            </div>
            <nav className="navbar fixed-bottom"
                 style={{backgroundColor: "#546FF1", height: "60px", borderRadius: "12px 12px 0 0", position: "absolute"}}>
                <div className="container-fluid d-flex justify-content-center gap-4">
                    <button className="btn btn-link nav-icon-small text-white" type="button">
                        <i className="fa-regular fa-calendar"></i>
                    </button>
                    <button className="btn btn-link nav-icon-small text-white" type="button">
                        <i className="fa-solid fa-compass"></i>
                    </button>
                    <button className="btn btn-link nav-icon-small text-white" type="button">
                        <i className="fa-solid fa-user"></i>
                    </button>
                </div>
            </nav>
        </>
    );
}