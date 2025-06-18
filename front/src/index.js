import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import LoginFront from "./LoginFront";
import TestLandingPage from "./TestLandingPage";

export default function App(){
    return (
        <BrowserRouter>
            <Routes>
                <Route path='/' element={<LoginFront />} />
                <Route path='/Test' element={<TestLandingPage />} />
            </Routes>
        </BrowserRouter>
    );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <App />
);