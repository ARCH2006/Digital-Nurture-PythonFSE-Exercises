import { courses } from './data.js';


const coursesGrid = document.querySelector('.courses-grid');
const totalCreditsDisplay = document.querySelector('#total-credits');
const searchInput = document.querySelector('#search-courses');
const sortButton = document.querySelector('#sort-credits');


 
const renderPortalDashboard = (courseList) => {
    coursesGrid.innerHTML = '';

    courseList.forEach((course) => {
        const { name, code, credits, grade } = course;

        const cardElement = document.createElement('article');
        cardElement.className = 'course-card';
        
        // Serialize identifying state metadata directly into safe data attributes
        cardElement.setAttribute('data-name', name);
        cardElement.setAttribute('data-grade', grade);

        // Populate internal HTML content structural templates
        cardElement.innerHTML = `
            <div class="card-header">
                <span class="course-code">${code}</span>
            </div>
            <h3>${name}</h3>
            <p class="course-meta">${credits} Credits assigned</p>
        `;

        // Safely map the memory component onto the active browser engine canvas 
        coursesGrid.appendChild(cardElement);
    });

    // 3. AGGREGATE SUMMARY CALCULATOR: Run mathematical reduce tracker pipeline
    const totalUnits = courseList.reduce((accumulator, item) => {
        return accumulator + item.credits;
    }, 0);

    // Update status bar tracking metrics directly
    if (totalCreditsDisplay) {
        totalCreditsDisplay.textContent = `Total Enrolled Credits: ${totalUnits} Units`;
    }
};


if (searchInput) {
    searchInput.addEventListener('input', (event) => {
        // Normalize typed incoming data terms to ignore uppercase scaling discrepancies
        const searchTerm = event.target.value.toLowerCase();

        // Check if data metrics include matching character strings
        const filteredCourses = courses.filter((course) => {
            return course.name.toLowerCase().includes(searchTerm);
        });

        renderPortalDashboard(filteredCourses);
    });
}


if (sortButton) {
    sortButton.addEventListener('click', () => {
        const sortedCourses = [...courses].sort((courseA, courseB) => {
            return courseB.credits - courseA.credits; // High-to-Low structural sort parameter
        });

        renderPortalDashboard(sortedCourses);
    });
}


if (coursesGrid) {
    coursesGrid.addEventListener('click', (event) => {
        // Hunt upwards along the event chain loop context to safely isolate matching card nodes
        const targetCardNode = event.target.closest('.course-card');

        if (!targetCardNode) return;

        const courseName = targetCardNode.getAttribute('data-name');
        const courseGrade = targetCardNode.getAttribute('data-grade');

        alert(`Course Selected:\n📖 Name: ${courseName}\n🎯 Grade Achieved: ${courseGrade}`);
    });
}


renderPortalDashboard(courses);
