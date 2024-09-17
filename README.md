
## Employee Management Application

### Project Overview

This is a web-based Employee Management Application built with Django. The application allows the CEO of a Company to manage employee data, including adding, updating, and deleting employee profiles. Each employee has a unique profile that includes essential information such as name, address, phone number, salary, designation, and a short description.

---

### Features

1. **Add Employees**: 
   - A form to add a new employee profile to the system.
   - Includes fields for name, address, phone number, salary, designation, and a short description.
   - Salary and Designation fields are non-editable once the profile is saved.

2. **Unique Employee Profile**:
   - Each employee has a unique profile to avoid duplicates.

3. **Update Employee Information**:
   - Allows updating employee details (name, address, phone number, and short description).
   - Salary and Designation fields cannot be edited after profile creation.

4. **Delete Employee**:
   - Admin can delete employee profiles from the system.

5. **Display All Employees**:
   - Homepage shows all employee profiles with name, designation, and short description.

6. **Navigation Bar**:
   - Links to Home, Add Employee, and Update/Delete Employee.

7. **Superuser Authentication**:
   - Superuser login: `admin` / `123`.
   - Django’s built-in authentication system is used to manage user logins and permissions.

---

### Project Setup

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd employee-management
   ```

6. **Run the server**:

   ```bash
   python manage.py runserver
   ```

   Open your browser and go to `http://127.0.0.1:8000/` to view the application.

---

### Key Files and Directories

- **`models.py`**: Defines the Employee model, with fields for name, address, phone number, salary, designation, and a short description.
- **`views.py`**: Contains the view functions to handle the application logic, such as adding, updating, and deleting employees.
- **`forms.py`**: Handles form rendering and validation for adding and updating employee profiles.
- **`urls.py`**: Maps URL patterns to the corresponding view functions.
- **`templates/`**: Contains all HTML templates for rendering the UI, such as forms, lists, and update pages.
- **`static/`**: Contains the CSS file (`style.css`) for styling the website.

---

### URL Routes

- **Home**: `/` — Displays all employee profiles.
- **Add Employee**: `/add/` — Form to add a new employee.
- **Manage Employees**: `/manage/` — List of employees with links to update or delete profiles.
- **Update Employee**: `/update/<id>/` — Edit an employee's profile (except for salary and designation).
- **Delete Employee**: `/delete/<id>/` — Delete an employee's profile.

---

### CSS Styling

The **CSS file** is located at `employees/static/employees/style.css` and provides basic styling for:

I applied css on this project. but it didn't properly works. and didn't find the main bugs.

---


## About The devloper :

```
Name : Sumon Roy
```
### educational qualification :
```
Computer Science and Engineering Discipline,
Khulna University.
Khulna.
```
### Social Link :

1. `Facebook` [Sumon Roy](https://www.facebook.com/sumonroysnr/)
2. `Linkedin` [Sumon Chandra Barman](https://www.linkedin.com/in/sumon-str/)
