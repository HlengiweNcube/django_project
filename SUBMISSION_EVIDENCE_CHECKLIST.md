# Submission Evidence Checklist (Unit 11-14)

Use this checklist to collect screenshot evidence in the correct order for submission.

## 1) Setup (before screenshots)

1. Open terminal in project root.
2. Run:

```bash
python manage.py test
```

3. Run:

```bash
coverage run manage.py test
coverage report
coverage html
```

4. Start development server:

```bash
python manage.py runserver
```

## 2) Create this screenshots folder

Create a folder named `submission_evidence/` in the project root.

## 3) Capture screenshots in this order

### A. Unit 11: Testing and Coverage

1. `01_tests_all_ok.png`
- Capture terminal showing:
  - `Ran 13 tests`
  - `OK`

2. `02_coverage_report.png`
- Capture terminal output of `coverage report` showing total percentage.

3. `03_coverage_html_index.png`
- Open `htmlcov/index.html` in browser and capture overview page.

### B. Unit 13: Password Reset Flow

4. `04_login_forgot_password_link.png`
- Login page with visible `Forgot Password?` link.

5. `05_password_reset_form.png`
- Password reset page with email input field.

6. `06_password_reset_done.png`
- Confirmation page after submitting email.

7. `07_password_reset_confirm.png`
- Reset confirmation page (`reset/<uidb64>/<token>/`) with new password fields.

8. `08_password_reset_complete.png`
- Final success page after password reset.

### C. Accessibility Evidence

9. `09_skip_to_content_and_nav_aria.png`
- Page showing:
  - Skip link (`Skip to main content`)
  - Navigation landmark in HTML inspector with `aria-label="Main navigation"`

10. `10_product_search_label_and_helper.png`
- Product list page showing:
  - Search label (`Search products`)
  - Helper text under search input.

### D. Deployment Evidence

11. `11_render_live_home.png`
- Live deployed site home/dashboard page on Render.

12. `12_render_live_feature_page.png`
- Any functional page on live site (products/imports/exports/inbox).

## 4) Optional but recommended evidence

13. `13_admin_roles_groups.png`
- Django admin screen showing groups (`Manager`, `Staff`).

14. `14_permissions_example.png`
- A restricted action that demonstrates permission control.

15. `15_js_live_filtering.png`
- Product list page while typing in search, showing rows filtering live.

16. `16_js_form_validation_or_confirm.png`
- Form validation message and/or delete confirmation dialog evidence.

## 5) Quick evidence index (paste into report)

- Unit 11 (Testing): `01_tests_all_ok.png`
- Unit 11 (Coverage): `02_coverage_report.png`, `03_coverage_html_index.png`
- Unit 13 (Password reset): `04` to `08`
- Accessibility: `09`, `10`
- Deployment: `11`, `12`

## 6) Final pre-submission check

- All screenshots are clear and readable.
- Terminal screenshots include command and result output.
- Password reset flow screenshots are in logical order.
- Evidence filenames match exactly.
- ZIP contains:
  - source code
  - README.md
  - requirements.txt
  - Procfile/runtime.txt/render.yaml
  - `submission_evidence/` folder

## 7) If password email was tested with console backend

Add this sentence to your report:

"Password reset functionality was implemented using Django auth views. During local development, email delivery was tested using Django's console backend; SMTP settings are configured via environment variables for deployment."
