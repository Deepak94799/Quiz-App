# **Quiz App**

## **About the APP**

The **Quiz App** is a web-based application built using the Django framework. It allows users to:
- Answer multiple-choice questions (MCQs).
- Track their performance, including the total number of questions attempted, correct answers, and percentage scores.
- Get instant feedback after submitting answers, with options to take more questions or end the quiz.

This project is ideal for anyone looking to practice Python concepts through quizzes or as a learning tool to understand Django development.

---

## **How to Run the Project?**

### **Prerequisites**
To run this project, ensure the following are installed:
1. Python (3.8 or above)
2. pip (Python package manager)
3. A virtual environment tool (optional but recommended)

### **Steps to Run the Project**
1. **Clone the Repository**:
```bash
   git clone https://github.com/<your-username>/quiz-app.git
   cd quiz-app
```
2. **Set Up a Virtual Environment (Optional but Recommended)**:

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\\Scripts\\activate
```

3. **Install Dependencies: Install all required packages listed in requirements.txt**:
```bash
pip install -r requirements.txt
```

4. **Run Migrations: Apply database migrations to set up the SQLite database**:
```bash
python manage.py migrate
```

5. **Collect Static Files: Collect all static files into a single directory for serving**:
```bash
python manage.py collectstatic
```

6. **Create a Superuser: Create an admin account to access the Django admin panel**:
```bash
python manage.py createsuperuser

```

7. **Run the Development Server: Start the Django development server**:
```bash
python manage.py runserver

```

8. **Access the App: Open your browser and go to**:
```bash
http://127.0.0.1:8000/
Use http://127.0.0.1:8000/admin/ to manage questions via the admin panel.
```

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this project as long as the original license is included.
