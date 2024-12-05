// Burger Menu
function initializeBurgerMenu() {
    const burgerButton = document.getElementById("burger-menu-button");
    const menuContent = document.getElementById("burger-menu-content");

    if (!burgerButton || !menuContent) {
        console.error("Burger-Menü-Elemente nicht gefunden");
        return;
    }

    burgerButton.addEventListener("click", (event) => {
        event.stopPropagation(); // Verhindert das Schließen durch Klick auf das Menü
        const isVisible = menuContent.style.display === "block";
        menuContent.style.display = isVisible ? "none" : "block";
    });

    document.addEventListener("click", () => {
        menuContent.style.display = "none";
    });
}

document.addEventListener("DOMContentLoaded", () => {
    fetch("../placeholder/footer-nav.html")
        .then((response) => response.text())
        .then((html) => {
            document.getElementById("footer-placeholder").innerHTML = html;
            initializeBurgerMenu(); // Burger-Menü nach Einfügen initialisieren
        })
        .catch((error) => console.error("Fehler beim Laden des Footers:", error));
});
