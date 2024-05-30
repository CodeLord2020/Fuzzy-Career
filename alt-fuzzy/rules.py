from skfuzzy import control as ctrl



############### SCIENCE FUZZY RULES #####################
scienceRules = [Arch_rule_1, Arch_rule_2, Arch_rule_3, Arch_rule_4, Arch_rule_5, Arch_rule_6, Arch_rule_7, Arch_rule_8, Arch_rule_9]


Arch_rule_1 = ctrl.Rule(Technical_Drawing['Excellent'] & Mathematics['Excellent'] & Physics['Good'], Architect['high'])
Arch_rule_2 = ctrl.Rule(Technical_Drawing['Excellent'] & Mathematics['Excellent'] & Computer_Studies['Excellent'], Architect['high'])
Arch_rule_3 = ctrl.Rule(Technical_Drawing['Excellent'] & Mathematics['Excellent'] & Geography['Good'], Architect['high'])


Arch_rule_4 = ctrl.Rule(Technical_Drawing['Good'] & Mathematics['Good'] & Physics['Average'], Architect['medium'])
Arch_rule_5 = ctrl.Rule(Technical_Drawing['Good'] & Mathematics['Good'] & Computer_Studies['Good'], Architect['medium'])
Arch_rule_6 = ctrl.Rule(Technical_Drawing['Good'] & Mathematics['Good'] & Geography['Average'], Architect['medium'])

Arch_rule_7 = ctrl.Rule(Technical_Drawing['Average'] & Mathematics['Average'] & Physics['Poor'], Architect['low'])
Arch_rule_8 = ctrl.Rule(Technical_Drawing['Average'] & Mathematics['Average'] & Computer_Studies['Average'], Architect['low'])
Arch_rule_9 = ctrl.Rule(Technical_Drawing['Average'] & Mathematics['Average'] & Geography['Poor'], Architect['low'])



Bio_rule_1 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'], Biologist['high'])
Bio_rule_2 = ctrl.Rule(Biology['Excellent'] & Chemistry['Good'] & Agricultural_Science['Excellent'], Biologist['high'])
Bio_rule_3 = ctrl.Rule(Biology['Excellent'] & Chemistry['Good'] & Physics['Good'], Biologist['high'])

Bio_rule_4 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Physics['Average'], Biologist['medium'])
Bio_rule_5 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Agricultural_Science['Good'], Biologist['medium'])
Bio_rule_6 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Physics['Average'], Biologist['medium'])

Bio_rule_7 = ctrl.Rule(Biology['Average'] & Chemistry['Average'], Biologist['low'])
Bio_rule_8 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Agricultural_Science['Average'], Biologist['low'])
Bio_rule_9 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Geography['Poor'], Biologist['low'])



Bot_rule_1 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Agricultural_Science['Good'], Botanist['high'])
Bot_rule_2 = ctrl.Rule(Biology['Excellent'] & Chemistry['Good'] & Agricultural_Science['Excellent'], Botanist['high'])
Bot_rule_2 = ctrl.Rule(Biology['Good'] & Chemistry['Excellent'] & Agricultural_Science['Excellent'], Botanist['high'])

Bot_rule_4 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Agricultural_Science['Average'], Botanist['medium'])
Bot_rule_5 = ctrl.Rule(Biology['Good'] & Chemistry['Average'] & Agricultural_Science['Good'], Botanist['medium'])
Bot_rule_6 = ctrl.Rule(Biology['Average'] & Chemistry['Good'] & Agricultural_Science['Good'], Botanist['medium'])
Bot_rule_7 = ctrl.Rule(Biology['Excellent'] & Chemistry['Average'] & Agricultural_Science['Good'], Botanist['medium'])


Bot_rule_8 = ctrl.Rule(Biology['Average'] & Chemistry['Excellent'] & Agricultural_Science['Average'], Botanist['low'])
Bot_rule_9 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Agricultural_Science['Average'], Botanist['low'])



Chem_rule_1 = ctrl.Rule(Chemistry['Excellent'] & Mathematics['Excellent'] & Physics['Good'], Chemist['high'])
Chem_rule_2 = ctrl.Rule(Chemistry['Excellent'] & Mathematics['Excellent'] & Biology['Good'], Chemist['high'])
Chem_rule_3 = ctrl.Rule(Chemistry['Excellent'] & Mathematics['Excellent'] & Computer_Studies['Excellent'], Chemist['high'])

Chem_rule_4 = ctrl.Rule(Chemistry['Good'] & Mathematics['Good'] & Physics['Average'], Chemist['medium'])
Chem_rule_5 = ctrl.Rule(Chemistry['Good'] & Mathematics['Good'] & Biology['Average'], Chemist['medium'])
Chem_rule_6 = ctrl.Rule(Chemistry['Good'] & Mathematics['Good'] & Computer_Studies['Good'], Chemist['medium'])

Chem_rule_7 = ctrl.Rule(Chemistry['Average'] & Mathematics['Average'] & Physics['Poor'], Chemist['low'])
Chem_rule_8 = ctrl.Rule(Chemistry['Average'] & Mathematics['Average'] & Biology['Poor'], Chemist['low'])
Chem_rule_9 = ctrl.Rule(Chemistry['Average'] & Mathematics['Average'] & Computer_Studies['Average'], Chemist['low'])



Comp_rule_1 = ctrl.Rule(Computer_Studies['Excellent'] & Mathematics['Excellent'] & Physics['Good'], Computing['high'])
Comp_rule_2 = ctrl.Rule(Computer_Studies['Excellent'] & Mathematics['Excellent'] & Chemistry['Good'], Computing['high'])
Comp_rule_3 = ctrl.Rule(Computer_Studies['Excellent'] & Mathematics['Excellent'] & Biology['Good'], Computing['high'])

Comp_rule_4 = ctrl.Rule(Computer_Studies['Good'] & Mathematics['Good'] & Physics['Average'], Computing['medium'])
Comp_rule_5 = ctrl.Rule(Computer_Studies['Good'] & Mathematics['Good'] & Chemistry['Average'], Computing['medium'])
Comp_rule_6 = ctrl.Rule(Computer_Studies['Good'] & Mathematics['Good'] & Biology['Average'], Computing['medium'])

