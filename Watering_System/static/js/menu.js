// Hide submenus
HideAllContent = () => {
    $("#Sys_info").addClass("disabledbutton");
    $("#Sys_info").find('input').each(function () {
        $(this).prop('disabled', true);
    });
}

UnhideContent = () => {
    $("#Sys_info").removeClass("disabledbutton");
    $("#Sys_info").find('input').each(function () {
        $(this).prop('disabled', false);
    });
}

$(document).ready(function () {
    url = window.location.href;
    var sys_info = document.getElementById("Sys_info");
    var content = document.getElementById("content-page");
    var sidemenu = document.getElementById("sidemenu");
    var sidebar_container = document.getElementById("sidebar-container");
    if (/Android|webOS|iPhone|iPad|Mac|Macintosh|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
        $('.menu-collapsed').removeClass('d-flex');
        $('.sidebar-submenu').removeClass('d-flex');
        $('.submenu-icon').removeClass('d-flex');
        $('#sidebar-container').removeClass('sidebar-expanded');

        $('.menu-collapsed').addClass('d-none');
        $('.sidebar-submenu').addClass('d-none');
        $('.submenu-icon').addClass('d-none');
        $('#sidebar-container').addClass('sidebar-collapsed');
        var min_mobile_menu_width = 100 + "px";
        // Treating d-flex/d-none on separators with title
        var SeparatorTitle = $('.sidebar-separator-title');
        if (SeparatorTitle.hasClass('d-flex')) {
            SeparatorTitle.removeClass('d-flex');
        }
        sidemenu.style.width = min_mobile_menu_width;
        sys_info.style.width = (content.offsetWidth - sidebar_container.offsetWidth - 30).toString() + "px";
    } else {
        document.getElementById("sidemenu").style.width = (document.getElementById("sidemenu").offsetWidth + 10).toString() + "px";
        sys_info.style.width = (content.offsetWidth - sidebar_container.offsetWidth - 30).toString() + "px";
    }
    $(".list-group a").each(function () {
        if (url == (this.href)) {
            $(this).addClass("active-link");
        }
    });
})

$('#body-row .collapse').collapse('hide');
// Collapse/Expand icon
$('#collapse-icon').addClass('fas fa-bars fa-2x mr-3');

// Collapse click
$('[data-toggle=sidebar-colapse]').click(function () {
    SidebarCollapse();
});
var sidemenu = document.getElementById("sidemenu");
const max_menu_width = (sidemenu.offsetWidth + 10).toString() + "px";
const max_mobile_menu_width = ((sidemenu.offsetWidth + 10) * 3).toString() + "px";
const CONTENT_HEIGHT = document.getElementById("Sys_info");

function SidebarCollapse() {
    $('.menu-collapsed').toggleClass('d-none');
    $('.sidebar-submenu').toggleClass('d-none');
    $('.submenu-icon').toggleClass('d-none');
    $('#sidebar-container').toggleClass('sidebar-expanded sidebar-collapsed');
    var SeparatorTitle = $('.sidebar-separator-title');
    var sidemenu = document.getElementById('sidemenu');
    var sys_info = document.getElementById("Sys_info");
    var content = document.getElementById("content-page");
    var sidebar_container = document.getElementById("sidebar-container");
    if (/Android|webOS|iPhone|iPad|Mac|Macintosh|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
        if (SeparatorTitle.hasClass('d-flex')) {
            sidemenu.style.width = sidebar_container.offsetWidth.toString() + "px";
            SeparatorTitle.removeClass('d-flex');
            sys_info.style.width = (content.offsetWidth - sidebar_container.offsetWidth - 30).toString() + "px";
            sys_info.style.marginLeft = "auto";
            UnhideContent();
        } else {
            SeparatorTitle.addClass('d-flex');
            sidemenu.style.zIndex = "11";
            sidemenu.style.position = "absolute";
            SeparatorTitle.addClass('d-flex');
            sidemenu.style.width = 250 + "px";
            sys_info.style.width = (content.offsetWidth - 100 - 30).toString() + "px";
            sys_info.style.marginLeft = 120 + "px";
            HideAllContent();
        }
        sidemenu.style.height = sys_info.offsetHeight.toString() + "px";
    } else {
        if (SeparatorTitle.hasClass('d-flex')) {
            sidemenu.style.width = sidebar_container.offsetWidth.toString() + "px";
            SeparatorTitle.removeClass('d-flex');
            sys_info.style.width = (content.offsetWidth - sidebar_container.offsetWidth - 30).toString() + "px";
        } else {
            SeparatorTitle.addClass('d-flex');
            sidemenu.style.width = max_menu_width;
            sys_info.style.width = (content.offsetWidth - sidebar_container.offsetWidth - 30).toString() + "px";
        }
        sidemenu.style.height = sys_info.offsetHeight.toString() + "px";
    }
}

$(window).resize(function () {
    if (/Android|webOS|iPhone|iPad|Mac|Macintosh|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
        SidebarCollapse();

    } else {
        location.reload();
    }
});