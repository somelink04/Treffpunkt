import React, { useState, useEffect } from 'react';
import "bootstrap-icons/font/bootstrap-icons.css";
import Navbar from "./NavbarComp";
import {Link} from "react-router-dom";

import {
    Camera,
    Book,
    Film,
    Basket,
    MusicNoteBeamed,
    Mic,
    Controller,
    Cup,
    Sun,
    Tools,
    Bag,
    Suitcase2,
    Palette
} from "react-bootstrap-icons";
import Scrollspy from "bootstrap/js/src/scrollspy";



const interests = [
    { name: "Filme", icon: <Film /> },
    { name: "Lesen", icon: <Book /> },
    { name: "Fotografie", icon: <Camera /> },
    { name: "Reisen", icon: <Suitcase2 /> },
    { name: "Kaffee", icon: <Cup /> },
    { name: "Basketball", icon: <Basket /> },
    { name: "Musik", icon: <MusicNoteBeamed /> },
    { name: "Singen", icon: <Mic /> },
    { name: "Gaming", icon: <Controller /> },
    { name: "Shoppen", icon: <Bag /> },
    { name: "Picknicken", icon: <Sun /> },
    { name: "Werken", icon: <Tools /> },
    { name: "Lorem", icon: <Palette /> },
    { name: "Lorem", icon: <Palette /> },
    { name: "Lorem", icon: <Palette /> },
];



export default function CategoryForm() {

    const [selected, setSelected] = useState([]);
    const [categories, setCategories] = useState([]);

    {/*Holen der Daten (Kategorien) von der Datenbank*/}
    //https://dev.to/antdp425/react-fetch-data-from-api-with-useeffect-27le
    useEffect(() => {
        fetch("api/settings/categories", {
            method: 'GET',
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('access_token')
            }
        })
            .then((response) => response.json())
            .then((data) => setCategories(data))
            .catch((err) => console.error("Fehler beim Laden der Kategorien:", err));
    }, []);

    {/*Toggle-Funktion*/}
    {/*https://stackoverflow.com/questions/69497702/how-to-keep-button-highlighted-when-clicked-in-react*/}
    const toggleCategory = (interest) => {
        setSelected((prev) =>
            prev.includes(interest)
                ? prev.filter((item) => item !== interest) // abwählen
                : [...prev, interest]                      // auswählen
        );
    };

    const handleSave = () => {
        console.log("Speichern:", selected);
        // Hier kommt fetch-Aufruf zum Speichern
    };

    const iconMap = {};
    interests.forEach((item) => {
        iconMap[item.name] = item.icon;
    });

    return (
        <>
            {/* Header */}
            <div
                className="bg-blue text-white px-4 py-4 fixed-top"
                style={{ borderRadius: '0 0 37px 37px', zIndex: 1000 }}
            >

                <header className="d-flex justify-content-between align-items-center">
                    <h1 className="fw-bold m-0">Deine Interessen</h1>

                    <div className="d-flex gap-3">
                        <Link to="/calendar"><img src="calendar.svg" width="25" height="25" alt=""/></Link>
                        <Link to="/categories"><img src="filter.svg" width="25" height="25" alt=""/></Link>
                    </div>
                </header>
            </div>

            <main>
            {/* Zentrale Inhalts-Karte */}
            <div className="content-card">
                {/* Scrollbares Grid für die Kategorien */}
                <div className="category-grid">
                    {categories.map((category) => (
                        <button
                            key={category.id} // Besser die ID aus der DB als den Index verwenden
                            className={`category-button ${
                                selected.includes(category.name) ? "selected" : ""
                            }`}
                            onClick={() => toggleCategory(category.name)}
                        >
                            {/* Dynamisches Icon-Mapping */}
                            {iconMap[category.name] || <Palette/>}
                            <span>{category.name}</span>
                        </button>
                    ))}

                    {/* Speichern-Button am unteren Rand der Karte */}
                    <button
                        type="button"
                        onClick={handleSave}
                        className="btn btn-orange w-100 rounded-pill mt-3 border-0 d-flex justify-content-center align-items-center" style={{
                        padding: "12px",
                    }}
                    >
                        <img src="save.svg" width="20" height="20" alt=""/>
                    </button>
                </div>
            </div>
            </main>
        <Navbar/>
        </>
    );
}