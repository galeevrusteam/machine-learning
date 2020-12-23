import pandas as pd
import numpy as np


def get_disease_possibilities(disease_data):
    patient_count = disease_data['Количество']
    sum_patient_count = patient_count[len(patient_count) - 1]
    possibilities = []
    for i in range(0, len(disease_data) - 1):
        possibilities.append(patient_count[i] / sum_patient_count)
    return possibilities


def get_possibilities_by_symptoms(test_symptoms, symptom_data, disease_possibilities):
    possibilities_by_symptoms = [None] * (len(disease_possibilities))
    for i in range(len(disease_possibilities)):
        possibilities_by_symptoms[i] = disease_possibilities[i]
        for j in range(len(symptom_data) - 1):
            if test_symptoms[j] == 1:
                possibility_str = symptom_data.iloc[j][i + 1]
                possibilities_by_symptoms[i] *= float(possibility_str.replace(',', '.'))
    return possibilities_by_symptoms


def get_disease(disease_data, symptom_data, test_symptoms):
    diseases = disease_data['Болезнь']
    disease_possibilities = get_disease_possibilities(disease_data)
    possibilities_by_symptoms = get_possibilities_by_symptoms(test_symptoms, symptom_data, disease_possibilities)
    return diseases[possibilities_by_symptoms.index(max(possibilities_by_symptoms))]


symptom_data = pd.read_csv('./symptom.csv', delimiter=';')
disease_data = pd.read_csv('./disease.csv', delimiter=';')
# the last string in disease.csv is sum
test_symptoms = [np.random.randint(0, 2) for i in range(len(symptom_data) - 1)]
print(test_symptoms)
disease = get_disease(disease_data, symptom_data, test_symptoms)
print(disease)
