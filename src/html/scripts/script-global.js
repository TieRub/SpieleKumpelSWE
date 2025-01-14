document.addEventListener('DOMContentLoaded', () => {
    const burgerMenu = document.getElementById('burgerMenu');
    const navLinks = document.getElementById('navLinks');

    burgerMenu.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
});
