import unittest
from unittest.mock import patch
import io
from ELS import add_course, assign_grades, enroll_course, generate_certificate, leave_feedback, view_enrolled_courses

class TestELearningSystem(unittest.TestCase):

    def setUp(self):
        global users, courses, user_courses, grades, feedback
        # Initialize system data
        users = {"admin": "admin123", "student1": "password1"}
        courses = {"C001": "Python Programming", "C002": "Data Structures"}
        user_courses = {"student1": ["C001", "C002"]}
        grades = {"student1": {"C001": "A", "C002": "A"}}
        feedback = {"C001": [{"user": "student1", "feedback": "Amazing experience!"}]}

    def test_add_course_success(self):
        with patch('builtins.input', side_effect=["C003", "Machine Learning"]):
            add_course()
            self.assertIn("C003", courses)
            self.assertEqual(courses["C003"], "Machine Learning")

    def test_generate_certificate_success(self):
        grades["student1"]["C002"] = "A"  # Ensure grade is assigned
        with patch('builtins.input', side_effect=["C002"]):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_output:
                generate_certificate("student1")
                self.assertIn("successfully completed the course", fake_output.getvalue())

    def test_leave_feedback_success(self):
        with patch('builtins.input', side_effect=["C001", "Very informative course!"]):
            leave_feedback("student1")
            self.assertIn("C001", feedback)
            self.assertEqual(feedback["C001"][-1]["feedback"], "Very informative course!")

    def test_view_enrolled_courses(self):
        with patch('sys.stdout', new_callable=io.StringIO) as fake_output:
            view_enrolled_courses("student1")
            self.assertIn("Python Programming", fake_output.getvalue())
            self.assertIn("Data Structures", fake_output.getvalue())

if __name__ == "__main__":
    unittest.main()
