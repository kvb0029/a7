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
        user_courses = {}
        assessments = {"C001": [("Q1", "What is Python?")]}
        grades = {}
        feedback = {}
        course_progress = {}

    def test_admin_login_success(self):
        with patch('getpass.getpass', return_value='admin123'):
            with patch('builtins.input', side_effect=["admin"]):
                self.assertEqual(login_user(), "admin")

    def test_admin_login_failure(self):
        with patch('getpass.getpass', return_value='wrongpass'):
            with patch('builtins.input', side_effect=["admin"]):
                self.assertIsNone(login_user())

    def test_register_user_success(self):
        with patch('builtins.input', side_effect=["student1"]):
            with patch('getpass.getpass', return_value="password1"):
                register_user()
                self.assertIn("student1", users)
                self.assertEqual(users["student1"], "password1")

    def test_register_user_existing(self):
        with patch('builtins.input', side_effect=["admin"]):
            with patch('getpass.getpass', return_value="newpassword"):
                with patch('sys.stdout', new_callable=io.StringIO) as fake_output:
                    register_user()
                    self.assertIn("Username already exists", fake_output.getvalue())

    def test_add_course_success(self):
        with patch('builtins.input', side_effect=["C003", "Machine Learning"]):
            add_course()
            self.assertIn("C003", courses)
            self.assertEqual(courses["C003"], "Machine Learning")

    def test_enroll_course_success(self):
        users["student1"] = "password1"
        with patch('builtins.input', side_effect=["C001"]):
            enroll_course("student1")
            self.assertIn("C001", user_courses["student1"])

    def test_take_quiz_correct(self):
        users["student1"] = "password1"
        user_courses["student1"] = ["C001"]
        with patch('builtins.input', side_effect=["C001", "a"]):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_output:
                take_quiz("student1")
                self.assertIn("You scored 1/1", fake_output.getvalue())

    def test_assign_grades_success(self):
        users["student1"] = "password1"
        user_courses["student1"] = ["C001"]
        with patch('builtins.input', side_effect=["student1", "C001", "A"]):
            assign_grades()
            self.assertIn("C001", grades["student1"])
            self.assertEqual(grades["student1"]["C001"], "A")

    def test_generate_certificate_success(self):
        users["student1"] = "password1"
        user_courses["student1"] = ["C001"]
        grades["student1"] = {"C001": "A"}
        with patch('builtins.input', side_effect=["C001"]):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_output:
                generate_certificate("student1")
                self.assertIn("successfully completed the course", fake_output.getvalue())

    def test_leave_feedback_success(self):
        users["student1"] = "password1"
        user_courses["student1"] = ["C001"]
        with patch('builtins.input', side_effect=["C001", "Great course!"]):
            leave_feedback("student1")
            self.assertIn("C001", feedback)
            self.assertEqual(feedback["C001"][0]["feedback"], "Great course!")

    def test_view_feedback(self):
        feedback["C001"] = [{"user": "student1", "feedback": "Great course!"}]
        with patch('sys.stdout', new_callable=io.StringIO) as fake_output:
            view_feedback()
            self.assertIn("Great course!", fake_output.getvalue())


if __name__ == "__main__":
    unittest.main()
