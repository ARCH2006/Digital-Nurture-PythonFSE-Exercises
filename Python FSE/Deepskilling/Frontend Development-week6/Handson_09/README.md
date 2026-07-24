# Hands-On 9: Accessibility Audit & Feature Implementation

An accessible, interactive Student Portal built with semantic **HTML5**, responsive **CSS3**, and native **Vanilla JavaScript**. This project applies WCAG 2.1 AA-informed accessibility practices while adding lightweight course sorting, grade feedback, and single-page-style navigation.

---

## Accessibility result

Google Chrome DevTools Lighthouse reports a **100/100 Accessibility score** for the completed portal.

![Chrome Lighthouse Accessibility audit showing a score of 100 out of 100](![alt text](image.png))

### WCAG 2.1 AA-oriented implementation

- **Semantic page structure:** Uses `header`, `nav`, `main`, `section`, `article`, and `footer` landmarks.
- **Logical headings:** Content follows a clear `h1` → `h2` → `h3` hierarchy for efficient screen-reader navigation.
- **Programmatic labels:** The course search field and all profile inputs have explicit `label[for]` elements that match their input `id` values.
- **Keyboard access:** Native links, inputs, and buttons retain their standard keyboard behavior. High-visibility `:focus-visible` styles make focus easy to track.
- **Accessible interaction:** Course cards contain semantic `<button>` elements; status updates are announced with `role="status"` and `aria-live="polite"`.
- **Colour contrast:** Text, controls, and focus indicators use high-contrast colour combinations.
- **Image accessibility:** The portal does not use content images. Any image added in future must include a meaningful `alt` attribute, or `alt=""` if purely decorative.
- **Skip navigation:** A “Skip to main content” link lets keyboard users bypass repeated navigation.

---

## Vanilla JavaScript features

The application uses no frameworks, libraries, or external dependencies. This keeps the page fast, transparent, and easy to audit for accessibility.

### Course sorting

- The **Sort by credits** control reads the visible text of every rendered course card.
- JavaScript extracts numerical values such as `4 credits` with a regular expression.
- The first click sorts courses in ascending credit order; the next click reverses the order.
- The button state and live status announcement update after every sort.

### Course-specific grade feedback

- Each **View grade** button identifies its own parent course card.
- The course title and grade are displayed in a native browser alert containing a clear passing-marks summary.
- Because native buttons are used, click, Enter, and Space activation work without custom keyboard handlers.

### Simulated client-side routes

- Header navigation links are intercepted with `preventDefault()`.
- The app writes the selected fragment route to browser history, logs the simulated route change, and smoothly scrolls to the matching page section.
- This avoids unnecessary page navigation and prevents empty-route/404-style reload behaviour.

![Student Portal showing descending credit sort, grade action buttons, and a Lighthouse audit](<Screenshot 2026-07-15 at 9.16.01 AM.png>)

---

## Run locally

Opening the HTML file directly with `file://` can cause browser security restrictions. Use Python’s local HTTP server instead.

1. Open **Terminal** on macOS.

2. Move to the Hands-On 9 directory:

   ```bash
   cd /Users/rohith/Desktop/frontend_week_03/Module2_FrontendDev/Rohith.V/Handson_09
   ```

3. Start the local server on port `8080`:

   ```bash
   python3 -m http.server 8080
   ```

4. In Chrome, visit:

   ```text
   http://localhost:8080
   ```

5. Stop the server at any time with <kbd>Control</kbd> + <kbd>C</kbd> in Terminal.

---

## Project structure

```text
Handson_09/
├── index.html     # Semantic page structure and accessible controls
├── styles.css     # Responsive layout, contrast, and focus styles
├── data.js        # Course data
├── app.js         # Sorting, grade actions, navigation, and form behaviour
├── README.md      # Project documentation
├── Screenshot 2026-07-15 at 9.16.13 AM.png
└── Screenshot 2026-07-15 at 9.16.01 AM.png
```

---

## Verification checklist

- [x] Lighthouse Accessibility: **100/100**
- [x] Search and profile inputs have associated labels
- [x] Headings are sequential and semantic
- [x] Interactive controls are keyboard reachable
- [x] Visible keyboard focus is provided
- [x] Course sorting toggles between ascending and descending order
- [x] Grade feedback is specific to the selected course
