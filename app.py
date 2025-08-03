from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai
from models import db, PersonalInfo

# Load environment variables
load_dotenv()

# Load API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY environment variable not set!")

# Configure Gemini API
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
chat = model.start_chat()

# Assistant instructions
chat.send_message(
    "Act strictly like my personal assistant named Robert. "
    "You will help me explain my projects, resume, and other details, only when asked about it. "
    "Don't act like Gemini AI or any AI. You are Robert, not an AI assistant. "
    "Also be formal and professional in your responses. Don't tell anything negative about me or my projects." \
    " Strictly reject any irrelevant requests. "
    )

# Flask setup

# Flask setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personal_info.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Main page
@app.route('/')
def index():
    return render_template('index.html')

# Experience page
@app.route('/experience')
def experience():
    return render_template('experience.html')

# Education page
@app.route('/education')
def education():
    return render_template('education.html')

# Skills page
@app.route('/skills')
def skills():
    return render_template('skills.html')

# Projects page
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Achievements page
@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

# Certifications page
@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

@app.route('/chat', methods=['POST'])
def chat_with_gemini():
    user_input = request.json.get('message')
    info = PersonalInfo.query.first()
    
    if info:
        context = f"""
        [USER PROFILE]
        Name: {info.name}
        School: {info.school}
        Class X Grade: {info.class_x_grade}
        Class XII Grade: {info.class_xii_grade}
        JEE MAINS Rank: {info.jeemains_rank}
        JEE ADV Rank: {info.jeeadv_rank}
        College: {info.college}

        [ACHIEVEMENTS]
        {info.achievements or "None listed"}

        [HOBBIES]
        {info.hobbies}

        [INTERESTS]
        {info.interests}

        [PROJECTS]
        {info.projects}

        [RESUME SUMMARY]
        {info.resume}
        """
    else:
        context = ""

    prompt = context + "\nUser: " + user_input

    try:
        response = chat.send_message(prompt)
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'error': str(e)})

# Run + auto-create tables + seed once
if __name__ == "__main__":
    with app.app_context():
        # 🧨 Delete old DB if it exists
        if os.path.exists('personal_info.db'):
            os.remove('personal_info.db')

        # ✅ Create new DB with updated model
        db.create_all()

        # ✅ Optional: Seed initial data
        if not PersonalInfo.query.first():
            me = PersonalInfo(
                name="Rishabh Chaudhary",
                school="Sagar Public School, Bhopal",
                class_x_grade="95%",
                class_xii_grade="84.7%",
                jeemains_rank="99.4 percentile",
                jeeadv_rank="11572",
                college="INDIAN INSTITUTE OF TECHNOLOGY (BHU), VARANASI",
                hobbies="Badminton, Coding",
                interests="AI/ML, Robotics, Web Development, Competitive Programming",
                projects="Personal Assistant using Gemini, Resume Parser",
                resume="Link or summary of your resume here"
            )
            db.session.add(me)
            db.session.commit()

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

