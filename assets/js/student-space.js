document.addEventListener('DOMContentLoaded', function() {
    // Gestion du formulaire de connexion
    const loginForm = document.querySelector('.login-form form');
    if (loginForm) {
        loginForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const studentId = document.getElementById('student-id').value;
            const password = document.getElementById('password').value;
            
            try {
                const response = await fetch('/api/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ student_id: studentId, password: password })
                });
                
                const data = await response.json();
                if (data.success) {
                    // Masquer le formulaire de connexion
                    document.querySelector('.login-section').style.display = 'none';
                    // Afficher le tableau de bord
                    document.querySelector('.student-dashboard').style.display = 'block';
                    // Charger les données de l'étudiant
                    loadStudentData();
                } else {
                    alert('Erreur de connexion : ' + data.message);
                }
            } catch (error) {
                console.error('Erreur:', error);
                alert('Une erreur est survenue lors de la connexion');
            }
        });
    }
    
    // Calendrier
    function initCalendar() {
        const calendar = document.querySelector('.calendar-grid');
        const date = new Date();
        const month = date.getMonth();
        const year = date.getFullYear();
        
        // Obtenir le premier jour du mois
        const firstDay = new Date(year, month, 1);
        const lastDay = new Date(year, month + 1, 0);
        
        // Créer les jours du calendrier
        let currentDate = 1;
        for (let i = 0; i < 42; i++) {
            const dayElement = document.createElement('div');
            dayElement.classList.add('calendar-day');
            
            if (i >= firstDay.getDay() && currentDate <= lastDay.getDate()) {
                dayElement.textContent = currentDate;
                
                // Ajouter la classe 'event' pour certaines dates (exemple)
                if (currentDate === 15 || currentDate === 25) {
                    dayElement.classList.add('event');
                    dayElement.setAttribute('data-event', 'Événement important');
                }
                
                currentDate++;
            }
            
            calendar.appendChild(dayElement);
        }
        
        // Ajouter des info-bulles pour les événements
        const eventDays = document.querySelectorAll('.calendar-day.event');
        eventDays.forEach(day => {
            day.addEventListener('click', function() {
                alert(this.getAttribute('data-event'));
            });
        });
    }
    
    // Charger les cours
    async function loadCourses() {
        try {
            const response = await fetch('/api/courses');
            const data = await response.json();
            
            if (data.success) {
                const coursesList = document.querySelector('.dashboard-card ul');
                coursesList.innerHTML = data.courses.map(course => 
                    `<li>${course.code} - ${course.name}</li>`
                ).join('');
            }
        } catch (error) {
            console.error('Erreur lors du chargement des cours:', error);
        }
    }
    
    // Charger les notes
    async function loadGrades() {
        try {
            const response = await fetch('/api/grades');
            const data = await response.json();
            
            if (data.success) {
                const gradesCard = document.querySelector('.dashboard-card:nth-child(4)');
                gradesCard.innerHTML = '<h3><i class="fas fa-chart-line"></i> Mes Notes</h3>' +
                    data.grades.map(grade => 
                        `<p>${grade.course_id}: ${grade.value}/20</p>`
                    ).join('');
            }
        } catch (error) {
            console.error('Erreur lors du chargement des notes:', error);
        }
    }
    
    // Fonction pour charger toutes les données de l'étudiant
    function loadStudentData() {
        loadCourses();
        loadGrades();
        initCalendar();
    }
    
    // Initialiser le calendrier au chargement
    initCalendar();
});

