// static/js/scripts.js

document.getElementById('shorten-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const url = document.getElementById('url').value;
    
    fetch('/shorten', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        const resultElement = document.getElementById('result');
        if (data.shortened_url) {
            resultElement.value = data.shortened_url;
        } else if (data.error) {
            resultElement.value = 'Error: ' + data.error;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function copyText() {
    var resultElement = document.getElementById("result");
    resultElement.select();
    document.execCommand("copy");
    alert("Copied the URL: " + resultElement.value);
}
