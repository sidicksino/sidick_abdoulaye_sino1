    // Détection du défilement pour fixer la navbar
    const header = document.getElementById('header');
    const scrollThreshold = 100; // Définir à partir de combien de pixels la navbar devient fixe

    window.addEventListener('scroll', () => {
        if (window.scrollY > scrollThreshold) {
            header.classList.add('fixed');
        } else {
            header.classList.remove('fixed');
        }
    });

    // Gestion du menu toggle (mobile)
    const menuToggle = document.getElementById('menu-toggle');
    const navMenu = document.getElementById('nav-menu');

    menuToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        menuToggle.classList.toggle('active');
    });

    // Animation du compteur
    const counters = document.querySelectorAll('.counter');

    counters.forEach((counter) => {
        counter.innerText = '0'; // Initial number

        const updateCounter = () => {
            const target = +counter.getAttribute('data-target'); // Get target number
            const count = +counter.innerText.replace('+', ''); // Remove "+" for calculations

            const increment = target / 100; // Adjust speed by changing the divisor

            if (count < target) {
                counter.innerText = `${Math.ceil(count + increment)}+`; // Add "+" to the number
                setTimeout(updateCounter, 60); // Animation speed
            } else {
                counter.innerText = `${target}+`; // Add "+" at the end
            }
        };

        updateCounter();
    });
	
    // Bouton "Retour en haut"
    const topButton = document.getElementById('topButton');

    // Afficher ou masquer le bouton en fonction du défilement
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) { // Afficher le bouton après 300 pixels de défilement
            topButton.classList.add('show');
        } else {
            topButton.classList.remove('show');
        }
    });

    // Retour en haut de la page lors du clic sur le bouton
    topButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth' // Défilement fluide
        });
    });