import React, { useState } from 'react';
import '../../../treffpunkt/src/style/LoginFront.css';

//Funktion LoginForm definieren
export default function LoginForm() {
    //Array Destructuring
    const [email, setEmail] = useState(''); //setEmail ist eine Funktion zum ändern des Wertes, useState('') bedeutet Eingabefeld ist leer
    const [password, setPassword] = useState('');

    const handleLogin = (e) => {
        e.preventDefault();     //Verhindert Neuladen der Seite nach dem Absenden
        alert(`Login mit: ${email} / ${password}`);
    };

    const handleForgotPassword = () => {
        alert('Kennwort vergessen');
    };

    const handleGuest = () => {
        alert('Als Gast anmelden');
    };

    return (
        <div className="login-container">
            <form> onSubmit={handleLogin}
            <div className="login-header">
                <h1>Treffpunkt.</h1>
            </div>

            <div className="login-card">
                <input
                    type="email"
                    placeholder="E-Mail"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}  //onChange reagiert auf Eingaben, e.target.value enthält den neuen Text
                    required
                />

                <input
                    type="password"
                    placeholder="Passwort"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <p style={{ color: 'red' }}>
                    {email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) ? 'Ungültige E-Mail-Adresse' : ''}
                </p>

                <button type="submit">Anmelden</button>

                <button type = "button" onClick={handleForgotPassword}>Passwort vergessen?</button>
            </div>

            <div className="separator">
                <span>Noch keinen Konto?</span>
            </div>

            <button type="button" onClick={handleGuest} className="guest-button">Gast</button>
            </form>
        </div>
    );
}