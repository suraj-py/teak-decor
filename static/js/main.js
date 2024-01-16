const menuBtn = document.querySelector('.menu-btn')
const sideBar = document.querySelector('.sidemenu')

const accountsBtn = document.querySelector('.accBtn')
const dropdownMenu = document.querySelector('.dropdown')

menuBtn.addEventListener('click', () => {
    console.log('working')
    sideBar.classList.toggle('hide')
})

accountsBtn.addEventListener('click', () => {
    console.log('working')
    dropdownMenu.classList.toggle('show')
})

document.addEventListener("DOMContentLoaded", function() {
  var navbar = document.getElementById("navbar");
  var initialHeight = 112; // Set your initial height

  window.addEventListener("scroll", function() {
    if (window.scrollY > 100) { // Adjust the scroll position where you want the change to occur
      navbar.style.height = "80px"; // Set the new height on scroll
    } else {
      navbar.style.height = initialHeight + "px"; // Set the initial height if not scrolled enough
    }
  });
});

