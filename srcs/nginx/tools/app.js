// script.js

// DOM elements
const submitButton = document.getElementById('submit-button');
const travelInput = document.getElementById('travel-input');
const mapContainer = document.getElementById('map');

// Backend API endpoint
const API_ENDPOINT = ' http://127.0.0.1:8888/api/suggestions'; // Replace with your actual backend endpoint

// Function to handle form submission
function handleFormSubmission() {
  const userInput = travelInput.value.trim();
  console.log('User input:', userInput);
  
  if (!userInput) {
    alert('Please enter a destination or preference!');
    return;
  }

  // Show loading indicator (you can customize this)
  mapContainer.innerHTML = '<p>Loading suggestions...</p>';

  // Send the user input to the backend API
  fetch(API_ENDPOINT, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query: userInput }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }
      return response.json();
    })
    .then((data) => {
      console.log('Received data:', data);
      updateMap(data.suggestions);
    })
    .catch((error) => {
      console.error('Error fetching suggestions:', error);
      mapContainer.innerHTML = '<p>Failed to load suggestions. Please try again.</p>';
    });
}

// Function to update the map with new suggestions
function updateMap(suggestions) {
  // Clear existing map content
  mapContainer.innerHTML = '';

  // If no suggestions, show a message
  if (!suggestions || suggestions.length === 0) {
    mapContainer.innerHTML = '<p>No suggestions found for your input.</p>';
    return;
  }

  _name = suggestions.name;
  _latitude = suggestions.latitude;
  _longitude = suggestions.longitude;

  // Example: Render suggestions as a list (replace with map logic later)
  // const suggestionList = document.createElement('ul');
  // suggestions.forEach((suggestion) => {
  //   const listItem = document.createElement('li');
  //   listItem.textContent = suggestion.name; // Assuming `name` is part of the API response
  //   suggestionList.appendChild(listItem);
  // });
  const suggestionList = document.createElement('ul');
  const listItem = document.createElement('li');
  listItem.textContent = suggestions.name; // Assuming `name` is part of the API response
  suggestionList.appendChild(listItem);

  mapContainer.appendChild(suggestionList);

  // Placeholder for map integration (e.g., Leaflet or Mapbox)
  // Example:
  // const map = L.map('map').setView([latitude, longitude], 13);
  // L.marker([latitude, longitude]).addTo(map).bindPopup('Destination').openPopup();
}

// Attach event listener to the submit button
submitButton.addEventListener('click', handleFormSubmission);
