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


/*
const interests = [
    {
        id: 1,
        name: "Filme",
        description: "Alles rund um das Thema Kino und Filme schauen."
    },
    {
        id: 2,
        name: "Lesen",
        description: "Bücher, Magazine und Artikel lesen."
    },
    {
        id: 3,
        name: "Fotografie",
        description: "Momente mit der Kamera festhalten."
    },
    {
        id: 4,
        name: "Reisen",
        description: "Neue Orte und Kulturen entdecken."
    },
    {
        id: 5,
        name: "Kaffee",
        description: "Gemütlich einen Kaffee trinken und plaudern."
    },
    {
        id: 6,
        name: "Basketball",
        description: "Ein paar Körbe werfen oder ein Spiel anschauen."
    },
    {
        id: 7,
        name: "Musik",
        description: "Konzerte besuchen oder selbst Musik machen."
    },
    {
        id: 8,
        name: "Singen",
        description: "Karaoke oder gemeinsames Singen."
    },
    {
        id: 9,
        name: "Gaming",
        description: "Videospiele auf Konsole oder PC."
    },
    {
        id: 10,
        name: "Shoppen",
        description: "Ein Einkaufsbummel durch die Stadt."
    },
    {
        id: 11,
        name: "Picknicken",
        description: "Im Park entspannen mit gutem Essen."
    },
    {
        id: 12,
        name: "Werken",
        description: "Heimwerken, Basteln und Bauen."
    },
    {
        id: 13,
        name: "Essen",
        description: "Neue Restaurants ausprobieren oder gemeinsam kochen."
    }
];
 */


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

            <main style={{marginTop: '100px'}}>
            {/* Zentrale Inhalts-Karte */}
            <div className="px-4 py-4 mb-5">
                {/* Scrollbares Grid für die Kategorien */}
                <div className="row">
                    {categories.map((category) => (
                        <div className="col-4 mb-3" key={category.id}>
                            <button
                                style={{borderRadius: '10px'}}
                                className={`category-button w-100 py-3 rounded-4 d-flex flex-column align-items-center justify-content-center border-0  ${
                                    selected.includes(category.name) ? "bg-blue text-white" : "bg-info text-white"
                                }`}
                                onClick={() => toggleCategory(category.name)}
                            >
                                <div className="mb-2 ">
                                    {iconMap[category.name] || <Sun size={28} />}
                                </div>
                                <span>{category.name}</span>
                            </button>
                        </div>
                    ))}
                </div>
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
            </main>
        <Navbar/>
        </>
    );
}