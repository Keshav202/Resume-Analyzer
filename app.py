from flask import Flask, render_template, request
import os

from resume_parser.parser import extract_text_from_resume
from resume_parser.skills import extract_skills, missing_skills, resume_score, predict_role

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = "Uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    # check if file is uploaded
    if "resume" not in request.files:
        return "No file uploaded"

    file = request.files["resume"]

    if file.filename == "":
        return "No file selected"

    print("FILE RECEIVED:", file.filename)

    # save file
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # extract text
    text = extract_text_from_resume(filepath)

    print("TEXT LENGTH:", len(text))

    # detect skills
    skills = extract_skills(text)

    print("SKILLS FOUND:", skills)

    # missing skills
    missing = missing_skills(skills)

    # calculate score
    score = resume_score(skills)

    # predict role
    role = predict_role(skills)

    print("SCORE:", score)
    return render_template(
    "result.html",
    resume_text=text,
    skills=skills,
    missing=missing,
    score=score,
    role=role
    )


if __name__ == "__main__":
    app.run(debug=True)