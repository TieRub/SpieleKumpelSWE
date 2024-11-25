// Function to dynamically load an HTML file into a specific element
function loadComponent(selector, file) {
    fetch(`placeholder/${file}`)
        .then(response => {
            if (!response.ok) throw new Error(`Error loading ${file}: ${response.statusText}`);
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
