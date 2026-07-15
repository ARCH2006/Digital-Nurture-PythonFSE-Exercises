from flask import Blueprint
from flask import jsonify
from flask import request
 
courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix ="/api/courses"
)

courses = []

def make_response_json(data, status_code):

    return jsonify({
        "status": "success",
        "data": data
    }), status_code
    


@courses_bp.route("/",methods = ["GET"])
def get_courses():
    return jsonify(courses)

@courses_bp.route("/",methods = ["POST"])
def create_course():
    data = request.get_json()
    # Check if request body is JSON
    if data is None:
        return jsonify({
            "status": "error",
            "message": "Request body must be JSON"
        }), 400
    required_fields = ["name","code","credits"]
    for field in required_fields:
        if field not in data:
            return jsonify({
                "status": "error",
                "message": f"{field} is required"
            }), 400
    courses.append(data)
    return make_response_json(data, 201)
              
    # courses.append(data)
    # return jsonify(data),201
    
@courses_bp.route("/<int:course_id>/", methods=["GET"])
def get_Course_by_id(course_id):
        if course_id >= len(courses):
            return jsonify({
            "status": "error",
            "message": "Course not found"
            }), 404

        return jsonify({
        "status": "success",
        "data": courses[course_id]
        })
        
@courses_bp.route("/<int:course_id>/", methods=["PUT"])
def update_course(course_id):
        if course_id >= len(courses):
            return jsonify({
            "status": "error",
            "message": "Course not found"
            }), 404
        
        data = request.get_json()
        courses[course_id] = data
        return jsonify({
        "status": "success",
        "data": courses[course_id]
         }), 200
@courses_bp.route("/<int:course_id>/", methods=["DELETE"])
def delete_course(course_id):

    if course_id >= len(courses):
        return jsonify({
            "status": "error",
            "message": "Course not found"
        }), 404

    deleted_course = courses.pop(course_id)

    return jsonify({
        "status": "success",
        "data": deleted_course
    }), 200