# Student Portal Course Catalog

## Overview

This HandsOn_03 project is a client-side Student Portal course catalog. It renders course cards from a JavaScript data module, calculates the total credits for the active list, and provides search, sorting, and selection feedback. The project demonstrates DOM updates and ES module usage without a frontend framework.

## Preview

![Student Portal Course Catalog](<output/Screenshot 2026-07-05 at 9.09.19 PM.png>)

## Features

- Dynamic course-card rendering from local data
- Course-name search
- Descending sort by credit value
- Total-credit calculation for the displayed courses
- Course selection alert with the course name and grade

## Tech Stack

- HTML5
- CSS3
- JavaScript (ES modules)
- `serve` for local static hosting

## Project Structure

```text
handson_03/
├── app.js       # Rendering, filtering, sorting, and event handling
├── data.js      # Course catalog data
├── index.html   # Application markup
├── styles.css   # Application styles
└── package.json # Development dependency definition
```

## Installation

```bash
git clone <repository-url>
cd Module2_FrontendDev/Rohith.V/handson_03
npm install
npx serve .
```

## Usage

Open the local URL printed by `serve`. Search by course name, select **Sort by Credits** to reorder the catalog, and click a course card to view its recorded grade.

## Configuration

No environment variables or configuration files are required.

## Future Improvements

- Remove the duplicate static catalog markup after dynamic rendering
- Add sorting direction controls
- Replace alert-based feedback with an in-page detail panel

## Contributing

Create a branch, make a focused change, and test search, sorting, and card selection before opening a pull request.

## License

ISC
