import json
import jsonschema
from jsonschema import validate

teacherSchema = {
    "type": "object",
    "properties": {
        "_name": {
            "type": "string"
        },
        "_name_course": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
}

course_schema = {
    "type": "object",
    "properties": {
        "_title": {
            "type": "string"
        },
        "_teacher": {
            "type": "string"
        },
        "_list_of_topics": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
}


def validate_json_teacher(json_data):
    try:
        validate(instance=json_data, schema=teacherSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


def validate_json_course(json_data):
    try:
        validate(instance=json_data, schema=course_schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


# def check_json(file_json):
#     teacher_valid = validate_json_teacher(file_json)
#       course_valid =  validate_json_course(file_json)
#     if not teacher_valid or not course_valid:
#         raise ValueError("incorrect data in json file")
#     return f'json file is valid'
