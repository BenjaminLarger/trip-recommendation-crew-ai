// script.js

// DOM elements
const submitButton = document.getElementById('submit-button');
const travelType = document.getElementById('travel-type');
const travelBudget = document.getElementById('travel-budget');
const travelTime = document.getElementById('travel-time');
const travelRegion = document.getElementById('travel-region');
const travelActivity = document.getElementById('travel-activity');
const mapContainer = document.getElementById('map');
departureCity = document.getElementById('departure-city');
// Backend API endpoint
const API_ENDPOINT_MAIN = ' http://127.0.0.1:8888/api/suggestions';
const API_INPUT_KEY = 'http://127.0.0.1:8888/api/input';

// Function to handle form submission
function handleFormSubmission() {
//  const userInput = travelInput.value.trim();
  const activities = getSelectedActivities();
  console.log('departure:', departureCity.value);
    const userInput = {
    "departureCity": departureCity.value,
    "travelType": travelType.value,
    "travelBudget": travelBudget.value,
    "travelTime": travelTime.value,
    "travelRegion": travelRegion.value,
    "travelActivity": activities,
    };
  console.log('User input:', userInput);
  
  if (!userInput) {
    alert('Please enter a destination or preference!');
    return;
  }

  // Add loading state to the submit button
  submitButton.disabled = true;
  submitButton.innerHTML = 'Loading...';

  // Send the user input to the backend API
  fetch(API_ENDPOINT_MAIN, {
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
      submitButton.disabled = false;
      submitButton.innerHTML = 'Submit';
      return response.json();
    })
    .then((data) => {
      submitButton.disabled = false;
      submitButton.innerHTML = 'Submit';
      console.log('Received data:', data);
      updateMap(data);
    })
    .catch((error) => {
      submitButton.disabled = false;
      submitButton.innerHTML = 'Submit';
      console.error('Error fetching suggestions:', error);
      alert('Failed to fetch suggestions. Please try again!');
    });
}


// Attach event listener to the submit button
submitButton.addEventListener('click', handleFormSubmission);

function getSelectedActivities() {
  const checkboxes = document.querySelectorAll('input[name="activity"]:checked');
  const selectedActivities = Array.from(checkboxes).map(checkbox => checkbox.value);
  console.log('Selected Activities:', selectedActivities);
  return selectedActivities;
}

async function fetchCities(query) {
  const suggestionsList = document.getElementById('city-suggestions');
  suggestionsList.innerHTML = ''; // Clear previous suggestions
  

  if (query.length < 3) {
    suggestionsList.style.display = 'none';
    return; // Don't fetch if query is too short
  }
  try {
    fetch(API_INPUT_KEY, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query: query }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Error: ${response.statusText}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Received data:', data);
        //{cities_suggestions: Array(10), status: 'success'}cities_suggestions: (10) ['Madrid', 'Madurai', 'Madison', 'Madan', 'Madiun', 'Madhyamgram', 'Madanapalle', 'Madhubani', 'Madinat as Sadis min Uktubar', 'Madrid']status: "success"[[Prototype]]: Object
        const citiesSuggestions = data.cities_suggestions;
        //// Update the suggestions list with the received data
        if (Object.keys(citiesSuggestions).length == 0) {
          suggestionsList.style.display = 'none'; // Hide suggestions if none found
          return;
        }
        suggestionsList.style.display = 'block'; // Show suggestions
        suggestionsList.innerHTML = ''; // Clear previous suggestions
        for (const [city, info] of Object.entries(citiesSuggestions)) {
          const li = document.createElement('li');
          li.textContent = `${city}`;
          li.style.padding = '8px';
          li.style.cursor = 'pointer';
          li.addEventListener('click', () => {
            document.getElementById('departure-city').value = city;
            suggestionsList.style.display = 'none'; // Hide suggestions after selection
            departureCity.value = city;
            console.log('departureCity.value :', departureCity.value);
            updateMapCityDeparture(city, info.latitude, info.longitude);
          });
          suggestionsList.appendChild(li);
        }
      });
  }
  catch (error) {
    console.error('Error fetching city suggestions:', error);
    suggestionsList.style.display = 'none';
  }
}
