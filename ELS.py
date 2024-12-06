import getpass


# Data Storage
users = {"admin": "admin123"}  # username: password
courses = {"C001": "Python Programming", "C002": "Data Structures", "C003": "Machine Learning"}
user_courses = {}  # username: [course_ids]
assessments = {"C001": [("Q1", "What is Python?"), ("Q2", "What is PEP8?")]}  # course_id: [(question_id, question)]
messages = []
grades = {}
feedback = {}
course_progress = {}

# User Registration
def register_user():
    print("\n=== User Registration ===")
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please try again.")
        return
    password = getpass.getpass("Enter a password: ")
    users[username] = password
    print("User registered successfully!")

# User Login
def login_user():
    print("\n=== User Login ===")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if users.get(username) == password:
        print("Login successful!")
        return username
    else:
        print("Invalid credentials. Please try again.")
        return None

# Add a Course
def add_course():
    print("\n=== Add a Course ===")
    course_id = input("Enter a Course ID: ")
    course_name = input("Enter the Course Name: ")
    courses[course_id] = course_name
    print(f"Course '{course_name}' added successfully!")

# View Available Courses
def view_courses():
    print("\n=== Available Courses ===")
    if not courses:
        print("No courses available.")
    else:
        for course_id, course_name in courses.items():
            print(f"{course_id}: {course_name}")

# Enroll in a Course
def enroll_course(username):
    print("\n=== Enroll in a Course ===")
    view_courses()
    course_id = input("Enter the Course ID to enroll: ")
    if course_id not in courses:
        print("Invalid Course ID. Please try again.")
    else:
        user_courses.setdefault(username, []).append(course_id)
        print(f"Enrolled in '{courses[course_id]}' successfully!")

# View Enrolled Courses
def view_enrolled_courses(username):
    print("\n=== Your Enrolled Courses ===")
    enrolled = user_courses.get(username, [])
    if not enrolled:
        print("You have not enrolled in any courses.")
    else:
        for course_id in enrolled:
            print(f"{course_id}: {courses[course_id]}")

# Add an Assessment
def add_assessment():
    print("\n=== Add an Assessment ===")
    course_id = input("Enter the Course ID: ")
    if course_id not in courses:
        print("Invalid Course ID.")
        return
    assessment_id = input("Enter an Assessment ID: ")
    assessment_details = input("Enter Assessment Details: ")
    assessments.setdefault(course_id, []).append((assessment_id, assessment_details))
    print(f"Assessment added for course '{courses[course_id]}'.")

# View Assessments for a Course
def view_assessments(username):
    print("\n=== View Assessments ===")
    enrolled_courses = user_courses.get(username, [])
    if not enrolled_courses:
        print("You are not enrolled in any courses.")
        return
    for course_id in enrolled_courses:
        print(f"\nAssessments for '{courses[course_id]}':")
        for assess_id, assess_detail in assessments.get(course_id, []):
            print(f"  {assess_id}: {assess_detail}")

def take_quiz(username):
    print("\n=== Take a Quiz ===")
    enrolled_courses = user_courses.get(username, [])
    if not enrolled_courses:
        print("You are not enrolled in any courses.")
        return
    print("Your Enrolled Courses:")
    for course_id in enrolled_courses:
        print(f"{course_id}: {courses[course_id]}")
    course_id = input("Enter the Course ID to take the quiz: ")
    if course_id not in enrolled_courses:
        print("You are not enrolled in this course.")
        return
    if course_id not in assessments or not assessments[course_id]:
        print("No quizzes available for this course.")
        return
    score = 0
    for idx, (question_id, question) in enumerate(assessments[course_id]):
        print(f"Q{idx + 1}: {question}")
        answer = input("Enter your answer: ")
        # Simulate correct answer as 'A' for demonstration
        if answer.lower() == 'a':
            score += 1
    print(f"You scored {score}/{len(assessments[course_id])}!")

def view_profile(username):
    print("\n=== View Profile ===")
    print(f"Username: {username}")
    print(f"Enrolled Courses: {', '.join([courses[course_id] for course_id in user_courses.get(username, [])])}")
    
def update_password(username):
    print("\n=== Update Password ===")
    current_password = getpass.getpass("Enter your current password: ")
    if users.get(username) != current_password:
        print("Incorrect password. Please try again.")
        return
    new_password = getpass.getpass("Enter your new password: ")
    users[username] = new_password
    print("Password updated successfully!")

messages = []

def send_message(username):
    print("\n=== Send a Message ===")
    message = input("Enter your message: ")
    messages.append({"sender": username, "message": message})
    print("Message sent successfully!")

def view_messages():
    print("\n=== View Messages ===")
    if not messages:
        print("No messages available.")
        return
    for idx, msg in enumerate(messages):
        print(f"{idx + 1}. {msg['sender']} says: {msg['message']}")

grades = {}

