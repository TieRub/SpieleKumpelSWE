// Function to dynamically load an HTML file into a specific element
function loadComponent(selector, file) {
    const filePath = `../placeholder/${file}`;
    fetch(filePath)
        .then(response => {
            if (!response.ok) throw new Error(`Error loading ${filePath}: ${response.statusText}`);
            return response.text();
        })
        .then(html => {
            document.querySelector(selector).innerHTML = html;
        })
        .catch(error => console.error(error));
}

// Load header and footer
loadComponent('#header-placeholder', 'header.html');
loadComponent('#footer-placeholder', 'footer.html');

// Scroll to top function
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Function to dynamically load an HTML file into a specific element
function loadComponent(selector, file) {
    const filePath = `../placeholder/${file}`;
    fetch(filePath)
        .then(response => {
            if (!response.ok) throw new Error(`Error loading ${filePath}: ${response.statusText}`);
            return response.text();
        })
        .then(html => {
            document.querySelector(selector).innerHTML = html;
        })
        .catch(error => console.error(error));
}

// Load header, footer, and sidebar
loadComponent('#header-placeholder', 'header.html');
loadComponent('#footer-placeholder', 'footer.html');
loadComponent('#sidebar-placeholder', 'sidebar.html'); // Added sidebar placeholder

// Function to toggle the sidebar
function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    if (sidebar.style.right === '0px') {
        sidebar.style.right = '-250px'; // Hide sidebar
    } else {
        sidebar.style.right = '0px'; // Show sidebar
    }
}

// Scroll to top function
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}
