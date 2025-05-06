from rdflib import Graph, Namespace, RDF, RDFS
import pandas as pd

# Chargement du graphe RDF
g = Graph()
g.parse(r"C:\Users\pc\Desktop\projet semantique\ontology\dddd.rdf", format="xml")

# Définition du namespace
EDU = Namespace("http://www.education-ontology.org/education-data-engineering#")

# Données à stocker dans Excel
rows = []

# Récupération de tous les apprenants
learners = g.subjects(RDF.type, EDU.Learner)

for learner in learners:
    name = g.value(subject=learner, predicate=RDFS.label)
    if not name:
        name = learner.split("#")[-1]

    print(f"\n🧑‍🎓 CV Académique de {name}")
    print("=" * 40)

    # Cours suivis
    print("\n🎓 Cours Suivis :")
    courses = []
    for _, _, course in g.triples((learner, EDU.enrolledIn, None)):
        course_label = g.value(subject=course, predicate=RDFS.label)
        courses.append(str(course_label or course.split('#')[-1]))
    if not courses:
        print(" Aucun cours trouvé.")
    else:
        for c in courses:
            print(f" - {c}")

    # Projets réalisés
    print("\n💼 Projets Réalisés :")
    projects = []
    for _, _, project in g.triples((learner, EDU.producesProject, None)):
        proj_label = g.value(subject=project, predicate=RDFS.label)
        proj_tech = g.value(subject=project, predicate=EDU.usesTechnology)
        tech_label = proj_tech.split("#")[-1] if proj_tech else "Inconnue"
        projects.append(f"{proj_label or project.split('#')[-1]} (Tech: {tech_label})")
    if not projects:
        print(" Aucun projet trouvé.")
    else:
        for p in projects:
            print(f" - {p}")

    # Compétences acquises
    print("\n🧠 Compétences Acquises :")
    skills = []
    for _, _, skill in g.triples((learner, EDU.achievedSkill, None)):
        skills.append(skill.split('#')[-1])
    if not skills:
        print(" Aucune compétence trouvée.")
    else:
        for s in skills:
            print(f" - {s}")

    # Ajout au tableau
    rows.append({
        "Nom Apprenant": name,
        "Cours Suivis": ", ".join(courses) if courses else "Aucun",
        "Projets Réalisés": ", ".join(projects) if projects else "Aucun",
        "Compétences Acquises": ", ".join(skills) if skills else "Aucune"
    })

# Création du DataFrame
df = pd.DataFrame(rows)

# Enregistrement dans un fichier Excel
output_path = r"C:\Users\pc\Desktop\projet semantique\ontology\cvs_apprenants.xlsx"
df.to_excel(output_path, index=False, engine='openpyxl')

print(f"\n✅ CVs exportés avec succès dans : {output_path}")
