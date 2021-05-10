function openProfileDropdown() {
  document.getElementById("nav-profile-dropdown-menu").classList.toggle("show");
}

function openSidebarFav() {
	if (window.innerWidth <= 400) {
        document.getElementById("sidebar-fav").style.borderLeftWidth = "0px"
        document.getElementById("sidebar-fav").style.width = "100%";
    }
    else {
        document.getElementById("sidebar-fav").style.borderLeftWidth = "0px"
        document.getElementById("sidebar-fav").style.width = "450px";
    }
}

function openSidebarBasket() {
  	if (window.innerWidth <= 400) {
        document.getElementById("sidebar-basket").style.borderLeftWidth = "0px"
        document.getElementById("sidebar-basket").style.width = "100%";
    }
    else {
        document.getElementById("sidebar-basket").style.borderLeftWidth = "0px"
    	document.getElementById("sidebar-basket").style.width = "450px";
    }
}

function openSidebarNav() {
	document.getElementById("sidebar-nav").style.borderLeftWidth = "2px"
  	document.getElementById("sidebar-nav").style.width = "75%";
}

function closeSidebar() {
  document.getElementById("sidebar-fav").style.width = "0";
  document.getElementById("sidebar-basket").style.width = "0";
  document.getElementById("sidebar-nav").style.width = "0";
  document.getElementById("sidebar-fav").style.borderWidth = "0px";
  document.getElementById("sidebar-basket").style.borderWidth = "0px";
  document.getElementById("sidebar-nav").style.borderWidth = "0px";
}

function closeToast() {
    document.getElementById("toast-container").classList.toggle("hide")
}