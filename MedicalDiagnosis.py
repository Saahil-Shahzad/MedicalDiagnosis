# Group Members:
# Hafiz Abdul Basit 472617
# Saahil Shahzad    469370
# Ahmed Mabood      467173


import customtkinter as ctk
from tkinter import messagebox

# Define disease probabilities function
def Diseases():
    return {
        "influenza": 0.127,  # A viral infection causing fever, cough, and fatigue
        "commoncold": 0.191,  # A viral infection causing a runny nose, sore throat, and sneezing
        "covid19": 0.013,  # A contagious respiratory disease caused by the SARS-CoV-2 virus
        "pneumonia": 0.006,  # An infection causing inflammation in the lungs, leading to cough and chest pain
        "tuberculosis": 0.003,  # A bacterial infection primarily affecting the lungs, leading to coughing and weight loss
        "asthma": 0.051,  # A chronic condition causing difficulty breathing due to narrowed airways
        "diabetes": 0.108,  # A metabolic disease characterized by high blood sugar levels
        "migraine": 0.152,  # A headache disorder often accompanied by nausea and sensitivity to light
        "mononucleosis": 0.025,  # A viral infection causing fever, sore throat, and swollen lymph nodes
        "allergicrhinitis": 0.254,  # An allergic reaction to airborne particles leading to a runny nose and sneezing
    }

# Define symptom probabilities function
def Symptoms():
    return {
        "fever": 0.091,  # Elevated body temperature often indicating an infection
        "cough": 0.085,  # A reflex action to clear the airways of irritants
        "fatigue": 0.079,  # A feeling of physical and mental exhaustion
        "headache": 0.068,  # Pain in the head, often due to tension, illness, or stress
        "sorethroat": 0.057,  # Inflammation of the throat causing pain or irritation
        "shortnessofbreath": 0.045,  # Difficulty in breathing or catching one's breath
        "runnynose": 0.062,  # Excess mucus production in the nasal passages
        "congestion": 0.057,  # Blockage or obstruction in the nasal passages
        "chestpain": 0.034,  # Discomfort or pain in the chest area
        "nausea": 0.040,  # A feeling of the need to vomit
        "lossoftaste": 0.023,  # A condition where the sense of taste is diminished or lost
        "nightsweats": 0.045,  # Excessive sweating at night, often due to an underlying condition
        "weightloss": 0.057,  # Unexplained loss of body weight
        "sneezing": 0.068,  # Sudden, involuntary expulsion of air from the nose and mouth
        "itchyeyes": 0.051,  # Irritation of the eyes causing a sensation of itching
        "vomiting": 0.045,  # The forceful expulsion of stomach contents through the mouth
        "sensitivitytolight": 0.057,  # A condition where the eyes become overly sensitive to light
    }

# Define conditional probabilities of symptoms given diseases function
def Symptoms_Given_diseases():
    return {
        "influenza": {"fever": 0.250, "cough": 0.200, "fatigue": 0.230, "headache": 0.170, "sorethroat": 0.150},  # Influenza symptoms
        "commoncold": {"fever": 0.160, "cough": 0.200, "fatigue": 0.180, "runnynose": 0.260, "sorethroat": 0.200},  # Cold symptoms
        "covid19": {"fever": 0.220, "cough": 0.210, "fatigue": 0.220, "lossoftaste": 0.180, "shortnessofbreath": 0.170},  # COVID-19 symptoms
        "pneumonia": {"fever": 0.240, "cough": 0.220, "fatigue": 0.200, "chestpain": 0.200, "shortnessofbreath": 0.140},  # Pneumonia symptoms
        "tuberculosis": {"fever": 0.230, "cough": 0.240, "fatigue": 0.210, "nightsweats": 0.190, "weightloss": 0.130},  # Tuberculosis symptoms
        "asthma": {"cough": 0.250, "shortnessofbreath": 0.270, "fatigue": 0.200, "chestpain": 0.150, "runnynose": 0.130},  # Asthma symptoms
        "diabetes": {"fatigue": 0.360, "fever": 0.140, "weightloss": 0.250, "sorethroat": 0.130, "nausea": 0.120},  # Diabetes symptoms
        "migraine": {"headache": 0.280, "nausea": 0.220, "fatigue": 0.180, "sensitivitytolight": 0.200, "vomiting": 0.120},  # Migraine symptoms
        "mononucleosis": {"fever": 0.240, "fatigue": 0.260, "sorethroat": 0.220, "headache": 0.160, "nausea": 0.120},  # Mononucleosis symptoms
        "allergicrhinitis": {"runnynose": 0.250, "sneezing": 0.270, "congestion": 0.220, "itchyeyes": 0.150, "fatigue": 0.110},  # Allergic rhinitis symptoms
    }

# Function to calculate disease probabilities based on input symptoms
def Calculate_Probabilities(input_symptoms):
    all_diseases = Diseases()
    disease_probabilities = {}

    for disease in all_diseases:
        final_prob = 1  # Initialize the final probability for the disease
        disease_probability = all_diseases[disease]
        
        for symptom in input_symptoms:
            all_symptoms = Symptoms()
            # Get the symptom probability
            if symptom in all_symptoms:
                symptom_probability = all_symptoms[symptom]
            symptoms_given_disease = Symptoms_Given_diseases()
            # Get the conditional probability of the symptom given the disease
            if symptom in symptoms_given_disease[disease]:
                symptoms_given_disease_probability = symptoms_given_disease[disease][symptom]
            else:
                symptoms_given_disease_probability = 0.001  # Handle missing symptom for disease
            
            # Calculate the probability of disease given symptoms using Bayes' theorem
            probability_disease_given_symptoms = (symptoms_given_disease_probability * disease_probability) / symptom_probability
            final_prob *= probability_disease_given_symptoms
        
        # Store the calculated probability for the disease
        disease_probabilities[disease] = final_prob

    # Normalize the probabilities so they sum up to 100%
    total_prob = sum(disease_probabilities.values())
    normalized_probabilities = {}
    for disease, prob in disease_probabilities.items():
        normalized_probabilities[disease] = (prob / total_prob) * 100

    # Find the most likely disease
    max_disease = max(normalized_probabilities, key=normalized_probabilities.get)
    max_probability = normalized_probabilities[max_disease]

    return normalized_probabilities, max_disease, max_probability

