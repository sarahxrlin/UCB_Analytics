// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $datetimeInput = document.querySelector("#datetime");
var $searchBtn = document.querySelector("#search");
var $datetimeInput = document.querySelector("#city");
var $searchBtn = document.querySelector("#search");
// var $datetimeInput = document.querySelector("#state");
// var $searchBtn = document.querySelector("#search");
// var $datetimeInput = document.querySelector("#country");
// var $searchBtn = document.querySelector("#search");
// var $datetimeInput = document.querySelector("#shape");
// var $searchBtn = document.querySelector("#search");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);

// Set filteredSightings to data initially
var filteredSightings = dataSet;

// renderTable renders the filteredSightings to the tbody
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < filteredSightings.length; i++) {
    // Get get the current sighting object and its fields
    var sightings = filteredSightings[i];
    var fields = Object.keys(sightings);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the sightings object, create a new cell at set its inner text to be the current value at the current sightings field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = sightings[field];
    }
  }
}

function handleSearchButtonClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterDatetime = $datetimeInput.value.trim().toLowerCase();

  // Set filteredSightings to an array of all sightings whose "datetimes" matches the filter
  filteredSightings = dataSet.filter(function(sightings) {
    var sightingsDatetime = sightings.datetime.toLowerCase();

    // If true, add the address to the filteredDatetime, otherwise don't add it to filteredDatetime
    return sightingsDatetime === filterDatetime;
  });
  renderTable();
}

// Render the table for the first time on page load
renderTable();
