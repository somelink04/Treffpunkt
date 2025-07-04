import React, { useState, useEffect } from "react";
import Navbar from "./NavbarComp";

// Testdaten zum Carousel-Navigieren
const testSlides = [
    {
        title: "Erstes Treffen",
        day: "01.07.2025",
        address: "Amberg",
        participants: 5,
    },
    {
        title: "Zweites Treffen",
        day: "02.07.2025",
        address: "Nürnberg",
        participants: 10,
    },
    {
        title: "Drittes Treffen",
        day: "03.07.2025",
        address: "München",
        participants: 8,
    },
];

export default function DashboardForm() {
    // Initialisierung mit Testdaten
    const [slides, setSlides] = useState(
        testSlides.map(slide => ({ ...slide, confirmed: false }))
    );
    const [currentIndex, setCurrentIndex] = useState(0);

    const prevSlide = () => {
        setCurrentIndex(prev => (prev > 0 ? prev - 1 : 0));
    };

    const nextSlide = () => {
        setCurrentIndex(prev => (prev < slides.length - 1 ? prev + 1 : prev));
    };

    const toggleConfirm = () => {
        setSlides(prevSlides => {
            const copy = [...prevSlides];
            copy[currentIndex].confirmed = !copy[currentIndex].confirmed;
            return copy;
        });
    };

    const slide = slides[currentIndex];

    return (
        <>
            {/* Header */}
            <div className="bg-blue text-white px-4 py-4 mb-5" style={{ borderRadius: '0 0 37px 37px' }}>
                <header className="d-flex justify-content-center">
                    <h1 className="fw-bold m-0">Treffen</h1>
                </header>
            </div>

            {/* Carousel */}
            <div className="container mt-4 text-white">
                <div className="position-relative text-center mt-4">
                    <button
                        onClick={prevSlide}
                        disabled={currentIndex === 0}
                        className="btn btn-transparent position-absolute start-0 top-50 translate-middle-y"
                    >
                        <img src="chevron-left.svg" width="24" height="24" alt="Zurück" />
                    </button>

                    <div className="slide-card mx-auto">
                        <h1 className="fw-bold">{slide.title}</h1>
                        <p>📅 {slide.day}</p>
                        <p>📍 {slide.address}</p>
                        <p>👥 {slide.participants}</p>
                        {slide.confirmed && (
                            <p className="text-success fw-semibold mt-3">✅ Zugestimmt</p>
                        )}
                    </div>

                    <button
                        onClick={nextSlide}
                        disabled={currentIndex === slides.length - 1}
                        className="btn btn-transparent position-absolute end-0 top-50 translate-middle-y"
                    >
                        <img src="chevron-right.svg" width="24" height="24" alt="Weiter" />
                    </button>
                </div>

                <div className="text-center mt-4">
                    <button
                        onClick={toggleConfirm}
                        className="btn btn-orange w-100 rounded-pill border-0 d-flex justify-content-center align-items-center"
                        style={{ padding: "12px" }}
                    >
                        <img src="check.svg" width="24" height="24" alt="Bestätigen" />
                    </button>
                </div>
            </div>
            <Navbar />
        </>
    );
}