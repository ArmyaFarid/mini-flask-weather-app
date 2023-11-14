const cityInput = document.querySelector(".city-input");
const searchButton = document.querySelector(".search-btn");
const locationButton = document.querySelector(".location-btn");
const goHomeButton = document.querySelector(".gohome-btn");


const currentWeatherDiv = document.querySelector(".current-weather");
const weatherCardsDiv = document.querySelector(".weather-cards");

const getUserCoordinates = () => {
    navigator.geolocation.getCurrentPosition(
        position => {
            const { latitude, longitude } = position.coords; // Get coordinates of user location
            const forecastSlider = document.getElementById('forecastSlider');

            const selectedDays = forecastSlider.value;
            // Get city name from coordinates using reverse geocoding API
            const url = `/weather?latitude=${latitude}&longitude=${longitude}&number_of_days_forcast=${selectedDays}`;
            window.location.href = url;
        },
        error => { // Show alert if user denied the location permission
            if (error.code === error.PERMISSION_DENIED) {
                alert("Geolocation request denied. Please reset location permission to grant access again.");
            } else {
                alert("Geolocation request error. Please reset location permission.");
            }
        });
}

goHomeButton.addEventListener("click",()=>{
    window.location.href ='/';
    console.log("clicked")
})

console.log("clicked")

locationButton.addEventListener("click", getUserCoordinates);
