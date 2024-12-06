import unittest
from unittest.mock import patch
import io
from ELS import *


# Assuming the main script is named e_learning_system.py, and the functions are imported here.
# from e_learning_system import users, register_user, login_user, add_course, enroll_course, grades, assign_grades, ...

class TestELearningSystem(unittest.TestCase):

    def setUp(self):
        # Reset data before each test
        global users, courses, user_courses, assessments, grades, feedback, course_progress
        users = {"admin": "admin123"}
        courses = {"C001": "Python Programming", "C002": "Data Structures"}
        user_courses = {"student1": ["C001"]}
        assessments = {"C001": [("Q1", "What is Python?")]}
        grades = {"student1": {"C001": "A"}}
        feedback = {"C001": [{"user": "student1", "feedback": "Great course!"}]}
        course_progress = {"student1": {"C001": 100}}

    def test_admin_login_success(self):
        with patch('getpass.getpass', return_value='admin123'):
            with patch('builtins.input', side_effect=["admin"]):
                self.assertEqual(login_user(), "admin")

    def test_register_user_success(self):
        with patch('builtins.input', side_effect=["student2"]):
            with patch('getpass.getpass', return_value="password2"):
                register_user()
                self.assertIn("student2", users)
                self.assertEqual(users["student2"], "password2")

    def test_add_course_success(self):
        with patch('builtins.input', side_effect=["C003", "Machine Learning"]):
            add_course()
            self.assertIn("C003", courses)
            self.assertEqual(courses["C003"], "Machine Learning")

    def test_enroll_course_success(self):
        with patch('builtins.input', side_effect=["C002"]):
            enroll_course("student1")
            self.assertIn("C002", user_courses["student1"])

    def test_take_quiz_correct(self):
        with patch('builtins.input', side_effect=["C001", "a"]):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_output:
                take_quiz("student1")
                self.assertIn("You scored 1/1", fake_output.getvalue())

    def test_assign_grades_success(self):
        with patch('builtins.input', side_effect=["student1", "C002", "B"]):
            assign_grades()
            self.assertIn("C002", grades["student1"])
            self.assertEqual(grades["student1"]["C002"], "B")

    def test_generate_certificate_success(self):
        with patch('builtins.input', side_effect=["C001"]):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_output:
                generate_certificate("student1")
                self.assertIn("successfully completed the course", fake_output.getvalue())

    def test_leave_feedback_success(self):
        with patch('builtins.input', side_effect=["C001", "Amazing experience!"]):
            leave_feedback("student1")
            self.assertIn("C001", feedback)
            self.assertEqual(feedback["C001"][-1]["feedback"], "Amazing experience!")

    def test_view_feedback(self):
        with patch('sys.stdout', new_callable=io.StringIO) as fake_output:
            view_feedback()
            self.assertIn("Great course!", fake_output.getvalue())

if __name__ == "__main__":
    unittest.main()
