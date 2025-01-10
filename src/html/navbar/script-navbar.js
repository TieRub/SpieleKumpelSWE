function initializeBurgerMenu() {
    const burgerButton = document.getElementById("navbar-menu-button");
    const menuContent = document.getElementById("navbar-menu-content");

    if (!burgerButton || !menuContent) {
        console.error("Burger-Menü-Elemente nicht gefunden");
        return;
    }

    // Event-Listener für den Burger-Button
    burgerButton.addEventListener("click", (event) => {
        event.stopPropagation(); // Verhindert das Schließen durch Klick auf das Menü
        const isVisible = menuContent.style.display === "block";
        menuContent.style.display = isVisible ? "none" : "block";
    });

    // Event-Listener für das Schließen des Menüs beim Klick außerhalb
    document.addEventListener("click", (event) => {
        if (!burgerButton.contains(event.target) && !menuContent.contains(event.target)) {
            // Nur schließen, wenn der Klick nicht innerhalb des Menüs oder Buttons war
            menuContent.style.display = "none";
        }
    });
}

document.addEventListener("DOMContentLoaded", () => {
    fetch("/navbar.html")  // Korrigierter Pfad, falls die Datei relativ zum Wurzelverzeichnis geladen wird
        .then((response) => {
            if (!response.ok) {
                throw new Error('Netzwerkantwort war nicht okay');
            }
            return response.text();
        })
        .then((html) => {
            document.getElementById("navbar").innerHTML = html;
            initializeBurgerMenu(); // Burger-Menü nach Einfügen initialisieren
        })
        .catch((error) => {
            console.error("Fehler beim Laden der Navbar:", error);
        });
});
