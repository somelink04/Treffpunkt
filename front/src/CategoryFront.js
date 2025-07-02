import React, { useState, useEffect } from 'react';
import "bootstrap-icons/font/bootstrap-icons.css";
import Button from 'react-bootstrap/Button'; // Import React-Bootstrap Button
import Row from 'react-bootstrap/Row'; // Import React-Bootstrap Row
import Col from 'react-bootstrap/Col'; // Import React-Bootstrap Col
import Container from 'react-bootstrap/Container';
import {
    ArrowLeft,
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
    Globe2,
    Headphones,
    Suitcase2,
    Palette
} from "react-bootstrap-icons";



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
        fetch("settings/categories/...") // oder: "https://your-api.com/...."
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

    return (
        <Container>
            <Row className="bg-primary text-white align-items-center py-2 px-3">
                <Col xs="auto">
                    <Button variant="primary">
                        <ArrowLeft />
                    </Button>
                </Col>
                <Col xs="auto">
                    {/* leer oder Platzhalter für Ausrichtung */}
                </Col>
                <Col className="text-center fw-bold">
                    Deine Interessen
                </Col>
            </Row>
            {/* Spalten und Zeilen mit Kategorien Dynamisch erzeugen */}
            <Row className="g-3 mt-4">
                {interests.map((item, idx) => (
                    <Col xs={4} key={idx}>
                        <button
                            className={`btn w-100 py-3 mb-2 text-white rounded ${
                                selected.includes(item.name) ? "bg-primary" : "bg-info"
                            }`}
                            onClick={() => toggleCategory(item.name)}
                        >
                            {item.icon}
                            <span className="d-block mt-1">{item.name}</span>
                        </button>
                    </Col>
                ))}
            </Row>
            {/* Speichern-Button */}
            <Row className="text-center mt-4">
                <Button className="btn btn-warning rounded-pill px-5">
                    <i className="bi bi-save" /> Speichern
                </Button>
            </Row>
        </Container>
    );
}