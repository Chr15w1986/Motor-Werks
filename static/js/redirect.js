// Simple timed redirect if the user does not click the home button
// Set to 5 seconds

setTimeout(function() {
    window.location.href = "/";
}, 5000); // Redirect after 5 seconds (5000 milliseconds)

// Countdown timer as a visual aid to the user
var countdownElement = document.getElementById('countdown');
var countdownTime = 5 * 60; // 5 minutes in seconds
var countdownInterval = setInterval(updateCountdown, 1000); // Update every second

function updateCountdown() {
    var minutes = Math.floor(countdownTime / 60);
    var seconds = countdownTime % 60;

    countdownElement.innerText = 'Redirecting in ' + minutes + ':' + seconds.toString().padStart(2, '0');

    if (countdownTime <= 0) {
        clearInterval(countdownInterval);
        window.location.href = "{% url 'profiles' %}"; // Redirect to the specified URL
    } else {
        countdownTime--;
    }
}
