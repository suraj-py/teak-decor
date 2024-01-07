const menuBtn = document.querySelector('.menu-btn')
const sideBar = document.querySelector('.sidemenu')

menuBtn.addEventListener('click', () => {
    console.log('working')
    sideBar.classList.toggle('open')
})