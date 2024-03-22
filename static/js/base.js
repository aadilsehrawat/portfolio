window.onload = function() {
    var headerHeight = document.getElementById('header').offsetHeight;
    var footerHeight = document.getElementById('footer').offsetHeight;
    var contentHeight = window.innerHeight - (headerHeight + footerHeight);
    document.querySelector('#content').style.marginTop = headerHeight + 'px';
    document.querySelector('#content').style.minHeight = contentHeight + 'px';
};