const API_KEY = "pk.eyJ1IjoidmJvYmVyIiwiYSI6ImNrMnpjYnQzNzBoY2kzY3BleHloOTNzajQifQ.uDtn2RDiTfiRJRmoglUZ3Q";

function markerSize(radius) {
  return radius * 10000;
}

var lightmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}",{
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
});

var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.dark",
  accessToken: API_KEY
});

var earthquakeMarkers = [];

var earthquake_data = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson"

d3.json(earthquake_data, function(response) {
    for (var i = 0; i < response.features.length; i++) {
      var coordinates = [response.features[i].geometry.coordinates[1],response.features[i].geometry.coordinates[0]];
      var radius = response.features[i].properties.mag;
      console.log(coordinates);
      console.log(radius);
      earthquakeMarkers.push(
        L.circle(coordinates, {
          stroke: false,
          fillOpacity: .75,
          color: "blue",
          fillColor: "blue",
          radius: markerSize(radius)
        }).addTo(myMap)
      );
    };
})

console.log(earthquakeMarkers);
var baseMaps = {
    "Light Map": lightmap,
    "Dark Map": darkmap
};
var earthquakes = L.layerGroup(earthquakeMarkers);

var overlayMaps = {
    "Earthquakes": earthquakes
};

var myMap = L.map("map", {
  center: [41.4993, -81.6944],
  zoom: 5,
  layers: [lightmap, earthquakes]
});

L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);
