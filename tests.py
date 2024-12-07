import unittest
from unittest.mock import patch
import io
from ELS import add_course, assign_grades, enroll_course, generate_certificate, leave_feedback, view_enrolled_courses, login_user

class TestELearningSystem(unittest.TestCase):

    def setUp(self):
        global users, courses, user_courses, grades, feedback
        # Initialize system data
        users = {"admin": "admin123", "student1": "password1"}
        courses = {"C001": "Python Programming", "C002": "Data Structures"}
        user_courses = {"student1": ["C001", "C002"]}
        grades = {"student1": {"C001": "A", "C002": "A"}}
        feedback = {"C001": [{"user": "student1", "feedback": "Amazing experience!"}]}

    # Test: Add Course
    def test_add_course_success(self):
        with patch('builtins.input', side_effect=["C003", "Machine Learning"]):
            add_course()
            self.assertIn("C003", courses)
            self.assertEqual(courses["C003"], "Machine Learning")

    # Test: Enroll in Course
    def test_enroll_course_success(self):
        with patch('builtins.input', side_effect=["C002"]):
            enroll_course("student1")
            self.assertIn("C002", user_courses["student1"])

    # Test: Assign Grades
    def test_assign_grades_success(self):
        with patch('builtins.input', side_effect=["student1", "C002", "A"]):
            assign_grades()
            self.assertEqual(grades["student1"]["C002"], "A")

    # Test: Generate Certificate
    def test_generate_certificate_success(self):
        with patch('builtins.input', side_effect=["C001"]):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_output:
                generate_certificate("student1")
                self.assertIn("successfully completed the course", fake_output.getvalue())

    # Test: Leave Feedback
    def test_leave_feedback_success(self):
        with patch('builtins.input', side_effect=["C001", "Very informative course!"]):
            leave_feedback("student1")
            self.assertIn("C001", feedback)
            self.assertEqual(feedback["C001"][-1]["feedback"], "Very informative course!")

    # Test: View Enrolled Courses
    def test_view_enrolled_courses(self):
        with patch('sys.stdout', new_callable=io.StringIO) as fake_output:
            view_enrolled_courses("student1")
            self.assertIn("Python Programming", fake_output.getvalue())
            self.assertIn("Data Structures", fake_output.getvalue())

    # Test: Admin Login
    def test_admin_login_success(self):
        with patch('builtins.input', side_effect=["admin"]):
            with patch('getpass.getpass', return_value="admin123"):
                self.assertEqual(login_user(), "admin")

if __name__ == "__main__":
    unittest.main()
