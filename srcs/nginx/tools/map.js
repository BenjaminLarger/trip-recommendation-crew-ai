// Initialize map
var map = L.map('map').setView([48.8566, 2.3522], 2); // Default to Paris
var markers = [];

// Tile layer (OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Function to update the map with new suggestions
function updateMap(suggestions) {
  // suggestions = Besancon
// : 
for (const [city, coordinates] of Object.entries(suggestions)) {
  console.log(`City: ${city}`);
  console.log(`Latitude: ${coordinates.latitude}`);
  console.log(`Longitude: ${coordinates.longitude}`);
  var marker = L.marker([coordinates.latitude, coordinates.longitude]).addTo(map);
}
}