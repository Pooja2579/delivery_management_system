// Example content for sneat-dashboard.js

document.addEventListener('DOMContentLoaded', function () {
    // Example of a basic script initialization
    console.log('Sneat Dashboard JavaScript loaded.');

    // Add any custom JavaScript functionality needed for your dashboard here

    // Example: Toggle sidebar
    const sidebarToggle = document.querySelector('.sidebar-toggle');
    sidebarToggle.addEventListener('click', function () {
        document.querySelector('.sidebar').classList.toggle('active');
    });

    // Add more functionalities as needed
});
