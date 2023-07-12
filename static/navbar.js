// Get the current URL pathname
var pathName = window.location.pathname;

// Get all the nav links
var navLinks = document.querySelectorAll('.navbar-nav .nav-link');

// Loop through each nav link
navLinks.forEach(function(link) {
    // Get the link URL
    var linkUrl = link.getAttribute('href');

    // Compare the link URL with the current URL pathname
    if (linkUrl === pathName) {
        // Add the active class to the matching nav link
        link.classList.add('active');
    }
});