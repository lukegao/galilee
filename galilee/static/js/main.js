
document.querySelector("button.navbar-toggler").addEventListener('click', function(){
    target = this.dataset.target;
    var nav = document.querySelector(target);
    nav.classList.toggle("collapse");
    this.classList.toggle("collapsed");
});
