# -*- coding: utf-8 -*-
"""
Système de Gestion Clinique Dentaire (Prototype)
Auteur: [Votre Nom Prénom] - Dentiste & Programmeur Informatique
Description: Un prototype pour la gestion des patients, du schéma dentaire et des ordonnances.
"""

class Patient:
    def __init__(self, patient_id, nom, age):
        self.patient_id = patient_id
        self.nom = nom
        self.age = age
        self.schema_dentaire = {}  # Ex: {16: "Carie - Composite Nécessaire", 46: "Endodontie Terminée"}
        self.ordonnances = []

    def ajouter_traitement(self, numero_dent, statut):
        """Ajoute un diagnostic ou un traitement selon le système de numérotation FDI (11-48)"""
        if 11 <= numero_dent <= 48:
            self.schema_dentaire[numero_dent] = statut
            print(f"[SUCCÈS] Traitement ajouté pour le patient {self.nom} (Dent {numero_dent}): {statut}")
        else:
            print("[ERREUR] Numéro de dent invalide ! Veuillez utiliser le système de notation FDI.")

    def creer_ordonnance(self, medicaments):
        """Génère une ordonnance médicale pour le patient"""
        self.ordonnances.append(medicaments)
        print(f"[SUCCÈS] Ordonnance créée pour {self.nom}: {', '.join(medicaments)}")

    def afficher_dossier_medical(self):
        """Affiche l'historique médical complet du patient sur la console"""
        print(f"\n--- DOSSIER MÉDICAL: {self.nom} (ID: {self.patient_id}, Âge: {self.age} ans) ---")
        print("Schéma Dentaire et Statuts Cliniques:")
        if not self.schema_dentaire:
            print("  - Aucun traitement enregistré.")
        for dent, statut in self.schema_dentaire.items():
            print(f"  * Dent N° {dent}: {statut}")
        
        print("Historique des Ordonnances:")
        if not self.ordonnances:
            print("  - Aucune ordonnance émise.")
        for idx, ordonnance in enumerate(self.ordonnances, 1):
            print(f"  * Ordonnance {idx}: {', '.join(ordonnance)}")
        print("-" * 60)


# --- SIMULATION ET TEST DU SYSTÈME ---
if __name__ == "__main__":
    print("Démarrage du Logiciel de Gestion Dentaire...\n")
    
    # 1. Création d'un nouveau patient (En utilisant vos compétences cliniques)
    patient1 = Patient(patient_id="P101", nom="Jean Dupont", age=34)
    
    # 2. Enregistrement des diagnostics et traitements (Simulation clinique)
    # Utilisation des termes médicaux français (Carie, Composite, Lésion périapicale)
    patient1.ajouter_traitement(16, "Carie occlusale - Restauration composite effectuée")
    patient1.ajouter_traitement(46, "Lésion périapicale - Traitement endodontique requis")
    
    # 3. Prescription de médicaments dentaires
    patient1.creer_ordonnance(["Amoxicilline 500mg", "Paracétamol 1g"])
    
    # 4. Génération du rapport médical complet
    patient1.afficher_dossier_medical()
