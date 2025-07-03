import React, { useEffect, useState } from "react";
import Navbar from "./NavbarComp";
import {Link} from "react-router-dom";


/*Anfrage mit fetch("settings/times", methode: "GET")
...
*/

/*Antwort nach fetch*/
const dataWeekdays = {
    weekdays: [
        { id: 1, name: "Montag" },
        { id: 2, name: "Dienstag" },
        { id: 3, name: "Mittwoch" },
        { id: 4, name: "Donnerstag" },
        { id: 5, name: "Freitag" },
        { id: 6, name: "Samstag" },
        { id: 7, name: "Sonntag" }
    ],
    hours: Array.from({ length: 24 }, (_, i) => i)
}

/*Anfrage nach Nutzerdaten fetch("settings/", methode: GET)
...
*/

/*Antwort nach fetch*/
const userData = {
    times: [
        {
            weekday: "Montag",
            hours: [9, 10, 11, 13, 14, 15],
        },
        {
            weekday: "Mittwoch",
            hours: [8, 9, 10],
        },
        {
            weekday: "Mittwoch",
            hours: [12, 13, 14, 15, 16],
        }
    ],
};

function WeekdayPicker({ value, onChange }) {
    return (
        <>
            {dataWeekdays.weekdays.map((day) => (
                <button
                    type="button"
                    key={day.id}
                    onClick={() => onChange(day.id)}
                    className="border-0 p-0 rounded-circle d-inline-flex align-items-center justify-content-center"
                    style={{
                        width: "40px",
                        height: "40px",
                        color: value === day.id ? "#fff" : "#546FF1",
                        backgroundColor: value === day.id ? "#FFB347" : "transparent"
                    }}
                >
                    {day.name.substring(0, 2)}
                </button>
            ))}
        </>
    );
}

function TimeRow({ id, startHour, endHour, hourOptions, onTimeChange, onDelete }) {
    return (
        <div className="d-flex align-items-center gap-2 mb-2">
            <select
                className="form-select"
                value={String(startHour).padStart(2, "0") + ":00"}
                onChange={(e) => onTimeChange(id, { startHour: parseInt(e.target.value) })}
            >
                {hourOptions.map((t) => (
                    <option key={t}>{t}</option>
                ))}
            </select>
            <select
                className="form-select"
                value={String(endHour).padStart(2, "0") + ":00"}
                onChange={(e) => onTimeChange(id, { endHour: parseInt(e.target.value) })}
            >
                {hourOptions.map((t) => (
                    <option key={t}>{t}</option>
                ))}
            </select>
            <button
                type="button"
                onClick={() => onDelete(id)}
                className="btn btn-orange border-0 rounded-circle d-inline-flex align-items-center justify-content-center"
                style={{
                    width: "40px",
                    height: "40px",
                }}
            >
                <img src="trash.svg" width="20" height="20" alt=""/>
            </button>
        </div>
    );
}

export default function CalendarForm() {
    const [selectedDayId, setSelectedDayId] = useState(dataWeekdays.weekdays[0].id);
    const [rows, setRows] = useState([]);
    const maxRows = 6;

    //Stunden-Optionen
    const hourOptions = dataWeekdays.hours.map((h) =>
        String(h).padStart(2, "0") + ":00"
    );

    // Einträge beim Wechsel des Wochentags laden
    useEffect(() => {
        const dayName = dataWeekdays.weekdays.find((d) => d.id === selectedDayId)?.name;
        const entries = userData.times
            .filter((entry) => entry.weekday === dayName)
            .map((entry) => ({
                id: Math.random(),
                startHour: entry.hours[0],
                endHour: entry.hours[entry.hours.length - 1]
            }));
        setRows(entries);
    }, [selectedDayId]);

    //Erstellen der Einträge
    const addRow = () => {
        if (rows.length < maxRows) {
            setRows((prev) => [...prev, { id: Math.random(), startHour: 0, endHour: 0 }]);
        }
    };

    //Löschen der Einträge
    const deleteRow = (id) => {
        setRows((prev) => prev.filter((r) => r.id !== id));
    };

    //Updaten der Einträge
    const updateRow = (id, changes) => {
        setRows((prev) => prev.map((r) => (r.id === id ? { ...r, ...changes } : r)));
    };

    return (
        <>
            <div className="position-relative min-vh-100 overflow-hidden">
                {/* Header */}
                <div
                    className="bg-blue text-white px-4 py-4"
                    style={{
                        height: "50vh",
                        borderRadius: "0 0 108px 37px"
                    }}
                >
                    <header className="d-flex justify-content-between align-items-center">
                        <h1 className="fw-bold m-0">Kalender</h1>

                        <div className="d-flex gap-3">
                            <Link to="/calendar"><img src="calendar.svg" width="25" height="25" alt=""/></Link>
                            <Link to="/category"><img src="filter.svg" width="25" height="25" alt=""/></Link>
                        </div>
                    </header>
                </div>

                {/* Centered Card */}
                <div
                    className="card p-4 pb-5 position-absolute top-50 start-50 translate-middle"
                    style={{
                        borderRadius: "23px",
                        width: "90%",
                        maxWidth: "340px",
                        height: "480px" //vorläufig
                    }}
                >
                    {/* Weekday Picker */}
                    <div className="d-flex justify-content-between mb-3">
                        <WeekdayPicker
                            value={selectedDayId}
                            onChange={setSelectedDayId}
                        />
                    </div>
                    <div className="flex-grow-1 overflow-auto">
                        {rows.length > 0 ? (
                            rows.map(({ id, startHour, endHour }) => (
                                <TimeRow
                                    key={id}
                                    id={id}
                                    startHour={startHour}
                                    endHour={endHour}
                                    hourOptions={hourOptions}
                                    onTimeChange={updateRow}
                                    onDelete={deleteRow}
                                />
                            ))
                        ) : (
                            <p className="text-muted">
                                Teile uns gerne mit wann du Zeit hast :)
                            </p>
                        )}
                    </div>

                    <button
                        type="button"
                        onClick={addRow}
                        className="btn btn-orange w-100 rounded-pill mt-3 border-0 d-flex justify-content-center align-items-center"
                        style={{
                            padding: "12px",
                        }}
                    >
                        <img src="plus.svg" width="20" height="20" alt=""/>
                    </button>
                </div>
            </div>
            <Navbar/>
        </>
    );
}