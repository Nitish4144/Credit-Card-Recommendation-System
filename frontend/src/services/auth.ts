import api from "./api";

export interface LoginResponse {
    access_token: string;
    token_type: string;
}

export interface User {
    id: number;
    email: string;
    created_at: string;
}

export async function signup(
    email: string,
    password: string
): Promise<User> {

    const response = await api.post(
        "/auth/signup",
        {
            email,
            password
        }
    );

    return response.data;
}

export async function login(
    email: string,
    password: string
): Promise<LoginResponse> {

    const form = new URLSearchParams();

    form.append("username", email);
    form.append("password", password);

    const response = await api.post(
        "/auth/login",
        form,
        {
            headers: {
                "Content-Type":
                    "application/x-www-form-urlencoded"
            }
        }
    );

    return response.data;
}

export async function getCurrentUser(): Promise<User> {

    const response = await api.get(
        "/auth/me"
    );

    return response.data;
}