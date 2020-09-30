var pageCounter =1;


var btn=document.getElementById("btn");
var animalContainer= document.getElementById("animal-info");

btn.addEventListener("click",function(){
//XMLHttpRequest tool help in sending and receiving data
    var ourRequest =new XMLHttpRequest();
    ourRequest.open('GET','https://learnwebcode.github.io/json-example/animals-'+pageCounter+'.json');
    ourRequest.onload=function(){
        //to check that we have successfully connected with the json file
        if (ourRequest.status >=200 && ourRequest.status<400){
                //console.log(ourRequest.responseText);
                var ourData=JSON.parse(ourRequest.responseText);
                // console.log(ourData[0])
                renderHTML(ourData);
        }else{
            console.log("Error connecting server");

        }
        

    };

    ourRequest.onerror=function( ){
        console.log("connection error");
    }

    ourRequest.send();
    pageCounter++;
    if(pageCounter > 3){
        btn.classList.add("hide-me");
    }
});

function renderHTML(data){
    var htmlString="";
    for(i=0;i<data.length;i++){
        htmlString +="<p><b>" + data[i].name + "</b> is a "+ data[i].species +"that likes to eat ";

        for (ii = 0; ii < data[i].foods.likes.length; ii++) {
            if (ii == 0) {
              htmlString += data[i].foods.likes[ii];
            } else {
              htmlString += " and " + data[i].foods.likes[ii];
            }
          }
      
          htmlString += ' and dislikes ';
      
          for (ii = 0; ii < data[i].foods.dislikes.length; ii++) {
            if (ii == 0) {
              htmlString += data[i].foods.dislikes[ii];
            } else {
              htmlString += " and " + data[i].foods.dislikes[ii];
            }
          }
      
          htmlString += '.</p>';
    }
    animalContainer.insertAdjacentHTML('beforeend',htmlString);

}





































/*
//object
var myCat={
    "name":"Meowsalot",
    "species":"cat",
    "favfood":"tuna"
}

myCat.name
//array
var myFavColors=["blue","green","purple"];

myFavColors[0];

//combine object and array
var thePets=[
    {"name":"Meowsalot",
    "species":"cat",
    "favfood":"tuna"},

    {"name":"Barky",
    "species":"dog",
    "favfood":"carrots"}
]

thePets[1].favfood //print carrots
*/