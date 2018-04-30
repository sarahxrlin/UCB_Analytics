// Load data from hours-of-tv-watched.csv
d3.csv("./hours-of-tv-watched.csv", function (error, tvData) {
  if (error) console.error;

  console.log(tvData);

  // log a list of names
  var names = tvData.map(data => data.name)
  console.log("names", names)

  // Cast the hours value to a number for each piece of tvData
  tvData.forEach(function (data) {
    data.hours = +data.hours; //casting this as a number
    console.log("Name:", data.name);
    console.log("Hours:", data.hours);
  });
});
