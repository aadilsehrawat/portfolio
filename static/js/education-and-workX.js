const buttons = document.querySelectorAll('.toggle-button');
buttons.forEach(button => {
    button.addEventListener('click', function(e) {
        let x = e.clientX - e.target.offsetLeft;
        let y = e.clientY - e.target.offsetTop;

        let ripples = document.createElement('ripple');
        ripples.style.left = x + 'px';
        ripples.style.top = y + 'px';
        this.appendChild(ripples);

        setTimeout(() => {
            ripples.remove()
        }, 1000);
    });
});

function redirectToURL(url) {
    setTimeout(function() {
        window.location.href = url;
    }, 500);
}