Comp_rule_7 = ctrl.Rule(Computer_Studies['Average'] & Mathematics['Average'] & Physics['Poor'], Computing['low'])
Comp_rule_8 = ctrl.Rule(Computer_Studies['Average'] & Mathematics['Average'] & Chemistry['Poor'], Computing['low'])
Comp_rule_9 = ctrl.Rule(Computer_Studies['Average'] & Mathematics['Average'] & Biology['Average'], Computing['low'])



Eng_rule_1 = ctrl.Rule(Physics['Excellent'] & Mathematics['Excellent'] & Chemistry['Good'], Engineering['high'])
Eng_rule_2 = ctrl.Rule(Physics['Excellent'] & Mathematics['Excellent'] & Technical_Drawing['Excellent'], Engineering['high'])
Eng_rule_3 = ctrl.Rule(Physics['Excellent'] & Mathematics['Excellent'] & Computer_Studies['Good'], Engineering['high'])

Eng_rule_4 = ctrl.Rule(Physics['Good'] & Mathematics['Good'] & Chemistry['Average'], Engineering['medium'])
Eng_rule_5 = ctrl.Rule(Physics['Good'] & Mathematics['Good'] & Technical_Drawing['Good'], Engineering['medium'])
Eng_rule_6 = ctrl.Rule(Physics['Good'] & Mathematics['Good'] & Computer_Studies['Average'], Engineering['medium'])

Eng_rule_7 = ctrl.Rule(Physics['Average'] & Mathematics['Average'] & Chemistry['Poor'], Engineering['low'])
Eng_rule_8 = ctrl.Rule(Physics['Average'] & Mathematics['Average'] & Technical_Drawing['Average'], Engineering['low'])
Eng_rule_9 = ctrl.Rule(Physics['Average'] & Mathematics['Average'] & Computer_Studies['Poor'], Engineering['low'])


Geo_rule_1 = ctrl.Rule(Geography['Excellent'] & Chemistry['Excellent'] & Physics['Good'], Geologist['high'])
Geo_rule_2 = ctrl.Rule(Geography['Excellent'] & Chemistry['Excellent'] & Biology['Good'], Geologist['high'])
Geo_rule_3 = ctrl.Rule(Geography['Excellent'] & Chemistry['Excellent'] & Agricultural_Science['Excellent'], Geologist['high'])

Geo_rule_4 = ctrl.Rule(Geography['Good'] & Chemistry['Good'] & Physics['Average'], Geologist['medium'])
Geo_rule_5 = ctrl.Rule(Geography['Good'] & Chemistry['Good'] & Biology['Average'], Geologist['medium'])
Geo_rule_6 = ctrl.Rule(Geography['Good'] & Chemistry['Good'] & Agricultural_Science['Good'], Geologist['medium'])

Geo_rule_7 = ctrl.Rule(Geography['Average'] & Chemistry['Average'] & Physics['Poor'], Geologist['low'])
Geo_rule_8 = ctrl.Rule(Geography['Average'] & Chemistry['Average'] & Biology['Poor'], Geologist['low'])
Geo_rule_9 = ctrl.Rule(Geography['Average'] & Chemistry['Average'] & Agricultural_Science['Average'], Geologist['low'])



Med_rule_1 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Physics['Good'], Medicine['high'])
Med_rule_2 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Agricultural_Science['Excellent'], Medicine['high'])
Med_rule_3 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Geography['Good'], Medicine['high'])

Med_rule_4 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Physics['Average'], Medicine['medium'])
Med_rule_5 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Agricultural_Science['Good'], Medicine['medium'])
Med_rule_6 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Geography['Average'], Medicine['medium'])

Med_rule_7 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Physics['Poor'], Medicine['low'])
Med_rule_8 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Agricultural_Science['Average'], Medicine['low'])
Med_rule_9 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Geography['Poor'], Medicine['low'])



Meteo_rule_1 = ctrl.Rule(Physics['Excellent'] & Mathematics['Excellent'] & Geography['Good'], Meteorologist['high'])
Meteo_rule_2 = ctrl.Rule(Physics['Excellent'] & Mathematics['Excellent'] & Computer_Studies['Excellent'], Meteorologist['high'])
Meteo_rule_3 = ctrl.Rule(Physics['Excellent'] & Mathematics['Excellent'] & Agricultural_Science['Good'], Meteorologist['high'])

Meteo_rule_4 = ctrl.Rule(Physics['Good'] & Mathematics['Good'] & Geography['Average'], Meteorologist['medium'])
Meteo_rule_5 = ctrl.Rule(Physics['Good'] & Mathematics['Good'] & Computer_Studies['Good'], Meteorologist['medium'])
Meteo_rule_6 = ctrl.Rule(Physics['Good'] & Mathematics['Good'] & Agricultural_Science['Average'], Meteorologist['medium'])

Meteo_rule_7 = ctrl.Rule(Physics['Average'] & Mathematics['Average'] & Geography['Poor'], Meteorologist['low'])
Meteo_rule_8 = ctrl.Rule(Physics['Average'] & Mathematics['Average'] & Computer_Studies['Average'], Meteorologist['low'])
Meteo_rule_9 = ctrl.Rule(Physics['Average'] & Mathematics['Average'] & Agricultural_Science['Poor'], Meteorologist['low'])



Micro_rule_1 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Physics['Good'], Microbiologist['high'])
Micro_rule_2 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Agricultural_Science['Excellent'], Microbiologist['high'])
Micro_rule_3 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Geography['Good'], Microbiologist['high'])

Micro_rule_4 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Physics['Average'], Microbiologist['medium'])
Micro_rule_5 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Agricultural_Science['Good'], Microbiologist['medium'])
Micro_rule_6 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Geography['Average'], Microbiologist['medium'])

Micro_rule_7 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Physics['Poor'], Microbiologist['low'])
Micro_rule_8 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Agricultural_Science['Average'], Microbiologist['low'])
Micro_rule_9 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Geography['Poor'], Microbiologist['low'])



