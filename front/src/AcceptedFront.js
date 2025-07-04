import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import Navbar from "./NavbarComp";

export default function AcceptedEvents() {
    const [events, setEvents] = useState([]);

    useEffect(() => {
        const fetchAcceptedEvents = async () => {
            try {
                //wird der token in LS gespeichert oder muss ich mir den hier erneut holen??
                const token = localStorage.getItem('token');

                const response = await fetch('/accepted', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`,
                    }
                });

                if (!response.ok) {
                    throw new Error('Fehler beim Abrufen der Events');
                }

                const data = await response.json();
                setEvents(data.slice(0, 3)); // nur die ersten 3 anzeigen
            } catch (error) {
                console.error('Fehler beim Laden der Events:', error);
            }
        };

        fetchAcceptedEvents();
    }, []);

    return (
        <>
            {/* ─────────── Header ─────────── */}
                <div
                    className="bg-blue text-white px-4 py-4 mb-5 fixed-top"
                    style={{
                        borderRadius: '0 0 37px 37px'
                    }}
                >
                    <header className="d-flex justify-content-between align-items-center">
                        <h1 className="fw-bold m-0">Deine Treffen</h1>

                        <div className="d-flex gap-3">
                            <Link to="/calendar"><img src="calendar.svg" width="25" height="25" alt=""/></Link>
                            <Link to="/category"><img src="filter.svg" width="25" height="25" alt=""/></Link>
                        </div>
                    </header>
                </div>

            {/* ─────────── Centered Card ─────────── */}
                <main className=" position-absolute top-50 start-50 translate-middle">
                    <div
                        className="card p-4 pb-5"
                        style={{
                            borderRadius: "23px",
                            width: "90%",
                            maxWidth: "340px",
                            height: "480px" //vorläufig
                        }}
                    >
                        <div className="accepted-events">
                            <h2>Angenommene Events</h2>
                            {events.length === 0 ? (
                                <p>Keine Events gefunden.</p>
                            ) : (
                                events.map(event => (
                                    <div key={event.id} className="event-card">
                                        <h3>{event.name}</h3>
                                        <p>{event.description}</p>
                                        <p><strong>Ort:</strong> {event.location}</p>
                                        <p>
                                            <strong>Datum:</strong> {event.date ? new Date(event.date).toLocaleString() : 'Unbekannt'}
                                        </p>
                                    </div>
                                ))
                            )}
                        </div>
                    </div>
                </main>
                <Navbar/>
        </>
    );
}