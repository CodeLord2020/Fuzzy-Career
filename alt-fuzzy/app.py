from flask import Flask, render_template, request, jsonify, redirect, url_for
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import io, json
import base64

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

with open('career_courses.json') as f:
    career_courses = json.load(f)



grade_to_score = {
    'A1': 90,
    'B2': 75,
    'B3': 70,
    'C4': 65,
    'C5': 60,
    'C6': 55,
    'D7': 49,
    'E8': 45,
    'F9': 39
}


fields = {

    'science': {
        'mandatory': ['English', 'Mathematics', 'Physics', 'Chemistry', 'Biology'],
        'optional': ['Computer_Studies', 'Agricultural_Science', 'Geography', 'Economics', 'Technical_Drawing', 'Catering/Crafts']
    },
    'commercial': {
        'mandatory': ['English', 'Mathematics', 'Economics', 'Commerce', 'Accounting'],
        'optional': ['Government', 'Biology', 'Civic_Education', 'Computer_Studies']
    },

    'arts': {
        'mandatory': ['English',  'Mathematics', 'Literature', 'Economics', 'Government'],
        'optional': ['Catering/Crafts', 'Civic_Education', 'History', 'Technical_Drawing', 'Law', 'Physical_Education', 'Computer_Studies']
    },

    'technology': {
        'mandatory': ['English', 'Mathematics', 'Physics', 'Chemistry', 'Computer_Studies'],
        'optional': ['Economics', 'Technical_Drawing', 'Biology', 'Data_Processing']
    }

}





careers = {
    'science': ["Biologist", "Chemist", "Chemical_Engineering", "Health", "Physicist", "Physical_Sciences", "Agriculture", "Geologist", "Computing", "Botanist", "Veterinarian",
                "Medicine", "Microbiologist", "Meteorologist", "Engineering", "Agricultural_Engineering", "Meteorologist", "Nutritionist", "Graphics", "Zoologist"],
    
    
    
    
    'commercial': ["Marketing_Manager", "Sales_Manager", "Entrepreneur", 'Education', 'Teacher', 'Business_Consultant', "Banker", "Financial_Analyst", "Politician",
                   "Human_Resources_Manager", "Project_Manager", "Supply_Chain_Manager", "Accountant", "Real_Estate_Agent"],
   
    
    
    
    'arts': ["Visual-Artist", "Musician", "Actor", "Writer", "Politician", "Journalist", "Teacher", "TV/Radio-Presenter",
    "Graphic-Designer", "Entrepreneur", "Fashion-Designer", "Interior-Designer", "Architect", "Filmmaker", "Animator"],
   
   
   
   
   
    'technology': ["Software_Engineer", "BigData_Engineer", "IT_Consultant", "IT_Project_Manager", "Network_Engineer",
                   "Architect", "Data_Scientist", "Data_Analyst", "Robotics", "Biomedical-Tech/Engr",]
}






def create_fuzzy_vars(subjects):
    fuzzy_vars = {}
    for subject in subjects['mandatory'] + subjects['optional']:
    # for subject in subjects:
        fuzzy_var = ctrl.Antecedent(np.arange(0, 101, 1), subject)
        fuzzy_var['Excellent'] = fuzz.gaussmf(fuzzy_var.universe, 85, 10)
        fuzzy_var['Good'] = fuzz.gaussmf(fuzzy_var.universe, 70, 10)
        fuzzy_var['Average'] = fuzz.gaussmf(fuzzy_var.universe, 55, 10)
        fuzzy_var['Poor'] = fuzz.gaussmf(fuzzy_var.universe, 30, 10)
        fuzzy_var['Very_Poor'] = fuzz.gaussmf(fuzzy_var.universe, 15, 10)
        fuzzy_vars[subject] = fuzzy_var
    return fuzzy_vars




science_fuzzy_vars = create_fuzzy_vars(fields['science'])
commercial_fuzzy_vars = create_fuzzy_vars(fields['commercial'])
arts_fuzzy_vars = create_fuzzy_vars(fields['arts'])
technology_fuzzy_vars = create_fuzzy_vars(fields['technology'])



career_outputs = {}
for career in careers['science'] + careers['commercial'] + careers['arts'] + careers['technology']:
    career_outputs[career] = ctrl.Consequent(np.arange(0, 1.1, 0.1), career)
    career_outputs[career]['low'] = fuzz.gaussmf(career_outputs[career].universe, 0.2, 0.1)
    career_outputs[career]['medium'] = fuzz.gaussmf(career_outputs[career].universe, 0.5, 0.1)
    career_outputs[career]['high'] = fuzz.gaussmf(career_outputs[career].universe, 0.8, 0.1)



science_rules = []
commercial_rules = []
arts_rules = []
technology_rules = []


# science_rules.append(ctrl.Rule(science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'], career_outputs['Chemist']['high']))
# science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'], career_outputs['Biologist']['high']))
# science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'], career_outputs['Physicist']['high']))
# science_rules.append(ctrl.Rule(science_fuzzy_vars['English']['Good'] & science_fuzzy_vars['Economics']['Good'], career_outputs['Geologist']['medium']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Accounting']['Excellent'], career_outputs['Accountant']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Commerce']['Good'], career_outputs['Business_Consultant']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Accounting']['Excellent'], career_outputs['Teacher']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Computer_Studies']['Good'], career_outputs['Business_Consultant']['medium']))

arts_rules.append(ctrl.Rule(arts_fuzzy_vars['Literature']['Excellent'] & arts_fuzzy_vars['History']['Excellent'], career_outputs['Writer']['high']))
arts_rules.append(ctrl.Rule(arts_fuzzy_vars['English']['Good'] & arts_fuzzy_vars['Government']['Good'], career_outputs['Business_Consultant']['medium']))

# technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Computer Studies']['Excellent'], career_outputs['Software_Engineer']['high']))
# technology_rules.append(ctrl.Rule(technology_fuzzy_vars['English']['Excellent'] & technology_fuzzy_vars['Chemistry']['Good'], career_outputs['Chemical-Engineer']['high']))


technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Technical_Drawing']['Excellent'] & technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Physics']['Excellent'], career_outputs['Architect']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Technical_Drawing']['Excellent'] & technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Excellent'] & technology_fuzzy_vars['Physics']['Good'], career_outputs['Architect']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Technical_Drawing']['Good'] & technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Excellent'] & technology_fuzzy_vars['Physics']['Good'], career_outputs['Architect']['medium']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Technical_Drawing']['Average'] | technology_fuzzy_vars['Mathematics']['Good'], career_outputs['Architect']['low']))

technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Data_Processing']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Excellent'], career_outputs['BigData_Engineer']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Economics']['Excellent'] & (technology_fuzzy_vars['Computer_Studies']['Excellent'] | technology_fuzzy_vars['English']['Excellent']), career_outputs['BigData_Engineer']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Data_Processing']['Good'] & technology_fuzzy_vars['Computer_Studies']['Excellent'] , career_outputs['BigData_Engineer']['medium']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Good'] & technology_fuzzy_vars['Data_Processing']['Excellent'] & (technology_fuzzy_vars['Computer_Studies']['Good'] | technology_fuzzy_vars['English']['Excellent']), career_outputs['BigData_Engineer']['medium']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Average'] | technology_fuzzy_vars['Computer_Studies']['Average'], career_outputs['BigData_Engineer']['low']))



technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Biology']['Excellent'] & technology_fuzzy_vars['Chemistry']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Excellent'], career_outputs['Biomedical-Tech/Engr']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Biology']['Excellent'] & technology_fuzzy_vars['Chemistry']['Good'] & (technology_fuzzy_vars['Computer_Studies']['Excellent'] | technology_fuzzy_vars['Mathematics']['Excellent']), career_outputs['Biomedical-Tech/Engr']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Biology']['Good'] & technology_fuzzy_vars['Chemistry']['Excellent'] & (technology_fuzzy_vars['Computer_Studies']['Good'] | technology_fuzzy_vars['Mathematics']['Good']), career_outputs['Biomedical-Tech/Engr']['medium']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Biology']['Average'] | technology_fuzzy_vars['Chemistry']['Average'] | technology_fuzzy_vars['Computer_Studies']['Average'], career_outputs['Biomedical-Tech/Engr']['low']))



technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Data_Processing']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Excellent'], career_outputs['Data_Scientist']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Economics']['Excellent'] & (technology_fuzzy_vars['Computer_Studies']['Excellent'] | technology_fuzzy_vars['English']['Excellent']), career_outputs['Data_Analyst']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Data_Processing']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Good'] & technology_fuzzy_vars['English']['Excellent'], career_outputs['Data_Analyst']['high']))

technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Data_Processing']['Good'] & technology_fuzzy_vars['Computer_Studies']['Excellent'] , career_outputs['Data_Scientist']['medium']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Good'] & technology_fuzzy_vars['Data_Processing']['Excellent'] & (technology_fuzzy_vars['Computer_Studies']['Good'] | technology_fuzzy_vars['English']['Excellent']), career_outputs['Data_Analyst']['medium']))

technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Average'] | technology_fuzzy_vars['Computer_Studies']['Average'], career_outputs['Data_Scientist']['low']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Average'] | technology_fuzzy_vars['Computer_Studies']['Average'] | technology_fuzzy_vars['English']['Average'], career_outputs['Data_Analyst']['low']))


technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Good'] | technology_fuzzy_vars['Chemistry']['Average'] | technology_fuzzy_vars['Computer_Studies']['Average'], career_outputs['Biomedical-Tech/Engr']['low']))

#IT Consultant next
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Excellent'] & (technology_fuzzy_vars['Physics']['Excellent'] | technology_fuzzy_vars['Technical_Drawing']['Excellent']), career_outputs['IT_Consultant']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Good'] & technology_fuzzy_vars['Technical_Drawing']['Excellent'], career_outputs['IT_Consultant']['medium']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Good'] & technology_fuzzy_vars['Computer_Studies']['Excellent'] & (technology_fuzzy_vars['Physics']['Good'] | technology_fuzzy_vars['Technical_Drawing']['Good']), career_outputs['IT_Consultant']['medium']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Average'] | technology_fuzzy_vars['Computer_Studies']['Average'] | technology_fuzzy_vars['Physics']['Average'], career_outputs['IT_Consultant']['low']))



technology_rules.append(ctrl.Rule(technology_fuzzy_vars['English']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Excellent'] & (technology_fuzzy_vars['Mathematics']['Excellent'] | technology_fuzzy_vars['Technical_Drawing']['Excellent']), career_outputs['IT_Project_Manager']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['English']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Excellent'] & (technology_fuzzy_vars['Mathematics']['Excellent'] | technology_fuzzy_vars['Economics']['Excellent']), career_outputs['IT_Project_Manager']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Good'] & technology_fuzzy_vars['Computer_Studies']['Good'] & (technology_fuzzy_vars['Economics']['Good'] | technology_fuzzy_vars['English']['Good']), career_outputs['IT_Project_Manager']['medium']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Good'] & technology_fuzzy_vars['Computer_Studies']['Good'] & (technology_fuzzy_vars['English']['Good'] | technology_fuzzy_vars['Technical_Drawing']['Good']), career_outputs['IT_Project_Manager']['medium']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Average'] | technology_fuzzy_vars['Computer_Studies']['Average'] | technology_fuzzy_vars['English']['Average'], career_outputs['IT_Project_Manager']['low']))


technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Excellent'] & technology_fuzzy_vars['Physics']['Excellent'] , career_outputs['Network_Engineer']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Good'] & (technology_fuzzy_vars['Physics']['Excellent'] | technology_fuzzy_vars['Technical_Drawing']['Excellent']), career_outputs['Network_Engineer']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Good'] & technology_fuzzy_vars['Computer_Studies']['Excellent'] & (technology_fuzzy_vars['Physics']['Good'] | technology_fuzzy_vars['Technical_Drawing']['Good']), career_outputs['Network_Engineer']['medium']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Average'] | technology_fuzzy_vars['Computer_Studies']['Average'] | technology_fuzzy_vars['Physics']['Average'], career_outputs['Network_Engineer']['low']))



technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Excellent'] & (technology_fuzzy_vars['Physics']['Excellent'] | technology_fuzzy_vars['Technical_Drawing']['Excellent']), career_outputs['Software_Engineer']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Excellent'] & (technology_fuzzy_vars['Physics']['Good'] | technology_fuzzy_vars['Technical_Drawing']['Good']), career_outputs['Software_Engineer']['medium']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Good'] & technology_fuzzy_vars['Computer_Studies']['Excellent'] & (technology_fuzzy_vars['Physics']['Excellent'] | technology_fuzzy_vars['Technical_Drawing']['Excellent']), career_outputs['Software_Engineer']['medium']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Average'] | technology_fuzzy_vars['Computer_Studies']['Average'] | technology_fuzzy_vars['Physics']['Average'], career_outputs['Software_Engineer']['low']))


technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Excellent'] & technology_fuzzy_vars['Physics']['Excellent'] & technology_fuzzy_vars['Technical_Drawing']['Excellent'], career_outputs['Robotics']['high']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Excellent'] & (technology_fuzzy_vars['Physics']['Excellent'] | technology_fuzzy_vars['Technical_Drawing']['Excellent']), career_outputs['Robotics']['medium']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Excellent'] & technology_fuzzy_vars['Computer_Studies']['Good'] & technology_fuzzy_vars['Physics']['Excellent'], career_outputs['Robotics']['medium']))
technology_rules.append(ctrl.Rule(technology_fuzzy_vars['Mathematics']['Good'] | technology_fuzzy_vars['Computer_Studies']['Average'] | technology_fuzzy_vars['Physics']['Good'], career_outputs['Robotics']['low']))





# & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good'])
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Agricultural_Science']['Excellent'], career_outputs['Agriculture']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Agricultural_Science']['Excellent'] & (science_fuzzy_vars['Physics']['Excellent'] | science_fuzzy_vars['Mathematics']['Excellent']), career_outputs['Agriculture']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Agricultural_Science']['Good'], career_outputs['Agriculture']['low']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Excellent'], career_outputs['Agricultural_Engineering']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Agricultural_Science']['Excellent'] & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']), career_outputs['Agricultural_Engineering']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Agricultural_Science']['Good'] | science_fuzzy_vars['Biology']['Average'] | science_fuzzy_vars['Chemistry']['Good'], career_outputs['Agricultural_Engineering']['low']))



science_rules.append(ctrl.Rule(science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'], career_outputs['Chemist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'], career_outputs['Biologist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'], career_outputs['Physicist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['English']['Good'] & science_fuzzy_vars['Economics']['Good'], career_outputs['Geologist']['medium']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Technical_Drawing']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Physics']['Good'], career_outputs['Architect']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Technical_Drawing']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Computer_Studies']['Excellent'], career_outputs['Architect']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Technical_Drawing']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Geography']['Good'], career_outputs['Architect']['high']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Technical_Drawing']['Good'] & science_fuzzy_vars['Mathematics']['Good'] & science_fuzzy_vars['Physics']['Average'], career_outputs['Architect']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Technical_Drawing']['Good'] & science_fuzzy_vars['Mathematics']['Good'] & science_fuzzy_vars['Computer_Studies']['Good'], career_outputs['Architect']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Technical_Drawing']['Good'] & science_fuzzy_vars['Mathematics']['Good'] & science_fuzzy_vars['Geography']['Average'], career_outputs['Architect']['medium']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Technical_Drawing']['Average'] & science_fuzzy_vars['Mathematics']['Average'] & science_fuzzy_vars['Physics']['Poor'], career_outputs['Architect']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Technical_Drawing']['Average'] & science_fuzzy_vars['Mathematics']['Average'] & science_fuzzy_vars['Computer_Studies']['Average'], career_outputs['Architect']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Technical_Drawing']['Average'] & science_fuzzy_vars['Mathematics']['Average'] & science_fuzzy_vars['Geography']['Poor'], career_outputs['Architect']['low']))




science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent']  & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']), career_outputs['Biologist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good']  & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']) & science_fuzzy_vars['Agricultural_Science']['Excellent'], career_outputs['Biologist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good']  & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']) & science_fuzzy_vars['Physics']['Good'], career_outputs['Biologist']['high']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Physics']['Average'], career_outputs['Biologist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Agricultural_Science']['Good'], career_outputs['Biologist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Physics']['Average'], career_outputs['Biologist']['medium']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Average'] & science_fuzzy_vars['Chemistry']['Average'], career_outputs['Biologist']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Average'] & science_fuzzy_vars['Chemistry']['Average'] & science_fuzzy_vars['Agricultural_Science']['Average'], career_outputs['Biologist']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Average'] & science_fuzzy_vars['Chemistry']['Average'] & science_fuzzy_vars['Geography']['Poor'], career_outputs['Biologist']['low']))




science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Good']  & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']), career_outputs['Botanist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Agricultural_Science']['Excellent'] & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']), career_outputs['Botanist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Excellent']  & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']), career_outputs['Botanist']['high']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Agricultural_Science']['Good'], career_outputs['Botanist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Good'], career_outputs['Botanist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Average'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Agricultural_Science']['Good'], career_outputs['Botanist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Agricultural_Science']['Good'], career_outputs['Botanist']['medium']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Average'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Average'], career_outputs['Botanist']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Average'] & science_fuzzy_vars['Chemistry']['Average'] & science_fuzzy_vars['Agricultural_Science']['Average'], career_outputs['Botanist']['low']))



science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'], career_outputs['Chemical_Engineering']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Mathematics']['Excellent'] & (science_fuzzy_vars['Agricultural_Science']['Good'] | science_fuzzy_vars['Physics']['Good']), career_outputs['Chemical_Engineering']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Mathematics']['Good'] | science_fuzzy_vars['Biology']['Good'] | science_fuzzy_vars['Chemistry']['Average'], career_outputs['Chemical_Engineering']['low']))





