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


