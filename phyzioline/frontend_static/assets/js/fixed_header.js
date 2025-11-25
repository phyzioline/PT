    window.addEventListener('scroll', function() {
        const header = document.querySelector('header');
        if (window.scrollY > 100) {
            header.classList.add('fixed-top');
            header.classList.add('shadow-sm');
        } else {
            header.classList.remove('fixed-top');
            header.classList.remove('shadow-sm');
        }
    });
