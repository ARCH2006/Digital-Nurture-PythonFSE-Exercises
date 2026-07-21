# Student Portal Dashboard

A single-page student portal built as **Handson_08**. The application lets a student browse a course catalog, search for courses, manage enrolments, and review their academic summary from one responsive Vue interface.

## Preview

![Student portal home screen](<Output_images/Screenshot 2026-07-12 at 9.26.51 PM.png>)

![Student portal course catalogue](<Output_images/Screenshot 2026-07-12 at 9.28.12 PM.png>)

## Features

- Browse a five-course catalog with course codes, names, and credit values.
- Search courses by name or course code.
- Enrol in a course or drop an existing enrolment from the catalog.
- View the current number of enrolled courses in the application header.
- See total enrolled credits update immediately across the catalog and profile pages.
- Review the registered schedule and remove courses from the profile dashboard.
- Navigate between Home, Courses, Profile, and parameterized course-detail routes.

## Technology Stack

- **Vue 3** — component-based user interface
- **Vite** — development server and production build tooling
- **Vue Router** — client-side navigation and dynamic route parameters
- **Pinia** — shared enrolment state and derived total-credit calculation
- **JavaScript** and **CSS** — application logic and styling

## Project Structure

```text
src/
├── components/
│   ├── CourseCard.vue       # Reusable course display and enrolment actions
│   └── Header.vue           # Portal title, student badge, and enrolment count
├── router/
│   └── index.js             # Application routes and navigation hook
├── stores/
│   └── enrollment.js        # Pinia store for enrolled courses and credits
├── views/
│   ├── HomeView.vue         # Welcome page
│   ├── CoursesView.vue      # Searchable course catalog
│   ├── CourseDetailView.vue # Dynamic course-detail route
│   └── ProfileView.vue      # Academic summary and registered schedule
├── App.vue                  # Main application shell and navigation
└── main.js                  # Vue, Pinia, and router initialization
```

## Getting Started

### Prerequisites

- Node.js `22.18.0` or later (or `24.12.0` or later)
- npm

### Installation

```bash
git clone <repository-url>
cd student-portal-vue
npm install
```

### Run locally

```bash
npm run dev
```

Vite will print the local development URL in the terminal, typically `http://localhost:5173`.

### Production build

```bash
npm run build
```

To preview the generated production build locally:

```bash
npm run preview
```

## Application Routes

| Route | View | Purpose |
| --- | --- | --- |
| `/` | Home | Displays the portal welcome page. |
| `/courses` | Courses Catalog | Lists and filters available courses; supports enrolment changes. |
| `/courses/:id` | Course Detail | Displays detail content for a course identifier. |
| `/profile` | My Profile | Shows enrolled credits and the registered schedule. |

## State Management

The `enrollment` Pinia store is the single source of truth for the student’s selected courses. It exposes:

- `enrolledCourses` — reactive collection of selected courses.
- `totalCredits` — computed sum of credits across selected courses.
- `enroll(course)` — adds a course once, preventing duplicate enrolments.
- `unenroll(courseId)` — removes a selected course by its identifier.

Because the header, catalog, and profile use the same store, enrolment counts and credit totals remain synchronized while navigating between views.

## Notes

- Course data is currently defined in the client application for demonstration purposes.
- Enrolment data is maintained in memory and resets when the page is refreshed.
- This project was created as a frontend learning exercise and can be extended with an API, authentication, persistent storage, and validation rules.

## Author

**Rohith V**  
Module 2 — Frontend Development | Handson_08
