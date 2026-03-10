skills_list = [
"python",
"java",
"c++",
"html",
"css",
"javascript",
"sql",
"mysql",
"wordpress",
"cloud computing",
"data structure",
"oop",
"flask",
"django",
"machine learning"
]


def extract_skills(text):

    found_skills = []
    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def missing_skills(found):
    return list(set(skills_list) - set(found))


def resume_score(found):

    score = (len(found) / len(skills_list)) * 100
    return round(score,2)

def predict_role(skills):

    roles = {
        "Data Scientist": ["python", "machine learning", "pandas", "numpy", "sql"],
        "Web Developer": ["html", "css", "javascript"],
        "Backend Developer": ["python", "flask", "django", "mysql"],
        "Software Developer": ["java", "c++", "data structure", "oop"],
        "Cloud Engineer": ["cloud computing", "aws"]
    }

    best_role = "Software Developer"
    max_match = 0

    for role, role_skills in roles.items():

        match = len(set(skills) & set(role_skills))

        if match > max_match:
            max_match = match
            best_role = role

    return best_role