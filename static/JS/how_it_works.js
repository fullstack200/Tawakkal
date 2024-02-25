function display1(a, b) {
    document.getElementById(a).className = document.getElementById(a).className.replace("line", "line active increase")
    console.log(document.getElementById(a).className)
    document.getElementById(b).style.display = "block";
}

function hide(a, b) {
    document.getElementById(a).className = document.getElementById(a).className.replace("line active increase", "line")
    document.getElementById(b).style.display = "none"
}