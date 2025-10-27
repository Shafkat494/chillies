# create_test_student.py
from app import app, db, Student

students = [
    {"name": "Test Student 1", "username": "student1", "password": "s123", "room": "101", "allergies": "", "food_type": "veg"},
    {"name": "Test Student 2", "username": "student2", "password": "s456", "room": "102", "allergies": "nuts", "food_type": "non-veg"},
]

with app.app_context():
    for data in students:
        if Student.query.filter_by(username=data["username"]).first():
            print("Student already exists:", data["username"])
        else:
            s = Student(
                name=data["name"],
                username=data["username"],
                room=data["room"],
                allergies=data["allergies"],
                food_type=data["food_type"]
            )
            s.set_password(data["password"])
            db.session.add(s)
            print("Created test student:", data["username"], "/", data["password"])
    db.session.commit()
