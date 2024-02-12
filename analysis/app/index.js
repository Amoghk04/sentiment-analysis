function analyse() {
    var data = document.getElementById('reviewInput').value;
    console.log(data);
    fetch('http://127.0.0.1:5000',
        {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                data: data,
                action: 'analyze'
            }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
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

            document.getElementById('analysis').textContent = sentiment+" - "+ ((highestScorelabel.score)*100).toFixed(2)+"%";
        })
        .catch(error => {
            console.error('Error sending data to Flask:', error);
        });
}

function generate() {
    var prompt = document.getElementById('promptInput').value;
    fetch('https://sentiment-analysis-spwi.vercel.app/',
    {
        method: "POST",
        headers: {
            'Content-type': 'application/json',
        },
        body: JSON.stringify({
            prompt: prompt,
            action: 'generate'
        }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(review => {
        console.log('Response From Flask: ', review.response);

        const responseData = review.response ? review.response : "No response returned from the model"

        document.getElementById('response').textContent = "\n" + responseData;
    })
    .catch(error => {
        console.error('Error sending data to Flask: ',error)
    })
}