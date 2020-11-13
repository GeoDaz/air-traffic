import { useEffect } from "react";

const { default: Table } = require("../components/Table")

const HomePage = () => {

    useEffect(()=>{
        fetch("http://localhost:5000/api/airports")
            .then((response) => response.json())
            .then((data) => {
                console.log("data", data)
            });
    }, [])

    return (
        <div>
            Page
        </div>
    );
}

export default HomePage;