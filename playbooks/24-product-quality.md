# 24 · Product Quality (What Users Actually Experience)

**Goal:** The product isn't only correct in code; it is **pleasant, clear, accessible, fast, and trustworthy** for the people who use it. This is often what separates a professional product from a working prototype.

## 1. User experience

- **Every screen has one main purpose** and one obvious next action.
- **Design all the states:** loading, empty, error, success, and partial data. Most rough-looking products forget the empty and error states.
- **Write errors in human terms:** what happened and what to do next. Never show a raw stack trace or error code alone.
- **Be consistent:** the same component, wording, and behavior for the same thing everywhere (a small design system or component library helps).
- **Test with real tasks:** walk through the main user journeys as a new user would, and fix every moment of confusion.

## 2. Accessibility

- Sufficient color contrast; never rely on color alone.
- Everything works with the keyboard, with visible focus.
- Images have alt text, and form fields have labels.
- Touch targets are large enough on mobile.
- Aim for WCAG 2.1 AA as the default target.

## 3. Language, RTL, and localization

- **Plan for multiple languages from the start** if there is any chance you'll need them: keep all UI text in translation files, never hard-coded.
- **Right-to-left (Arabic, Hebrew, Persian):** use logical CSS properties (`margin-inline-start`, not `margin-left`), mirror the layout and directional icons, and test with real RTL text, including mixed Arabic/English and numbers.
- Format dates, numbers, and currencies by locale.
- Choose fonts that render the target scripts well.

## 4. Performance (as users feel it)

- Fast first load (Core Web Vitals for the web; startup time for apps).
- Immediate feedback on every action (optimistic UI, spinners, or progress bars).
- Optimize images and lazy-load what isn't needed yet.
- Measure on a mid-range phone and a slow network, not only on a fast laptop.

## 5. Trust

- Clear privacy information; ask for permissions only when they're needed, and explain why.
- Destructive actions ask for confirmation, or can be undone.
- Never lose user input: autosave drafts, and keep form data after errors.

## Checklist for each user-facing feature

- [ ] All states designed: loading, empty, error, success.
- [ ] Keyboard and screen-reader basics work; contrast passes.
- [ ] No hard-coded UI text; RTL checked if relevant.
- [ ] Feels fast on a mid-range phone.
- [ ] Errors explain what to do next.
