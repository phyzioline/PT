// Main JavaScript file for Ask Your Doctor website
$(document).ready(function() {
    
    // Initialize all components
    initializeNavigation();
    initializeAnimations();
    initializeForms();
    initializeSearch();
    initializeModals();
    initializeTooltips();
    
    // Navigation functionality
    function initializeNavigation() {
        // Smooth scrolling for anchor links
        $('a[href^="#"]').on('click', function(e) {
            e.preventDefault();
            const target = $(this.getAttribute('href'));
            if (target.length) {
                $('html, body').stop().animate({
                    scrollTop: target.offset().top - 100
                }, 1000);
            }
        });
        
        // Active navigation highlighting
        $(window).on('scroll', function() {
            const scrollPos = $(window).scrollTop();
            $('.nav-link').each(function() {
                const currLink = $(this);
                const refElement = $(currLink.attr('href'));
                if (refElement.length && 
                    refElement.position().top <= scrollPos + 100 && 
                    refElement.position().top + refElement.height() > scrollPos + 100) {
                    $('.nav-link').removeClass('active');
                    currLink.addClass('active');
                }
            });
        });
        
        // Mobile menu close on link click
        $('.navbar-nav .nav-link').on('click', function() {
            $('.navbar-collapse').collapse('hide');
        });
        
        // Dropdown hover effect
        $('.dropdown').hover(
            function() {
                $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(300);
            },
            function() {
                $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(300);
            }
        );
    }
    
    // Animation functionality
    function initializeAnimations() {
        // Fade in elements on scroll
        function fadeInOnScroll() {
            $('.fade-in-up, .fade-in-left, .fade-in-right').each(function() {
                const elementTop = $(this).offset().top;
                const elementBottom = elementTop + $(this).outerHeight();
                const viewportTop = $(window).scrollTop();
                const viewportBottom = viewportTop + $(window).height();
                
                if (elementBottom > viewportTop && elementTop < viewportBottom) {
                    $(this).addClass('animate');
                }
            });
        }
        
        $(window).on('scroll', fadeInOnScroll);
        fadeInOnScroll(); // Initial check
        
        // Counter animation
        function animateCounters() {
            $('.counter').each(function() {
                const $this = $(this);
                const countTo = $this.attr('data-count');
                
                $({ countNum: $this.text() }).animate({
                    countNum: countTo
                }, {
                    duration: 2000,
                    easing: 'linear',
                    step: function() {
                        $this.text(Math.floor(this.countNum));
                    },
                    complete: function() {
                        $this.text(this.countNum);
                    }
                });
            });
        }
        
        // Trigger counter animation when in view
        $(window).on('scroll', function() {
            $('.counter').each(function() {
                const elementTop = $(this).offset().top;
                const viewportBottom = $(window).scrollTop() + $(window).height();
                
                if (elementTop < viewportBottom && !$(this).hasClass('animated')) {
                    $(this).addClass('animated');
                    animateCounters();
                }
            });
        });
        
        // Parallax effect for hero section
        $(window).on('scroll', function() {
            const scrolled = $(window).scrollTop();
            const parallax = $('.hero-section');
            const speed = scrolled * 0.5;
            
            parallax.css('transform', 'translateY(' + speed + 'px)');
        });
    }
    
    // Form functionality
    function initializeForms() {
        // Contact form submission
        $('#contactForm').on('submit', function(e) {
            e.preventDefault();
            
            const form = $(this);
            const submitBtn = form.find('button[type="submit"]');
            const originalText = submitBtn.text();
            
            // Show loading state
            submitBtn.html('<span class="spinner"></span> Sending...').prop('disabled', true);
            
            // Simulate form submission
            setTimeout(function() {
                showNotification('Message sent successfully!', 'success');
                form[0].reset();
                submitBtn.text(originalText).prop('disabled', false);
            }, 2000);
        });
        
        // Login form submission
        $('#loginForm').on('submit', function(e) {
            e.preventDefault();
            
            const form = $(this);
            const submitBtn = form.find('button[type="submit"]');
            const originalText = submitBtn.text();
            
            // Show loading state
            submitBtn.html('<span class="spinner"></span> Signing in...').prop('disabled', true);
            
            // Simulate login
            setTimeout(function() {
                showNotification('Login successful!', 'success');
                submitBtn.text(originalText).prop('disabled', false);
                // Redirect to dashboard or home page
                window.location.href = 'index.html';
            }, 2000);
        });
        
        // Registration form submission
        $('#registerForm').on('submit', function(e) {
            e.preventDefault();
            
            const form = $(this);
            const password = form.find('#password').val();
            const confirmPassword = form.find('#confirmPassword').val();
            
            if (password !== confirmPassword) {
                showNotification('Passwords do not match!', 'error');
                return;
            }
            
            const submitBtn = form.find('button[type="submit"]');
            const originalText = submitBtn.text();
            
            // Show loading state
            submitBtn.html('<span class="spinner"></span> Creating account...').prop('disabled', true);
            
            // Simulate registration
            setTimeout(function() {
                showNotification('Account created successfully!', 'success');
                submitBtn.text(originalText).prop('disabled', false);
                // Switch to login form or redirect
                switchToLogin();
            }, 2000);
        });
        
        // User type selection
        $('.user-type-btn').on('click', function() {
            $('.user-type-btn').removeClass('active');
            $(this).addClass('active');
            $('#userType').val($(this).data('type'));
        });
        
        // Password visibility toggle
        $('.password-toggle').on('click', function() {
            const input = $(this).siblings('input');
            const icon = $(this).find('i');
            
            if (input.attr('type') === 'password') {
                input.attr('type', 'text');
                icon.removeClass('fa-eye').addClass('fa-eye-slash');
            } else {
                input.attr('type', 'password');
                icon.removeClass('fa-eye-slash').addClass('fa-eye');
            }
        });
    }
    
    // Search functionality
    function initializeSearch() {
        // Live search for jobs, courses, doctors
        $('.search-input').on('input', function() {
            const searchTerm = $(this).val().toLowerCase();
            const targetCards = $('.item-card');
            
            if (searchTerm === '') {
                targetCards.show();
                return;
            }
            
            targetCards.each(function() {
                const cardText = $(this).text().toLowerCase();
                if (cardText.includes(searchTerm)) {
                    $(this).show();
                } else {
                    $(this).hide();
                }
            });
        });
        
        // Filter functionality
        $('.filter-select').on('change', function() {
            const filterValue = $(this).val();
            const filterType = $(this).data('filter');
            const targetCards = $('.item-card');
            
            if (filterValue === '' || filterValue === 'all') {
                targetCards.show();
                return;
            }
            
            targetCards.each(function() {
                const cardData = $(this).data(filterType);
                if (cardData && cardData.toString().toLowerCase() === filterValue.toLowerCase()) {
                    $(this).show();
                } else {
                    $(this).hide();
                }
            });
        });
        
        // Advanced search toggle
        $('.advanced-search-toggle').on('click', function() {
            $('.advanced-search').slideToggle();
            $(this).find('i').toggleClass('fa-chevron-down fa-chevron-up');
        });
    }
    
    // Modal functionality
    function initializeModals() {
        // Doctor profile modal
        $('.view-doctor-btn').on('click', function() {
            const doctorId = $(this).data('doctor-id');
            loadDoctorProfile(doctorId);
        });
        
        // Job details modal
        $('.view-job-btn').on('click', function() {
            const jobId = $(this).data('job-id');
            loadJobDetails(jobId);
        });
        
        // Course details modal
        $('.view-course-btn').on('click', function() {
            const courseId = $(this).data('course-id');
            loadCourseDetails(courseId);
        });
        
        // Appointment booking modal
        $('.book-appointment-btn').on('click', function() {
            const doctorId = $(this).data('doctor-id');
            showAppointmentModal(doctorId);
        });
    }
    
    // Tooltip initialization
    function initializeTooltips() {
        // Initialize Bootstrap tooltips
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function(tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
        
        // Initialize Bootstrap popovers
        const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
        popoverTriggerList.map(function(popoverTriggerEl) {
            return new bootstrap.Popover(popoverTriggerEl);
        });
    }
    
    // Utility functions
    function showNotification(message, type = 'info') {
        const alertClass = type === 'success' ? 'alert-success' : 
                          type === 'error' ? 'alert-danger' : 'alert-info';
        
        const notification = $(`
            <div class="alert ${alertClass} alert-dismissible fade show position-fixed" 
                 style="top: 100px; right: 20px; z-index: 9999; min-width: 300px;">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>
        `);
        
        $('body').append(notification);
        
        // Auto-dismiss after 5 seconds
        setTimeout(function() {
            notification.alert('close');
        }, 5000);
    }
    
    function loadDoctorProfile(doctorId) {
        // Simulate loading doctor profile data
        const doctorData = {
            name: 'Dr. Sarah Johnson',
            specialty: 'Cardiologist',
            experience: '15 years',
            rating: 4.9,
            reviews: 234,
            education: 'Harvard Medical School',
            languages: ['English', 'Spanish'],
            about: 'Dr. Johnson is a board-certified cardiologist with over 15 years of experience...'
        };
        
        // Populate modal with doctor data
        $('#doctorModal .modal-title').text(doctorData.name);
        $('#doctorModal .modal-body').html(`
            <div class="row">
                <div class="col-md-4">
                    <img src="../assets/images/doctor-placeholder.jpg" class="img-fluid rounded" alt="${doctorData.name}">
                </div>
                <div class="col-md-8">
                    <h5>${doctorData.specialty}</h5>
                    <p><strong>Experience:</strong> ${doctorData.experience}</p>
                    <p><strong>Rating:</strong> ${doctorData.rating}/5 (${doctorData.reviews} reviews)</p>
                    <p><strong>Education:</strong> ${doctorData.education}</p>
                    <p><strong>Languages:</strong> ${doctorData.languages.join(', ')}</p>
                    <p><strong>About:</strong> ${doctorData.about}</p>
                </div>
            </div>
        `);
        
        $('#doctorModal').modal('show');
    }
    
    function loadJobDetails(jobId) {
        // Simulate loading job details
        const jobData = {
            title: 'Senior Nurse - ICU',
            company: 'City General Hospital',
            location: 'New York, NY',
            salary: '$75,000 - $95,000',
            type: 'Full-time',
            description: 'We are seeking an experienced ICU nurse to join our team...',
            requirements: ['BSN degree', '3+ years ICU experience', 'BLS certification'],
            benefits: ['Health insurance', 'Retirement plan', 'Paid time off']
        };
        
        // Populate modal with job data
        $('#jobModal .modal-title').text(jobData.title);
        $('#jobModal .modal-body').html(`
            <div class="job-details">
                <h6>Company: ${jobData.company}</h6>
                <p><strong>Location:</strong> ${jobData.location}</p>
                <p><strong>Salary:</strong> ${jobData.salary}</p>
                <p><strong>Type:</strong> ${jobData.type}</p>
                <h6>Description:</h6>
                <p>${jobData.description}</p>
                <h6>Requirements:</h6>
                <ul>${jobData.requirements.map(req => `<li>${req}</li>`).join('')}</ul>
                <h6>Benefits:</h6>
                <ul>${jobData.benefits.map(benefit => `<li>${benefit}</li>`).join('')}</ul>
            </div>
        `);
        
        $('#jobModal').modal('show');
    }
    
    function loadCourseDetails(courseId) {
        // Simulate loading course details
        const courseData = {
            title: 'Advanced Cardiology Certification',
            instructor: 'Dr. Michael Chen',
            duration: '8 weeks',
            price: '$299',
            level: 'Advanced',
            description: 'Comprehensive course covering advanced cardiology topics...',
            curriculum: ['Heart anatomy', 'Diagnostic procedures', 'Treatment protocols'],
            schedule: 'Tuesdays and Thursdays, 7:00 PM - 9:00 PM'
        };
        
        // Populate modal with course data
        $('#courseModal .modal-title').text(courseData.title);
        $('#courseModal .modal-body').html(`
            <div class="course-details">
                <h6>Instructor: ${courseData.instructor}</h6>
                <p><strong>Duration:</strong> ${courseData.duration}</p>
                <p><strong>Price:</strong> ${courseData.price}</p>
                <p><strong>Level:</strong> ${courseData.level}</p>
                <p><strong>Schedule:</strong> ${courseData.schedule}</p>
                <h6>Description:</h6>
                <p>${courseData.description}</p>
                <h6>Curriculum:</h6>
                <ul>${courseData.curriculum.map(item => `<li>${item}</li>`).join('')}</ul>
            </div>
        `);
        
        $('#courseModal').modal('show');
    }
    
    function showAppointmentModal(doctorId) {
        // Show appointment booking modal
        $('#appointmentModal').modal('show');
        
        // Initialize date picker for appointment
        const today = new Date();
        const tomorrow = new Date(today);
        tomorrow.setDate(tomorrow.getDate() + 1);
        
        $('#appointmentDate').attr('min', tomorrow.toISOString().split('T')[0]);
    }
    
    function switchToLogin() {
        // Switch from register to login form
        $('.auth-toggle').trigger('click');
    }
    
    // Back to top button
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 300) {
            $('#backToTop').fadeIn();
        } else {
            $('#backToTop').fadeOut();
        }
    });
    
    $('#backToTop').on('click', function() {
        $('html, body').animate({ scrollTop: 0 }, 800);
    });
    
    // Loading screen
    $(window).on('load', function() {
        $('#loadingScreen').fadeOut();
    });
    
    // Newsletter subscription
    $('#newsletterForm').on('submit', function(e) {
        e.preventDefault();
        const email = $(this).find('input[type="email"]').val();
        
        if (email) {
            showNotification('Thank you for subscribing to our newsletter!', 'success');
            $(this)[0].reset();
        }
    });
    
    // FAQ accordion
    $('.faq-question').on('click', function() {
        const answer = $(this).next('.faq-answer');
        const icon = $(this).find('i');
        
        $('.faq-answer').not(answer).slideUp();
        $('.faq-question i').not(icon).removeClass('fa-minus').addClass('fa-plus');
        
        answer.slideToggle();
        icon.toggleClass('fa-plus fa-minus');
    });
    
    // Rating system
    $('.rating-stars .star').on('click', function() {
        const rating = $(this).data('rating');
        const stars = $(this).parent().find('.star');
        
        stars.removeClass('active');
        stars.slice(0, rating).addClass('active');
        
        $(this).parent().next('input').val(rating);
    });
    
    // Image lazy loading
    function lazyLoadImages() {
        const images = document.querySelectorAll('img[data-src]');
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    }
    
    lazyLoadImages();
    
    // Print functionality
    $('.print-btn').on('click', function() {
        window.print();
    });
    
    // Share functionality
    $('.share-btn').on('click', function() {
        if (navigator.share) {
            navigator.share({
                title: document.title,
                url: window.location.href
            });
        } else {
            // Fallback: copy to clipboard
            navigator.clipboard.writeText(window.location.href).then(() => {
                showNotification('Link copied to clipboard!', 'success');
            });
        }
    });
});

// Additional utility functions
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

function formatDate(date) {
    return new Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    }).format(new Date(date));
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Export functions for use in other scripts
window.AskYourDoctor = {
    showNotification,
    loadDoctorProfile,
    loadJobDetails,
    loadCourseDetails,
    showAppointmentModal,
    formatCurrency,
    formatDate,
    debounce
};

