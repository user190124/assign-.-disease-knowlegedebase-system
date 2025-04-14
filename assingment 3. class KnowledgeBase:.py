class KnowledgeBase:
def __init__(self):  # Fixed double underscores
	self.diseases = {
		"Common Cold": {"symptoms": ["sneezing", "runny_nose"], "treatment": "rest and fluids", "severity": "low"},
		"Flu": {"symptoms": ["fever", "cough", "body_aches"], "treatment": "rest and fluids", "severity": "medium"},
		"Pneumonia": {"symptoms": ["fever", "cough", "shortness_of_breath"], "treatment": "antibiotics", "severity": "high"},
		"Tuberculosis": {"symptoms": ["cough", "weight_loss", "night_sweats"], "treatment": "antibiotics", "severity": "high"},
		"Covid19": {"symptoms": ["fever", "cough", "shortness_of_breath"], "treatment": "antivirus", "severity": "high"},
		"Malaria": {"symptoms": ["fever", "headache", "vomiting"], "treatment": "antimalaria", "severity": "medium"}
	}
	# Fixed relationships structure (symptom -> diseases)
	# Map symptoms to the diseases they are associated with
	self.relationships = {
		"sneezing": ["Common Cold"],
		"runny_nose": ["Common Cold"],
		"fever": ["Flu", "Pneumonia", "Covid19", "Malaria"],
		"cough": ["Flu", "Pneumonia", "Tuberculosis", "Covid19"],
		"body_aches": ["Flu"],
		"shortness_of_breath": ["Pneumonia", "Covid19"],
		"weight_loss": ["Tuberculosis"],
		"night_sweats": ["Tuberculosis"],
		"headache": ["Malaria"],
		"vomiting": ["Malaria"]
	}
	# Initialize an empty list to track patient history
	self.patient_history = []
def get_disease(self, symptoms, duration):
	possible = {}
	for symptom in symptoms:
		# Get diseases associated with each symptom
		for disease in self.relationships.get(symptom, []):
			possible[disease] = possible.get(disease, 0) + 1

	# Verify all required symptoms are present
	matches = []
	for disease, count in possible.items():
		required_symptoms = self.diseases[disease]["symptoms"]
		# Check count matches AND all symptoms present
		if any(s in symptoms for s in required_symptoms):
			# Calculate the probability of the disease based on the number of matching symptoms
			probability = count / len(required_symptoms)
			matches.append((disease, probability))
	# Sort the matches by probability in descending order
	matches.sort(key=lambda x: x[1], reverse=True)
	return matches
def add_patient_history(self, symptoms, diagnosis):
	# Add the symptoms and diagnosis to the patient's history
	self.patient_history.append({"symptoms": symptoms, "diagnosis": diagnosis})

# Create instance
kb = KnowledgeBase()
print("Medical Diagnosis System")
print("Available symptoms:", ", ".join(kb.relationships.keys()))
print("\nEnter the symptoms you have (comma-separated):")
# Get and clean input
user_input = input("> ").lower().replace(" ", "_").split(',')
symptoms = [s.strip() for s in user_input]
print("\nEnter the duration of symptoms in days:")
duration = int(input("> ").strip())
# Get possible diagnoses based on symptoms and duration
diagnoses = kb.get_disease(symptoms, duration)
if diagnoses:
	print("\nPossible diagnoses:")
	for disease, probability in diagnoses:
		# Print the possible diagnoses with their treatments, probabilities, and severity levels
		print(f"- {disease}: {kb.diseases[disease]['treatment']} (Probability: {probability:.2f}, Severity: {kb.diseases[disease]['severity']})")  # Fixed f-string syntax
		# Add the symptoms and diagnosis to the patient's history
		kb.add_patient_history(symptoms, disease)
else:
	print("\nNo matching diagnoses found") 

	# Add the symptoms and "No diagnosis" to the patient's history
	kb.add_patient_history(symptoms, "No diagnosis")
 
NOTE:
- `key=lambda x: x[1]` specifies a key function that extracts the second element of each tuple (`x[1]`) to use for sorting. - `reverse=True` sorts the list in descending order (highest probability first).