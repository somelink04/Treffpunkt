import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import Navbar from "./NavbarComp";

/*
const testData = [
    {
        id: "1",
        name: "Spazieren",
        description: "BeschreibungBeschreibungBeschreibung",
        location: "Amberg",
        date: "20.06.2025",
        participants: [
            { "firstname": "Maria", "surname": "Müller", "age": 29 },
            { "firstname": "John",  "surname": "Doe",     "age": 34 },
            { "firstname": "Lena",  "surname": "Schmidt", "age": 26 }
        ]
    },
    {
        id: 2,
        name: "Tennis",
        description: "BeschreibungBeschreibungBeschreibungBeschreibungBeschreibung",
        location: "Regensburg",
        date: "01.07.2025",
        participants: [
            { firstname: "Klaus",     surname: "Meier",    age: 41 },
            { firstname: "Sophie",    surname: "Becker",   age: 32 },
            { firstname: "Alexandra", surname: "Neumann",  age: 27 },
            { firstname: "David",     surname: "Klein",    age: 36 }
        ]
    },
    {
        id: 3,
        name: "Grillen",
        description: "BeschreibungBeschreibung",
        location: "Nürnberg",
        date: "03.12.2025",
        participants: [
            { firstname: "Emma",    surname: "Fischer",  age: 30 },
            { firstname: "Noah",    surname: "Weber",    age: 38 },
            { firstname: "Mia",     surname: "Richter",  age: 25 },
            { firstname: "Leon",    surname: "Hartmann", age: 33 },
            { firstname: "Chloe",   surname: "Wolf",     age: 29 }
        ]
    }
];
 */

export default function AcceptedEvents() {
    const [events, setEvents] = useState([]);
    const [openDropdownId, setOpenDropdownId] = useState(null);

    useEffect(() => {
        const fetchAcceptedEvents = async () => {
            try {
                //wird der token in LS gespeichert oder muss ich mir den hier erneut holen??
                const token = localStorage.getItem('access_token');

                const response = await fetch('/api/events/accepted', {
                    method: 'GET',
                    headers: {
                        "Authorization": "Bearer " + token,
                    }
                });
                if (!response.ok) {
                    throw new Error('Fehler beim Abrufen der Events');
                }
                const data = await response.json();
                // Stelle sicher, dass alle IDs Strings sind
                const normalized = data.slice(0, 3).map(event => ({
                    ...event,
                    id: event.id.toString(),
                }));
                setEvents(normalized);
            } catch (error) {
                console.error('Fehler beim Laden der Events:', error);
            }
        };
        fetchAcceptedEvents();
    }, []);

    const handleDotsClick = (id) => {
        setOpenDropdownId(prev => (prev === id ? null : id));
    };

    const handleCancel = async (id) => {
        try {
            /*
            const token = localStorage.getItem('token');
            const response = await fetch('/accepted', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ${token}',
                },
                body: JSON.stringify({ id }),
            });
            if (!response.ok) {
                throw new Error('Fehler beim Absagen des Events');
            }
             */

            // Entferne das Event anhand der String-ID
            setEvents(prev => prev.filter(event => event.id.toString() !== id.toString()));
        } catch (error) {
            console.error('Fehler beim Absagen des Events:', error);
        } finally {
            setOpenDropdownId(null);
        }
    };

    return (
        <>
            {/* ─────────── Header ─────────── */}
            <div
                className="bg-blue text-white px-4 py-4 fixed-top"
                style={{ borderRadius: '0 0 37px 37px', zIndex: 1000 }}
            >
                <header className="d-flex justify-content-between align-items-center">
                    <h1 className="fw-bold m-0">Deine Treffen</h1>
                    <div className="d-flex gap-3">
                        <Link to="/calendar">
                            <img src="calendar.svg" width="25" alt="" />
                        </Link>
                        <Link to="/categories">
                            <img src="filter.svg" width="25" alt="" />
                        </Link>
                    </div>
                </header>
            </div>

            {/* ─────────── Cards ─────────── */}
            <main className="pt-5 px-3"
                  style={{
                      position: 'absolute',
                      top: '55px',
                      bottom: '70px',
                      left: 0,
                      right: 0,
                      overflowY: 'auto',
                  }}
            >
                {events.length === 0 ? (
                    <p className="mt-4 text-center text-muted">Du hast keine Events angenommen :(</p>
                ) : (
                    events.map(event => (
                        <div
                            key={event.id}
                            className="card mb-4 position-relative"
                            style={{ borderRadius: '12px' }}
                        >
                            {/* ─────────── Card-Header ─────────── */}
                            <div className="d-flex align-items-center px-3 py-2 justify-content-between">
                                <div className="bg-blue rounded-circle d-flex align-items-center justify-content-center" style={{ width: '40px', height: '40px' }}>
                                    <img src="fill.svg" width="25" height="25" alt="" />
                                </div>
                                <div className="flex-grow-1 px-3">
                                    <h5 className="m-0 fw-bold">{event.name}.</h5>
                                    <p className="m-0 text-muted"><small>am {event.date.slice(0, -5)}</small></p>
                                </div>
                                <div className="d-flex align-items-center justify-content-center" style={{ width: '40px', height: '40px' }}>
                                    <button
                                        type="button"
                                        className="btn border-0 shadow-none"
                                        onClick={() => handleDotsClick(event.id)}
                                    >
                                        <img src="dots.svg" width="25" height="25" alt="Mehr Optionen" />
                                    </button>
                                </div>
                            </div>

                            {/* Dropdown */}
                            {openDropdownId === event.id && (
                                <div className="position-absolute bg-white border shadow-sm" style={{ top: '55px', right: '15px', zIndex: 1100 }}>
                                    <button
                                        type="button"
                                        className="dropdown-item text-danger"
                                        onClick={() => handleCancel(event.id)}
                                    >
                                        Absagen
                                    </button>
                                </div>
                            )}

                            <div className="bg-secondary mb-2 w-100" style={{ height: '190px' }} />
                            <div className="d-flex px-3 gap-2 mb-1 align-items-center">
                                <img src="location-blue.svg" width="24" height="24" alt="Ort" />
                                <span>{event.location}</span>
                            </div>
                            <div className="d-flex px-3 gap-2 mb-1 align-items-center">
                                <img src="users-blue.svg" width="24" height="24" alt="Teilnehmer" />
                                <span>{event.participants.length}</span>
                            </div>
                            <p className="mt-3 px-3 pb-2 text-muted text-wrap">{event.description}</p>
                        </div>
                    ))
                )}
            </main>
            <Navbar />
        </>
    );
}