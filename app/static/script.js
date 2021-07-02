
/*--------sentiment dropdown----------*/
var open=document.getElementById("open-sentiment");
open.addEventListener("click", function(){
  //console.log("test");
  //this.classList.toggle("choose-open");
  
  //toggle the div that displays the emotion options
 var section = this.nextElementSibling;
  if (section.style.maxHeight) {
			section.style.maxHeight = null;
     //toggle the class that switches + with - 
      this.className="choose-sentiment";
		} else {
			section.style.maxHeight = section.scrollHeight + "px";
      this.className="choose-open";
		}
});

/*-------navigation bar/side bar------*/
function makeResponsive(){
 // console.log("test");
   var sideNav = document.getElementById("side-bar");
  var cover= document.getElementById("cover");
    cover.style.display="block";
    sideNav.style.width="250px";
}
function closeSideBar(){
    var sideNav = document.getElementById("side-bar");
  var cover= document.getElementById("cover");
    cover.style.display="none";
    sideNav.style.width="0";
}


window.addEventListener('resize', function(){
   var sideNav = document.getElementById("side-bar");
    var cover= document.getElementById("cover");
                       if (window.innerWidth > 800 && sideNav.style.width=="250px") {

    cover.style.display="none";
  //console.log("hi");
                       }
  else if (window.innerWidth < 800 && sideNav.style.width=="250px"){

    cover.style.display="block";
  }
 });


/*-------returning generated text------*/
var textbox = document.getElementById("generate");
var text_content =textbox.value;
//clear textbox if user has not tried the product
if (text_content=="None"){
  console.log("True");
  textbox.value="";
}
else{
  console.log("False");
  var test=JSON.parse(text_content);
}


console.log(test);
/*for (var i = 0; i<text_content.length;i++){
  //console.log(text_content[i]);
  if (text_content[i]=="'"){
    console.log(text_content[i]);
    text_content.replace(i,'"');
  }
}*/

//test=JSON.parse(text_content);
//console.log(test);




