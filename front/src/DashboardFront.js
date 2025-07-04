import React, {useEffect, useState} from "react";
import Navbar from "./NavbarComp";
import { Link } from "react-router-dom";

/*Antwort nach fetch("/" methode: GET )*/
const testSlides = [
    {
        id: 1,
        name: "Fußball",
        description: "Eine beliebte Teamsportart, die weltweit gespielt wird.",
        location: "Amberg",
        date: "01.07.2025"
    },
    {
        id: 2,
        name: "Kochen",
        description: "Die Kunst der Zubereitung von Speisen und kulinarischen Gerichten.",
        location: "Nürnberg",
        date: "20.06.2025"
    },
    {
        id: 3,
        name: "Schwimmen",
        description: "Eine körperlich anspruchsvolle Wassersportart.",
        location: "Berlin",
        date: "03.12.2025"
    }
];

export default function DashboardForm() {
    const mapSlides = (slides) => {
        return slides.map((slide) => ({ ...slide, confirmed: false }))
    };

    const [slides, setSlides] = useState([]);
    const [currentIndex, setCurrentIndex] = useState(0);

    useEffect(() => {
        const fetchData = async () => {
            await fetch("api/events/suggestion", {
                method: "GET",
                headers: {
                    "Authorization": `Bearer ${localStorage.getItem("access_token")}`
                }
            })
                .then(res => res.json())
                .then(res => {
                    setSlides(mapSlides(res));
                })
        }
        fetchData()
    },[]);

    // Infinite wrap-around
    const prevSlide = () => {
        setCurrentIndex((prev) => (prev > 0 ? prev - 1 : slides.length - 1));
    };
    const nextSlide = () => {
        setCurrentIndex((prev) => (prev < slides.length - 1 ? prev + 1 : 0));
    };


    const handleCheck = () => {
        const removed = slides[currentIndex];
        console.log(JSON.stringify(removed));

        const newSlides = slides.filter((_, idx) => idx !== currentIndex);

        let newIndex = currentIndex;
        if (newSlides.length === 0) {
            newIndex = 0;
        } else if (newIndex >= newSlides.length) {
            newIndex = 0;
        }
        setSlides(newSlides);
        setCurrentIndex(newIndex);
    };

    if (slides.length === 0) {
        return (
            <>
                <div className="bg-blue text-white px-4 py-4 mb-5" style={{ borderRadius: "0 0 37px 37px" }}>
                    <header className="d-flex justify-content-between align-items-center">
                        <h1 className="fw-bold m-0">Für dich</h1>
                    </header>
                </div>
                <div className="container mt-4 text-center ">
                    <h5 className="fw-bold text-muted">Neue Events gibt es nächsten Sonntag :)</h5>
                </div>
                <Navbar />
            </>
        );
    }

    const slide = slides[currentIndex];
    return (
        <>
            {/* ─────────── Header ─────────── */}
            <div className="bg-blue text-white px-4 py-4 mb-5" style={{ borderRadius: "0 0 37px 37px" }}>
                <header className="d-flex justify-content-between align-items-center">
                    <h1 className="fw-bold m-0">Für dich</h1>
                    <div className="d-flex gap-3">
                        <Link to="/calendar">
                            <img src="calendar.svg" width="25" height="25" alt="" />
                        </Link>
                        <Link to="/categories">
                            <img src="filter.svg" width="25" height="25" alt="" />
                        </Link>
                    </div>
                </header>
            </div>

            <div className="container">
                <div className="position-relative text-center mt-4">

                    {/* Linker Button */}
                    <button
                        onClick={prevSlide}
                        className="btn btn-orange border-0 rounded-circle d-inline-flex align-items-center justify-content-center position-absolute start-0 top-50 translate-middle-y"
                        style={{ zIndex: 10, width: "45px", height: "45px" }}
                    >
                        <img src="chevron-left.svg" width="24" height="24" alt="" />
                    </button>

                    {/* ─────────── Card ─────────── */}
                    <div
                        className="card shadow mx-auto pt-5 d-flex flex-column align-items-center justify-content-center"
                        style={{ borderRadius: "23px", width: "90%", maxWidth: "340px", height: "480px" }}
                    >
                        <h1 className="display-1 fw-bold mt-4 mb-3">{slide.name}</h1>
                        <div>
                            <div className="d-flex gap-2 mb-2">
                                <img src="calendar-blue.svg" width="24" height="24" alt="" />
                                <span>{slide.date}</span>
                            </div>

                            <div className="d-flex gap-2 mb-2">
                                <img src="location-blue.svg" width="24" height="24" alt="" />
                                <span>{slide.location}</span>
                            </div>

                            <div className="d-flex gap-2">
                                <img src="users-blue.svg" width="24" height="24" alt="" />
                                <span>{slide.participants}</span> {/* kann gelöscht werden falls nicht benötigt */}
                            </div>
                        </div>
                        <div
                            className="mt-5 px-5"
                             style={{
                             }}>
                            <span className="text-muted text-wrap">{slide.description}</span>
                        </div>
                    </div>

                    {/* Rechter Button */}
                    <button
                        onClick={nextSlide}
                        className="btn btn-orange border-0 rounded-circle d-inline-flex align-items-center justify-content-center position-absolute end-0 top-50 translate-middle-y"
                        style={{ zIndex: 10, width: "45px", height: "45px" }}
                    >
                        <img src="chevron-right.svg" width="24" height="24" alt="" />
                    </button>
                </div>

                <div className="mt-4">
                    <button
                        onClick={handleCheck}
                        className="btn btn-orange w-100 rounded-pill border-0 d-flex justify-content-center align-items-center"
                        style={{ padding: "12px" }}
                    >
                        <img src="check.svg" width="24" height="24" alt="Check" />
                    </button>
                </div>
            </div>

            <Navbar />
        </>
    );
}