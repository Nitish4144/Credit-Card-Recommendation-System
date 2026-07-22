import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";


export default function Login() {
    const { login } = useAuth();

    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleSubmit: React.FormEventHandler<HTMLFormElement> = async (e) => {
        e.preventDefault();
        try{
            await login(email, password);
            navigate("/dashboard");
        } catch{
            setError("Invalid email or password");
        }
    };

    return (
        <div
            style= {{
                color: "white",
                textAlign: "center",
                maxWidth: 400,
                margin: "100px auto",
            }}
            >

            <h2>Login</h2>

            <form onSubmit={handleSubmit}>
                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                    />

                    <br />
                    <br />

                    <input
                        type="password"
                        placeholder="Password"  
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        />

                        <br />
                        <br />
                        <button type ="submit">Login</button>
            </form>

            {error && <p style={{ color: "red" }}>{error}</p>}
            <Link to="/signup">Create Account</Link>
        </div>
    )
}