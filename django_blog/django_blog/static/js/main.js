const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function () {
  $('message').fadeOut('slow');
}, 3000);

document.addEventListener('DOMContentLoaded', () => {});
function toggleUserMenu(isOverlay = false) {
  const userMenu = document.querySelector('.topbar__user-menu');
  const overlay = document.querySelector('.topbar__user-overlay');
  if (!isOverlay) {
    if (userMenu.style.display == 'block') {
      userMenu.style.display = 'none';
      overlay.style.display = 'none';
    } else {
      userMenu.style.display = 'block';
      overlay.style.display = 'block';
    }
    return;
    //If click to overlay, we hide the menu and overlay
  } else {
    userMenu.style.display = 'none';
    overlay.style.display = 'none';
  }
}

function toggleMenu() {
  const userMenu = document.querySelector('.topbar__user-menu');
  const overlay = document.querySelector('.topbar__user-overlay');
  if (userMenu.style.display == 'block') {
    userMenu.style.display = 'none';
    overlay.style.display = 'none';
  } else {
    userMenu.style.display = 'block';
    overlay.style.display = 'block';
  }
}

function toggleSearchForm() {
  console.log('toggle search form');
  const searchForm = document.getElementById('topbar-search-form');
  if (searchForm.style.display == 'block') {
    searchForm.style.display = 'none';
  } else {
    searchForm.style.display = 'block';
  }
}