Micro_rule_1 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Physics['Good'], Microbiologist['high'])
Micro_rule_2 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Agricultural_Science['Excellent'], Microbiologist['high'])
Micro_rule_3 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Geography['Good'], Microbiologist['high'])

Micro_rule_4 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Physics['Average'], Microbiologist['medium'])
Micro_rule_5 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Agricultural_Science['Good'], Microbiologist['medium'])
Micro_rule_6 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Geography['Average'], Microbiologist['medium'])

Micro_rule_7 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Physics['Poor'], Microbiologist['low'])
Micro_rule_8 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Agricultural_Science['Average'], Microbiologist['low'])
Micro_rule_9 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Geography['Poor'], Microbiologist['low'])



Phys_rule_1 = ctrl.Rule(Physics['Excellent'] & Mathematics['Excellent'] & Chemistry['Good'], Physicist['high'])
Phys_rule_2 = ctrl.Rule(Physics['Excellent'] & Mathematics['Excellent'] & Computer_Studies['Excellent'], Physicist['high'])
Phys_rule_3 = ctrl.Rule(Physics['Excellent'] & Mathematics['Excellent'] & Geography['Good'], Physicist['high'])

Phys_rule_4 = ctrl.Rule(Physics['Good'] & Mathematics['Good'] & Chemistry['Average'], Physicist['medium'])
Phys_rule_5 = ctrl.Rule(Physics['Good'] & Mathematics['Good'] & Computer_Studies['Good'], Physicist['medium'])
Phys_rule_6 = ctrl.Rule(Physics['Good'] & Mathematics['Good'] & Geography['Average'], Physicist['medium'])

Phys_rule_7 = ctrl.Rule(Physics['Average'] & Mathematics['Average'] & Chemistry['Poor'], Physicist['low'])
Phys_rule_8 = ctrl.Rule(Physics['Average'] & Mathematics['Average'] & Computer_Studies['Average'], Physicist['low'])
Phys_rule_9 = ctrl.Rule(Physics['Average'] & Mathematics['Average'] & Geography['Poor'], Physicist['low'])



Teach_rule_1 = ctrl.Rule(English['Excellent'] & Biology['Good'] & Chemistry['Good'], Teacher['high'])
Teach_rule_2 = ctrl.Rule(English['Excellent'] & Mathematics['Good'] & Physics['Good'], Teacher['high'])
Teach_rule_3 = ctrl.Rule(English['Excellent'] & Any_Subject['Excellent'] & Any_Subject['Good'], Teacher['high'])

Teach_rule_4 = ctrl.Rule(English['Good'] & Biology['Average'] & Chemistry['Average'], Teacher['medium'])
Teach_rule_5 = ctrl.Rule(English['Good'] & Mathematics['Average'] & Physics['Average'], Teacher['medium'])
Teach_rule_6 = ctrl.Rule(English['Good'] & Any_Subject['Good'] & Any_Subject['Average'], Teacher['medium'])

Teach_rule_7 = ctrl.Rule(English['Average'] & Biology['Poor'] & Chemistry['Poor'], Teacher['low'])
Teach_rule_8 = ctrl.Rule(English['Average'] & Mathematics['Poor'] & Physics['Poor'], Teacher['low'])
Teach_rule_9 = ctrl.Rule(English['Average'] & Any_Subject['Average'] & Any_Subject['Poor'], Teacher['low'])



Vet_rule_1 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Physics['Good'], Veterinarian['high'])
Vet_rule_2 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Agricultural_Science['Excellent'], Veterinarian['high'])
Vet_rule_3 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Geography['Good'], Veterinarian['high'])

Vet_rule_4 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Physics['Average'], Veterinarian['medium'])
Vet_rule_5 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Agricultural_Science['Good'], Veterinarian['medium'])
Vet_rule_6 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Geography['Average'], Veterinarian['medium'])

Vet_rule_7 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Physics['Poor'], Veterinarian['low'])
Vet_rule_8 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Agricultural_Science['Average'], Veterinarian['low'])
Vet_rule_9 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Geography['Poor'], Veterinarian['low'])



Zoo_rule_1 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Physics['Good'], Zoologist['high'])
Zoo_rule_2 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Agricultural_Science['Excellent'], Zoologist['high'])
Zoo_rule_3 = ctrl.Rule(Biology['Excellent'] & Chemistry['Excellent'] & Geography['Good'], Zoologist['high'])

Zoo_rule_4 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Physics['Average'], Zoologist['medium'])
Zoo_rule_5 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Agricultural_Science['Good'], Zoologist['medium'])
Zoo_rule_6 = ctrl.Rule(Biology['Good'] & Chemistry['Good'] & Geography['Average'], Zoologist['medium'])

Zoo_rule_7 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Physics['Poor'], Zoologist['low'])
Zoo_rule_8 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Agricultural_Science['Average'], Zoologist['low'])
Zoo_rule_9 = ctrl.Rule(Biology['Average'] & Chemistry['Average'] & Geography['Poor'], Zoologist['low'])








############### COMMERCIAL FUZZY RULES #####################

Accountant_rule_1 = ctrl.Rule(Accounting['Excellent'] & Mathematics['Excellent'] & Economics['Excellent'], Accountant['high'])
Accountant_rule_2 = ctrl.Rule(Accounting['Excellent'] & Commerce['Excellent'] & Economics['Excellent'], Accountant['high'])
Accountant_rule_3 = ctrl.Rule(Accounting['Excellent'] & Computer_Studies['Excellent'], Accountant['high'])

Accountant_rule_4 = ctrl.Rule(Accounting['Good'] & Mathematics['Good'] & Economics['Good'], Accountant['medium'])
Accountant_rule_5 = ctrl.Rule(Accounting['Good'] & Commerce['Good'] & Economics['Good'], Accountant['medium'])
Accountant_rule_6 = ctrl.Rule(Accounting['Good'] & Computer_Studies['Good'], Accountant['medium'])

Accountant_rule_7 = ctrl.Rule(Accounting['Average'] & Mathematics['Average'] & Economics['Average'], Accountant['low'])
Accountant_rule_8 = ctrl.Rule(Accounting['Average'] & Commerce['Average'] & Economics['Average'], Accountant['low'])
Accountant_rule_9 = ctrl.Rule(Accounting['Average'] & Computer_Studies['Average'], Accountant['low'])



