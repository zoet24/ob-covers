function openSidebarFav() {
	document.getElementById("sidebar-fav").style.borderWidth = "4px"
	if (window.innerWidth <= 576) {
        document.getElementById("sidebar-fav").style.width = "75%";
    }
    else if (window.innerWidth <= 768) {
        document.getElementById("sidebar-fav").style.width = "50%";
    }
    else if (window.innerWidth <= 992) {
        document.getElementById("sidebar-fav").style.width = "33%";
    }
    else {
    	document.getElementById("sidebar-fav").style.width = "25%";
    }
}

function openSidebarBasket() {
	document.getElementById("sidebar-basket").style.borderWidth = "4px"
  	if (window.innerWidth <= 576) {
        document.getElementById("sidebar-basket").style.width = "75%";
    }
    else if (window.innerWidth <= 768) {
        document.getElementById("sidebar-basket").style.width = "50%";
    }
    else if (window.innerWidth <= 992) {
        document.getElementById("sidebar-basket").style.width = "33%";
    }
    else {
    	document.getElementById("sidebar-basket").style.width = "25%";
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