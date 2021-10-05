function test(){
    var test1 = document.getElementById("divCheckbox"), clickme = document.getElementById("myBtn");
    test1.style.display = "inline";
}


var now = new Date(Date.now());
var formatted = now.getHours() + ":" + now.getMinutes();

document.getElementById("hm").value = formatted;
var formatted2 = now.getHours() + ":" + now.getMinutes();

