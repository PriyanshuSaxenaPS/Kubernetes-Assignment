
const express = require("express");

const app = express();

const PORT = process.env.PORT || 5001;

app.use(express.json());

// Home route
app.get("/", (req, res) => {
    res.json({
        message: "Welcome to Express Backend API",
        status: "running"
    });
});

// API route used by Flask frontend
app.get("/api/message", (req, res) => {
    res.json({
        message: "Hello from Express.js Backend! Kubernetes communication is working successfully.",
        backend: "Express.js",
        status: "success"
    });
});

// Health check route
app.get("/health", (req, res) => {
    res.status(200).json({
        status: "healthy",
        service: "express-backend"
    });
});

// Start server
app.listen(PORT, "0.0.0.0", () => {
    console.log(`Express server running on port ${PORT}`);
});
