`Bu dosya reference_chart.html sayfasındaki d3.js görsellerini oluşturmaktadır.`;
const width = 1200;
const height = 750;
const padding = 50;
d3.json("http://localhost:8000/api/referans/").then(function (datas) {
  const yScale = d3
    .scaleLinear()
    .domain(d3.extent(datas, (d) => d.book_on_loan))
    .range([height - padding, padding]);
  const xScale = d3
    .scaleLinear()
    .domain(d3.extent(datas, (d) => d.user_from_inside))
    .range([padding, width - padding]);

  const radiusScale = d3
    .scaleLinear()
    .domain(d3.extent(datas, (d) => d.book_on_loan))
    .range([2, 20]);
  
  const xAxis = d3
    .axisBottom(xScale)
    .tickSize(-height + 2 * padding)
    .tickSizeOuter(0);
  const yAxis = d3
    .axisLeft(yScale)
    .tickSize(-width + 2 * padding)
    .tickSizeOuter(0);

  d3.select("svg")
    .append("g")
    .attr("transform", "translate(0," + (height - padding) + ")")
    .call(xAxis);

  d3.select("svg")
    .append("g")
    .attr("transform", "translate(" + padding + ",0)")
    .call(yAxis);

  d3.select("svg")
    .attr("width", width)
    .attr("height", height)
    .selectAll("circle")
    .data(datas)
    .enter()
    .append("circle")
    .attr("cx", (d) => xScale(d.user_from_inside))
    .attr("cy", (d) => yScale(d.book_on_loan))
    .attr("r", (d) => radiusScale(d.book_on_loan));

  d3.select("svg")
    .append("text")
    .attr("transform", " rotate(-90) translate(-"+ (height-(padding/2))  +",-"+(padding*1.5)+")")
    .attr("x", padding/ 2)
    .attr("y", padding )
    .attr("dy", "2.5em")
    .style("text-anchor", "left")
    .text("Ödünç verilen kitap sayısı")

  d3.select("svg")
    .append("text")
    .attr("x", width / 2)
    .attr("y", height - padding)
    .attr("dy", "1.5em")
    .style("text-anchor", "middle")
    .text("Tüm zamanlarda gelen kullanıcı sayısı ile ödünç verilen kitap sayısı ilişkisi");
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
