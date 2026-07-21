# Student Portal React Application

## Overview

This HandsOn_05 project is a React-based Student Portal for browsing and managing course registrations. It loads placeholder API data, maps that data onto a local course catalog, and falls back to local courses if the request fails. The application demonstrates component composition, hooks, controlled search input, and client-side enrollment state.

## Preview

![Student Portal course catalogue](<Output/Screenshot 2026-07-08 at 10.28.49 AM.png>)

![Student Portal registration view](<Output/Screenshot 2026-07-08 at 10.29.07 AM.png>)

## Features

- Course catalog loaded through a browser fetch request
- Local fallback catalog when the request fails
- Search by course name or code
- Course enrollment with duplicate prevention
- Registration list with course removal
- Loading, empty, and request-error states

## Tech Stack

- React 18
- React DOM
- Vite
- JavaScript
- JSONPlaceholder API

## Project Structure

```text
Handson_05/
├── src/
│   ├── components/      # Header, footer, profile, and course-card components
│   ├── App.jsx          # Application state and page composition
│   ├── coursesData.js   # Fallback course catalog
│   └── main.jsx         # React entry point
├── index.html
└── package.json
```

## Installation

```bash
git clone <repository-url>
cd Module2_FrontendDev/Rohith.V/Handson_05
npm install
npm run dev
```

## Usage

Open the Vite development URL printed in the terminal. Search the course catalog, select a course to enroll, and use **Drop** in the registration box to remove it. If the API request is unavailable, the application shows the local fallback catalog.

## Configuration

No environment variables are required. An internet connection is required to load the initial JSONPlaceholder response; the local fallback works without it.

## API Endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `https://jsonplaceholder.typicode.com/posts` | Supplies placeholder records used to initialize the course list. |

## Future Improvements

- Move inline styles into reusable style modules
- Persist enrollment selections between page refreshes
- Replace placeholder API data with a course service

## Contributing

Create a branch, make a focused change, run the application locally, and open a pull request with a clear summary.

## License

[Add license information]
