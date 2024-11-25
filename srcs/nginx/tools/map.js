// Initialize map
var map = L.map('map').setView([48.8566, 2.3522], 2); // Default to Paris
var markers = [];

// Tile layer (OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Function to update the map with new suggestions
function updateMap(suggestions) {
  // Clear existing map content
  // mapContainer.innerHTML = '';

  // If no suggestions, show a message
  if (!suggestions || suggestions.length === 0) {
    mapContainer.innerHTML = '<p>No suggestions found for your input.</p>';
    return;
  }

  _name = suggestions.name;
  _latitude = suggestions.latitude;
  _longitude = suggestions.longitude;
  console.log('Name:', _name);
  console.log('Latitude:', _latitude);
  console.log('Longitude:', _longitude);

  markers.forEach(marker => map.removeLayer(marker));
  markers = [];
  // Create a marker at the specified coordinates
  var marker = L.marker([_latitude, _longitude]).addTo(map);
  markers.push(marker);

// Set the view of the map to the new marker
  map.setView([_latitude, _longitude], 10);
}