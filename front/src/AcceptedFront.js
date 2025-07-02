import React, {useEffect, useState} from 'react';

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
                        <p><strong>Datum:</strong> {event.date ? new Date(event.date).toLocaleString() : 'Unbekannt'}
                        </p>
                    </div>
                ))
            )}
        </div>
    );
}