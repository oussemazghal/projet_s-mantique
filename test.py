from rdflib import Graph, Namespace, RDF

# Fonction pour extraire le nom local depuis un URI
def local_name(uri):
    return uri.split("#")[-1]

# Chargement du graphe RDF
g = Graph()
g.parse(r"C:\Users\pc\Desktop\projet semantique\ontology\dddd.rdf", format="xml")

# Namespace
EDU = Namespace("http://www.education-ontology.org/education-data-engineering#")

# ✅ Requête 1
print("✅ Requête 1 – Apprenants, leurs projets et les technologies utilisées")
query1 = """
PREFIX : <http://www.education-ontology.org/education-data-engineering#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?learner ?project ?technology
WHERE {
  ?learner rdf:type :Learner .
  ?learner :producesProject ?project .
  ?project :usesTechnology ?technology .
}
"""
for row in g.query(query1):
    print(f"Learner: {local_name(row.learner)}, Project: {local_name(row.project)}, Technology: {local_name(row.technology)}")

# ✅ Requête 2
print("\n✅ Requête 2 – Modules, compétences couvertes et ressources pédagogiques")
query2 = """
PREFIX : <http://www.education-ontology.org/education-data-engineering#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?module ?skill ?resource
WHERE {
  ?module rdf:type :ProgrammingModule .
  ?module :coversSkill ?skill .
  ?module :hasResource ?resource .
}
"""
for row in g.query(query2):
    print(f"Module: {local_name(row.module)}, Skill: {local_name(row.skill)}, Resource: {local_name(row.resource)}")

# ✅ Requête 3
print("\n✅ Requête 3 – Enseignants, cours enseignés, modules inclus")
query3 = """
PREFIX : <http://www.education-ontology.org/education-data-engineering#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?instructor ?course ?module
WHERE {
  ?instructor rdf:type :Instructor .
  ?instructor :teaches ?course .
  ?course :includesModule ?module .
}
"""
for row in g.query(query3):
    print(f"Instructor: {local_name(row.instructor)}, Course: {local_name(row.course)}, Module: {local_name(row.module)}")

# ✅ Requête 4
print("\n✅ Requête 4 – Apprenants, cours suivis, modules associés")
query4 = """
PREFIX : <http://www.education-ontology.org/education-data-engineering#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?learner ?course ?module
WHERE {
  ?learner rdf:type :Learner .
  ?learner :enrolledIn ?course .
  ?course :includesModule ?module .
}
"""
for row in g.query(query4):
    print(f"Learner: {local_name(row.learner)}, Course: {local_name(row.course)}, Module: {local_name(row.module)}")
