const  XHR = new XMLHttpRequest();
XHR.onreadystatechange = function(){
    if(XHR.readyState == 4 && XHR.status == 200) {
        console.log(XHR.responseText);
        const data = JSON.parse(XHR.responseText);
        console.log(data);
    }
}

XHR.open("GET", "http://localhost:8000/api/referans/")
XHR.send();