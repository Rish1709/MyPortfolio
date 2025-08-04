# My Portfolio Website

view it at : https://myportfolio-9dti.onrender.com/

A modern, responsive personal portfolio website built with Flask, HTML, CSS, and Jinja2. This site showcases my projects, achievements, education, skills, and more, with a professional and visually appealing interface.

It also features an integrated AI-powered personal assistant chatbot (using Google Gemini API) that can answer questions about my portfolio, projects, and background in a professional manner.

## Features
- Clean, modern UI with responsive design
- Project and skills showcase
- Achievements, certifications, and education sections
- Integrated personal assistant chatbot (Gemini API)
- Easy navigation using Flask routes and Jinja2 templates
- Consistent styling across all pages

## Tech Stack
- Python 3
- Flask
- Jinja2
- HTML5 & CSS3
- JavaScript (jQuery)
- Google Generative AI (Gemini)
- SQLite (via SQLAlchemy)

## Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation
1. Clone the repository:
   ```sh
   git clone <https://github.com/Rish1709/MyPortfolio>
   cd MyPortfolio
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file with your Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
4. Run the application:
   ```sh
   python app.py
   ```
5. Open your browser and go to `http://127.0.0.1:5000/`

## Folder Structure
```
MyPortfolio/
├── app.py
├── models.py
├── static/
├── templates/
├── instance/
├── README.md
└── ...
```

## Customization
- Update your personal info, projects, and achievements in the database or seed data in `app.py`.
- Modify styles in the `static/` CSS files.
- Edit HTML templates in the `templates/` folder.

## License
This project is licensed under the MIT License.

## Contact
- Email: rishabhc1709@gmail.com
- LinkedIn: [Rishabh Chaudhary](https://www.linkedin.com/in/rishabh-chaudhary-7b865227a)
- GitHub: [Rish1709](https://github.com/Rish1709)