# GUI Application Class for Expert Diagnosis System
class ExpertDiagnosisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Diagnosis Expert System")
        self.root.geometry("1200x800")
        
        # Set appearance mode for the UI
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Container frame to hold the UI components
        self.container = ctk.CTkFrame(self.root, corner_radius=20, fg_color="white")
        self.container.pack(pady=30, padx=30, fill="both", expand=True)

        # Input Screen Setup
        self.screen1 = ctk.CTkFrame(self.container, corner_radius=0, fg_color="lightblue")
        self.screen1.pack(fill="both", expand=True)

        # Title label for the input screen
        self.title_label = ctk.CTkLabel(self.screen1, text="Enter Symptoms", font=("Helvetica", 50, "bold"), anchor="center", text_color="darkblue")
        self.title_label.pack(pady=30)

        # Frame for symptom input dropdowns
        self.input_frame = ctk.CTkFrame(self.screen1, corner_radius=20, fg_color="lightgreen")
        self.input_frame.pack(pady=30, padx=30)

        # List to hold the symptom dropdowns for user input
        self.symptom_dropdowns = []
        self.symptom_keys = [""]+list(Symptoms().keys())  # Symptom options for dropdowns
        for i in range(5):
            label = ctk.CTkLabel(self.input_frame, text=f"Symptom {i+1}: ", font=("Helvetica", 20), text_color="black")
            label.grid(row=i, column=0, padx=20, pady=20, sticky="w")
            dropdown = ctk.CTkOptionMenu(self.input_frame, values=self.symptom_keys, font=("Helvetica", 20), width=400, corner_radius=15)
            dropdown.grid(row=i, column=1, padx=20, pady=20)
            self.symptom_dropdowns.append(dropdown)

        # Button to trigger the calculation of probabilities
        self.calc_button = ctk.CTkButton(self.screen1, text="Calculate Probabilities", command=self.show_results, font=("Helvetica", 20), corner_radius=15, width=300, height=50, fg_color="green", hover_color="darkgreen")
        self.calc_button.pack(pady=30)

    # Method to display the results after calculations
    def show_results(self):
        input_symptoms = []
        for dropdown in self.symptom_dropdowns:
            symptom = dropdown.get().strip().lower().replace(" ", "")
            if symptom:
                input_symptoms.append(symptom)

        # Check if at least one symptom is selected
        if not input_symptoms:
            messagebox.showwarning("Input Error", "Please select at least one symptom.")
            return

        # Calculate disease probabilities based on selected symptoms
        normalized_probabilities, max_disease, max_probability = Calculate_Probabilities(input_symptoms)

        # Switch to results screen
        self.screen1.pack_forget()
        self.screen2 = ctk.CTkFrame(self.container, corner_radius=20)
        self.screen2.pack(fill="both", expand=True)

        # Title Label for Results
        self.title_label = ctk.CTkLabel(
            self.screen2, 
            text="Diagnosis Results", 
            font=("Helvetica", 40, "bold"), 
            anchor="center"
        )
        self.title_label.pack(pady=20)

        # Scrollable frame for displaying disease probabilities
        self.scrollable_frame = ctk.CTkScrollableFrame(self.screen2, width=1000, height=300, corner_radius=20)
        self.scrollable_frame.pack(pady=20, padx=20)

        # Display each disease with its probability
        for disease, prob in normalized_probabilities.items():
            disease_frame = ctk.CTkFrame(self.scrollable_frame, corner_radius=15)
            disease_frame.pack(pady=10, padx=10, fill="x")

            label = ctk.CTkLabel(
                disease_frame, 
                text=f"{disease.capitalize()}: {round(prob, 2)}%", 
                font=("Helvetica", 20)
            )
            label.pack(side="left", padx=20, pady=10)

            # Display progress bar indicating probability
            progress_bar = ctk.CTkProgressBar(disease_frame, width=300)
            progress_bar.set(prob / 100)
            progress_bar.pack(side="right", padx=20, pady=10)

        # Highlight the most likely disease
        highlight_frame = ctk.CTkFrame(self.screen2, corner_radius=20)
        highlight_frame.pack(pady=20, padx=20, fill="x")

        highlight_label = ctk.CTkLabel(
            highlight_frame, 
            text=f"Most Likely Disease: {max_disease.capitalize()} ({round(max_probability, 2)}%)", 
            font=("Helvetica", 30, "bold"), 
            text_color="red"
        )
        highlight_label.pack(pady=10)

        # Back button to return to the input screen
        self.back_button = ctk.CTkButton(
            self.screen2, 
            text="Back to Input", 
            command=self.back_to_input, 
            font=("Helvetica", 20), 
            corner_radius=15, 
            width=200, 
            height=50
        )
        self.back_button.pack(pady=30)

    # Method to return to the input screen
    def back_to_input(self):
        self.screen2.pack_forget()
        self.screen1.pack(fill="both", expand=True)

# Main entry point
if __name__ == "__main__":
    root = ctk.CTk()
    app = ExpertDiagnosisApp(root)
    root.mainloop()
