# Complaint Management System

## **Overview**
The Complaint Management System is a Django-based web application that simplifies the complaint resolution process. It enables users to submit complaints, track their status, and communicate with administrators. The system emphasizes usability, security, and efficiency, making it ideal for organizations seeking structured complaint handling.

---

## **Features**
- **User Authentication**: Secure login and signup for authorized users.
- **Complaint Submission**: Intuitive form for users to lodge complaints.
- **Track Complaints**: Users can view real-time updates on complaint status.
- **Contact Support**: Dedicated section for users to get in touch for assistance.
- **Responsive Design**: Optimized for both desktop and mobile devices.

---

## **Tech Stack**
- **Frontend**: HTML, CSS, Bootstrap  
- **Backend**: Django (Python)  
- **Database**: SQLite (default), customizable for PostgreSQL or MySQL

---

## **Installation Instructions**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/complaint-management-system.git
   cd complaint-management-system
   ```
2. Create a virtual environment and activate it:
  ```bash
  python -m venv env
  source env/bin/activate   # On Windows: env\Scripts\activate
  ```
3. Install required dependencies:
  ```bash
  pip install -r requirements.txt
  ```
4. Apply migrations to set up the database:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
5. Run the development server:
  ```bash
  python manage.py runserver
  ```
6. Open your browser and navigate to http://127.0.0.1:8000

## **Usage**
1. User Registration: New users can sign up to create an account.
2. Submit a Complaint: Log in and fill out the form to lodge a complaint.
3. View Complaints: Track the progress and status of submitted complaints.
4. Contact Support: Use the contact form for additional inquiries.
