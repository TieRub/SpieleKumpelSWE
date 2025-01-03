function initializeBurgerMenu() {
    const burgerButton = document.getElementById("navbar-menu-button");
    const menuContent = document.getElementById("navbar-menu-content");

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
    fetch("../navbar/navbar.html")
        .then((response) => response.text())
        .then((html) => {
            document.getElementById("navbar").innerHTML = html;
            initializeBurgerMenu(); // Burger-Menü nach Einfügen initialisieren
        })
        .catch((error) => console.error("Fehler beim Laden des Footers:", error));
});