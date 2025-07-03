import React from 'react';
import ReactDOM from 'react-dom/client';
import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import LoginFront from "./LoginFront";
import CalendarFront from "./CalendarFront";
import DashboardFront from "./DashboardFront"
import CategoryFront from "./CategoryFront";
import SettingsFront from "./SettingsFront";
import AcceptedFront from "./AcceptedFront";

export default function App(){
    return (
            <Routes>
                <Route index element={<Navigate to="/login" />} />
                <Route path='/login' element={<LoginFront />} />
                <Route path='/calendar' element={<CalendarFront />} />
                <Route path='/profile' element={<SettingsFront />} />
                <Route path='/categories' element={<CategoryFront />} />
                <Route path='/dashboard' element={<DashboardFront />} />
                <Route path='/accepted' element={<AcceptedFront />} />
            </Routes>
    );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <BrowserRouter>
        <App />
    </BrowserRouter>
);