Banker_rule_1 = ctrl.Rule(Economics['Excellent'] & Commerce['Excellent'] & Accounting['Excellent'], Banker['high'])
Banker_rule_2 = ctrl.Rule(Mathematics['Excellent'] & Commerce['Excellent'] & Accounting['Good'], Banker['high'])
Banker_rule_3 = ctrl.Rule(Economics['Excellent'] & Commerce['Excellent'] & Computer_Studies['Excellent'], Banker['high'])

Banker_rule_4 = ctrl.Rule(Economics['Good'] & Commerce['Good'] & Accounting['Good'], Banker['medium'])
Banker_rule_5 = ctrl.Rule(Mathematics['Good'] & Commerce['Good'] & Accounting['Average'], Banker['medium'])
Banker_rule_6 = ctrl.Rule(Economics['Good'] & Commerce['Good'] & Computer_Studies['Good'], Banker['medium'])

Banker_rule_7 = ctrl.Rule(Economics['Average'] & Commerce['Average'] & Accounting['Average'], Banker['low'])
Banker_rule_8 = ctrl.Rule(Mathematics['Average'] & Commerce['Average'] & Accounting['Poor'], Banker['low'])
Banker_rule_9 = ctrl.Rule(Economics['Average'] & Commerce['Average'] & Computer_Studies['Average'], Banker['low'])



BusConsult_rule_1 = ctrl.Rule(Economics['Excellent'] & Commerce['Excellent'] & Government['Excellent'], Business-Consultant['high'])
BusConsult_rule_2 = ctrl.Rule(Economics['Excellent'] & Commerce['Excellent'] & Civic_Education['Excellent'], Business-Consultant['high'])
BusConsult_rule_3 = ctrl.Rule(Economics['Excellent'] & Commerce['Excellent'] & Accounting['Excellent'], Business-Consultant['high'])

BusConsult_rule_4 = ctrl.Rule(Economics['Good'] & Commerce['Good'] & Government['Good'], Business-Consultant['medium'])
BusConsult_rule_5 = ctrl.Rule(Economics['Good'] & Commerce['Good'] & Civic_Education['Good'], Business-Consultant['medium'])
BusConsult_rule_6 = ctrl.Rule(Economics['Good'] & Commerce['Good'] & Accounting['Good'], Business-Consultant['medium'])

BusConsult_rule_7 = ctrl.Rule(Economics['Average'] & Commerce['Average'] & Government['Average'], Business-Consultant['low'])
BusConsult_rule_8 = ctrl.Rule(Economics['Average'] & Commerce['Average'] & Civic_Education['Average'], Business-Consultant['low'])
BusConsult_rule_9 = ctrl.Rule(Economics['Average'] & Commerce['Average'] & Accounting['Average'], Business-Consultant['low'])



Entrepreneur_rule_1 = ctrl.Rule(Economics['Excellent'] & Commerce['Excellent'] & Government['Excellent'], Entrepreneur['high'])
Entrepreneur_rule_2 = ctrl.Rule(Economics['Excellent'] & Commerce['Excellent'] & Civic_Education['Excellent'], Entrepreneur['high'])
Entrepreneur_rule_3 = ctrl.Rule(Economics['Excellent'] & Commerce['Excellent'] & Accounting['Excellent'], Entrepreneur['high'])

Entrepreneur_rule_4 = ctrl.Rule(Economics['Good'] & Commerce['Good'] & Government['Good'], Entrepreneur['medium'])
Entrepreneur_rule_5 = ctrl.Rule(Economics['Good'] & Commerce['Good'] & Civic_Education['Good'], Entrepreneur['medium'])
Entrepreneur_rule_6 = ctrl.Rule(Economics['Good'] & Commerce['Good'] & Accounting['Good'], Entrepreneur['medium'])

Entrepreneur_rule_7 = ctrl.Rule(Economics['Average'] & Commerce['Average'] & Government['Average'], Entrepreneur['low'])
Entrepreneur_rule_8 = ctrl.Rule(Economics['Average'] & Commerce['Average'] & Civic_Education['Average'], Entrepreneur['low'])
Entrepreneur_rule_9 = ctrl.Rule(Economics['Average'] & Commerce['Average'] & Accounting['Average'], Entrepreneur['low'])



FinAnalyst_rule_1 = ctrl.Rule(Economics['Excellent'] & Accounting['Excellent'] & Mathematics['Excellent'], Financial_Analyst['high'])
FinAnalyst_rule_2 = ctrl.Rule(Economics['Excellent'] & Accounting['Excellent'] & Computer_Studies['Excellent'], Financial_Analyst['high'])
FinAnalyst_rule_3 = ctrl.Rule(Economics['Excellent'] & Commerce['Excellent'] & Accounting['Excellent'], Financial_Analyst['high'])

FinAnalyst_rule_4 = ctrl.Rule(Economics['Good'] & Accounting['Good'] & Mathematics['Good'], Financial_Analyst['medium'])
FinAnalyst_rule_5 = ctrl.Rule(Economics['Good'] & Accounting['Good'] & Computer_Studies['Good'], Financial_Analyst['medium'])
FinAnalyst_rule_6 = ctrl.Rule(Economics['Good'] & Commerce['Good'] & Accounting['Good'], Financial_Analyst['medium'])

FinAnalyst_rule_7 = ctrl.Rule(Economics['Average'] & Accounting['Average'] & Mathematics['Average'], Financial_Analyst['low'])
FinAnalyst_rule_8 = ctrl.Rule(Economics['Average'] & Accounting['Average'] & Computer_Studies['Average'], Financial_Analyst['low'])
FinAnalyst_rule_9 = ctrl.Rule(Economics['Average'] & Commerce['Average'] & Accounting['Average'], Financial_Analyst['low'])



HRM_rule_1 = ctrl.Rule(English['Excellent'] & Economics['Excellent'] & Civic_Education['Excellent'], Human_Resources_Manager['high'])
HRM_rule_2 = ctrl.Rule(English['Excellent'] & Economics['Excellent'] & Government['Excellent'], Human_Resources_Manager['high'])
HRM_rule_3 = ctrl.Rule(English['Excellent'] & Economics['Excellent'] & Accounting['Excellent'], Human_Resources_Manager['high'])

