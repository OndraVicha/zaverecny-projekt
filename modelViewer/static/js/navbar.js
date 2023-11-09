function updatemenu() {
  if (document.getElementById('responsive-menu').checked == true) {
    document.getElementById('menu').style.borderBottomRightRadius = '0';
    document.getElementById('menu').style.borderBottomLeftRadius = '0';
  }else{
    document.getElementById('menu').style.borderRadius = '20px';
  }
}

window.addEventListener('scroll', function () {
  const menuWrapper = document.getElementById('menu-wrapper');
  const offset = window.pageYOffset;

  if (offset > 0) {
    menuWrapper.classList.add('fixed');
  } else {
    menuWrapper.classList.remove('fixed');
  }
});

document.addEventListener("DOMContentLoaded", function () {
  // When the page is loaded, add the "visible" class to the menu.
  var menu = document.getElementById("menu");
  menu.classList.add("visible");
});