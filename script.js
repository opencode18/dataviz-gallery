console.log("Hello");
var vizClass = document.querySelectorAll(".viz");
var container = document.querySelector(".container");
var dropdownList = document.querySelector(".dropdown-list"); 
var dropdownBtn = document.querySelector(".dropdown-btn");
var dropdown = document.querySelector(".dropdown");

var viz = 
        [
            {
                "name" : "Average Temperature",
                "viz" : "avg-temp/avg-temp.png"
            },
            {
                "name" : "Equity Graph",
                "viz" : "Equity-graphs/graph.jpg"
            },
            {
                "name" : "High Jump",
                "viz" : "highjump/final_plot.png"
            },
            {
                "name" : "Hotels",
                "viz" : "hotels/hotel.png"
            },
            {
                "name" : "Music Download",
                "viz" : "music-downloads/Python/final_plot.png"
            },
            {
                "name" : "Sudoku",
                "viz" : "sudoku/final_lot.png"
            }
        ];

for(var i = 0; i < viz.length; i++)
{
    var div1 = document.createElement("div");
    var div2 = document.createElement("div");
    var li1 = document.createElement("li");
    div1.classList.add("viz");
    li1.classList.add("dropdown-list");
    var image = document.createElement("img");
    image.setAttribute("src", viz[i].viz);
    image.setAttribute("width", "150%");
    var hr = document.createElement("hr");
    var h1 = document.createElement("h1");
    var t = document.createTextNode(viz[i].name);
    var t2 = document.createTextNode(viz[i].name);
    h1.appendChild(t);
    li1.appendChild(t2);
    dropdownList.appendChild(li1);
    // vizClass[i].appendChild(h1);
    // vizClass[i].appendChild(image);
    div1.appendChild(h1);
    div1.appendChild(image);
    div2.appendChild(hr);
    container.appendChild(div1);
    container.appendChild(div2);
}

var dropdownLi = document.querySelectorAll(".dropdown-list li");
var divs = document.querySelectorAll(".container div.viz");

dropdownBtn.addEventListener("click", function()
    {
        console.log("Hello");
        dropdown.classList.toggle("dropdown-visible");
    });
var top = [];

for(var j = 0; j < dropdownLi.length; j++)
{
    top[j] = divs[j].offsetTop;
    console.log(divs[j].offsetTop);
}

for(var j = 0; j < dropdownLi.length; j++)
{
    // top1 = divs[j].offsetTop;
    dropdownLi[j].addEventListener("click", function()
    {
        for(var k = 0; k < dropdownLi.length; k++)
        {
            if(this == dropdownLi[k])
            {
                console.log(divs[k].offsetTop);
                window.scroll({ top: divs[k].offsetTop - 150, left: 0, behavior: "smooth" }); 
            }
        }
    });
}





