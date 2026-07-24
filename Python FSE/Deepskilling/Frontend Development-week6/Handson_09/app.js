/* Student Portal interactions: no libraries or network requests required. */
const coursesGrid = document.querySelector('.courses-grid');
const totalCreditsDisplay = document.querySelector('#total-credits');
const courseStatus = document.querySelector('#course-status');
const selectedCourse = document.querySelector('#selected-course');
const searchInput = document.querySelector('#search-courses');
const sortButton = document.querySelector('.sort-btn, #sort-credits');
const profileForm = document.querySelector('#profile-form');
const profileStatus = document.querySelector('#profile-status');
const menuToggle = document.querySelector('.menu-toggle');
const mainNavigation = document.querySelector('#main-navigation');
let isAscending = true;

function updateCourseSummary(courseList) {
  const totalCredits = courseList.reduce((total, course) => total + course.credits, 0);
  if (totalCreditsDisplay) totalCreditsDisplay.textContent = `Total enrolled credits: ${totalCredits}`;
  if (courseStatus) courseStatus.textContent = `${courseList.length} course${courseList.length === 1 ? '' : 's'} shown.`;
}

function createCourseCard(course) {
  const card = document.createElement('article');
  card.className = 'course-card';
  card.tabIndex = 0;
  card.dataset.grade = course.grade;
  card.innerHTML = `
    <p class="course-code">${course.code}</p>
    <h3>${course.name}</h3>
    <p>${course.credits} credits</p>
    <button type="button">View grade</button>
  `;
  return card;
}

function renderCourses(courseList) {
  if (!coursesGrid) return;
  coursesGrid.replaceChildren(...courseList.map(createCourseCard));
  updateCourseSummary(courseList);
}

function creditsFromCard(card) {
  const match = card.textContent.match(/(\d+)\s*credits?/i);
  return match ? Number(match[1]) : 0;
}

function showCourseGrade(card) {
  const courseName = card.querySelector('h3')?.textContent.trim() || 'Selected course';
  const grade = card.dataset.grade || 'Not available';
  const message = `${courseName}\n\nPassing marks matrix\nCurrent grade: ${grade}\nPassing mark: 40%\nStatus: Passed`;

  window.alert(message);
  if (selectedCourse) selectedCourse.textContent = `${courseName}: current grade ${grade}.`;
}

if (coursesGrid) {
  coursesGrid.addEventListener('click', (event) => {
    const card = event.target.closest('.course-card');
    if (card) showCourseGrade(card);
  });

  coursesGrid.addEventListener('keydown', (event) => {
    const card = event.target.closest('.course-card');
    if (event.key === 'Enter' && card) {
      event.preventDefault();
      showCourseGrade(card);
    }
  });
}

if (searchInput) {
  searchInput.addEventListener('input', () => {
    const query = searchInput.value.trim().toLowerCase();
    renderCourses(courses.filter((course) => course.name.toLowerCase().includes(query)));
  });
}

if (sortButton && coursesGrid) {
  sortButton.addEventListener('click', () => {
    const sortedCards = [...coursesGrid.querySelectorAll('.course-card')]
      .sort((first, second) => (creditsFromCard(first) - creditsFromCard(second)) * (isAscending ? 1 : -1));

    coursesGrid.replaceChildren(...sortedCards);
    sortButton.setAttribute('aria-pressed', String(isAscending));
    sortButton.textContent = isAscending ? 'Sort by credits: ascending' : 'Sort by credits: descending';
    if (courseStatus) courseStatus.textContent = `Courses sorted by credits in ${isAscending ? 'ascending' : 'descending'} order.`;
    isAscending = !isAscending;
  });
}

document.querySelectorAll('nav a[href^="#"]').forEach((link) => {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    const route = link.getAttribute('href');
    const destination = document.querySelector(route);
    if (!destination) return;

    console.info(`Student Portal route changed to ${route}`);
    try {
      window.history.pushState({}, '', route);
    } catch {
      window.location.hash = route;
    }
    document.querySelectorAll('nav a[aria-current="page"]').forEach((currentLink) => {
      currentLink.removeAttribute('aria-current');
    });
    link.setAttribute('aria-current', 'page');
    if (menuToggle?.getAttribute('aria-expanded') === 'true') menuToggle.click();
    destination.scrollIntoView({ behavior: 'smooth' });
  });
});

if (menuToggle && mainNavigation) {
  const mobileViewport = window.matchMedia('(max-width: 600px)');

  const updateMenuVisibility = () => {
    const isMobile = mobileViewport.matches;
    const isOpen = menuToggle.getAttribute('aria-expanded') === 'true';
    mainNavigation.hidden = isMobile && !isOpen;
  };

  menuToggle.addEventListener('click', () => {
    const isOpen = menuToggle.getAttribute('aria-expanded') === 'true';
    menuToggle.setAttribute('aria-expanded', String(!isOpen));
    updateMenuVisibility();
  });

  mobileViewport.addEventListener('change', () => {
    menuToggle.setAttribute('aria-expanded', 'false');
    updateMenuVisibility();
  });

  updateMenuVisibility();
}

if (profileForm) {
  profileForm.addEventListener('submit', (event) => {
    event.preventDefault();
    if (profileStatus) profileStatus.textContent = 'Profile saved successfully.';
  });
}

renderCourses(courses);
