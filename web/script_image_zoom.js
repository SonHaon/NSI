var modal = document.getElementById('myModal');
var modal_image = document.getElementById("img_show");
var images = document.getElementsByClassName('modal-img');

for (var i = 0; i < images.length; i++) {
    images[i].onclick = function(){
        modal.style.display = "block";
        modal_image.src = this.src;
    }
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}