HRM_rule_4 = ctrl.Rule(English['Good'] & Economics['Good'] & Civic_Education['Good'], Human_Resources_Manager['medium'])
HRM_rule_5 = ctrl.Rule(English['Good'] & Economics['Good'] & Government['Good'], Human_Resources_Manager['medium'])
HRM_rule_6 = ctrl.Rule(English['Good'] & Economics['Good'] & Accounting['Good'], Human_Resources_Manager['medium'])

HRM_rule_7 = ctrl.Rule(English['Average'] & Economics['Average'] & Civic_Education['Average'], Human_Resources_Manager['low'])
HRM_rule_8 = ctrl.Rule(English['Average'] & Economics['Average'] & Government['Average'], Human_Resources_Manager['low'])
HRM_rule_9 = ctrl.Rule(English['Average'] & Economics['Average'] & Accounting['Average'], Human_Resources_Manager['low'])



MarketingManager_rule_1 = ctrl.Rule(Economics['Excellent'] & Commerce['Excellent'] & Government['Excellent'], Marketing_Manager['high'])
MarketingManager_rule_2 = ctrl.Rule(Economics['Excellent'] & Commerce['Excellent'] & Civic_Education['Excellent'], Marketing_Manager['high'])
MarketingManager_rule_3 = ctrl.Rule(Economics['Excellent'] & Commerce['Excellent'] & Accounting['Excellent'], Marketing_Manager['high'])

MarketingManager_rule_4 = ctrl.Rule(Economics['Good'] & Commerce['Good'] & Government['Good'], Marketing_Manager['medium'])
MarketingManager_rule_5 = ctrl.Rule(Economics['Good'] & Commerce['Good'] & Civic_Education['Good'], Marketing_Manager['medium'])
MarketingManager_rule_6 = ctrl.Rule(Economics['Good'] & Commerce['Good'] & Accounting['Good'], Marketing_Manager['medium'])

MarketingManager_rule_7 = ctrl.Rule(Economics['Average'] & Commerce['Average'] & Government['Average'], Marketing_Manager['low'])
MarketingManager_rule_8 = ctrl.Rule(Economics['Average'] & Commerce['Average'] & Civic_Education['Average'], Marketing_Manager['low'])
MarketingManager_rule_9 = ctrl.Rule(Economics['Average'] & Commerce['Average'] & Accounting['Average'], Marketing_Manager['low'])



ProjectManager_rule_1 = ctrl.Rule(English['Excellent'] & Mathematics['Excellent'] & Economics['Excellent'], Project_Manager['high'])
ProjectManager_rule_2 = ctrl.Rule(English['Excellent'] & Commerce['Excellent'] & Government['Excellent'], Project_Manager['high'])
ProjectManager_rule_3 = ctrl.Rule(English['Excellent'] & Accounting['Excellent'] & Computer_Studies['Excellent'], Project_Manager['high'])

ProjectManager_rule_4 = ctrl.Rule(English['Good'] & Mathematics['Good'] & Economics['Good'], Project_Manager['medium'])
ProjectManager_rule_5 = ctrl.Rule(English['Good'] & Commerce['Good'] & Government['Good'], Project_Manager['medium'])
ProjectManager_rule_6 = ctrl.Rule(English['Good'] & Accounting['Good'] & Computer_Studies['Good'], Project_Manager['medium'])

ProjectManager_rule_7 = ctrl.Rule(English['Average'] & Mathematics['Average'] & Economics['Average'], Project_Manager['low'])
ProjectManager_rule_8 = ctrl.Rule(English['Average'] & Commerce['Average'] & Government['Average'], Project_Manager['low'])
ProjectManager_rule_9 = ctrl.Rule(English['Average'] & Accounting['Average'] & Computer_Studies['Average'], Project_Manager['low'])



RealEstateAgent_rule_1 = ctrl.Rule(English['Excellent'] & Mathematics['Excellent'] & Economics['Excellent'], Real_Estate_Agent['high'])
RealEstateAgent_rule_2 = ctrl.Rule(English['Excellent'] & Commerce['Excellent'] & Government['Excellent'], Real_Estate_Agent['high'])
RealEstateAgent_rule_3 = ctrl.Rule(English['Excellent'] & Accounting['Excellent'] & Computer_Studies['Excellent'], Real_Estate_Agent['high'])

RealEstateAgent_rule_4 = ctrl.Rule(English['Good'] & Mathematics['Good'] & Economics['Good'], Real_Estate_Agent['medium'])
RealEstateAgent_rule_5 = ctrl.Rule(English['Good'] & Commerce['Good'] & Government['Good'], Real_Estate_Agent['medium'])
RealEstateAgent_rule_6 = ctrl.Rule(English['Good'] & Accounting['Good'] & Computer_Studies['Good'], Real_Estate_Agent['medium'])

RealEstateAgent_rule_7 = ctrl.Rule(English['Average'] & Mathematics['Average'] & Economics['Average'], Real_Estate_Agent['low'])
RealEstateAgent_rule_8 = ctrl.Rule(English['Average'] & Commerce['Average'] & Government['Average'], Real_Estate_Agent['low'])
RealEstateAgent_rule_9 = ctrl.Rule(English['Average'] & Accounting['Average'] & Computer_Studies['Average'], Real_Estate_Agent['low'])



SalesManager_rule_1 = ctrl.Rule(Economics['Excellent'] & Commerce['Excellent'] & Government['Excellent'], Sales_Manager['high'])
SalesManager_rule_2 = ctrl.Rule(Economics['Excellent'] & Commerce['Excellent'] & Civic_Education['Excellent'], Sales_Manager['high'])
SalesManager_rule_3 = ctrl.Rule(Economics['Excellent'] & Commerce['Excellent'] & Accounting['Excellent'], Sales_Manager['high'])

