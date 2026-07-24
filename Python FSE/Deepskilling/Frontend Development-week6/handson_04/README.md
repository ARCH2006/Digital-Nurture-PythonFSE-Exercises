# EduPortal Pro Dashboard

A responsive academic dashboard built for Handson_04. It combines local course data with practical asynchronous JavaScript patterns, including `fetch`, `async`/`await`, `Promise.all`, loading states, and recoverable notification errors.

## Preview

![EduPortal Pro dashboard](<Output_image/Screenshot 2026-07-16 at 4.45.42 PM.png>)

![EduPortal Pro notifications](<Output_image/Screenshot 2026-07-16 at 4.51.43 PM.png>)

## Features

- Live clock with a time-aware greeting
- Searchable course catalogue with total enrolled-credit calculation
- Concurrent profile requests using `Promise.all`
- Notification panel with an initial error state and retry flow
- Realistic local academic notifications after retry
- Responsive sidebar dashboard layout

## Tech stack

- HTML5
- CSS3
- JavaScript (ES modules)
- Fetch API and Promises
- Axios CDN integration for request-interceptor demonstration
- JSONPlaceholder user API for asynchronous request examples

## Project structure

```text
handson_04/
├── app.js       # Dashboard rendering, events, and async workflows
├── data.js      # Course and notification data
├── index.html   # Application markup
├── styles.css   # Dashboard styling
└── Output_image/# Project screenshots
```

## Run locally

From the `handson_04` folder, start a static server:

```bash
python3 -m http.server 5510
```

Then open [http://localhost:5510](http://localhost:5510).

## How it works

On startup, the dashboard loads the course catalogue and runs two profile requests concurrently. The notification panel intentionally begins with an error state so the retry behavior can be tested. Selecting **Retry Connection** loads the local academic updates; the filter box then searches the notification titles and messages.

## Learning outcomes

- Model loading, success, and failure states in a user interface.
- Use `Promise.all` to coordinate independent asynchronous tasks.
- Keep display data separate from rendering logic.
- Provide a clear, recoverable error experience instead of a blank or broken panel.

## Author

**Rohith V**  
Module 2 — Frontend Development | Handson_04
