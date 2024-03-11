var slideIndex = 1;
var liste_images = ['images/I_love_HTML.jpg', 'images/banniere.png', 'images/1200px-HTML5_logo_and_wordmark.svg.png', 'images/NSI.webp', 'images/Bandeau2_NSI.jpg', 'images/logo-st-e.jpg', 'images/i-love-python.png', 'images/CSS3_logo_and_wordmark.svg.png', 'images/html.png', 'images/specilaite-nsi.jpeg'];

showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function showSlides(n) {
    var images = liste_images
    var slides = document.getElementsByClassName("slide");
    if (n > images.length) {slideIndex = 1}
    if (n < 1) {slideIndex = images.length}
    slides[0].src = images[slideIndex-1];
}