SalesManager_rule_4 = ctrl.Rule(Economics['Good'] & Commerce['Good'] & Government['Good'], Sales_Manager['medium'])
SalesManager_rule_5 = ctrl.Rule(Economics['Good'] & Commerce['Good'] & Civic_Education['Good'], Sales_Manager['medium'])
SalesManager_rule_6 = ctrl.Rule(Economics['Good'] & Commerce['Good'] & Accounting['Good'], Sales_Manager['medium'])

SalesManager_rule_7 = ctrl.Rule(Economics['Average'] & Commerce['Average'] & Government['Average'], Sales_Manager['low'])
SalesManager_rule_8 = ctrl.Rule(Economics['Average'] & Commerce['Average'] & Civic_Education['Average'], Sales_Manager['low'])
SalesManager_rule_9 = ctrl.Rule(Economics['Average'] & Commerce['Average'] & Accounting['Average'], Sales_Manager['low'])



SupplyChainManager_rule_1 = ctrl.Rule(English['Excellent'] & Mathematics['Excellent'] & Economics['Excellent'], Supply_Chain_Manager['high'])
SupplyChainManager_rule_2 = ctrl.Rule(English['Excellent'] & Commerce['Excellent'] & Accounting['Excellent'], Supply_Chain_Manager['high'])
SupplyChainManager_rule_3 = ctrl.Rule(English['Excellent'] & Government['Excellent'] & Computer_Studies['Excellent'], Supply_Chain_Manager['high'])

SupplyChainManager_rule_4 = ctrl.Rule(English['Good'] & Mathematics['Good'] & Economics['Good'], Supply_Chain_Manager['medium'])
SupplyChainManager_rule_5 = ctrl.Rule(English['Good'] & Commerce['Good'] & Accounting['Good'], Supply_Chain_Manager['medium'])
SupplyChainManager_rule_6 = ctrl.Rule(English['Good'] & Government['Good'] & Computer_Studies['Good'], Supply_Chain_Manager['medium'])

SupplyChainManager_rule_7 = ctrl.Rule(English['Average'] & Mathematics['Average'] & Economics['Average'], Supply_Chain_Manager['low'])
SupplyChainManager_rule_8 = ctrl.Rule(English['Average'] & Commerce['Average'] & Accounting['Average'], Supply_Chain_Manager['low'])
SupplyChainManager_rule_9 = ctrl.Rule(English['Average'] & Government['Average'] & Computer_Studies['Average'], Supply_Chain_Manager['low'])



Teacher_rule_1 = ctrl.Rule(English['Excellent'] & Mathematics['Excellent'] & Economics['Excellent'], Teacher['high'])
Teacher_rule_2 = ctrl.Rule(English['Excellent'] & Mathematics['Excellent'] & Civic_Education['Excellent'], Teacher['high'])
Teacher_rule_3 = ctrl.Rule(English['Excellent'] & Mathematics['Excellent'] & Computer_Studies['Excellent'], Teacher['high'])

Teacher_rule_4 = ctrl.Rule(English['Good'] & Mathematics['Good'] & Economics['Good'], Teacher['medium'])
Teacher_rule_5 = ctrl.Rule(English['Good'] & Mathematics['Good'] & Civic_Education['Good'], Teacher['medium'])
Teacher_rule_6 = ctrl.Rule(English['Good'] & Mathematics['Good'] & Computer_Studies['Good'], Teacher['medium'])

Teacher_rule_7 = ctrl.Rule(English['Average'] & Mathematics['Average'] & Economics['Average'], Teacher['low'])
Teacher_rule_8 = ctrl.Rule(English['Average'] & Mathematics['Average'] & Civic_Education['Average'], Teacher['low'])
Teacher_rule_9 = ctrl.Rule(English['Average'] & Mathematics['Average'] & Computer_Studies['Average'], Teacher['low'])



############### ARTS FUZZY RULES #####################

Actor_rule_1 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Civic_Education['Excellent'], Actor['high'])
Actor_rule_2 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & History['Excellent'], Actor['high'])
Actor_rule_3 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Technical_Drawing['Excellent'], Actor['high'])

Actor_rule_4 = ctrl.Rule(English['Good'] & Literature['Good'] & Civic_Education['Good'], Actor['medium'])
Actor_rule_5 = ctrl.Rule(English['Good'] & Literature['Good'] & History['Good'], Actor['medium'])
Actor_rule_6 = ctrl.Rule(English['Good'] & Literature['Good'] & Technical_Drawing['Good'], Actor['medium'])

Actor_rule_7 = ctrl.Rule(English['Average'] & Literature['Average'] & Civic_Education['Average'], Actor['low'])
Actor_rule_8 = ctrl.Rule(English['Average'] & Literature['Average'] & History['Average'], Actor['low'])
Actor_rule_9 = ctrl.Rule(English['Average'] & Literature['Average'] & Technical_Drawing['Average'], Actor['low'])



Animator_rule_1 = ctrl.Rule(Mathematics['Good'] & Technical_Drawing['Excellent'] & Computer_Studies['Excellent'], Animator['high'])
Animator_rule_2 = ctrl.Rule(Mathematics['Excellent'] & Technical_Drawing['Excellent'] & Computer_Studies['Good'], Animator['high'])
Animator_rule_2 = ctrl.Rule(Mathematics['Excellent'] & Computer_Studies['Excellent'] & Technical_Drawing['Good'], Animator['high'])

Animator_rule_4 = ctrl.Rule(Mathematics['Excellent'] & Computer_Studies['Good'] & Technical_Drawing['Good'], Animator['medium'])
Animator_rule_5 = ctrl.Rule(Mathematics['Good'] & Computer_Studies['Excellent'] & Technical_Drawing['Good'], Animator['medium'])
Animator_rule_6 = ctrl.Rule(Mathematics['Good'] & Computer_Studies['Good'] & Technical_Drawing['Excellent'], Animator['medium'])

Animator_rule_4 = ctrl.Rule(Mathematics['average'] | Computer_Studies['average'] | Technical_Drawing['average'], Animator['low'])

Animator_rule_4 = ctrl.Rule(English['Good'] & Literature['Good'] & Computer_Studies['Good'], Animator['medium'])
Animator_rule_5 = ctrl.Rule(English['Good'] & Literature['Good'] & Technical_Drawing['Good'],  Animator['medium'])


