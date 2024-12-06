//footer-nav
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

//index
document.addEventListener("DOMContentLoaded", () => {
    const eventList = document.querySelector(".event-list");
    const overlay = document.getElementById("overlay");
    const scrollButton = document.getElementById("scroll-button");

    for (let i = 1; i <= 20; i++) {
        const eventItem = document.createElement("div");
        eventItem.className = "event-item";
        eventItem.innerHTML = `
      <img src="../../picture/icon-event.png" alt="">
      <span class="title">Event ${i}</span>
    `;
        eventList.appendChild(eventItem);

        eventItem.addEventListener("click", () => {
            const isExpanded = eventItem.classList.toggle("expanded");
            if (isExpanded) {
                eventItem.innerHTML += `
          <textarea readonly placeholder="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut in porttitor est. Praesent ullamcorper dui non malesuada ultrices. Nunc lobortis ultrices velit, eget cursus purus interdum ut. Vivamus semper dolor velit, vel iaculis lectus imperdiet nec. Fusce varius, odio ac aliquet tincidunt, lorem erat mollis nulla, ac viverra ante tellus ac mauris. Mauris porta tempor gravida. Morbi nec velit purus. Morbi ut hendrerit mauris."></textarea>
          <button>Beitreten</button>
        `;
            } else {
                eventItem.innerHTML = `
          <img src="../../picture/icon-event.png" alt="Event">
          <span class="title">Event ${i}</span>
        `;
            }
        });
    }

    scrollButton.addEventListener("click", () => {
        overlay.style.display = "block";
    });

    overlay.addEventListener("click", (e) => {
        if (e.target === overlay) {
            overlay.style.display = "none";
        }
    });
});
