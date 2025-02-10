import os
from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(mongo_uri)

db = client.student_db
students_collection = db.students

def add(student=None):

    existing_student = students_collection.find_one({
        'first_name': student.first_name,
        'last_name': student.last_name
    })

    if existing_student:
        return 'already exists', 409

    student_data = student.to_dict()
    result = students_collection.insert_one(student_data)

    student.student_id = str(result.inserted_id)
    #return student.student_id
    return {"student_id": student.student_id}, 200

def get_by_id(student_id=None, subject=None):

    student = students_collection.find_one({'_id': ObjectId(student_id)})

    if not student:
        return 'not found', 404

    student['student_id'] = student_id
    print(student)
    return student

def delete(student_id=None):

    student = students_collection.find_one({'_id': ObjectId(student_id)})

    if not student:
        return 'not found', 404

    result = students_collection.delete_one({'_id': ObjectId(student_id)})
    if result.deleted_count == 1:
        return student_id
    else:
        return 'not found', 404