def assign_grades():
    print("\n=== Assign Grades ===")
    username = input("Enter the student username: ")
    if username not in users or username == "admin":
        print("Invalid username.")
        return
    view_enrolled_courses(username)
    course_id = input("Enter the Course ID to assign a grade: ")
    if course_id not in user_courses.get(username, []):
        print("The student is not enrolled in this course.")
        return
    grade = input("Enter the grade: ")
    grades.setdefault(username, {})[course_id] = grade
    print(f"Grade '{grade}' assigned successfully for course '{courses[course_id]}'.")

def view_grades(username):
    print("\n=== View Grades ===")
    user_grades = grades.get(username, {})
    if not user_grades:
        print("No grades assigned yet.")
    else:
        for course_id, grade in user_grades.items():
            print(f"{courses[course_id]}: {grade}")

def generate_certificate(username):
    print("\n=== Generate Completion Certificate ===")
    enrolled_courses = user_courses.get(username, [])
    if not enrolled_courses:
        print("You are not enrolled in any courses.")
        return
    print("Your Enrolled Courses:")
    for course_id in enrolled_courses:
        print(f"{course_id}: {courses[course_id]}")
    course_id = input("Enter the Course ID for the certificate: ")
    if course_id not in enrolled_courses:
        print("You are not enrolled in this course.")
        return
    if username not in grades or course_id not in grades[username]:
        print("No grade assigned for this course yet. Complete the course to get a certificate.")
        return
    print(f"Certificate of Completion: {username} successfully completed the course '{courses[course_id]}' with grade '{grades[username][course_id]}'.")

feedback = {}

def leave_feedback(username):
    print("\n=== Leave Feedback ===")
    enrolled_courses = user_courses.get(username, [])
    if not enrolled_courses:
        print("You are not enrolled in any courses.")
        return
    print("Your Enrolled Courses:")
    for course_id in enrolled_courses:
        print(f"{course_id}: {courses[course_id]}")
    course_id = input("Enter the Course ID to leave feedback: ")
    if course_id not in enrolled_courses:
        print("You are not enrolled in this course.")
        return
    feedback_text = input("Enter your feedback: ")
    feedback.setdefault(course_id, []).append({"user": username, "feedback": feedback_text})
    print("Feedback submitted successfully!")

def view_feedback():
    print("\n=== View Feedback ===")
    if not feedback:
        print("No feedback available.")
        return
    for course_id, feedbacks in feedback.items():
        print(f"\nFeedback for '{courses[course_id]}':")
        for fb in feedbacks:
            print(f"{fb['user']} says: {fb['feedback']}")

course_progress = {}

def update_progress(username, course_id, progress):
    course_progress.setdefault(username, {})[course_id] = progress
    print(f"Progress for '{courses[course_id]}' updated to {progress}%.")

def view_progress(username):
    print("\n=== View Progress ===")
    user_progress = course_progress.get(username, {})
    if not user_progress:
        print("No progress data available.")
    else:
        for course_id, progress in user_progress.items():
            print(f"{courses[course_id]}: {progress}% completed")


# Menu for Admin
# Admin Functions
def admin_login():
    username = input("Enter admin username: ")
    password = getpass.getpass("Enter admin password: ")
    if users.get(username) == password and username == "admin":
        print("Admin login successful!")
        admin_menu()
    else:
        print("Invalid admin credentials.")

