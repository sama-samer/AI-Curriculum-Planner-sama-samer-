# AI-Curriculum-Planner-sama-samer-
project/
│
├── main.ipynb                 # Main notebook (run this)
├── curriculum.py              # Curriculum graph builder
├── students.py                # Student simulator
├── simulated_student_data.csv # Auto-generated dataset
├── curriculum_graph_visualization.png # Auto-generated graph visualization
├── README.md                  # This file
python:3.8+
pip install networkx matplotlib pandas faker numpy
pip install -r requirements.txt
ython -m venv advising_env
source advising_env/bin/activate  # or advising_env\Scripts\activate (Windows)
 How to Run the Project
Download or clone the repo into a local folder.

Make sure main.ipynb, curriculum.py, and students.py are in the same directory.

Open and run main.ipynb in Jupyter Notebook or VS Code.

The notebook will:

Build a graph-based curriculum

Simulate 100 students (with GPA, interests, grades)

Generate personalized course recommendations using:

🔹 Heuristic method (interest + eligibility + load)

🔹 Reinforcement Learning (Q-learning)

Outputs:

 simulated_student_data.csv → contains all student profiles

 curriculum_graph_visualization.png → visual map of courses

 Printed recommendations for first 10 students

 How the RL Works
States = Courses completed so far

Actions = Courses the student is eligible to take

Rewards = Simulated GPA + bonus for aligned interests

Goal = Learn which course sequences lead to higher GPA and graduation
