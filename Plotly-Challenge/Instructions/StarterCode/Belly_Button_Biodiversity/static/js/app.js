function buildMetadata(sample) {
  var table = d3.select("#sample-metadata");
  var url = `/metadata/${sample}`;
  console.log(url)
  d3.json(url).then(function (sample_metadata) {

    console.log(sample_metadata)
    var data1 = sample_metadata;

    table.html("");

    Object.entries(sample_metadata).forEach(([key, value]) => {
      table.append("h6").text(`${key}: ${value}`);
    });
  });
  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample
  // Use d3 to select the panel with id of `#sample-metadata`

  // Use `.html("") to clear any existing metadata

  // Use `Object.entries` to add each key and value pair to the panel
  // Hint: Inside the loop, you will need to use d3 to append new
  // tags for each key-value in the metadata.

  // BONUS: Build the Gauge Chart
  // buildGauge(data.WFREQ);
}

function buildCharts(sample2) {
  var url2 = `/samples/${sample2}`;
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var pie = d3.select("#pie");
  d3.json(url2).then(function (pie_data) {
    pie.html("");
    var pie_values = pie_data.sample_values.slice(0, 10);
    var pie_label = pie_data.otu_ids.slice(0, 10);
    var pie_hovertext = pie_data.otu_labels.slice(0, 10);

    var trace1 = {
      labels: pie_label,
      values: pie_values,
      type: "pie",
      hoverinfo: pie_hovertext
    };

    var piedata = [trace1];

    Plotly.plot("pie", piedata)
  });

  // @TODO: Build a Bubble Chart using the sample data
  var bubble = d3.select("#bubble");
  d3.json(url2).then(function (bubble_data) {
    bubble.html("");
    var otu_ids = bubble_data.otu_ids;
    var sample_values = bubble_data.sample_values;
    var otu_labels = bubble_data.otu_labels;
    var trace2 = {
      x: otu_ids,
      y: sample_values,
      mode: "markers",
      marker: {
        size: sample_values,
        color: otu_ids
      },
      text: otu_labels
    };

    var layout = {
      showlegend: false,
      height: 600,
      width: 1200
    };

    var bubbledata = [trace2];
    Plotly.plot("bubble", bubbledata, layout)
  });
  // @TODO: Build a Pie Chart

  // HINT: You will need to use slice() to grab the top 10 sample_values,
  // otu_ids, and labels (10 each).
};

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
};

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
};

// Initialize the dashboard
init();
