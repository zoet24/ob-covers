function openProfileDropdown() {
  document.getElementById("nav-profile-dropdown-menu").classList.toggle("show");
}

function openSidebarFav() {
    document.getElementById("sidebar-fav").style.right = "0";
}

function openSidebarBasket() {
    document.getElementById("sidebar-basket").style.right = "0";
}

function openSidebarNav() {
  	document.getElementById("sidebar-nav").style.right = "0";
}

function closeSidebar() {
  document.getElementById("sidebar-fav").style.right = "-105%";
  document.getElementById("sidebar-basket").style.right = "-105%";
  document.getElementById("sidebar-nav").style.right = "-105%";
}

function closeToast() {
    document.getElementById("toast-container").classList.toggle("hide")
}