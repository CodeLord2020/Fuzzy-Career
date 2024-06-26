from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


science_subjects = [
    'English', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Other'
]

commercial_subjects = [
    'English', 'Mathematics', 'Government', 'Commerce', 'Economics', 'Accounting'
]

arts_subjects = [
    'English', 'Literature', 'Law', 'Government', 'History', 'Other'
]

technology_subjects = [
    'English', 'Mathematics', 'Physics', 'Chemistry', 'Computer Studies', 'Data Processing'
]



science_careers = [
    "Biologist", "Chemist", "Physicist", "Geologist", "Marine Biologist",
    "Astronomer", "Microbiologist", "Meteorologist", "Environmental Scientist", "Data Scientist"
]

commercial_careers = [
    "Marketing Manager", "Sales Manager", "Accountant", "Financial Analyst", "Business Consultant",
    "Human Resources Manager", "Project Manager", "Supply Chain Manager", "Business Lawyer", "Real Estate Agent"
]

arts_careers = [
    "Visual Artist", "Musician", "Actor", "Writer", "Dancer",
    "Graphic Designer", "Fashion Designer", "Interior Designer", "Architect", "Filmmaker"
]

technology_careers = [
    "Software Engineer", "Computer Engineer", "Web Developer", "Data Analyst", "Cybersecurity Analyst",
    "Network Engineer", "Artificial Intelligence Engineer", "Robotics Engineer", "Biomedical Engineer", "Chemical Engineer"
]


def create_fuzzy_vars(subjects):
    fuzzy_vars = {}
    for subject in subjects:
        fuzzy_var = ctrl.Antecedent(np.arange(0, 101, 1), subject)
        fuzzy_var['Excellent'] = fuzz.gaussmf(fuzzy_var.universe, 85, 10)
        fuzzy_var['Good'] = fuzz.gaussmf(fuzzy_var.universe, 70, 10)
        fuzzy_var['Average'] = fuzz.gaussmf(fuzzy_var.universe, 55, 10)
        fuzzy_var['Poor'] = fuzz.gaussmf(fuzzy_var.universe, 30, 10)
        fuzzy_var['Very_Poor'] = fuzz.gaussmf(fuzzy_var.universe, 15, 10)
        fuzzy_vars[subject] = fuzzy_var
    return fuzzy_vars



science_fuzzy_vars = create_fuzzy_vars(science_subjects)

commercial_fuzzy_vars = create_fuzzy_vars(commercial_subjects)

arts_fuzzy_vars = create_fuzzy_vars(arts_subjects)

technology_fuzzy_vars = create_fuzzy_vars(technology_subjects)



career_outputs = {}
for career in science_careers + commercial_careers + arts_careers + technology_careers:
    career_outputs[career] = ctrl.Consequent(np.arange(0, 1.1, 0.1), career)
    career_outputs[career]['low'] = fuzz.gaussmf(career_outputs[career].universe, 0.2, 0.1)
    career_outputs[career]['medium'] = fuzz.gaussmf(career_outputs[career].universe, 0.5, 0.1)
    career_outputs[career]['high'] = fuzz.gaussmf(career_outputs[career].universe, 0.8, 0.1)



science_rules = []
commercial_rules = []
arts_rules = []
technology_rules = []

# Example rules for science careers
science_rules.append(ctrl.Rule(science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'], career_outputs['Chemist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'], career_outputs['Biologist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'], career_outputs['Physicist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['English']['Good'] & science_fuzzy_vars['Other']['Good'], career_outputs['Geologist']['medium']))

# Example rules for commercial careers
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Accounting']['Excellent'], career_outputs['Accountant']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Commerce']['Good'], career_outputs['Business Consultant']['medium']))

# Example rules for arts careers
arts_rules.append(ctrl.Rule(arts_fuzzy_vars['Literature']['Excellent'] & arts_fuzzy_vars['History']['Excellent'], career_outputs['Writer']['high']))
arts_rules.append(ctrl.Rule(arts_fuzzy_vars['English']['Good'] & arts_fuzzy_vars['Government']['Good'], career_outputs['Business Lawyer']['medium']))

# Example rules for technology careers
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Computer Studies']['Excellent'], career_outputs['Software Engineer']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['English']['Excellent'] & technology_fuzzy_vars['Chemistry']['Good'], career_outputs['Chemical Engineer']['high']))


control_systems = {
    'science': ctrl.ControlSystem(science_rules),
    'commercial': ctrl.ControlSystem(commercial_rules),
    'arts': ctrl.ControlSystem(arts_rules),
    'technology': ctrl.ControlSystem(technology_rules)
}

simulations = {field: ctrl.ControlSystemSimulation(control_system) for field, control_system in control_systems.items()}


def compute_recommendations(field, inputs):
    sim = simulations[field]
    
    for subject, value in inputs.items():
        sim.input[subject] = value
    
    print(sim.input)
    
    sim.compute()
    
    career_scores = {career: sim.output[career] for career in career_outputs if career in sim.output}
    sorted_careers = sorted(career_scores.items(), key=lambda item: item[1], reverse=True)
    
    return sorted_careers




fields = {
    'science': ['English Language', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Other (Agric, Geography, Further Math, Computer Studies)'],
    'commercial': ['English Language', 'Mathematics', 'Government', 'Commerce', 'Economics', 'Financial Accounting'],
    'arts': ['English Language', 'Literature in English', 'Law', 'Government', 'History', 'One other subject (Economics, Geography, Religious Studies, Nigerian Language)'],
    'technology': ['English Language', 'Mathematics', 'Physics', 'Chemistry', 'Computer Studies', 'Data Processing']
}

careers = {
    'science': ['Biologist', 'Chemist', 'Physicist', 'Geologist', 'Marine Biologist', 'Astronomer', 'Microbiologist', 'Meteorologist', 'Environmental Scientist', 'Data Scientist'],
    'commercial': ['Marketing Manager', 'Sales Manager', 'Accountant', 'Financial Analyst', 'Business Consultant', 'Human Resources Manager', 'Project Manager', 'Supply Chain Manager', 'Business Lawyer', 'Real Estate Agent'],
    'arts': ['Visual Artist', 'Musician', 'Actor', 'Writer', 'Dancer', 'Graphic Designer', 'Fashion Designer', 'Interior Designer', 'Architect', 'Filmmaker'],
    'technology': ['Software Engineer', 'Computer Engineer', 'Web Developer', 'Data Analyst', 'Cybersecurity Analyst', 'Network Engineer', 'Artificial Intelligence Engineer', 'Robotics Engineer', 'Biomedical Engineer', 'Chemical Engineer']
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_subjects', methods=['POST'])
def get_subjects():
    field = request.json.get('field')
    subjects = fields.get(field, [])
    return jsonify(subjects)

@app.route('/submit_scores', methods=['POST'])
def submit_scores():
    data = request.json
    field = data.get('field')
    scores = data.get('scores')
    recommendations = compute_recommendations(field, scores)
    
    return jsonify(recommendations)



if __name__ == '__main__':
    app.run(debug=True)
