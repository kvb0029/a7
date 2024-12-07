import getpass
from ELS import *
import unittest

class TestElearningSystem(unittest.TestCase):
    def test_register_user(self):
        initial_user_count = len(users)
        register_user()
        final_user_count = len(users)
        self.assertEqual(final_user_count, initial_user_count + 1, "User registration failed")
    
    def test_login_user(self):
        username, password = "test_user", "test_password"
        users[username] = password  # Add a test user
        
        # Test valid credentials
        self.assertEqual(login_user(), username, "Login failed with valid credentials")
        
        # Test invalid credentials
        del users[username]  # Remove the test user
        self.assertIsNone(login_user(), "Login succeeded with invalid credentials")
    
    def test_add_course(self):
        initial_course_count = len(courses)
        add_course()
        final_course_count = len(courses)
        self.assertEqual(final_course_count, initial_course_count + 1, "Adding course failed")
    
    def test_enroll_course(self):
        username = "test_student"
        users[username] = "password123"  # Create a test student
        user_courses[username] = []  # Ensure no prior enrollments

        # Enroll in a course
        enroll_course(username)
        self.assertIn(username, user_courses, "Enrollment failed")
        self.assertGreater(len(user_courses[username]), 0, "No course enrolled")
    
    def test_take_quiz(self):
        username = "test_student"
        course_id = "C001"
        assessments[course_id] = [("Q1", "What is Python?")]  # Add a test assessment
        user_courses[username] = [course_id]  # Enroll the student in the test course

        # Simulate taking the quiz
        take_quiz(username)
        # No automated scoring validation here, as scoring depends on user input

if __name__ == "__main__":
    unittest.main()
