import { useState } from "react";
import api from "../services/api";

function UploadForm() {
    const [file, setFile] = useState<File | null>(null);
    const [message, setMessage] = useState("");

    const uploadFile = async () => {
        if (!file) {
            setMessage("Please select a file");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        try {
            console.log("Uploading...");

            const response = await api.post("/upload", formData);
            
            const data = response.data;
            // const data = await response.json();
            console.log("Response:", response);


            console.log("Data:", data);

            setMessage(`Uploaded ${data.count} transactions`);
        } catch (error) {
            console.error(error);
            setMessage("Upload failed");
        }
    };
    console.log("Current message:", message);
    return (
        <div>
            <input
                type="file"
                accept=".csv"
                onChange={(e) =>
                    setFile(e.target.files?.[0] || null)
                }
            />

            <button onClick={uploadFile}>
                Upload da CSV
            </button>

            <p>{message}</p>
        </div>
    );
}

export default UploadForm;