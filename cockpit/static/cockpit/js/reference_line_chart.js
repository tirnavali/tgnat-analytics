`Bu dosya reference_chart.html sayfasındaki d3.js görsellerini oluşturmaktadır.`;

const margin = { top: 10, right: 30, bottom: 30, left: 60 };
const width = 1200;
const height = 750;
const padding = 50;
let verim = "";
let rafined_data = "";

const data_preprocess = function (data) {
  //Bu veriyi sıralı almak gerkecek sorun burada
  rafined_data = data.map((d) =>( {date: d3.timeParse('%Y-%m-%d')(d.date), value : d.user_from_inside }))};


  // return { date: d3.timeParse("%Y-%m-%d")(d.date), value: d.photocopy };



d3.json("http://localhost:8000/api/referans/").then(function (datas) {
  console.log(datas);
  verim = datas;
  data_preprocess(datas)

  rafined_data.sort(function(a,b){
    if (a.date > b.date){ return 1}
    if (b.date > a.date) { return -1}
});

  const yScale = d3
    .scaleLinear()
    .domain(d3.extent(datas, (d) => d.user_from_inside))
    .range([height - padding, padding]);

  const xScale = d3
    .scaleTime()
    .domain(d3.extent(rafined_data, (d) => d.date))
    .range([padding, width - padding]);

  const radiusScale = d3
    .scaleLinear()
    .domain(d3.extent(datas, (d) => d.user_from_inside))
    .range([2, 15]);

  const xAxis = d3
    .axisBottom(xScale)
    .tickSize(-height + 2 * padding)
    .tickSizeOuter(0);
  const yAxis = d3
    .axisLeft(yScale)
    .tickSize(-width + 2 * padding)
    .tickSizeOuter(0);

  const line = d3.line()
    .x(d => xScale(d.date))
    .y(d => yScale(d.value))

  d3.select("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(0," + (height - padding) + ")")
    .call(xAxis);

  d3.select("svg")
    .append("g")
    .attr("transform", "translate(" + padding + ",0)")
    .call(yAxis);

  d3.select("svg")
    .append("path")
    .datum(rafined_data)
    .attr("fill", "none")
    .attr("stroke", "steelblue")
    .attr("stroke-width", 2.5)
    .attr("d", line(rafined_data))

  d3.select("svg")
    .attr("width", width)
    .attr("height", height)
    .selectAll("circle")
    .data(rafined_data)
    .enter()
    .append("circle")
    .attr("cx", (d) => xScale(d.date))
    .attr("cy", (d) => yScale(d.value))
    .attr("r", 2.5);

  d3.select("svg")
    .append("text")
    .attr("x", width / 2)
    .attr("y", height - padding)
    .attr("dy", "2.5em")
    .style("text-anchor", "middle")
    .text("Tarihe göre gelen kullanıcı sayısındaki değişim");

  d3.select("svg")
  .append("text")
  .attr("transform", " rotate(-90) translate(-"+ (height-(padding/2))  +",-"+(padding*1.5)+")")
  .attr("x", padding/ 2)
  .attr("y", padding )
  .attr("dy", "2.5em")
  .style("text-anchor", "left")
  .text("Kütüphaneye gelen kullanıcı sayısı")
});


let datas = "";
// const  XHR = new XMLHttpRequest();
// XHR.onreadystatechange = function(){
//     if(XHR.readyState == 4 && XHR.status == 200) {
//         console.log(XHR.responseText);
//         data = JSON.parse(XHR.responseText);
//         console.log(data);
//     }
// }

// XHR.open("GET", "http://localhost:8000/api/referans/")
// XHR.send();

const data_url = "http://localhost:8000/api/referans/";
d3.json(
  data_url,
  function (data) {
    datas = data;
  },
  d3.autoType
);

// d3.json("http://localhost:8000/api/referans/").then(function(data) {
//   console.log(data);
//   x = d3.scaleLinear()
//     .domain([0, d3.max(data, d => d.photocopy)])
//     .range([500 - 50, 50])

//   y = d3.scaleLinear()
//     .domain([0, d3.max(data, d => d.borrowed_books)])
//     .range([500 - 50, 50])

//    line = d3.line()
//     .x(d => x(d.photocopy))
//     .y(d => y(d.borrowed_books))

//     console.log(line(data));

//     d3.select("svg")
//         .attr("d", line(data))
//         .enter()
// });
