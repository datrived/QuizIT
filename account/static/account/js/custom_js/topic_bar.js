 window.onload= function(){
  update_heading("All Topics");
}

update_heading = function (topic_name) {
  var el = document.getElementById("update_heading");
  el.style.opacity = 0;
  el.innerHTML = 'Attempts Split For "'+topic_name+'"';
  el.style.opacity = 1;
}

var margin = {top: 20, right: 55, bottom: 30, left: 40},
    width  = 1000 - margin.left - margin.right,
    height = 500  - margin.top  - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .rangeRound([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

var color = d3.scale.ordinal()
    .range(["#00bfff","#ff9900"]);
    
var svg = d3.select("#topic_bar_chart").append("svg")
    .attr("width",  width  + margin.left + margin.right)
    .attr("height", height + margin.top  + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  var data = topicBarChartData;
  var labelVar = 'courseTopic';
  var varNames = d3.keys(data[0]).filter(function (key) { return key !== labelVar;});
  color.domain(varNames);

  data.forEach(function (d) {
    var y0 = 0;
    d.mapping = varNames.map(function (name) { 
      return {
        name: name,
        label: d[labelVar],
        y0: y0,
        y1: y0 += +d[name]
      };
    });
    d.total = d.mapping[d.mapping.length - 1].y1;
  });
  console.log(data);

  x.domain(data.map(function (d) { return d.courseTopic; }));
  y.domain([0, d3.max(data, function (d) { return d.total; })]);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text") 
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Count");

  var selection = svg.selectAll(".series")
      .data(data)
    .enter().append("g")
      .attr("class", "series")
      .attr("transform", function (d) { return "translate(" + x(d.courseTopic) + ",0)"; });

  selection.selectAll("rect")
    .data(function (d) { return d.mapping; })
  .enter().append("rect")
    .attr("width", x.rangeBand())
    .attr("y", function (d) { return y(d.y1); })
    .attr("height", function (d) { return y(d.y0) - y(d.y1); })
    .style("fill", function (d) { return color(d.name); })
    .style("stroke", "grey");
    // .on("mouseover", function (d) { showPopover.call(this, d); update_heading(d.label); update(d.label); })
    // .on("mouseout",  function (d) { removePopovers(); update_heading("All Topics"); update("All"); });
    
    selection.append("text")
    .attr("x", x.rangeBand()-45 )
    .attr("y", function (d) { return y(d.total)-10; })
    .attr("dy", ".75em")
    .text(function(d) { return d.total+" / "+d3.format(".0%")(d.mapping[d.mapping.length - 1].y0/d.total) ; }); 

    // .on("mouseover", function (d) { showPopover.call(this, d); update_heading(d.label); update(d.label); })
    // .on("mouseout",  function (d) { removePopovers(); update_heading("All Topics"); update("All"); })

  var legend = svg.selectAll(".legend")
      .data(varNames.slice().reverse())
    .enter().append("g")
      .attr("class", "legend")
      .attr("transform", function (d, i) { return "translate(55," + i * 20 + ")"; });

  legend.append("rect")
      .attr("x", width - 10)
      .attr("width", 10)
      .attr("height", 10)
      .style("fill", color)
      .style("stroke", "grey");

  legend.append("text")
      .attr("x", width - 12)
      .attr("y", 6)
      .attr("dy", ".35em")
      .style("text-anchor", "end")
      .text(function (d) { return d; });

  function removePopovers () {
    $('.popover').each(function() {
      $(this).remove();
    }); 
  }

  function showPopover (d) {
    $(this).popover({
      title: d.name,
      placement: 'auto top',
      container: 'body',
      trigger: 'manual',
      html : true,
      content: function() { 
        return "Course Topic: ";
               //+ "<br/>Count: " + d3.format(",")(d.value ? d.value: d.y1 - d.y0); 
             }
    });
    $(this).popover('show')
  }