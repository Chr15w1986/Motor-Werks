// Simple timed redirect if the user does not click the home button
// Set to 5 seconds

const countdownElement = document.getElementById('countdown');
const form = document.getElementById('return-form');
const delay = 5000;
let countdown = 5;

const redirectToHomePage = () => {
    window.location.href = "/";
};

const updateCountdown = () => {
    countdownElement.textContent = countdown;
    countdown--;

    if (countdown >= 0) {
        setTimeout(updateCountdown, 1000);
    } else {
        redirectToHomePage();
    }
};

setTimeout(updateCountdown, 1000);

form.addEventListener('submit', (e) => {
    e.preventDefault();
});