science_rules.append(ctrl.Rule(science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Catering/Crafts']['Excellent'], career_outputs['Nutritionist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Catering/Crafts']['Good'], career_outputs['Nutritionist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Catering/Crafts']['Excellent'], career_outputs['Nutritionist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Catering/Crafts']['Average'], career_outputs['Nutritionist']['low']))


science_rules.append(ctrl.Rule(science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Biology']['Excellent']  & (science_fuzzy_vars['English']['Excellent'] | science_fuzzy_vars['Mathematics']['Excellent']), career_outputs['Chemist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Good'] & science_fuzzy_vars['Biology']['Good'], career_outputs['Chemist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Good'] & science_fuzzy_vars['Biology']['Good'], career_outputs['Chemist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Mathematics']['Good'] & science_fuzzy_vars['Agricultural_Science']['Good'], career_outputs['Chemist']['medium']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Chemistry']['Average'] & science_fuzzy_vars['Mathematics']['Average'] & science_fuzzy_vars['Physics']['Poor'], career_outputs['Chemist']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Chemistry']['Average'] & science_fuzzy_vars['Mathematics']['Average'] & science_fuzzy_vars['Biology']['Poor'], career_outputs['Chemist']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Chemistry']['Average'] & science_fuzzy_vars['Mathematics']['Average'] & science_fuzzy_vars['Computer_Studies']['Average'], career_outputs['Chemist']['low']))



science_rules.append(ctrl.Rule(science_fuzzy_vars['Computer_Studies']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Physics']['Good'], career_outputs['Computing']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Computer_Studies']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'], career_outputs['Computing']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Computer_Studies']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Biology']['Good'], career_outputs['Computing']['high']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Computer_Studies']['Good'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Physics']['Excellent'], career_outputs['Computing']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Computer_Studies']['Good'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'], career_outputs['Computing']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Computer_Studies']['Good'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Technical_Drawing']['Excellent'], career_outputs['Computing']['medium']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Computer_Studies']['Average'] | science_fuzzy_vars['Mathematics']['Average'], career_outputs['Computing']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Computer_Studies']['Average'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'], career_outputs['Computing']['low']))





science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'], career_outputs['Engineering']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Technical_Drawing']['Excellent'], career_outputs['Engineering']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Computer_Studies']['Excellent'], career_outputs['Engineering']['medium']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Good'] & science_fuzzy_vars['Chemistry']['Good'], career_outputs['Engineering']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Good'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Technical_Drawing']['Excellent'], career_outputs['Engineering']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Good'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Computer_Studies']['Excellent'], career_outputs['Engineering']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Average'] & science_fuzzy_vars['Mathematics']['Average'] & science_fuzzy_vars['Chemistry']['Poor'], career_outputs['Engineering']['low']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Average'] | science_fuzzy_vars['Mathematics']['Average'] | science_fuzzy_vars['Technical_Drawing']['Poor'], career_outputs['Engineering']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Average'] & science_fuzzy_vars['Mathematics']['Average'] & science_fuzzy_vars['Chemistry']['Poor'], career_outputs['Engineering']['low']))




science_rules.append(ctrl.Rule(science_fuzzy_vars['Geography']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Physics']['Good']  & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']), career_outputs['Geologist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Geography']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Biology']['Good']  & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']), career_outputs['Geologist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Geography']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Excellent']  & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']), career_outputs['Geologist']['high']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Geography']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Physics']['Average'], career_outputs['Geologist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Geography']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Biology']['Average'], career_outputs['Geologist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Geography']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Agricultural_Science']['Average'], career_outputs['Geologist']['medium']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Geography']['Average'] & science_fuzzy_vars['Chemistry']['Average'] & science_fuzzy_vars['Physics']['Poor'], career_outputs['Geologist']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Geography']['Average'] & science_fuzzy_vars['Chemistry']['Average'] & science_fuzzy_vars['Biology']['Poor'], career_outputs['Geologist']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Geography']['Average'] & science_fuzzy_vars['Chemistry']['Average'] & science_fuzzy_vars['Agricultural_Science']['Average'], career_outputs['Geologist']['low']))



science_rules.append(ctrl.Rule(science_fuzzy_vars['Technical_Drawing']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Physics']['Excellent'], career_outputs['Graphics']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Computer_Studies']['Excellent'], career_outputs['Graphics']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Technical_Drawing']['Good'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Physics']['Excellent'], career_outputs['Graphics']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Technical_Drawing']['Average'] | science_fuzzy_vars['Mathematics']['Average'], career_outputs['Graphics']['low']))



science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']), career_outputs['Health']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Agricultural_Science']['Excellent'], career_outputs['Health']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & (science_fuzzy_vars['Agricultural_Science']['Good'] | science_fuzzy_vars['English']['Good']), career_outputs['Health']['high']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Physics']['Excellent'], career_outputs['Health']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Good'], career_outputs['Health']['medium']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Average'] | science_fuzzy_vars['Chemistry']['Average'], career_outputs['Health']['low']))



science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['English']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'], career_outputs['Medicine']['high']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Physics']['Excellent'] & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']), career_outputs['Medicine']['medium']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] | science_fuzzy_vars['Chemistry']['Good'] | science_fuzzy_vars['Physics']['Good'] | science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good'], career_outputs['Medicine']['low']))





science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Geography']['Excellent'], career_outputs['Meteorologist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'], career_outputs['Meteorologist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Geography']['Good'] & science_fuzzy_vars['Chemistry']['Good'], career_outputs['Meteorologist']['high']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Good'] & science_fuzzy_vars['Mathematics']['Good'] & science_fuzzy_vars['Geography']['Average'], career_outputs['Meteorologist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Good'] & science_fuzzy_vars['Mathematics']['Good'] & science_fuzzy_vars['Computer_Studies']['Good'], career_outputs['Meteorologist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Good'] & science_fuzzy_vars['Mathematics']['Good'] & science_fuzzy_vars['Agricultural_Science']['Average'], career_outputs['Meteorologist']['medium']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Average'] & science_fuzzy_vars['Mathematics']['Average'] & science_fuzzy_vars['Geography']['Poor'], career_outputs['Meteorologist']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Average'] & science_fuzzy_vars['Mathematics']['Average'] & science_fuzzy_vars['Computer_Studies']['Average'], career_outputs['Meteorologist']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Average'] & science_fuzzy_vars['Mathematics']['Average'] & science_fuzzy_vars['Agricultural_Science']['Poor'], career_outputs['Meteorologist']['low']))