Architect_rule_1 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Technical_Drawing['Excellent'], Architect['high'])
Architect_rule_2 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Computer_Studies['Excellent'], Architect['high'])
Architect_rule_3 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Mathematics['Excellent'], Architect['high'])

Architect_rule_4 = ctrl.Rule(English['Good'] & Literature['Good'] & Technical_Drawing['Good'], Architect['medium'])
Architect_rule_5 = ctrl.Rule(English['Good'] & Literature['Good'] & Computer_Studies['Good'], Architect['medium'])
Architect_rule_6 = ctrl.Rule(English['Good'] & Literature['Good'] & Mathematics['Good'], Architect['medium'])

Architect_rule_7 = ctrl.Rule(English['Average'] & Literature['Average'] & Technical_Drawing['Average'], Architect['low'])
Architect_rule_8 = ctrl.Rule(English['Average'] & Literature['Average'] & Computer_Studies['Average'], Architect['low'])
Architect_rule_9 = ctrl.Rule(English['Average'] & Literature['Average'] & Mathematics['Average'], Architect['low'])



Athlete_rule_1 = ctrl.Rule(Physical_Education['Excellent'] & English['Excellent'], Athlete['high'])
Athlete_rule_2 = ctrl.Rule(Physical_Education['Excellent'] & Mathematics['Excellent'], Athlete['high'])
Athlete_rule_3 = ctrl.Rule(Physical_Education['Excellent'] & Civic_Education['Excellent'], Athlete['high'])

Athlete_rule_4 = ctrl.Rule(Physical_Education['Good'] & English['Good'], Athlete['medium'])
Athlete_rule_5 = ctrl.Rule(Physical_Education['Good'] & Mathematics['Good'], Athlete['medium'])
Athlete_rule_6 = ctrl.Rule(Physical_Education['Good'] & Civic_Education['Good'], Athlete['medium'])

Athlete_rule_7 = ctrl.Rule(Physical_Education['Average'] & English['Average'], Athlete['low'])
Athlete_rule_8 = ctrl.Rule(Physical_Education['Average'] & Mathematics['Average'], Athlete['low'])
Athlete_rule_9 = ctrl.Rule(Physical_Education['Average'] & Civic_Education['Average'], Athlete['low'])



Filmmaker_rule_1 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & History['Excellent'], Filmmaker['high'])
Filmmaker_rule_2 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Civic_Education['Excellent'], Filmmaker['high'])
Filmmaker_rule_3 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Government['Excellent'], Filmmaker['high'])

Filmmaker_rule_4 = ctrl.Rule(English['Good'] & Literature['Good'] & History['Good'], Filmmaker['medium'])
Filmmaker_rule_5 = ctrl.Rule(English['Good'] & Literature['Good'] & Civic_Education['Good'], Filmmaker['medium'])
Filmmaker_rule_6 = ctrl.Rule(English['Good'] & Literature['Good'] & Government['Good'], Filmmaker['medium'])

Filmmaker_rule_7 = ctrl.Rule(English['Average'] & Literature['Average'] & History['Average'], Filmmaker['low'])
Filmmaker_rule_8 = ctrl.Rule(English['Average'] & Literature['Average'] & Civic_Education['Average'], Filmmaker['low'])
Filmmaker_rule_9 = ctrl.Rule(English['Average'] & Literature['Average'] & Government['Average'], Filmmaker['low'])



GraphicDesigner_rule_1 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Technical_Drawing['Excellent'], Graphic_Designer['high'])
GraphicDesigner_rule_2 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Computer_Studies['Excellent'], Graphic_Designer['high'])
GraphicDesigner_rule_3 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & History['Excellent'], Graphic_Designer['high'])

GraphicDesigner_rule_4 = ctrl.Rule(English['Good'] & Literature['Good'] & Technical_Drawing['Good'], Graphic_Designer['medium'])
GraphicDesigner_rule_5 = ctrl.Rule(English['Good'] & Literature['Good'] & Computer_Studies['Good'], Graphic_Designer['medium'])
GraphicDesigner_rule_6 = ctrl.Rule(English['Good'] & Literature['Good'] & History['Good'], Graphic_Designer['medium'])

GraphicDesigner_rule_7 = ctrl.Rule(English['Average'] & Literature['Average'] & Technical_Drawing['Average'], Graphic_Designer['low'])
GraphicDesigner_rule_8 = ctrl.Rule(English['Average'] & Literature['Average'] & Computer_Studies['Average'], Graphic_Designer['low'])
GraphicDesigner_rule_9 = ctrl.Rule(English['Average'] & Literature['Average'] & History['Average'], Graphic_Designer['low'])



Journalist_rule_1 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Civic_Education['Excellent'], Journalist['high'])
Journalist_rule_2 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & History['Excellent'], Journalist['high'])
Journalist_rule_3 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Government['Excellent'], Journalist['high'])

Journalist_rule_4 = ctrl.Rule(English['Good'] & Literature['Good'] & Civic_Education['Good'], Journalist['medium'])
Journalist_rule_5 = ctrl.Rule(English['Good'] & Literature['Good'] & History['Good'], Journalist['medium'])
Journalist_rule_6 = ctrl.Rule(English['Good'] & Literature['Good'] & Government['Good'], Journalist['medium'])

Journalist_rule_7 = ctrl.Rule(English['Average'] & Literature['Average'] & Civic_Education['Average'], Journalist['low'])
Journalist_rule_8 = ctrl.Rule(English['Average'] & Literature['Average'] & History['Average'], Journalist['low'])
Journalist_rule_9 = ctrl.Rule(English['Average'] & Literature['Average'] & Government['Average'], Journalist['low'])



Musician_rule_1 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & History['Excellent'], Musician['high'])
Musician_rule_2 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Civic_Education['Excellent'], Musician['high'])
Musician_rule_3 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Law['Excellent'], Musician['high'])

Musician_rule_4 = ctrl.Rule(English['Good'] & Literature['Good'] & History['Good'], Musician['medium'])
Musician_rule_5 = ctrl.Rule(English['Good'] & Literature['Good'] & Civic_Education['Good'], Musician['medium'])
Musician_rule_6 = ctrl.Rule(English['Good'] & Literature['Good'] & Law['Good'], Musician['medium'])

