import { useEffect } from "react";


function UploadPage() {

    useEffect(() => {
        console.log("upload page mounted");
    },[]);

    const handleUpload = () => {
        alert(" Upload feature coming soon")
    }

    return (
        <div> 
            <h2> Upload Transaction file</h2>

            <input type="file" />

            <button onClick={handleUpload}>Upload</button>
        </div>
    );
}


export default UploadPage;