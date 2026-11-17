
from flask import Flask, render_template, request

app = Flask(__name__)

industry_data = {
    "Data Analyst": {
        "skills": ["Python", "SQL", "Power BI", "Excel"],
        "courses": {
            "Power BI": "Power BI Training",
            "Excel": "Advanced Excel Training"
        }
    },
    "Web Developer": {
        "skills": ["HTML", "CSS", "JavaScript", "React"],
        "courses": {
            "JavaScript": "JavaScript Programming",
            "React": "React Development"
        }
    },
    "Software Engineer": {
        "skills": ["Python", "Java", "C++", "DSA"],
        "courses": {
            "Java": "Java Programming",
            "DSA": "Data Structures and Algorithms"
        }
    }
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        name = request.form["name"]
        role = request.form["role"]
        entered = request.form["skills"]

        student_skills = [
            skill.strip().lower()
            for skill in entered.split(",")
            if skill.strip()
        ]

        required = industry_data[role]["skills"]

        available = [
            skill for skill in required
            if skill.lower() in student_skills
        ]

        missing = [
            skill for skill in required
            if skill.lower() not in student_skills
        ]

        courses = [
            industry_data[role]["courses"][skill]
            for skill in missing
            if skill in industry_data[role]["courses"]
        ]

        result = {
            "name": name,
            "role": role,
            "available": available,
            "missing": missing,
            "courses": courses
        }

    return render_template(
        "index.html",
        roles=industry_data.keys(),
        result=result
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
