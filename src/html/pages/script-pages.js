document.addEventListener('DOMContentLoaded', function () {
    // Funktion, die prüft, ob der Benutzer eingeloggt ist
    function checkLoginStatus() {
        const userLoggedIn = localStorage.getItem('userLoggedIn'); // Oder ein Cookie

        // Überprüfen, ob der Benutzer auf einer der Seiten 'feed.html' oder 'profile.html' ist
        const currentPage = window.location.pathname.split('/').pop();

        if ((currentPage === 'feed.html' || currentPage === 'profile.html') && !userLoggedIn) {
            // Weiterleitung zur Login-Seite, wenn nicht eingeloggt
            window.location.href = 'logging.html';
        }
    }

    // Login-Status checken bei Seitenaufruf
    checkLoginStatus();

    // Login-Funktion
    const loginBtn = document.getElementById('login-btn');
    loginBtn && loginBtn.addEventListener('click', function() {
        const email = document.getElementById('login-email').value;
        const password = document.getElementById('login-password').value;

        // Login mit der Datenbank (API-Call)
        fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        }).then(response => response.json())
          .then(data => {
              if (data.success) {
                  localStorage.setItem('userLoggedIn', true); // Benutzer als eingeloggt markieren
                  window.location.href = 'profile.html'; // Weiterleitung zu Profilseite
              } else {
                  alert('Login fehlgeschlagen');
              }
          });
    });

    // Account-Erstellung
    const submitCreate = document.getElementById('submit-create');
    submitCreate && submitCreate.addEventListener('click', function() {
        const email = document.getElementById('create-email').value;
        const username = document.getElementById('create-username').value;
        const password = document.getElementById('create-password').value;

        // Check, ob E-Mail und Benutzername bereits existieren
        fetch('/api/check-account', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, username })
        }).then(response => response.json())
          .then(data => {
              if (data.exists) {
                  alert('E-Mail oder Benutzername bereits vergeben');
              } else {
                  // Account erstellen
                  fetch('/api/create-account', {
                      method: 'POST',
                      headers: {
                          'Content-Type': 'application/json'
                      },
                      body: JSON.stringify({ email, username, password })
                  }).then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            alert('Account erfolgreich erstellt');
                            localStorage.setItem('userLoggedIn', true); // Benutzer als eingeloggt markieren
                            window.location.href = 'profile.html'; // Weiterleitung zum Profil
                        } else {
                            alert('Account-Erstellung fehlgeschlagen');
                        }
                    });
              }
          });
    });

    // Öffnen des Account erstellen Modals
    const createAccountBtn = document.getElementById('create-account-btn');
    createAccountBtn && createAccountBtn.addEventListener('click', function() {
        const accountModal = document.getElementById('account-modal');
        const loginContainer = document.getElementById('login-container');
        accountModal.style.display = 'flex';
        loginContainer.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
    });

    // Schließen des Account erstellen Modals
    const closeModal = document.getElementById('close-modal');
    closeModal && closeModal.addEventListener('click', function() {
        const accountModal = document.getElementById('account-modal');
        const loginContainer = document.getElementById('login-container');
        accountModal.style.display = 'none';
        loginContainer.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
    });
});
