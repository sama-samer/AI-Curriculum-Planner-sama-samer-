import random
import numpy as np
from faker import Faker

def get_eligible_courses(graph, completed_courses_dict, failed_courses_set):
    completed_ids = set(completed_courses_dict.keys())
    eligible = []

    for course_id in set(graph.nodes()) - completed_ids:
        prereqs = set(graph.predecessors(course_id))
        if prereqs.issubset(completed_ids):
            eligible.append(course_id)

    # Add failed courses (retake policy)
    eligible.extend(list(failed_courses_set))
    return list(set(eligible))

def simulate_students(graph, num_students=100):
    faker = Faker()
    students_data = []
    all_interests = ['AI', 'Security', 'Data Science']

    for i in range(num_students):
        student = {
            'student_id': i,
            'name': faker.name(),
            'interests': random.sample(all_interests, k=random.randint(1, 2)),
            'completed_courses': {},
            'failed_courses': set(),
            'gpa': 0.0
        }

        num_terms = random.randint(1, 6)
        for _ in range(num_terms):
            eligible = get_eligible_courses(graph, student['completed_courses'], student['failed_courses'])
            if not eligible:
                break

            course_load = random.randint(3, 5)
            courses_to_take = random.sample(eligible, k=min(len(eligible), course_load))

            for course in courses_to_take:
                grade = round(max(0.0, min(4.0, np.random.normal(loc=3.0, scale=0.7))), 2)
                if grade >= 2.0:
                    student['completed_courses'][course] = grade
                    student['failed_courses'].discard(course)
                else:
                    student['failed_courses'].add(course)

        if student['completed_courses']:
            final_gpa = np.mean(list(student['completed_courses'].values()))
            student['gpa'] = round(final_gpa, 2)

        students_data.append(student)

    return students_data
