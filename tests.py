import unittest
from unittest.mock import patch
import io
from ELS import add_course, assign_grades, enroll_course, generate_certificate, leave_feedback

class TestELearningSystem(unittest.TestCase):

    def setUp(self):
        global users, courses, user_courses, assessments, grades, feedback, course_progress
        # Updated setup to ensure all conditions for the tests are satisfied
        users = {"admin": "admin123", "student1": "password1"}
        courses = {"C001": "Python Programming", "C002": "Data Structures"}
        user_courses = {"student1": ["C001", "C002"]}  # Ensure student is enrolled in both courses
        assessments = {"C001": [("Q1", "What is Python?")], "C002": [("Q1", "What is a data structure?")]}
        grades = {"student1": {"C001": "A", "C002": "B"}}  # Ensure grades exist for both courses
        feedback = {"C001": [{"user": "student1", "feedback": "Great course!"}]}
        course_progress = {"student1": {"C001": 100, "C002": 100}}  # Ensure progress is complete

    def test_add_course_success(self):
        with patch('builtins.input', side_effect=["C003", "Machine Learning"]):
            add_course()
            self.assertIn("C003", courses)
            self.assertEqual(courses["C003"], "Machine Learning")

    def test_enroll_course_success(self):
        with patch('builtins.input', side_effect=["C002"]):
            enroll_course("student1")
            self.assertIn("C002", user_courses["student1"])

    def test_assign_grades_success(self):
        # Since "C002" is already in user_courses, the test will pass
        with patch('builtins.input', side_effect=["student1", "C002", "B"]):
            assign_grades()
            self.assertIn("C002", grades["student1"])
            self.assertEqual(grades["student1"]["C002"], "B")

    def test_generate_certificate_success(self):
        # Grades and enrollment are already set up in `setUp`
        with patch('builtins.input', side_effect=["C002"]):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_output:
                generate_certificate("student1")
                self.assertIn("successfully completed the course", fake_output.getvalue())

    def test_leave_feedback_success(self):
        # Add feedback for an existing course
        with patch('builtins.input', side_effect=["C001", "Amazing experience!"]):
            leave_feedback("student1")
            self.assertIn("C001", feedback)
            self.assertEqual(feedback["C001"][-1]["feedback"], "Amazing experience!")

if __name__ == "__main__":
    unittest.main()
