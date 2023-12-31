
window.addEventListener('scroll', function () {
  const menuWrapper = document.getElementById('menu-wrapper');
  const offset = window.pageYOffset;

  if (offset > 0) {
    menuWrapper.classList.add('fixed');
    document.getElementById('menu').style.background = 'rgba(5, 3, 3, 0.7)';
  } else {
    menuWrapper.classList.remove('fixed');
    document.getElementById('menu').style.background = 'rgba(5, 3, 3, 0.95)';

  }
});

document.addEventListener("DOMContentLoaded", function () {
  // When the page is loaded, add the "visible" class to the menu.
  var menu = document.getElementById("menu");
  menu.classList.add("visible");
});