from app import db

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    students = db.relationship('Student', backref='grade')

class House(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    colour = db.Column(db.Text)
    students = db.relationship('Student', backref='house')
    # TODO: Add a class for the database model for the House table

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'), nullable=False)
    english_mark = db.Column(db.Integer)
    science_mark = db.Column(db.Integer)
    mathematics_mark = db.Column(db.Integer)
    does_homework = db.Column(db.Boolean)
    stays_on_task = db.Column(db.Boolean)
    