Musician_rule_7 = ctrl.Rule(English['Average'] & Literature['Average'] & History['Average'], Musician['low'])
Musician_rule_8 = ctrl.Rule(English['Average'] & Literature['Average'] & Civic_Education['Average'], Musician['low'])
Musician_rule_9 = ctrl.Rule(English['Average'] & Literature['Average'] & Law['Average'], Musician['low'])



Politician_rule_1 = ctrl.Rule(English['Excellent'] & Government['Excellent'] & Civic_Education['Excellent'], Politician['high'])
Politician_rule_2 = ctrl.Rule(English['Excellent'] & Government['Excellent'] & History['Excellent'], Politician['high'])
Politician_rule_3 = ctrl.Rule(English['Excellent'] & Government['Excellent'] & Law['Excellent'], Politician['high'])

Politician_rule_4 = ctrl.Rule(English['Good'] & Government['Good'] & Civic_Education['Good'], Politician['medium'])
Politician_rule_5 = ctrl.Rule(English['Good'] & Government['Good'] & History['Good'], Politician['medium'])
Politician_rule_6 = ctrl.Rule(English['Good'] & Government['Good'] & Law['Good'], Politician['medium'])

Politician_rule_7 = ctrl.Rule(English['Average'] & Government['Average'] & Civic_Education['Average'], Politician['low'])
Politician_rule_8 = ctrl.Rule(English['Average'] & Government['Average'] & History['Average'], Politician['low'])
Politician_rule_9 = ctrl.Rule(English['Average'] & Government['Average'] & Law['Average'], Politician['low'])



Teacher_rule_1 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Government['Excellent'], Teacher['high'])
Teacher_rule_2 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & History['Excellent'], Teacher['high'])
Teacher_rule_3 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Economics['Excellent'], Teacher['high'])

Teacher_rule_4 = ctrl.Rule(English['Good'] & Literature['Good'] & Government['Good'], Teacher['medium'])
Teacher_rule_5 = ctrl.Rule(English['Good'] & Literature['Good'] & History['Good'], Teacher['medium'])
Teacher_rule_6 = ctrl.Rule(English['Good'] & Literature['Good'] & Economics['Good'], Teacher['medium'])

Teacher_rule_7 = ctrl.Rule(English['Average'] & Literature['Average'] & Government['Average'], Teacher['low'])
Teacher_rule_8 = ctrl.Rule(English['Average'] & Literature['Average'] & History['Average'], Teacher['low'])
Teacher_rule_9 = ctrl.Rule(English['Average'] & Literature['Average'] & Economics['Average'], Teacher['low'])



TVRadioPresenter_rule_1 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Civic_Education['Excellent'], TV_Radio_Presenter['high'])
TVRadioPresenter_rule_2 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Government['Excellent'], TV_Radio_Presenter['high'])
TVRadioPresenter_rule_3 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & History['Excellent'], TV_Radio_Presenter['high'])

TVRadioPresenter_rule_4 = ctrl.Rule(English['Good'] & Literature['Good'] & Civic_Education['Good'], TV_Radio_Presenter['medium'])
TVRadioPresenter_rule_5 = ctrl.Rule(English['Good'] & Literature['Good'] & Government['Good'], TV_Radio_Presenter['medium'])
TVRadioPresenter_rule_6 = ctrl.Rule(English['Good'] & Literature['Good'] & History['Good'], TV_Radio_Presenter['medium'])

TVRadioPresenter_rule_7 = ctrl.Rule(English['Average'] & Literature['Average'] & Civic_Education['Average'], TV_Radio_Presenter['low'])
TVRadioPresenter_rule_8 = ctrl.Rule(English['Average'] & Literature['Average'] & Government['Average'], TV_Radio_Presenter['low'])
TVRadioPresenter_rule_9 = ctrl.Rule(English['Average'] & Literature['Average'] & History['Average'], TV_Radio_Presenter['low'])



VisualArtist_rule_1 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Civic_Education['Excellent'], Visual_Artist['high'])
VisualArtist_rule_2 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Technical_Drawing['Excellent'], Visual_Artist['high'])
VisualArtist_rule_3 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & History['Excellent'], Visual_Artist['high'])

VisualArtist_rule_4 = ctrl.Rule(English['Good'] & Literature['Good'] & Civic_Education['Good'], Visual_Artist['medium'])
VisualArtist_rule_5 = ctrl.Rule(English['Good'] & Literature['Good'] & Technical_Drawing['Good'], Visual_Artist['medium'])
VisualArtist_rule_6 = ctrl.Rule(English['Good'] & Literature['Good'] & History['Good'], Visual_Artist['medium'])

VisualArtist_rule_7 = ctrl.Rule(English['Average'] & Literature['Average'] & Civic_Education['Average'], Visual_Artist['low'])
VisualArtist_rule_8 = ctrl.Rule(English['Average'] & Literature['Average'] & Technical_Drawing['Average'], Visual_Artist['low'])
VisualArtist_rule_9 = ctrl.Rule(English['Average'] & Literature['Average'] & History['Average'], Visual_Artist['low'])



Writer_rule_1 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & History['Excellent'], Writer['high'])
Writer_rule_2 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Civic_Education['Excellent'], Writer['high'])
Writer_rule_3 = ctrl.Rule(English['Excellent'] & Literature['Excellent'] & Law['Excellent'], Writer['high'])

Writer_rule_4 = ctrl.Rule(English['Good'] & Literature['Good'] & History['Good'], Writer['medium'])
Writer_rule_5 = ctrl.Rule(English['Good'] & Literature['Good'] & Civic_Education['Good'], Writer['medium'])
Writer_rule_6 = ctrl.Rule(English['Good'] & Literature['Good'] & Law['Good'], Writer['medium'])

Writer_rule_7 = ctrl.Rule(English['Average'] & Literature['Average'] & History['Average'], Writer['low'])
Writer_rule_8 = ctrl.Rule(English['Average'] & Literature['Average'] & Civic_Education['Average'], Writer['low'])
Writer_rule_9 = ctrl.Rule(English['Average'] & Literature['Average'] & Law['Average'], Writer['low'])
