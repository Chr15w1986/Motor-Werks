// Simple timed redirect if the user does not click the home button
// Set to 5 seconds

var countdownElement = document.getElementById('countdown');
var countdownTime = 5;
countdownElement.innerText = 'Redirecting in: ' + countdownTime;

setTimeout(function() {
    window.location.href = "/";
}, 5000); // Redirect after 5 seconds (5000 milliseconds)

var countdownInterval = setInterval(updateCountdown, 1000); // Update every second

function updateCountdown() {
    countdownTime--;
    countdownElement.innerText = 'Redirecting in: ' + countdownTime;

    if (countdownTime <= 0) {
        clearInterval(countdownInterval);
    }
}
