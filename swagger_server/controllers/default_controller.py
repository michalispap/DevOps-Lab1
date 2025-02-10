import connexion
import six

from swagger_server.service.student_service import *
from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util

def add_student(body=None):  # noqa: E501

    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
        return add(body)
    return 500, 'error'

def delete_student(student_id):  # noqa: E501

    return delete(student_id)

def get_student_by_id(student_id):  # noqa: E501

    return get_by_id(student_id)