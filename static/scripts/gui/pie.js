// START PIE CHART //
let height = 100;
let margin = 10;
let stackColors = ['#FBB65B', '#513551', '#de3163'];

// Create dummy data
let data = JSON.parse(document.getElementById('pie-data').textContent);

// set the color scale
let color = d3.scaleOrdinal()
    .domain(["Accessible", "Semi-Accesible", "Not Accesible"])
    .range(stackColors);

// Compute the position of each group on the pie:
let pie = d3.pie()
    .sort(null) // Do not sort group by size
    .value(function (d) { return d.value; });
let a11y_pie_data = pie(d3.entries(data));

let pieSvg = d3.select("#viz_status")
    .append("svg")
    .attr("preserveAspectRatio", "xMinYMin meet")
    .attr("viewBox", "0 0 400 120");

let pieSvgGraph = pieSvg
    .append("g");

let pieSvgSlices = pieSvgGraph
    .selectAll('allSlices')
    .data(a11y_pie_data)
    .enter()
    .append('path');

let pieSvgLegendKeys = pieSvgGraph.selectAll("myDots")
    .data(a11y_pie_data)
    .enter()
    .append("text");

let pieSvgLegendValues = pieSvgGraph.selectAll("mylabels")
    .data(a11y_pie_data)
    .enter()
    .append("text");
// END PIE CHART //

// A function that finishes to draw the chart for a specific device size.
function drawChart() {

    // get the current width of the div where the chart appear, and attribute it to Svg
    currentWidth = 400;

    // append the svg object to the div called 'viz_status'
    pieSvg
        .attr("width", currentWidth)
        .attr("height", height);

    // The radius of the pieplot is half the width or half the height (smallest one). I subtract a bit of margin.
    let radius = 64;

    pieSvgGraph
        .attr("transform", "translate(" + radius + "," + radius + ")");

    // The arc generator
    let arc = d3.arc()
        .innerRadius(radius * 0.5)         // This is the size of the donut hole
        .outerRadius(radius * 0.8);

    // Another arc that won't be drawn. Just for labels positioning
    let outerArc = d3.arc()
        .innerRadius(radius * 0.9)
        .outerRadius(radius * 0.9);

    // Build the pie chart: Basically, each part of the pie is a path that we build using the arc function.
    pieSvgSlices
        .attr('d', arc)
        .attr('fill', function (d) { return (color(d.data.key)) })
        .attr("stroke", "white")
        .style("stroke-width", "2px")
        .style("opacity", 1.0);

    pieSvgLegendKeys
        .attr("x", 80)
        .attr("y", function (d, i) { return 32 - radius + i * 40 }) // 100 is where the first dot appears. 25 is the distance between dots
        .style("fill", function (d) { return (color(d.data.key)) })
        .text(function (d) { return d.data.key })
        .attr("font-size", "32")
        .attr("text-anchor", "left")
        .style("alignment-baseline", "middle");

    pieSvgLegendValues
        .attr("x", 312)
        .attr("y", function (d, i) { return 32 - radius + i * 40 }) // 100 is where the first dot appears. 25 is the distance between dots
        .style("fill", function (d) { return (color(d.data.key)) })
        .text(function (d) { return d.data.value })
        .attr("font-size", "32")
        .attr("text-anchor", "right")
        .style("alignment-baseline", "middle");
}
// Initialize the chart
drawChart();

