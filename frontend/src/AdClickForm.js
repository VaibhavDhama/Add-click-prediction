import React, { useState } from "react";
import axios from "axios";
import "./AdClickForm.css"; // Importing CSS file for styling

const AdClickForm = () => {
    const [formData, setFormData] = useState({
        timeSpent: "",
        age: "",
        income: "",
        internetUsage: "",
        gender: "0",
        adTopic: "",
    });

    const [prediction, setPrediction] = useState(null);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://127.0.0.1:5000/predict", {
                "Daily Time Spent on Site": parseFloat(formData.timeSpent),
                "Age": parseInt(formData.age),
                "Area Income": parseFloat(formData.income),
                "Daily Internet Usage": parseFloat(formData.internetUsage),
                "Gender": parseInt(formData.gender),
                "Ad Topic Line": formData.adTopic,
            });

            setPrediction(response.data.prediction);
        } catch (error) {
            console.error("Error:", error);
        }
    };

    const handleReset = () => {
        setFormData({
            timeSpent: "",
            age: "",
            income: "",
            internetUsage: "",
            gender: "0",
            adTopic: "",
        });
        setPrediction(null);
    };

    return (
        <div className="form-container">
            <h2 className="form-title">Ad Click Prediction</h2>
            <form onSubmit={handleSubmit} className="form">
                <label>Daily Time Spent on Site:</label>
                <input type="number" name="timeSpent" value={formData.timeSpent} onChange={handleChange} required />

                <label>Age:</label>
                <input type="number" name="age" value={formData.age} onChange={handleChange} required />

                <label>Area Income:</label>
                <input type="number" name="income" value={formData.income} onChange={handleChange} required />

                <label>Daily Internet Usage:</label>
                <input type="number" name="internetUsage" value={formData.internetUsage} onChange={handleChange} required />

                <label>Gender:</label>
                <select name="gender" value={formData.gender} onChange={handleChange}>
                    <option value="0">Female</option>
                    <option value="1">Male</option>
                </select>

                <label>Ad Topic Line:</label>
                <input type="text" name="adTopic" value={formData.adTopic} onChange={handleChange} required />

                <div className="button-group">
                    <button type="submit" className="submit-btn">Predict</button>
                    <button type="button" className="reset-btn" onClick={handleReset}>Reset</button>
                </div>
            </form>

            {prediction !== null && (
                <h3 className="prediction-result">
                    Prediction: {prediction === 1 ? "✅ Will Click Ad" : "❌ Will Not Click Ad"}
                </h3>
            )}
        </div>
    );
};

export default AdClickForm;
