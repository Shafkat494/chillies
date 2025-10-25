# create_test_student.py
from app import app, db, Student

username = "student1"
password = "s123"      # test password (you can change)

with app.app_context():
    # skip if exists
    if Student.query.filter_by(username=username).first():
        print("Student already exists:", username)
    else:
        s = Student(name="Test Student", username=username, room="101", allergies="", food_type="veg")
        s.set_password(password)
        db.session.add(s)
        db.session.commit()
        print("Created test student:", username, "/", password)
