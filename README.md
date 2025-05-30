👥 Collaboration:
- Ce projet a été réalisé dans le cadre d’un mini-projet universitaire portant sur les technologies sémantiques, en collaboration avec mon collègue Mohamed Amine Salhi.
Nous avons travaillé ensemble sur toutes les étapes : la modélisation de l’ontologie, l’ajout des règles SWRL, l'exécution des requêtes SPARQL, la visualisation du graphe, et le développement des scripts Python d’exploitation.

- Ce travail collaboratif nous a permis de mieux comprendre les concepts du Web sémantique appliqués à un domaine concret et riche : l’éducation dans le domaine de l’ingénierie des données.
# 🧠 Ontologie du domaine Éducation – Data Engineering

Ce projet présente une ontologie pour le domaine de l'éducation, avec un focus spécifique sur le **Data Engineering** (ingénierie des données).

## 📋 Table des matières
- [🎯 Domaine choisi](#-domaine-choisi)
- [✅ Justification du choix](#-justification-du-choix)
- [🧠 Concepts clés identifiés](#-concepts-clés-identifiés)
  - [🔷 Classes principales](#-classes-principales)
  - [🔸 Sous-classes](#-sous-classes-proposées)
- [🔗 Relations entre les concepts](#-relations-entre-les-concepts-propriétés)
- [🌐 Namespaces utilisés](#-namespaces-utilisés)
- [🖼️ Visualisation de l'ontologie](#-visualisation-de-lontologie)
- [📊 Requêtes SPARQL](#-requêtes-sparql-exécutées-avec-résultats)
- [📘 Axiomes OWL](#-axiomes-owl-utilisés-dans-lontologie)
- [🧮 Règles SWRL](#-règles-swrl-implémentées)
- [📝 Propriétés de données](#-propriétés-de-données)
- [🔄 Structure de l'ontologie](#-structure-de-lontologie)
- [💻 Scripts Python d'exploitation](#-scripts-python-dexploitation)

## 🎯 Domaine choisi

Le domaine choisi pour ce projet est celui de **l'éducation**, avec un focus spécifique sur le **Data Engineering** (ou ingénierie des données). Il s'agit d'un sous-domaine des sciences informatiques qui forme des étudiants aux compétences en manipulation, traitement, stockage et analyse de grandes quantités de données.

## ✅ Justification du choix

Le choix du domaine **Éducation – Data Engineering** s'explique par plusieurs raisons :

- 🎓 **Alignement académique** : Le sujet est en cohérence avec notre formation actuelle en informatique, ce qui facilite la compréhension des concepts à modéliser.
- 📊 **Richesse conceptuelle** : Le domaine permet de relier des entités variées (cours, compétences, enseignants, projets, technologies, etc.) tout en ayant une structure logique exploitable en ontologie.
- 🧠 **Utilité pédagogique** : Une telle ontologie pourrait servir à :
  - recommander des parcours d'apprentissage adaptés aux compétences acquises,
  - structurer des ressources pédagogiques selon leur type, difficulté ou technologie utilisée,
  - suivre l'évolution des apprenants et leurs progrès dans l'acquisition de compétences en Data Engineering.

## 🧠 Concepts clés identifiés

### 🔷 **Classes principales**

| Classe            | Description                                              |
|-------------------|----------------------------------------------------------|
| `Learner`         | Représente un apprenant inscrit dans un programme.       |
| `Instructor`      | Personne responsable d'un cours ou module.              |
| `Course`          | Unité d'enseignement regroupant plusieurs modules.      |
| `Module`          | Partie spécifique d'un cours (ex: Python, Hadoop…).      |
| `Skill`           | Compétence technique ou théorique à acquérir.           |
| `Assessment`      | Évaluation liée à une compétence ou un cours.           |
| `LearningResource`| Ressource pédagogique (vidéo, document, lien, etc.).    |
| `Project`         | Cas pratique ou projet développé par un apprenant.      |
| `Technology`      | Outil, framework ou langage utilisé dans les cours.     |

### 🔸 **Sous-classes proposées**

| Sous-classe        | Super-classe   | Description                                      |
|--------------------|----------------|--------------------------------------------------|
| `BigDataModule`    | `Module`       | Modules axés sur les frameworks Big Data (Hadoop, Spark…) |
| `ProgrammingModule`| `Module`       | Modules de programmation (Python, Scala, etc.)  |
| `Quiz`             | `Assessment`   | Évaluations rapides de type QCM.                |
| `Exam`             | `Assessment`   | Épreuves longues et formelles.                  |
| `PracticalProject` | `Project`      | Projets appliqués à des cas réels ou simulés.   |

## 🔗 Relations entre les concepts (propriétés)

Voici les principales relations définies entre les classes de l'ontologie :

| Propriété          | Domaine → Portée            | Description                                                      |
|--------------------|-----------------------------|------------------------------------------------------------------|
| `teaches`          | `Instructor → Course`        | L'enseignant donne un cours                                      |
| `enrolledIn`       | `Learner → Course`           | L'apprenant est inscrit à un cours                               |
| `includesModule`   | `Course → Module`            | Le cours est composé de plusieurs modules                        |
| `coversSkill`      | `Module → Skill`             | Le module enseigne une ou plusieurs compétences                  |
| `assesses`         | `Assessment → Skill`         | L'évaluation mesure une compétence particulière                  |
| `achievedSkill`    | `Learner → Skill`            | Compétence acquise par l'apprenant                               |
| `producesProject`  | `Learner → Project`          | L'apprenant réalise un projet                                    |
| `usesTechnology`   | `Project → Technology`       | Le projet utilise des technologies spécifiques                   |
| `hasResource`      | `Module → LearningResource`  | Le module est accompagné de ressources pédagogiques              |
| `followsModule`    | `Learner → Module`           | L'apprenant suit un module spécifique                            |
| `isTaughtBy`       | `Learner → Instructor`       | L'apprenant est enseigné par un instructeur                      |
| `isEnrolledBy`     | `Course → Learner`           | Le cours a des apprenants inscrits (inverse de `enrolledIn`)     |

## 🌐 Namespaces utilisés

Afin d'assurer la compatibilité avec les standards du Web sémantique, les namespaces suivants sont utilisés dans notre ontologie :

| Préfixe | URI | Utilisation prévue |
|--------|-----|--------------------|
| `rdf:` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` | Syntaxe RDF de base |
| `rdfs:` | `http://www.w3.org/2000/01/rdf-schema#` | Définition de classes et propriétés |
| `xsd:` | `http://www.w3.org/2001/XMLSchema#` | Types de données (string, int, date...) |
| `owl:` | `http://www.w3.org/2002/07/owl#` | Modélisation OWL pour classes, restrictions |
| `foaf:` | `http://xmlns.com/foaf/0.1/` | Pour les personnes (`Learner`, `Instructor`) |
| `dc:` | `http://purl.org/dc/elements/1.1/` | Métadonnées (titre, créateur, date…) |
| `skos:` | `http://www.w3.org/2004/02/skos/core#` | Vocabulaire hiérarchique ou thématique |

## 🖼️ Visualisation de l'ontologie
![Visualisation](img/graph.png)
![Visualisation](img/graph2.png)

## 📊 Requêtes SPARQL exécutées avec résultats

### 🔁 Préfixes utilisés dans toutes les requêtes :
```sparql
PREFIX : <http://www.education-ontology.org/education-data-engineering#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
```

### ✅ Requête 1 – Apprenants, leurs projets et les technologies utilisées
```sparql
SELECT ?learner ?project ?technology
WHERE {
  ?learner rdf:type :Learner .
  ?learner :producesProject ?project .
  ?project :usesTechnology ?technology .
}
```
| learner | project               | technology |
| ------- | --------------------- | ---------- |
| Nour    | ML Project            | Python     |
| Oussema | Data Analysis Project | Python     |

### ✅ Requête 2 – Modules, compétences couvertes et ressources pédagogiques
```sparql
SELECT ?module ?skill ?resource
WHERE {
  ?module :coversSkill ?skill .
  ?module :hasResource ?resource .
  ?module rdf:type :ProgrammingModule .
}
```
| module         | skill         | resource             |
|----------------|---------------|----------------------|
| Python Module  | Python Basics | Intro to Python PDF  |

### ✅ Requête 3 – Enseignants, cours enseignés, modules inclus
```sparql
SELECT ?instructor ?course ?module
WHERE {
  ?instructor :teaches ?course .
  ?course :includesModule ?module .
  ?instructor rdf:type :Instructor .
}
```
| instructor   | course                 | module         |
|--------------|------------------------|----------------|
| MrBenSalah   | Data Engineering Course | Spark Module   |
| MrBenSalah   | Data Engineering Course | Python Module  |

### ✅ Requête 4 – Apprenants, cours suivis, modules associés
```sparql
SELECT ?learner ?course ?module
WHERE {
  ?learner :enrolledIn ?course .
  ?course :includesModule ?module .
  ?learner rdf:type :Learner .
}
```
| learner | course                  | module                  |
| ------- | ----------------------- | ----------------------- |
| Salma   | AI Course               | Machine Learning Module |
| Oussema | Data Engineering Course | Spark Module            |
| Oussema | Data Engineering Course | Python Module           |

## 📘 Axiomes OWL utilisés dans l'ontologie

### ✅ 1. Équivalences de classes (`owl:equivalentClass`)

🔸 **PythonLearner ≡ Learner ⊓ (achievedSkill value PythonBasics)**  
Cela signifie que tout `PythonLearner` est un `Learner` ayant acquis la compétence `PythonBasics`.

```owl
PythonLearner ≡ Learner ⊓ (achievedSkill value PythonBasics)
```

🔸 **Exam ≡ Assessment ⊓ LearningResource**  
Tout `Exam` est à la fois une évaluation et une ressource pédagogique.

```owl
Exam ≡ Assessment ⊓ LearningResource
```

### ✅ 2. Disjonctions (`owl:disjointWith`)

🔸 **Instructor ⊓ Learner ≡ ⊥**  
Aucun individu ne peut être à la fois `Instructor` et `Learner`.

```owl
Instructor ⊓ Learner ≡ ⊥
```

🔸 **DisjointClasses(Course, Module, Project)**  
`Course`, `Module` et `Project` sont des concepts bien distincts sans chevauchement.

```owl
DisjointClasses(Course, Module, Project)
```

### ✅ 3. Restriction de cardinalité (`owl:minQualifiedCardinality`)

🔸 **Module ⊆ (≥1 coversSkill.Skill)**  
Tout `Module` doit couvrir **au moins une compétence**.

```owl
Module ⊆ (≥1 coversSkill.Skill)
```

### ✅ 4. Propriétés inverses (`owl:inverseOf`)

🔸 `enrolledIn` ⟷ `isEnrolledBy`  
🔸 `teaches` ⟷ `isTaughtBy`

```owl
inverseOf(enrolledIn, isEnrolledBy)
inverseOf(teaches, isTaughtBy)
```

## 🧮 Règles SWRL implémentées

### 🔹 Règle S1 – Un apprenant suit un module inclus dans un cours auquel il est inscrit
```swrl
Learner(?l) ^ enrolledIn(?l, ?c) ^ includesModule(?c, ?m) -> followsModule(?l, ?m)
```

### 🔹 Règle S2 – Si un apprenant crée un projet utilisant une technologie, alors il a acquis cette compétence
```swrl
producesProject(?l, ?p) ^ usesTechnology(?p, ?t) -> achievedSkill(?l, ?t)
```

### 🔹 Règle S3 – Si un cours inclut un module qui couvre une compétence, alors le cours couvre aussi cette compétence
```swrl
includesModule(?c, ?m) ^ coversSkill(?m, ?s) -> coversSkill(?c, ?s)
```

### 🔹 Règle S4 – Si un instructeur enseigne un cours et un apprenant est inscrit à ce cours, alors cet apprenant est enseigné par cet instructeur
```swrl
enrolledIn(?l, ?c) ^ teaches(?i, ?c) -> isTaughtBy(?l, ?i)
```

## 📝 Propriétés de données

L'ontologie inclut également des propriétés de données pour enrichir les descriptions des individus :

| Propriété      | Domaine    | Portée     | Description                        |
|----------------|------------|------------|------------------------------------|
| `hasDeadline`  | `Project`  | `xsd:date` | Date limite pour rendre un projet  |

## 🔄 Structure de l'ontologie

### 📚 Classes et hiérarchie
- L'ontologie comporte 9 classes principales avec différentes sous-classes
- Des relations de subsomption (hiérarchie) sont définies entre les classes

### 🔍 Individus
L'ontologie inclut plusieurs individus, notamment :
- Apprenants : Salma, Nour, Oussema
- Instructeurs : MrBenSalah
- Cours : Data Engineering Course, AI Course
- Modules : Python Module, Spark Module, Module ML
- Projets : ML Project, Data Analysis Project
- Technologies : Python
- Compétences : Python Basics, ML Basics
- Ressources : Intro to Python PDF, Machine Learning Book

### 🧩 Annotations
Des annotations sont utilisées pour :
- Documenter les classes et propriétés
- Ajouter des labels multilingues
- Fournir des métadonnées sur l'ontologie elle-même (créateur, version, etc.)

## 💻 Scripts Python d'exploitation

Pour exploiter pleinement notre ontologie, nous avons développé deux scripts Python utilisant la bibliothèque RDFlib :

### 📊 Script 1 : Génération de CV académiques

Ce script extrait les informations relatives à chaque apprenant pour générer des "CV académiques" structurés et les exporte dans un fichier Excel pour une consultation facile.

```python
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
```

### 🔍 Script 2 : Exécution de requêtes SPARQL

Ce script exécute les quatre requêtes SPARQL présentées dans la documentation et affiche les résultats de manière claire et formattée.

```python
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
```

Ces scripts démontrent la puissance pratique de notre ontologie pour extraire des informations pertinentes sur les parcours d'apprentissage et les relations entre les différentes entités du domaine éducatif.