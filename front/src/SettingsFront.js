import React, { useState } from "react";

export default function SettingsPage() {
    const [username, setUsername] = useState("");
    const [interests, setInterests] = useState("");
    const [timezone, setTimezone] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        alert('Einstellungen gespeichert!');
    };

    return (
        <>
            {/* Top Navbar */}
            <nav
                className="navbar navbar-light px-3 d-flex justify-content-between align-items-center"
                style={{ backgroundColor: '#546FF1', height: '7vh', borderRadius: '0 0 5px 5px' }}
            >
                <h1 className="navbar-brand text-white mb-0" style={{ fontSize: '1.8rem', fontWeight: 600 }}>
                    Einstellungen
                </h1>
                <div className="d-flex gap-3">
                    <button className="btn text-white p-0">
                        <i className="fa-solid fa-calendar-days"></i>
                    </button>
                    <button className="btn text-white p-0">
                        <i className="fa-solid fa-filter"></i>
                    </button>
                </div>
            </nav>

            {/* Settings Content */}
            <div className="container mt-4 mb-5" style={{ height: '80vh' }}>
                <div
                    className="card shadow p-4 d-flex flex-column justify-content-between"
                    style={{ backgroundColor: '#546FF1', borderRadius: '2.8rem', height: '100%' }}
                >
                    <div>
                        <h2 className="mb-4 text-white" style={{ fontSize: '1.7rem' }}>
                            Profilinformationen
                        </h2>

                        {/* Display User Info */}
                        <div className="mb-3 text-white">
                            <label className="form-label fw-bold" style={{ fontSize: '1.3rem' }}>
                                Benutzername:
                            </label>
                            <p style={{ fontSize: '1.1rem' }}>{username}</p>
                        </div>

                        <div className="mb-3 text-white">
                            <label className="form-label fw-bold" style={{ fontSize: '1.3rem' }}>
                                Interessen:
                            </label>
                            <p style={{ fontSize: '1.1rem' }}>{interests}</p>
                        </div>

                        <div className="mb-3 text-white">
                            <label className="form-label fw-bold" style={{ fontSize: '1.3rem' }}>
                                Wochenzeiten:
                            </label>
                            <p style={{ fontSize: '1.1rem' }}>{timezone}</p>
                        </div>
                    </div>

                    {/* Editable Fields */}
                    <form onSubmit={handleSubmit}>
                        <hr className="border-light" />

                        <div className="mb-3">
                            <button type="button" className="btn btn-light w-100 rounded-pill">
                                Hobbys ändern
                            </button>
                        </div>

                        <div className="mb-3">
                            <button type="button" className="btn btn-light w-100 rounded-pill">
                                PLZ ändern
                            </button>
                        </div>

                        <div className="mb-3">
                            <button type="button" className="btn btn-light w-100 rounded-pill">
                                Uhrzeit ändern
                            </button>
                        </div>

                        <button
                            type="submit"
                            className="btn w-100 rounded-pill"
                            style={{ backgroundColor: '#FFC107' }}
                        >
                            Speichern
                        </button>
                    </form>
                </div>
            </div>

            {/* Bottom Navbar */}
            <nav
                className="navbar fixed-bottom"
                style={{ backgroundColor: '#546FF1', height: '7vh', borderRadius: '5px 5px 0 0' }}
            >
                <div className="container-fluid d-flex justify-content-center gap-4">
                    <button className="btn text-white">
                        <i className="fa-regular fa-calendar"></i>
                    </button>
                    <button
                        className="btn text-white d-flex justify-content-center align-items-center "

                    >
                        <i className="fa-solid fa-compass"></i>
                    </button>
                    <button
                        className="btn text-white d-flex justify-content-center align-items-center rounded-circle"
                        style={{ backgroundColor: '#FFC107', width: '40px', height: '40px' }}
                    >
                        <i className="fa-solid fa-user"></i>
                    </button>
                </div>
            </nav>
        </>
    );
}