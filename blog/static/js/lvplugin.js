var lvstyle = document.getElementById('lw');
// var on = document.getElementById('lv-on');
// var off = document.getElementById('lv-off');


function GetStyle () {
lvstyle.setAttribute("href", "/static/css/lowvision.css");
document.getElementById('lv-on').style.display = "none";
document.getElementById('lv-off').style.display = "block";
}

function GetStyleBack () {
lvstyle.setAttribute("href", "#");
document.getElementById('lv-off').style.display =" none";
document.getElementById('lv-on').style.display = "block";
}
