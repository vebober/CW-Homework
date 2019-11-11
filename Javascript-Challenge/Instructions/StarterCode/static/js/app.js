// from data.js
var tableData = data;

var button = d3.select("#filter-btn");

button.on("click", function() {
    var inputElement = d3.select("#datetime");
    var inputValue = inputElement.property("value");
    console.log(inputValue);
    console.log(tableData);

    var filteredData = tableData.filter(sighting => sighting.datetime === inputValue);

    console.log(filteredData);

    d3.select(".table-striped").selectAll("tbody")
        .selectAll("tr")
        .data(filteredData)
        .enter()
        .append("tr")
        .html(function(d) {
            return `<td>${d.datetime}</td><td>${d.city}</td><td>${d.state}</td><td>${d.country}</td><td>${d.shape}</td><td>${d.durationMinutes}</td><td>${d.comments}</td>`
    });

});


// d3.select(".table-striped").selectAll("tbody").selectAll("tr")
//   .data(austinWeather)
//   .enter()
//   .append("tr")
//   .html(function(d) {
//     return `<td>${d.date}</td><td>${d.low}</td><td>${d.high}</td>`;
//   })