science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent']  & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']), career_outputs['Microbiologist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Excellent'] & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']), career_outputs['Microbiologist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Good'] & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']), career_outputs['Microbiologist']['high']))


science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Good'] & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']),  career_outputs['Microbiologist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Agricultural_Science']['Excellent']& (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']),  career_outputs['Microbiologist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Good'],  career_outputs['Microbiologist']['medium']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Average'] | science_fuzzy_vars['Chemistry']['Average'],  career_outputs['Microbiologist']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Average'],  career_outputs['Microbiologist']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Average'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Geography']['Poor'],  career_outputs['Microbiologist']['low']))


science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Good'] & science_fuzzy_vars['Mathematics']['Excellent'] & (science_fuzzy_vars['Geography']['Excellent'] | science_fuzzy_vars['Technical_Drawing']['Excellent']), career_outputs['Physical_Sciences']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & (science_fuzzy_vars['Computer_Studies']['Excellent'] | science_fuzzy_vars['Chemistry']['Excellent']), career_outputs['Physical_Sciences']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Good'] & science_fuzzy_vars['Mathematics']['Good'] & (science_fuzzy_vars['Technical_Drawing']['Excellent'] | science_fuzzy_vars['Chemistry']['Excellent']), career_outputs['Physical_Sciences']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Average'] | science_fuzzy_vars['Mathematics']['Average'], career_outputs['Physical_Sciences']['low']))


science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & (science_fuzzy_vars['English']['Excellent'] | science_fuzzy_vars['Technical_Drawing']['Excellent']), career_outputs['Physicist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Computer_Studies']['Excellent'], career_outputs['Physicist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Excellent'] & (science_fuzzy_vars['English']['Excellent'] | science_fuzzy_vars['Chemistry']['Excellent']), career_outputs['Physicist']['high']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Excellent'] & science_fuzzy_vars['Mathematics']['Good'] & science_fuzzy_vars['Chemistry']['Good'], career_outputs['Physicist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Good'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Computer_Studies']['Good'], career_outputs['Physicist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Good'] & science_fuzzy_vars['Mathematics']['Excellent'] & science_fuzzy_vars['Chemistry']['Average'], career_outputs['Physicist']['medium']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Average'] | science_fuzzy_vars['Mathematics']['Average'], career_outputs['Physicist']['low']))
# science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Good'] & science_fuzzy_vars['Mathematics']['Average'] & science_fuzzy_vars['Computer_Studies']['Average'], career_outputs['Physicist']['low']))
# science_rules.append(ctrl.Rule(science_fuzzy_vars['Physics']['Good'] & science_fuzzy_vars['Mathematics']['Average'] & science_fuzzy_vars['Geography']['Poor'], career_outputs['Physicist']['low']))





# science_rules.append(ctrl.Rule(science_fuzzy_vars['English']['Excellent'] & science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Good'], career_outputs['Teacher']['high']))
# science_rules.append(ctrl.Rule(science_fuzzy_vars['English']['Excellent'] & science_fuzzy_vars['Mathematics']['Good'] & science_fuzzy_vars['Physics']['Good'], career_outputs['Teacher']['high']))
# science_rules.append(ctrl.Rule(science_fuzzy_vars['English']['Excellent'] & science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'], career_outputs['Teacher']['high']))

# science_rules.append(ctrl.Rule(science_fuzzy_vars['English']['Good'] & science_fuzzy_vars['Biology']['Average'] & science_fuzzy_vars['Chemistry']['Average'], career_outputs['Teacher']['medium']))
# science_rules.append( ctrl.Rule(science_fuzzy_vars['English']['Good'] & science_fuzzy_vars['Mathematics']['Average'] & science_fuzzy_vars['Physics']['Average'], career_outputs['Teacher']['medium']))
# science_rules.append(ctrl.Rule(science_fuzzy_vars['English']['Good'] & science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Average'], career_outputs['Teacher']['medium']))

# science_rules.append(ctrl.Rule(science_fuzzy_vars['English']['Average'] & science_fuzzy_vars['Biology']['Poor'] & science_fuzzy_vars['Chemistry']['Poor'], career_outputs['Teacher']['low']))
# science_rules.append(ctrl.Rule(science_fuzzy_vars['English']['Average'] & science_fuzzy_va& (science_fuzzy_vars['English']['Excellent'] | science_fuzzy_vars['Mathematics']['Excellent'])rs['Mathematics']['Poor'] & science_fuzzy_vars['Physics']['Poor'], career_outputs['Teacher']['low']))
# science_rules.append(ctrl.Rule(science_fuzzy_vars['English']['Average'] & science_fuzzy_vars['Biology']['Average'] & science_fuzzy_vars['Chemistry']['Poor'], career_outputs['Teacher']['low']))





science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Physics']['Good'] & (science_fuzzy_vars['English']['Excellent'] | science_fuzzy_vars['Mathematics']['Excellent']), career_outputs['Veterinarian']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Good'] & (science_fuzzy_vars['English']['Excellent'] | science_fuzzy_vars['Mathematics']['Excellent']), career_outputs['Veterinarian']['high']))
# science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['']['Good'], career_outputs['Veterinarian']['high']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Physics']['Excellent'] & (science_fuzzy_vars['English']['Excellent'] | science_fuzzy_vars['Mathematics']['Excellent']), career_outputs['Veterinarian']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Agricultural_Science']['Excellent'] & (science_fuzzy_vars['English']['Excellent'] | science_fuzzy_vars['Mathematics']['Excellent']), career_outputs['Veterinarian']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Geography']['Excellent'] & (science_fuzzy_vars['English']['Excellent'] | science_fuzzy_vars['Mathematics']['Excellent']), career_outputs['Veterinarian']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Excellent'] & (science_fuzzy_vars['English']['Excellent'] | science_fuzzy_vars['Mathematics']['Excellent']), career_outputs['Veterinarian']['medium']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Good'], career_outputs['Veterinarian']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['English']['Average'] | science_fuzzy_vars['Mathematics']['Average'], career_outputs['Veterinarian']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Average'] | science_fuzzy_vars['Chemistry']['Average'], career_outputs['Veterinarian']['low']))






