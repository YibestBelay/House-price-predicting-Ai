document.getElementById("prediction-form").addEventListener("submit", async function (event) {
    event.preventDefault();

    const data = {
        rm: parseFloat(document.getElementById("rm").value),
        lstat: parseFloat(document.getElementById("lstat").value),
        ptratio: parseFloat(document.getElementById("ptratio").value),
        indus: parseFloat(document.getElementById("indus").value)
    };

    try {
        const response = await fetch("https://your-render-app.onrender.com/predict/", ...{
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify(inputData),
})


        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`Server Error: ${errorText}`);
        }

        const result = await response.json();
        document.getElementById("result").innerText = `Predicted Price: $${result.predicted_price.toFixed(2)}`;
    } catch (error) {
        document.getElementById("result").innerText = `Error: ${error.message}`;
        console.error("Prediction Error:", error);
    }
});