def admin_menu():
    while True:
        print("\n=== Admin Menu ===")
        print("1. Add Course")
        print("2. View Messages")
        print("3. Assign Grades")
        print("4. View Feedback")
        print("5. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_course()
        elif choice == "2":
            view_messages()
        elif choice == "3":
            assign_grades()
        elif choice == "4":
            view_feedback()
        elif choice == "5":
            print("Admin logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_course():
    print("\n=== Add Course ===")
    course_id = input("Enter new course ID: ")
    course_name = input("Enter new course name: ")
    if course_id in courses:
        print("Course ID already exists.")
        return
    courses[course_id] = course_name
    print(f"Course '{course_name}' added successfully!")

# Menu for Students
# Student Functions
def register_student():
    print("\n=== Register as Student ===")
    username = input("Enter username: ")
    if username in users:
        print("Username already exists. Please try another.")
        return
    password = getpass.getpass("Enter password: ")
    users[username] = password
    print("Student registration successful!")

def student_login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if users.get(username) == password and username != "admin":
        print("Student login successful!")
        student_menu(username)
    else:
        print("Invalid student credentials.")

def student_menu(username):
    while True:
        print("\n=== Student Menu ===")
        print("1. View Profile")
        print("2. Enroll in Course")
        print("3. Take Quiz")
        print("4. View Grades")
        print("5. Leave Feedback")
        print("6. View Progress")
        print("7. Generate Certificate")
        print("8. Send Message to Admin")
        print("9. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_profile(username)
        elif choice == "2":
            enroll_in_course(username)
        elif choice == "3":
            take_quiz(username)
        elif choice == "4":
            view_grades(username)
        elif choice == "5":
            leave_feedback(username)
        elif choice == "6":
            view_progress(username)
        elif choice == "7":
            generate_certificate(username)
        elif choice == "8":
            send_message(username)
        elif choice == "9":
            print("Student logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

def view_profile(username):
    print("\n=== View Profile ===")
    print(f"Username: {username}")
    print(f"Enrolled Courses: {', '.join([courses[course_id] for course_id in user_courses.get(username, [])])}")

def enroll_in_course(username):
    print("\n=== Enroll in Course ===")
    print("Available Courses:")
    for course_id, course_name in courses.items():
        print(f"{course_id}: {course_name}")
    course_id = input("Enter the Course ID to enroll: ")
    if course_id not in courses:
        print("Invalid Course ID.")
        return
    user_courses.setdefault(username, []).append(course_id)
    print(f"Successfully enrolled in '{courses[course_id]}'.")

def take_quiz(username):
    print("\n=== Take a Quiz ===")
    enrolled_courses = user_courses.get(username, [])
    if not enrolled_courses:
        print("You are not enrolled in any courses.")
        return
    print("Your Enrolled Courses:")
    for course_id in enrolled_courses:
        print(f"{course_id}: {courses[course_id]}")
    course_id = input("Enter the Course ID to take the quiz: ")
    if course_id not in enrolled_courses or course_id not in assessments:
        print("No quizzes available for this course.")
        return
    score = 0
    for idx, (question_id, question) in enumerate(assessments[course_id]):
        print(f"Q{idx + 1}: {question}")
        answer = input("Enter your answer: ")
        if answer.lower() == 'a':  # Simulated correct answer
            score += 1
    print(f"You scored {score}/{len(assessments[course_id])}!")

def send_message(username):
    print("\n=== Send a Message ===")
    message = input("Enter your message: ")
    messages.append({"sender": username, "message": message})
    print("Message sent successfully!")

def view_messages():
    print("\n=== View Messages ===")
    if not messages:
        print("No messages available.")
        return
    for idx, msg in enumerate(messages):
        print(f"{idx + 1}. {msg['sender']} says: {msg['message']}")

def assign_grades():
    print("\n=== Assign Grades ===")
    username = input("Enter the student username: ")
    if username not in users or username == "admin":
        print("Invalid username.")
        return
    print("Enrolled Courses:")
    for course_id in user_courses.get(username, []):
        print(f"{course_id}: {courses[course_id]}")
    course_id = input("Enter the Course ID to assign a grade: ")
    grade = input("Enter the grade: ")
    grades.setdefault(username, {})[course_id] = grade
    print("Grade assigned successfully!")

def view_grades(username):
    print("\n=== View Grades ===")
    user_grades = grades.get(username, {})
    if not user_grades:
        print("No grades available.")
        return
    for course_id, grade in user_grades.items():
        print(f"{courses[course_id]}: {grade}")

def leave_feedback(username):
    print("\n=== Leave Feedback ===")
    enrolled_courses = user_courses.get(username, [])
    if not enrolled_courses:
        print("You are not enrolled in any courses.")
        return
    print("Your Enrolled Courses:")
    for course_id in enrolled_courses:
        print(f"{course_id}: {courses[course_id]}")
    course_id = input("Enter the Course ID to leave feedback: ")
    feedback_text = input("Enter your feedback: ")
    feedback.setdefault(course_id, []).append({"user": username, "feedback": feedback_text})
    print("Feedback submitted successfully!")

def view_feedback():
    print("\n=== View Feedback ===")
    if not feedback:
        print("No feedback available.")
        return
    for course_id, feedbacks in feedback.items():
        print(f"\nFeedback for '{courses[course_id]}':")
        for fb in feedbacks:
            print(f"{fb['user']} says: {fb['feedback']}")

def view_progress(username):
    print("\n=== View Progress ===")
    user_progress = course_progress.get(username, {})
    if not user_progress:
        print("No progress data available.")
        return
    for course_id, progress in user_progress.items():
        print(f"{courses[course_id]}: {progress}% completed")

def generate_certificate(username):
    print("\n=== Generate Certificate ===")
    enrolled_courses = user_courses.get(username, [])
    if not enrolled_courses:
        print("You are not enrolled in any courses.")
        return
    print("Your Enrolled Courses:")
    for course_id in enrolled_courses:
        print(f"{course_id}: {courses[course_id]}")
    course_id = input("Enter the Course ID for the certificate: ")
    if username not in grades or course_id not in grades[username]:
        print("No grade assigned for this course yet. Complete the course to get a certificate.")
        return
    print(f"Certificate: {username} successfully completed '{courses[course_id]}' with grade '{grades[username][course_id]}'.")

def main():
    while True:
        print("\n=== E-Learning System ===")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Register as Student")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
         admin_login()
        elif choice == "2":
         student_login()
        elif choice == "3":
         register_student()
        elif choice == "4":
            print("Thank you for using the E-Learning System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Initialize the admin account
    users["admin"] = "admin123"
    main()
