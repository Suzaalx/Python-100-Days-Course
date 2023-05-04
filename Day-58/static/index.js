const handleNav = document.querySelector('.hamburger');
const closeNav = document.querySelector('.close');
const nav = document.querySelector('.mob-nav');

handleNav.addEventListener('click', () => {
    nav.classList.toggle('open');
    handleNav.classList.toggle('hide')
    });
closeNav.addEventListener('click', () => {
    nav.classList.toggle('open');
    handleNav.classList.toggle('hide')
    });