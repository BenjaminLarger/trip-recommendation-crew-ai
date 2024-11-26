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

  // If userInput 400 error, the API will return an error message
  if (userInput.includes('error')) {
    alert('Please provide an ai friendly prompt. Example : I want to visit warm cities with beautiful beaches in Europe.');
    return;
  }

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
      updateMap(data);
    })
    .catch((error) => {
      console.error('Error fetching suggestions:', error);
    });
}

// Attach event listener to the submit button
submitButton.addEventListener('click', handleFormSubmission);
