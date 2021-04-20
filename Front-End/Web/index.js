function showAbout()
{
    
    // var k = 180;
    // document.querySelector("#title").style.transform = "rotatey(" + k + "deg)";
    // document.querySelector("#title").style.transitionDuration = "0.5s"

    document.querySelector("#title").classList.add("hidden");
    document.querySelector("#about").classList.remove("hidden");
}

function showHome()
{
    // var k = 0;
    // document.querySelector("#title").style.transform = "rotatey(" + k + "deg)";
    // document.querySelector("#title").style.transitionDuration = "0.5s"
    
    document.querySelector("#title").classList.remove("hidden");
    document.querySelector("#about").classList.add("hidden");
}