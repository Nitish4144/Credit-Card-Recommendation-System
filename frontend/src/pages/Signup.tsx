import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Signup() {
    const { signup } = useAuth();

    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleSubmit: React.FormEventHandler<HTMLFormElement> = async (e) => {
        e.preventDefault();

        try {
            await signup(email, password);
            navigate("/login");
        } catch {
            setError("Signup failed");
        }
    };

    return (
        <div
            style={{
                maxWidth: 400,
                margin: "100px auto",
            }}
        >
            <h2>Create Account</h2>

            <form onSubmit={handleSubmit}>
                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />

                <br />
                <br />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <br />
                <br />

                <button type="submit">Signup</button>
            </form>

            {error && <p>{error}</p>}

            <Link to="/login">
                Already have an account?
            </Link>
        </div>
    );
}