`Bu dosya reference_chart.html sayfasındaki d3.js görsellerini oluşturmaktadır.`
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
d3.json(data_url, function(data){ datas = data}, d3.autoType)

d3.json("http://localhost:8000/api/referans/").then(function(data) {
  console.log(data);
  x = d3.scaleLinear()
    .domain([0, d3.max(data, d => d.photocopy)])
    .range([500 - 50, 50])

  y = d3.scaleLinear()
    .domain([0, d3.max(data, d => d.borrowed_books)])
    .range([500 - 50, 50])

    
   line = d3.line()
    .x(d => x(d.photocopy))
    .y(d => y(d.borrowed_books))

    console.log(line(data));
});

x = d3.scaleLinear()
.domain([0, d3.max(datas, d => d.photocopy)])
.range([500 - 50, 50])




y = d3.scaleLinear()
    .domain([0, d3.max(datas, d => d.borrowed_books)])
    .range([500 - 50, 50])



line = d3.line()
    .x(d => x(d.photocopy))
    .y(d => y(d.borrowed_books))
