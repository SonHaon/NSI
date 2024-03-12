modal = document.getElementById('myModal');
modal_image = document.getElementById("img_show");
liste_images = ['images/I_love_HTML.jpg', 'images/banniere.png', 'images/1200px-HTML5_logo_and_wordmark.svg.png', 'images/NSI.webp', 'images/Bandeau2_NSI.jpg', 'images/logo-st-e.jpg', 'images/i-love-python.png', 'images/CSS3_logo_and_wordmark.svg.png', 'images/html.png', 'images/specilaite-nsi.jpeg'];


function Unzoom() {
    modal.style.display = "none"
}

function Zoom_slideshow(i) {
    modal.style.display = "block"
    modal_image.src = liste_images[i-1]
}

function Zoom(src) {
    modal.style.display = "block"
    modal_image.src = src
}