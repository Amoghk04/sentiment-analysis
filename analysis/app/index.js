function analyse() {
    var data = document.getElementById('reviewInput').value;
    fetch('http://127.0.0.1:5000',
        {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                data: data
            }),
        })
        .then(response => {
            console.log(response);
            return response.json()})
        .then(data => {
            console.log('Response From Flask:', data);

            const result = data.result[0];

            const highestScorelabel = result.reduce((maxLabel, currentLabel) =>{
                return currentLabel.score > maxLabel.score ? currentLabel : maxLabel;
            }, {score: -Infinity});

            let sentiment;
            if (highestScorelabel.label==='POS') {
                sentiment = "Positive";
            } else if (highestScorelabel.label==="NEG") {
                sentiment = 'Negative'; 
            } else {
                sentiment = 'Neutral';
            }

            document.getElementById('analysis').textContent = "";

            document.getElementById('analysis').textContent = sentiment;
        })
        .catch(error => {
            console.error('Error sending data to Flask:', error);
        });
}