science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Agricultural_Science']['Excellent'] & (science_fuzzy_vars['English']['Good'] | science_fuzzy_vars['Mathematics']['Good']), career_outputs['Zoologist']['high']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Good'] & (science_fuzzy_vars['English']['Excellent'] | science_fuzzy_vars['Mathematics']['Good']), career_outputs['Zoologist']['high']))


science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Excellent'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Agricultural_Science']['Good'], career_outputs['Zoologist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Good'] & science_fuzzy_vars['Agricultural_Science']['Excellent'], career_outputs['Zoologist']['medium']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Excellent'] & science_fuzzy_vars['Agricultural_Science']['Good'], career_outputs['Zoologist']['medium']))

science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Average'] | science_fuzzy_vars['Agricultural_Science']['Average'], career_outputs['Zoologist']['low']))
science_rules.append(ctrl.Rule(science_fuzzy_vars['Biology']['Good'] & science_fuzzy_vars['Chemistry']['Poor'] & science_fuzzy_vars['Agricultural_Science']['Good'], career_outputs['Zoologist']['low']))


# science_rules.append(Arch_rule_1, Arch_rule_2, Arch_rule_3, Arch_rule_4, Arch_rule_5, Arch_rule_6, Arch_rule_7, Arch_rule_8, Arch_rule_9)
# science_rules.append(Bio_rule_1, Bio_rule_2, Bio_rule_3, Bio_rule_4, Bio_rule_5, Bio_rule_6, Bio_rule_7, Bio_rule_8, Bio_rule_9)
# science_rules.append(Bot_rule_1, Bot_rule_2, Bot_rule_3, Bot_rule_4, Bot_rule_5, Bot_rule_6, Bot_rule_7, Bot_rule_8, Bot_rule_9)
# science_rules.append(Chem_rule_1, Chem_rule_2, Chem_rule_3, Chem_rule_4, Chem_rule_5, Chem_rule_6, Chem_rule_7)
# science_rules.append(Comp_rule_1, Comp_rule_2, Comp_rule_3, Comp_rule_4, Comp_rule_5, Comp_rule_6, Comp_rule_7, Comp_rule_8)
# science_rules.append(Eng_rule_1, Eng_rule_2, Eng_rule_3, Eng_rule_4, Eng_rule_5, Eng_rule_6, Eng_rule_7, Eng_rule_8, Eng_rule_9)
# science_rules.append(Geo_rule_1, Geo_rule_2, Geo_rule_3, Geo_rule_4, Geo_rule_5, Geo_rule_6, Geo_rule_7, Geo_rule_8, Geo_rule_9)
# science_rules.append(Hea_rule_1, Hea_rule_2, Hea_rule_3, Hea_rule_4, Hea_rule_5, Hea_rule_6)
# science_rules.append(Med_rule_1, Med_rule_2, Med_rule_3)




commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Accounting']['Excellent'] & commercial_fuzzy_vars['Mathematics']['Excellent'] & commercial_fuzzy_vars['Economics']['Excellent'], career_outputs['Accountant']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Accounting']['Excellent'] & commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Economics']['Excellent'], career_outputs['Accountant']['high']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Accounting']['Good'] & commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Computer_Studies']['Excellent'], career_outputs['Accountant']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Accounting']['Good'] & commercial_fuzzy_vars['Mathematics']['Excellent'] & commercial_fuzzy_vars['Economics']['Excellent'], career_outputs['Accountant']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Accounting']['Excellent'] &  commercial_fuzzy_vars['Mathematics']['Good'] & (commercial_fuzzy_vars['Computer_Studies']['Excellent'] |  commercial_fuzzy_vars['Economics']['Excellent']) , career_outputs['Accountant']['medium']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Accounting']['Average'] & commercial_fuzzy_vars['Mathematics']['Average'], career_outputs['Accountant']['low']))




commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Mathematics']['Good'] &  commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Accounting']['Excellent'], career_outputs['Banker']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Computer_Studies']['Excellent'], career_outputs['Banker']['high']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Commerce']['Good'] &  (commercial_fuzzy_vars['Computer_Studies']['Excellent'] | commercial_fuzzy_vars['Accounting']['Excellent']), career_outputs['Banker']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Good'] & commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Commerce']['Excellent'] &  (commercial_fuzzy_vars['Computer_Studies']['Excellent'] | commercial_fuzzy_vars['Accounting']['Excellent']), career_outputs['Banker']['medium']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Average'] | commercial_fuzzy_vars['Mathematics']['Average'] | commercial_fuzzy_vars['Commerce']['Average'] | commercial_fuzzy_vars['Accounting']['Average'], career_outputs['Banker']['low']))




commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Government']['Excellent'], career_outputs['Business_Consultant']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Accounting']['Excellent'] & commercial_fuzzy_vars['English']['Good'], career_outputs['Business_Consultant']['high']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Commerce']['Good'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Government']['Excellent'], career_outputs['Business_Consultant']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Good'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Government']['Excellent'], career_outputs['Business_Consultant']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Good'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Accounting']['Excellent'], career_outputs['Business_Consultant']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Commerce']['Good'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Accounting']['Excellent'], career_outputs['Business_Consultant']['medium']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Average'] | commercial_fuzzy_vars['Commerce']['Average'] | commercial_fuzzy_vars['Accounting']['Average'] | commercial_fuzzy_vars['Government']['Average'] , career_outputs['Business_Consultant']['low']))






commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Biology']['Excellent'], career_outputs['Education']['high']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Biology']['Excellent'], career_outputs['Education']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Biology']['Good'], career_outputs['Education']['medium']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Average'] | commercial_fuzzy_vars['Biology']['Average'], career_outputs['Education']['low']))





commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Government']['Excellent'], career_outputs['Entrepreneur']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Accounting']['Excellent'] & commercial_fuzzy_vars['English']['Good'], career_outputs['Entrepreneur']['high']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Commerce']['Good'] & commercial_fuzzy_vars['Government']['Excellent'], career_outputs['Entrepreneur']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Good'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Government']['Excellent'], career_outputs['Entrepreneur']['medium']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Average'] | commercial_fuzzy_vars['Commerce']['Average'] | commercial_fuzzy_vars['English']['Average'] , career_outputs['Entrepreneur']['low']))




commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Mathematics']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Accounting']['Good'] & commercial_fuzzy_vars['Government']['Excellent'], career_outputs['Financial_Analyst']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Mathematics']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Accounting']['Excellent'] & commercial_fuzzy_vars['English']['Good'], career_outputs['Financial_Analyst']['high']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Mathematics']['Excellent'] & commercial_fuzzy_vars['Accounting']['Good'] & commercial_fuzzy_vars['Government']['Excellent'], career_outputs['Financial_Analyst']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Accounting']['Excellent'] & commercial_fuzzy_vars['Government']['Excellent'], career_outputs['Financial_Analyst']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Mathematics']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Accounting']['Good'], career_outputs['Financial_Analyst']['medium']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Mathematics']['Average'] | commercial_fuzzy_vars['Commerce']['Average'] | commercial_fuzzy_vars['Accounting']['Average'] , career_outputs['Financial_Analyst']['low']))



commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Civic_Education']['Excellent'], career_outputs['Human_Resources_Manager']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Civic_Education']['Excellent'] & commercial_fuzzy_vars['Government']['Excellent'], career_outputs['Human_Resources_Manager']['high']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Economics']['Good'] & commercial_fuzzy_vars['Civic_Education']['Good'], career_outputs['Human_Resources_Manager']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Civic_Education']['Good'] & commercial_fuzzy_vars['Government']['Good'], career_outputs['Human_Resources_Manager']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Economics']['Good'] & commercial_fuzzy_vars['Civic_Education']['Excellent'], career_outputs['Human_Resources_Manager']['medium']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Average'] | commercial_fuzzy_vars['Economics']['Average'] | commercial_fuzzy_vars['Civic_Education']['Average'] | commercial_fuzzy_vars['Government']['Average'], career_outputs['Human_Resources_Manager']['low']))




commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Government']['Excellent'], career_outputs['Marketing_Manager']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Civic_Education']['Excellent'], career_outputs['Marketing_Manager']['high']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['English']['Good']  & commercial_fuzzy_vars['Commerce']['Good'] & commercial_fuzzy_vars['Government']['Good'], career_outputs['Marketing_Manager']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Commerce']['Good'] & commercial_fuzzy_vars['Civic_Education']['Good'], career_outputs['Marketing_Manager']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Good'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Accounting']['Good'], career_outputs['Marketing_Manager']['medium']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Average'] | commercial_fuzzy_vars['Commerce']['Average'] & commercial_fuzzy_vars['English']['Average'], career_outputs['Marketing_Manager']['low']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Civic_Education']['Average'], career_outputs['Marketing_Manager']['low']))





commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Government']['Excellent'] & commercial_fuzzy_vars['Economics']['Excellent'], career_outputs['Politician']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Economics']['Excellent'], career_outputs['Politician']['high']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Government']['Good'] & commercial_fuzzy_vars['Economics']['Good'], career_outputs['Politician']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Commerce']['Good'] & commercial_fuzzy_vars['Economics']['Excellent'], career_outputs['Politician']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Government']['Excellent'] & commercial_fuzzy_vars['Economics']['Excellent'], career_outputs['Politician']['medium']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Average'] | commercial_fuzzy_vars['Government']['Average'] | commercial_fuzzy_vars['Economics']['Average'], career_outputs['Politician']['low']))



commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Civic_Education']['Excellent'] & commercial_fuzzy_vars['Economics']['Excellent'], career_outputs['Project_Manager']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Computer_Studies']['Excellent'] & commercial_fuzzy_vars['Civic_Education']['Excellent'], career_outputs['Project_Manager']['high']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Computer_Studies']['Good'] & commercial_fuzzy_vars['Economics']['Good'], career_outputs['Project_Manager']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Civic_Education']['Good'] & commercial_fuzzy_vars['Economics']['Good'], career_outputs['Project_Manager']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Civic_Education']['Good'], career_outputs['Project_Manager']['medium']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Average'] | commercial_fuzzy_vars['Civic_Education']['Average'] | commercial_fuzzy_vars['Economics']['Average'], career_outputs['Project_Manager']['low']))




commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Economics']['Excellent'], career_outputs['Real_Estate_Agent']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Government']['Excellent'], career_outputs['Real_Estate_Agent']['high']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Economics']['Good'], career_outputs['Real_Estate_Agent']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Government']['Excellent'], career_outputs['Real_Estate_Agent']['medium']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Average'] | commercial_fuzzy_vars['Commerce']['Average'] | commercial_fuzzy_vars['Economics']['Average'], career_outputs['Real_Estate_Agent']['low']))



commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Government']['Excellent'], career_outputs['Sales_Manager']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Civic_Education']['Excellent'], career_outputs['Sales_Manager']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Accounting']['Excellent'], career_outputs['Sales_Manager']['high']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Good'] & commercial_fuzzy_vars['Commerce']['Good'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Government']['Good'], career_outputs['Sales_Manager']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Good'] & commercial_fuzzy_vars['Commerce']['Good'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Civic_Education']['Good'], career_outputs['Sales_Manager']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Good'] & commercial_fuzzy_vars['Commerce']['Good'] & commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Accounting']['Good'], career_outputs['Sales_Manager']['medium']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Average'] & commercial_fuzzy_vars['Commerce']['Average'] & commercial_fuzzy_vars['Government']['Average'], career_outputs['Sales_Manager']['low']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Average'] & commercial_fuzzy_vars['Commerce']['Average'] & commercial_fuzzy_vars['Civic_Education']['Average'], career_outputs['Sales_Manager']['low']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['Economics']['Average'] & commercial_fuzzy_vars['Commerce']['Average'] & commercial_fuzzy_vars['Accounting']['Average'], career_outputs['Sales_Manager']['low']))



commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Economics']['Excellent'], career_outputs['Supply_Chain_Manager']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Accounting']['Excellent'], career_outputs['Supply_Chain_Manager']['high']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Commerce']['Excellent'] & commercial_fuzzy_vars['Economics']['Excellent'], career_outputs['Supply_Chain_Manager']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Excellent'] & commercial_fuzzy_vars['Accounting']['Good'] & commercial_fuzzy_vars['Economics']['Excellent'], career_outputs['Supply_Chain_Manager']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Accounting']['Excellent'] & commercial_fuzzy_vars['Commerce']['Excellent'], career_outputs['Supply_Chain_Manager']['medium']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Average'] | commercial_fuzzy_vars['Commerce']['Average'] | commercial_fuzzy_vars['Economics']['Average'], career_outputs['Supply_Chain_Manager']['low']))




commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Economics']['Excellent'], career_outputs['Teacher']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Civic_Education']['Excellent'], career_outputs['Teacher']['high']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Computer_Studies']['Excellent'], career_outputs['Teacher']['high']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Economics']['Good'], career_outputs['Teacher']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Civic_Education']['Good'], career_outputs['Teacher']['medium']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Good'] & commercial_fuzzy_vars['Mathematics']['Good'] & commercial_fuzzy_vars['Computer_Studies']['Good'], career_outputs['Teacher']['medium']))

commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Average'] & commercial_fuzzy_vars['Mathematics']['Average'] & commercial_fuzzy_vars['Economics']['Average'], career_outputs['Teacher']['low']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Average'] & commercial_fuzzy_vars['Mathematics']['Average'] & commercial_fuzzy_vars['Civic_Education']['Average'], career_outputs['Teacher']['low']))
commercial_rules.append(ctrl.Rule(commercial_fuzzy_vars['English']['Average'] & commercial_fuzzy_vars['Mathematics']['Average'] & commercial_fuzzy_vars['Computer_Studies']['Average'], career_outputs['Teacher']['low']))








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
    sim.compute()
    career_scores = {career: sim.output[career] for career in career_outputs if career in sim.output}
    sorted_careers = sorted(career_scores.items(), key=lambda item: item[1], reverse=True)
    return sorted_careers

@app.route('/started')
def index():
    return render_template('index.html')

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/get_subjects', methods=['POST'])
def get_subjects():
    field = request.json.get('field')
    subjects = fields.get(field, [])
    return jsonify(subjects)

@app.route('/submit_scores', methods=['POST'])
def submit_scores():
    data = request.json
    print(data)
    field = data.get('field')
    scores = data.get('scores', {})

    # Get the mandatory and optional subjects for the selected field
    # mandatory_subjects = fields[field]['mandatory']
    optional_subjects = fields[field]['optional']
    
    # Add default scores for missing optional subjects
    for subject in optional_subjects:
        if subject not in scores:
            scores[subject] = 'E8'
            
    numerical_scores = {subject: grade_to_score[grade] for subject, grade in scores.items()}
    print(numerical_scores)
    # Proceed with the fuzzy logic processing using the numerical scores
    all_recommendations = compute_recommendations(field, numerical_scores)
    recommendations = all_recommendations[:5]
    recommended_careers = []
    for career_name, score in recommendations:
        courses = career_courses.get(career_name, [])
        recommended_careers.append((career_name, score, courses))
    
    print(recommended_careers)
    response = jsonify(recommended_careers)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response






@app.route('/results')
def results(): 
    return render_template('resultpage.html')


if __name__ == '__main__':
    app.run(debug=True)



# science_subjects = ['English', 'Mathematics', 'Physics', 'career_outputs['Chemist']ry', 'Biology', 'Other']
# commercial_subjects = ['English', 'Mathematics', 'Government', 'Commerce', 'Economics', 'Accounting']
# arts_subjects = ['English', 'Literature', 'Law', 'Government', 'History', 'Other']
# technology_subjects = ['English', 'Mathematics', 'Physics', 'Chemistry', 'Computer Studies', 'Data Processing']


# fields = {
#     'science': ['English', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Other'],
#     'commercial': ['English', 'Mathematics', 'Government', 'Commerce', 'Economics', 'Accounting'],
#     'arts': ['English', 'Literature', 'Law', 'Government', 'History', 'Other'],
#     'technology': ['English', 'Mathematics', 'Physics', 'Chemistry', 'Computer Studies', 'Data Processing']
# }



# science_careers = ["Biologist", "Chemist", "Physicist", "Geologist", "Marine Biologist",
#                    "Astronomer", "Microbiologist", "Meteorologist", "Environmental Scientist", "Data Scientist"]
# commercial_careers = ["Marketing Manager", "Sales Manager", "Accountant", "Financial Analyst", "Business Consultant",
#                       "Human Resources Manager", "Project Manager", "Supply Chain Manager", "Business Lawyer", "Real Estate Agent"]
# arts_careers = ["Visual Artist", "Musician", "Actor", "Writer", "Dancer",
#                 "Graphic Designer", "Fashion Designer", "Interior Designer", "Architect", "Filmmaker"]
# technology_careers = ["Software Engineer", "Computer_Engineer", "Web Developer", "Data Analyst", "Cybersecurity Analyst",
#                       "Network Engineer", "Artificial Intelligence Engineer", "Robotics Engineer", "Biomedical Engineer", "Chemical Engineer"]


# science_fuzzy_vars = create_fuzzy_vars(science_subjects)
# commercial_fuzzy_vars = create_fuzzy_vars(commercial_subjects)
# arts_fuzzy_vars = create_fuzzy_vars(arts_subjects)
# technology_fuzzy_vars = create_fuzzy_vars(technology_subjects)


# @app.route('/submit_scores', methods=['POST'])
# def submit_scores():
#     data = request.json
#     field = data.get('field')
#     scores = data.get('scores')
#     recommendations = compute_recommendations(field, scores)
    
#     charts = []
#     for career in sim.output:
#         img = io.BytesIO()
#         career_outputs[career].view(sim=sim)
#         plt.savefig(img, format='png')
#         img.seek(0)
#         chart_url = base64.b64encode(img.getvalue()).decode()
#         charts.append(f"data:image/png;base64,{chart_url}")
#         plt.close()
    
#     return render_template('resultpage.html', recommendations=recommendations, charts=charts)