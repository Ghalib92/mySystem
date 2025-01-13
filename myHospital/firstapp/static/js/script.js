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
