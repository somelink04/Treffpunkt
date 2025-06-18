import React, { useState } from "react";
import  { useNavigate } from 'react-router-dom';
import "./style/LoginFront.css";

export default function LoginForm() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    const hashPassword = async (pw) => {
        const encoder = new TextEncoder();
        const data = encoder.encode(pw);
        const hashBuffer = await window.crypto.subtle.digest("SHA-256", data);
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        return hashArray.map((b) => b.toString(16).padStart(2, "0")).join("");
    };

    const handleLogin = async (e) => {
        e.preventDefault();

        console.log("Eingabe Benutzername:", username);
        console.log("Eingabe Passwort:", password);

        const hash = await hashPassword(password);
        console.log("gehashtes Passwort:", hash);

        // LOGIN-REQUEST
        const loginRes = await fetch("auth/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password: hash})
        });

        if (!loginRes.ok){
            console.error("Login fehlgeschlagen:", loginRes.status);
            return;
        }

        const loginData = await loginRes.json();
        const at = loginData.access_token;
        console.log("Access-Token:", at);

        // IDENTITY-REQUEST
        const identRes = await fetch("auth/ident", {
            method: "GET",
            headers: { "Authorization": "Bearer " + at }
        });

        if (!identRes.ok){
            console.error("Ident-Aufruf fehlgeschlagen:", identRes.status);
            return;
        }

        const identData = await identRes.json();
        console.log("Ident-Antwort:", identData);
        navigate("/home");
    };

    return (
        <>
            <header
                className="d-flex justify-content-center align-items-center bg-blue"
                style={{
                    height: "382px",
                    borderBottomLeftRadius: "37px",
                    borderBottomRightRadius: "108px",
                    marginBottom: "-4.5rem"
                }}>
                <h1 className="display-1 text-white fw-bold m-0">Treffpunkt.</h1>
            </header>

            <div
                className="card d-grid p-4 pb-5 m-auto"
                style={{
                    borderRadius: "23px",
                    maxWidth: "340px"
                }}>
                <form onSubmit={handleLogin} className="d-grid gap-3">
                    <input
                        className="form-control"
                        type="text"
                        placeholder="Benutzername"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                    <input
                        className="form-control"
                        type="password"
                        placeholder="Passwort"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                    <button
                        className="btn btn-orange w-100"
                        type="submit"
                    >
                        Anmeldung
                    </button>
                </form>
            </div>
        </>
    );
}