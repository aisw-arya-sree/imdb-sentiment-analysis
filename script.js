function analyzeSentiment() {
    var inputReview = document.getElementById('input-review').value;

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ review: inputReview })
    })
    .then(response => response.json())
    .then(data => {
        var predictionResult = document.getElementById('prediction-result');
        predictionResult.innerText = data.prediction;
    })
    .catch(error => console.error('Error:', error));
}

