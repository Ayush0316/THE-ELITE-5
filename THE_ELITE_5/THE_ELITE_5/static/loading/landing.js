window.addEventListener("scroll", function () {
    const scrollPosition = window.scrollY;

    if (scrollPosition > 0) {
        document.querySelector("nav").style.background = "#9232ea"; // Change to black with 0.8 opacity
    } else {
        document.querySelector("nav").style.background = "rgba(0, 0, 0, 0)"; // Change back to transparent
    }
});
