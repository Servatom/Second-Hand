function showAbout()
{
    
    document.querySelector("#title").classList.add("hidden");
    document.querySelector("#about").classList.remove("hidden");
}

function showHome()
{
    document.querySelector("#title").classList.remove("hidden");
    document.querySelector("#about").classList.add("hidden");
}