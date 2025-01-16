document.getElementById('contactForm').addEventListener('submit', function (e) {
    e.preventDefault();
    alert('Thank you for reaching out! We will get back to you shortly.');
});
document.addEventListener('DOMContentLoaded', () => {
    const appointmentForm = document.querySelector('#appointment-form');
    const physicalForm = document.querySelector('#physical-form');

    if (appointmentForm) {
        appointmentForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Your online appointment has been booked successfully!');
            appointmentForm.reset();
        });
    }

    if (physicalForm) {
        physicalForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Your physical appointment has been scheduled successfully!');
            physicalForm.reset();
        });
    }
});
// Fade-in effect for the booking success page
window.onload = function() {
    var successMessage = document.querySelector('.booking-success-message');
    successMessage.style.opacity = 0;

    setTimeout(function() {
        successMessage.style.transition = 'opacity 1s ease-in';
        successMessage.style.opacity = 1;
    }, 100); // Fade-in delay
};

// Auto-redirect after 5 seconds (Optional)
setTimeout(function() {
    window.location.href = '/';  // Redirect to homepage after 5 seconds
}, 5000);

