function openProfileDropdown() {
  document.getElementById("nav-profile-dropdown-menu").classList.toggle("show");
}

function openSidebarFav() {
	document.getElementById("sidebar-fav").style.borderLeftWidth = "4px"
	if (window.innerWidth <= 576) {
        document.getElementById("sidebar-fav").style.width = "85%";
    }
    else if (window.innerWidth <= 768) {
        document.getElementById("sidebar-fav").style.width = "85%";
    }
    else if (window.innerWidth <= 992) {
        document.getElementById("sidebar-fav").style.width = "50%";
    }
    else {
    	document.getElementById("sidebar-fav").style.width = "50%";
    }
}

function openSidebarBasket() {
	document.getElementById("sidebar-basket").style.borderLeftWidth = "4px"
  	if (window.innerWidth <= 400) {
        document.getElementById("sidebar-basket").style.borderLeftWidth = "0px"
        document.getElementById("sidebar-basket").style.width = "100%";
    }
    // else if (window.innerWidth <= 768) {
    //     document.getElementById("sidebar-basket").style.width = "80%";
    // }
    // else if (window.innerWidth <= 992) {
    //     document.getElementById("sidebar-basket").style.width = "50%";
    // }
    else {
    	document.getElementById("sidebar-basket").style.width = "450px";
    }
}

function openSidebarNav() {
	document.getElementById("sidebar-nav").style.borderWidth = "4px"
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

// Add function for clicking out of sidebars and menus to close (https://www.w3schools.com/howto/howto_js_dropdown.asp)