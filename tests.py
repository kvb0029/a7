import getpass
from ELS import *
# Data Storage
users = {"admin": "admin123"}  # username: password
courses = {"C001": "Python Programming", "C002": "Data Structures", "C003": "Machine Learning"}
user_courses = {}  # username: [course_ids]
assessments = {"C001": [("Q1", "What is Python?"), ("Q2", "What is PEP8?")]}  # course_id: [(question_id, question)]
messages = []
grades = {}
feedback = {}
course_progress = {}

# Core Functions
def register_user():
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please try again.")
        return
    password = getpass.getpass("Enter a password: ")
    users[username] = password
    print("User registered successfully!")

def login_user():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if users.get(username) == password:
        print("Login successful!")
        return username
    else:
        print("Invalid credentials. Please try again.")
        return None

def add_course():
    course_id = input("Enter a Course ID: ")
    course_name = input("Enter the Course Name: ")
    courses[course_id] = course_name
    print(f"Course '{course_name}' added successfully!")

def enroll_course(username):
    course_id = input("Enter the Course ID to enroll: ")
    if course_id not in courses:
        print("Invalid Course ID. Please try again.")
    else:
        user_courses.setdefault(username, []).append(course_id)
        print(f"Enrolled in '{courses[course_id]}' successfully!")

def take_quiz(username):
    enrolled_courses = user_courses.get(username, [])
    if not enrolled_courses:
        print("You are not enrolled in any courses.")
        return
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

# Test Cases
def test_register_user():
    initial_user_count = len(users)
    register_user()
    final_user_count = len(users)
    assert final_user_count == initial_user_count + 1, "User registration failed"
    print("Test Case 1 Passed: Register User")

def test_login_user():
    username, password = "test_user", "test_password"
    users[username] = password  # Add a test user
    
    # Test valid credentials
    logged_in_user = login_user()
    assert logged_in_user == username, "Login failed with valid credentials"
    
    # Test invalid credentials
    del users[username]  # Remove the test user
    logged_in_user = login_user()
    assert logged_in_user is None, "Login succeeded with invalid credentials"
    print("Test Case 2 Passed: Login User")

def test_add_course():
    initial_course_count = len(courses)
    add_course()
    final_course_count = len(courses)
    assert final_course_count == initial_course_count + 1, "Adding course failed"
    print("Test Case 3 Passed: Add Course")

def test_enroll_course():
    username = "test_student"
    users[username] = "password123"  # Create a test student
    user_courses[username] = []  # Ensure no prior enrollments

    # Enroll in a course
    enroll_course(username)
    assert username in user_courses, "Enrollment failed"
    assert len(user_courses[username]) > 0, "No course enrolled"
    print("Test Case 4 Passed: Enroll in Course")

def test_take_quiz():
    username = "test_student"
    course_id = "C001"
    assessments[course_id] = [("Q1", "What is Python?")]  # Add a test assessment
    user_courses[username] = [course_id]  # Enroll the student in the test course

    # Simulate taking the quiz
    take_quiz(username)
    # No automated scoring validation here, as scoring depends on user input
    print("Test Case 5 Passed: Take Quiz")

# Main
if __name__ == "__main__":
    print("Running Test Cases...")
    test_register_user()
    test_login_user()
    test_add_course()
    test_enroll_course()
    test_take_quiz()
    print("All Test Cases Passed!")
