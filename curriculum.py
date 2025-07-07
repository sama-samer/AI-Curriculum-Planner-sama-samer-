import networkx as nx

def build_curriculum_graph():
    graph = nx.DiGraph()

    courses = {
        'CS101': {'name': 'Intro to Programming', 'credits': 3, 'area': 'Core'},
        'CS102': {'name': 'Data Structures', 'credits': 3, 'area': 'Core'},
        'MATH101': {'name': 'Calculus I', 'credits': 4, 'area': 'Core'},
        'AI301': {'name': 'Foundations of AI', 'credits': 3, 'area': 'AI'},
        'AI401': {'name': 'Machine Learning', 'credits': 3, 'area': 'AI'},
        'SEC301': {'name': 'Intro to Cybersecurity', 'credits': 3, 'area': 'Security'},
        'SEC401': {'name': 'Network Security', 'credits': 3, 'area': 'Security'},
        'DS301': {'name': 'Intro to Data Science', 'credits': 3, 'area': 'Data Science'},
    }

    for course_id, metadata in courses.items():
        graph.add_node(course_id, **metadata)

    prereqs = [
        ('CS101', 'AI301'),
        ('CS101', 'SEC301'),
        ('CS101', 'DS301'),
        ('CS102', 'AI401'),
        ('AI301', 'AI401'),
        ('SEC301', 'SEC401'),
    ]

    for prereq, course in prereqs:
        graph.add_edge(prereq, course)

    if not nx.is_directed_acyclic_graph(graph):
        raise ValueError("Curriculum contains a cycle! Check prerequisites.")

    return graph
