import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define the subject combinations for each field
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

# Define the careers for each field
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

# Function to create fuzzy variables for a given list of subjects
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

# Creating fuzzy variables for each field
science_fuzzy_vars = create_fuzzy_vars(science_subjects)
commercial_fuzzy_vars = create_fuzzy_vars(commercial_subjects)
arts_fuzzy_vars = create_fuzzy_vars(arts_subjects)
technology_fuzzy_vars = create_fuzzy_vars(technology_subjects)

# Output variables for career recommendations
career_outputs = {}
for career in science_careers + commercial_careers + arts_careers + technology_careers:
    career_outputs[career] = ctrl.Consequent(np.arange(0, 1.1, 0.1), career)
    career_outputs[career]['low'] = fuzz.gaussmf(career_outputs[career].universe, 0.2, 0.1)
    career_outputs[career]['medium'] = fuzz.gaussmf(career_outputs[career].universe, 0.5, 0.1)
    career_outputs[career]['high'] = fuzz.gaussmf(career_outputs[career].universe, 0.8, 0.1)

# Define fuzzy rules for each career based on subject grades
# Here we define some example rules. You'll need to expand these based on your actual requirements.

rules = []

# Example rules for science careers
rules.append(ctrl.Rule(science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'], career_outputs['Chemist']['high']))
rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'], career_outputs['Biologist']['high']))
rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'], career_outputs['Physicist']['high']))
rules.append(ctrl.Rule(science_fuzzy_vars['Other']['Good'] & science_fuzzy_vars['English']['Good'], career_outputs['Geologist']['medium']))

# Example rules for commercial careers
rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Accounting']['Excellent'], career_outputs['Accountant']['high']))
rules.append(ctrl.Rule(commercial_fuzzy_vars['Government']['Good'] & commercial_fuzzy_vars['Commerce']['Good'], career_outputs['Business Consultant']['medium']))

# Example rules for arts careers
rules.append(ctrl.Rule(arts_fuzzy_vars['Literature']['Excellent'] & arts_fuzzy_vars['History']['Excellent'], career_outputs['Writer']['high']))
rules.append(ctrl.Rule(arts_fuzzy_vars['Law']['Good'] & arts_fuzzy_vars['Government']['Good'], career_outputs['Business Lawyer']['medium']))

# Example rules for technology careers
rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Computer Studies']['Excellent'], career_outputs['Software Engineer']['high']))
rules.append(ctrl.Rule(technology_fuzzy_vars['Physics']['Excellent'] & technology_fuzzy_vars['Chemistry']['Good'], career_outputs['Chemical Engineer']['high']))

# Create control systems and simulations for each field
control_systems = {
    'science': ctrl.ControlSystem(rules),
    'commercial': ctrl.ControlSystem(rules),
    'arts': ctrl.ControlSystem(rules),
    'technology': ctrl.ControlSystem(rules)
}

simulations = {field: ctrl.ControlSystemSimulation(control_system) for field, control_system in control_systems.items()}

# Function to compute career recommendations based on user inputs
def compute_recommendations(field, inputs):
    sim = simulations[field]
    
    for subject, value in inputs.items():
        sim.input[subject] = value
    
    sim.compute()
    
    career_scores = {career: sim.output[career] for career in career_outputs if career in sim.output}
    sorted_careers = sorted(career_scores.items(), key=lambda item: item[1], reverse=True)
    
    return sorted_careers

# Function to plot membership functions

# def plot_membership_functions(fuzzy_vars):
#     for subject, var in fuzzy_vars.items():
#         plt.figure()
#         for label in var.terms:
#             plt.plot(var.universe, var[label].mf, label=label)
#         plt.title(f'Membership Functions for {subject}')
#         plt.xlabel('Score')
#         plt.ylabel('Membership')
#         plt.legend()
#         plt.show()


# Function to plot career recommendation results

# def plot_career_recommendations(recommendations):
#     careers, scores = zip(*recommendations)
#     plt.figure()
#     plt.barh(careers, scores)
#     plt.xlabel('Score')
#     plt.title('Career Recommendations')
#     plt.show()

# Example usage
field = 'science'
user_inputs = {
    'English': 80,
    'Mathematics': 90,
    'Physics': 85,
    'Chemistry': 78,
    'Biology': 88,
    'Other': 70
}

# Plot membership functions
# plot_membership_functions(science_fuzzy_vars)

# Compute and plot career recommendations

recommendations = compute_recommendations(field, user_inputs)
print("Career Recommendations:")
for career, score in recommendations:
    print(f"{career}: {score:.2f}")

# Plot career recommendations
# plot_career_recommendations(recommendations)
