let menu = document.querySelector('#menu-btn');
let navbar = document.querySelector('.nav-bar');
let nav = document.querySelector('.nav');
var images = document.getElementsByClassName("image");
var email = document.querySelector('.email')
var subject =  document.querySelector('.subject')
var mailname =  document.querySelector('.name')
var message =  document.querySelector('.message')

var error = document.querySelector('.error');

menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

window.onscroll = () =>{
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
    


  if(window.scrollY > 80){
    nav.classList.add('active');
    navbar.classList.add('margin');
    
    
  }else{
    nav.classList.remove('active');
  }
}

window.addEventListener('scroll', () => {
  var reveal = document.querySelectorAll('.reveal');
  var one = document.querySelector('.one');
  var two = document.querySelector('.two');
  var three = document.querySelector('.three');
  var four = document.querySelector('.four');
  



  for (var i = 0; i < reveal.length; i++){
    var windowHeight = window.innerHeight;
    var revealTop = reveal[i].getBoundingClientRect().top;
    var revealPoint = 150;

    if(revealTop < windowHeight - revealPoint){
      reveal[i].classList.add('active');
      one.classList.add('active');
      two.classList.add('active');
      three.classList.add('active');
      four.classList.add('active');
    }
    else{
      reveal[i].classList.remove('active');
      
     
    }
  }
})

function validation() {
  if (email==="" && mailname==="" && subject ==="" && message==="") {
        error.style.display = "block";
        return false;
    }

    
    
}