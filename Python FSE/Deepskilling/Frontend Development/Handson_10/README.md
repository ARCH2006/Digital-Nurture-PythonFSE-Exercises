# Handson 10 — Advanced API Integration & State Management

A focused React application demonstrating a centralized API service layer, Redux Toolkit async workflows, and resilient global error handling through a course catalogue.

## Preview

![Handson 10 course catalogue](<Output_image/Screenshot 2026-07-16 at 4.09.55 PM.png>)

## Why this project?

Handson 10 shows how to keep UI components small and predictable: data access lives in an API layer, asynchronous state lives in Redux, and components consume data through selectors.

## Features

- **Centralized API layer** — `apiClient` and `courseApi` keep data-access logic outside UI components.
- **Async Redux state** — `createAsyncThunk` models loading, success, and failure states for course requests.
- **Selectors** — components use selectors rather than coupling directly to the Redux state structure.
- **Mock course service** — the catalogue runs locally without requiring an external backend.
- **Global error boundary** — rendering errors are logged and replaced with a friendly recovery screen.

## Tech stack

- React 19
- Redux Toolkit and React Redux
- Vite
- JavaScript (ES Modules)

## Project structure

```text
src/
├── api/
│   ├── apiClient.js       # Centralized mock API client
│   └── courseApi.js       # Course-specific API functions
├── components/
│   └── ErrorBoundary.jsx  # Global render-error fallback
├── pages/
│   └── CoursesPage.jsx    # Redux-connected catalogue UI
├── store/
│   ├── courseSlice.js     # Thunk, reducers, and selectors
│   └── index.js           # Redux store configuration
├── App.jsx
└── main.jsx
```

## Getting started

### Prerequisites

- Node.js 18 or later
- npm

### Install and run

```bash
cd Module2_FrontendDev/Rohith.V/Handson_10
npm install
npm run dev
```

Open the local address printed by Vite, normally [http://localhost:5173](http://localhost:5173).

### Production build

```bash
npm run build
```

## How data flows

```text
CoursesPage → dispatch(fetchAllCourses)
            → courseSlice thunk → courseApi → apiClient
            → Redux state update → selectors → CoursesPage
```

The thunk handles each request lifecycle state:

- `pending` — show a loading state.
- `fulfilled` — store and display the returned courses.
- `rejected` — store and display a user-friendly error message.

## State-management perspective

| Framework | State approach | Trade-off |
| --- | --- | --- |
| React + Redux Toolkit | Slices, async thunks, and selectors provide predictable shared state. | Structured async flows with moderate setup. |
| Angular + NgRx | Actions, reducers, selectors, and effects separate pure state changes from side effects. | Highly scalable but more verbose. |
| Vue + Pinia | Reactive stores combine state, getters, and actions. | Minimal boilerplate and a gentle learning curve. |

## Error handling

Request failures are handled by the Redux thunk's rejected state. Rendering failures are handled by `ErrorBoundary`, which logs the error and displays a recovery UI instead of a blank screen.
