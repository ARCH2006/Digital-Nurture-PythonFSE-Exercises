# Student Portal

## Overview

This HandsOn_06 project is a React single-page Student Portal for viewing a course catalog and managing registrations. It uses React Router for page navigation and Redux Toolkit for the shared enrollment state. Students can enroll from the catalog, view their registered courses on the profile page, and remove registrations.

## Preview

![Student Portal course catalogue](<Output/Screenshot 2026-07-10 at 12.43.54 PM.png>)

![Student Portal profile](<Output/Screenshot 2026-07-10 at 12.44.08 PM.png>)

## Features

- Home, catalog, profile, and dynamic course-detail routes
- Local course catalog with schedule and description data
- Redux-managed enrollment and removal actions
- Duplicate enrollment prevention in the reducer
- Profile page showing active registrations

## Tech Stack

- React 19
- React Router DOM
- Redux Toolkit and React Redux
- Vite
- ESLint

## Project Structure

```text
student-portal/
├── src/
│   ├── components/         # Page and shared UI components
│   ├── coursesData.js      # Course catalog data
│   ├── enrollmentSlice.js  # Enrollment reducer and actions
│   ├── store.js            # Redux store configuration
│   ├── App.jsx             # Route definitions and application shell
│   └── main.jsx            # Application entry point
├── public/                 # Static assets
└── package.json
```

## Installation

```bash
git clone <repository-url>
cd Module2_FrontendDev/Rohith.V/Handson_06/student-portal
npm install
npm run dev
```

## Usage

Open the Vite development URL shown in the terminal. Use **Catalog** to enroll in courses, then open **Profile** to review or drop registered courses. Course-detail routes are available at `/courses/:courseId`.

## Configuration

No environment variables or configuration files are required.

## Future Improvements

- Link each catalog card to its course-detail route
- Persist enrollment data between page refreshes
- Add a not-found route and route-level error handling
- Add automated tests for enrollment state and routes

## Contributing

Create a branch, make a focused change, run `npm run lint`, and verify the application locally before opening a pull request.

## License

[Add license information]
