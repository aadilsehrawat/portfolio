// const observer = new IntersectionObserver((entries) => {
//     entries.forEach((entry) => {
//         if (entry.isIntersecting) {
//             entry.target.classList.add('custom-show');
//         } else {
//             entry.target.classList.remove('custom-show');
//         }
//     });
// });

// const hiddenElements = document.querySelectorAll('.custom-hidden');
// hiddenElements.forEach((element) => observer.observe(element));


function hasCrossed(element) {
    const rect = element.getBoundingClientRect();
    const viewportHeight = window.innerHeight;
    return rect.top - viewportHeight * 0.75 <= 0;
}

function handleScroll() {
    const hiddenElements = document.querySelectorAll('.custom-hidden');
    hiddenElements.forEach((element) => {
        if (hasCrossed(element)) {
            element.classList.add('custom-show');
        } else {
            element.classList.remove('custom-show');
        }
    });
}
window.addEventListener('scroll', handleScroll);
handleScroll();
