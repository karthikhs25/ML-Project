function checkSpam() {
    const emailText = document.getElementById('emailText').value;
    const resultDiv = document.getElementById('result');
    resultDiv.classList.remove('show');
    resultDiv.innerText = "Checking...";
    setTimeout(() => {
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email: emailText })
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerText = 
                data.result === 'spam' ? "🚨 This is SPAM!" : "✅ This is NOT spam (ham).";
            resultDiv.classList.add('show');
            resultDiv.style.color = data.result === 'spam' ? "#e74c3c" : "#27ae60";
        })
        .catch(error => {
            resultDiv.innerText = "Error: " + error;
            resultDiv.classList.add('show');
            resultDiv.style.color = "#e74c3c";
        });
    }, 400); // Simulate a short delay for animation
}