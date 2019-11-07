// from data.js
var tableData = data;

var button = d3.select("#button");

button.on("click", function() {
    var inputElement = d3.select("#datetime");
    var inputValue = inputElement.property("value");
    console.log(inputValue);
    console.log(tableData);

    var filterData = tableData.filter(sighting => sighting.datetime ===inputValue);
    console.log(filterData);
});
