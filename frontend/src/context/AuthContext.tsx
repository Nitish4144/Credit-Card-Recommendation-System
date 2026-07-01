import {
    createContext,
    useContext,
    useEffect,
    useState,
    ReactNode,
} from "react";

import {
    login as loginApi,
    signup as signupApi,
    getCurrentUser,
    User,
} from "../services/auth";

interface AuthContextType {
    user: User | null;
    loading: boolean;

    login: (email:string, password:string) => Promise<User>;
    signup: (email:string, password:string) => Promise<User>;
    logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({children}: {children: ReactNode}) {
    const [user, setUser] = useState<User | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function loadUser() {
            const token = localStorage.getItem("token");

            if(!token){
                setLoading(false);
                return; 
            }

            try{
                const currentUser = await getCurrentUser();
                setUser(currentUser);
            } catch {
                localStorage.removeItem("token");
            }

            setLoading(false);
        }

        loadUser();
    },[]);



    async function login(email: string,password: string) {
            const response = await loginApi(email,password);

            localStorage.setItem( "token",response.access_token);

            const currentUser = await getCurrentUser();
            setUser(currentUser);

            return currentUser;
        }

        async function signup( email: string,password: string ) {
            const user = await signupApi(email,password);
            return user;
        }

        function logout() { 
            localStorage.removeItem("token");
            setUser(null);

            // return ;
        }

        return (
            <AuthContext.Provider
                value={{
                    user,
                    loading,
                    login,
                    signup,
                    logout,
                }}
            >
                {children}
            </AuthContext.Provider>
        );
    }

    export function useAuth() {
    const context = useContext(AuthContext);

    if (!context) {
        throw new Error(
            "useAuth must be used inside AuthProvider"
        );
    }

    return context;
}