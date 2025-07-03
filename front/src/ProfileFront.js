import React, { useState, useEffect } from "react";
import Navbar from "./NavbarComp";
import { Link } from "react-router-dom";

/*Anfrage mit fetch("/settings", methode: "GET")
...
*/

const testData = {
    user: {
        firstname: "Heinz",
        surname: "Müller",
        username: "Heinz61",
        dayofbirth: "21.07.2003",
        email: "heinz.müller60@beispiel.de",
        gender: "männlich",
        region: "Amberg"
    }
};
export default function SettingsPage() {
    const [interests, setInterests] = useState();
    const [timezone, setTimezone] = useState();
    const { firstname, surname, username, dayofbirth, region } = testData.user;
    const initial = firstname.charAt(0).toUpperCase();

    const handleSubmit = (e) => {
        e.preventDefault();
        alert("Einstellungen gespeichert!");
    };

    return (
        <>
            {/* Header */}
            <div
                className="bg-blue text-white px-4 py-4"
                style={{ height: "50vh", borderRadius: "0 0 108px 37px" }}
            >
                <header className="d-flex justify-content-between align-items-center">
                    <h1 className="fw-bold m-0">{username}</h1>
                    <div className="d-flex gap-3">
                        <Link to="/calendar">
                            <img src="calendar.svg" width="25" height="25" alt="Kalender" />
                        </Link>
                        <Link to="/category">
                            <img src="filter.svg" width="25" height="25" alt="Filter" />
                        </Link>
                    </div>
                </header>
            </div>

            {/* Profile Card */}
            <div
                className="card p-4 pb-5 position-absolute top-50 start-50 translate-middle"
                style={{
                    borderRadius: "23px",
                    width: "90%",
                    maxWidth: "340px",
                    height: "70vh",
                }}
            >
                <div className="position-relative mb-4" style={{ top: "-80px" }}>
                    <div
                        className="rounded-circle bg-danger text-white d-flex align-items-center justify-content-center mx-auto"
                        style={{
                            width: "130px",
                            height: "130px",
                            fontSize: "48px",
                            lineHeight: "120px",
                            border: "4px solid #546FF1",
                        }}
                    >
                        {initial}
                    </div>
                    <h5 className="mt-2 fw-bold text-center">
                        {firstname} {surname}
                    </h5>
                </div>
                <div style={{ marginTop: "-70px" }} >
                    <div className="d-flex align-items-center ">
                        <img src="calendar.svg" width="25" height="25" className="me-2" alt="Geburtstag" />
                        <span>{dayofbirth}</span>
                    </div>

                    <div className="d-flex align-items-center">
                        <img src="location.svg" width="25" height="25" className="me-2" alt="Region" />
                        <span>{region}</span>
                    </div>
                </div>

                {/* Editable Fields */}
                {/* Keine Ahnung bro nicht von mir*/}
                <form onSubmit={handleSubmit}>
                    <hr className="border-light"/>

                    <div className="mb-3">
                        <button
                            type="button"
                            className="btn btn-light w-100 rounded-pill"
                            onClick={() => {
                                const newInterests = prompt("Neue Interessen eingeben:", interests);
                                if (newInterests !== null) setInterests(newInterests);
                            }}
                        >
                            Hobbys ändern
                        </button>
                    </div>

                    <div className="mb-3">
                        <button
                            type="button"
                            className="btn btn-light w-100 rounded-pill"
                            onClick={() => {
                                const newRegion = prompt("Neue PLZ/Region eingeben:", region);
                                if (newRegion !== null) setTimezone(newRegion);
                            }}
                        >
                            PLZ ändern
                        </button>
                    </div>

                    <div className="mb-3">
                        <button
                            type="button"
                            className="btn btn-light w-100 rounded-pill"
                            onClick={() => {
                                const newTimezone = prompt("Neue Uhrzeit/Wochenzeiten eingeben:", timezone);
                                if (newTimezone !== null) setTimezone(newTimezone);
                            }}
                        >
                            Uhrzeit ändern
                        </button>
                    </div>

                    <button
                        type="submit"
                        className="btn btn-orange w-100 rounded-pill mt-3 border-0 d-flex justify-content-center align-items-center"
                    >
                        Speichern
                    </button>
                </form>
            </div>


            <Navbar/>
        </>
    );
}