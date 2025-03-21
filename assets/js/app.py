from flask import Flask, request, jsonify, session, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__, static_folder='assets')
app.config['SECRET_KEY'] = 'votre_clé_secrète_ici'  # À changer en production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.String(20), primary_key=True)  # Numéro d'étudiant
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    program = db.Column(db.String(100))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(100))
    student_id = db.Column(db.String(20), db.ForeignKey('student.id'))

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    student_id = db.Column(db.String(20), db.ForeignKey('student.id'))
    value = db.Column(db.Float)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student-space')
def student_space():
    return render_template('student-space.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    student_id = data.get('student_id')
    password = data.get('password')
    
    student = Student.query.get(student_id)
    if student and student.check_password(password):
        session['student_id'] = student_id
        return jsonify({
            'success': True,
            'student': {
                'id': student.id,
                'name': student.name,
                'program': student.program
            }
        })
    return jsonify({'success': False, 'message': 'Identifiants incorrects'})

@app.route('/api/courses')
def get_courses():
    if 'student_id' not in session:
        return jsonify({'success': False, 'message': 'Non authentifié'})
    
    courses = Course.query.filter_by(student_id=session['student_id']).all()
    return jsonify({
        'success': True,
        'courses': [{'code': c.code, 'name': c.name} for c in courses]
    })

@app.route('/api/grades')
def get_grades():
    if 'student_id' not in session:
        return jsonify({'success': False, 'message': 'Non authentifié'})
    
    grades = Grade.query.filter_by(student_id=session['student_id']).all()
    return jsonify({
        'success': True,
        'grades': [{'course_id': g.course_id, 'value': g.value} for g in grades]
    })

def init_db():
    with app.app_context():
        db.create_all()
        # Ajouter quelques données de test
        if not Student.query.get('20230001'):
            student = Student(
                id='20230001',
                name='John Doe',
                email='john.doe@example.com',
                program='Informatique'
            )
            student.set_password('test123')
            db.session.add(student)
            
            courses = [
                Course(code='INFO101', name='Introduction à la programmation', student_id='20230001'),
                Course(code='INFO102', name='Bases de données', student_id='20230001'),
                Course(code='MATH101', name='Mathématiques discrètes', student_id='20230001')
            ]
            for course in courses:
                db.session.add(course)
            
            db.session.commit()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
