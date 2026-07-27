from flask import Blueprint
from flask import jsonify
from flask import request
from extensions import db
from courses.models import Course, Enrollment,Student
 
courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix ="/api/courses"
)


def make_response_json(data, status_code):

    return jsonify({
        "status": "success",
        "data": data
    }), status_code
    


@courses_bp.route("/",methods = ["GET"])

def get_courses():

    courses = Course.query.all()

    return jsonify(
        [course.to_dict() for course in courses]
    )


@courses_bp.route("/", methods=["POST"])
def create_course():

    data = request.get_json()
    if "title" not in data:
            return jsonify({"error": "Title required"}), 400
    
    course = Course(
        title=data["title"],
        department_id=data["department_id"],
        
    )

    db.session.add(course)

    db.session.commit()

    return make_response_json(course.to_dict(), 201)
    
@courses_bp.route("/<int:course_id>/", methods=["GET"])
def get_course_by_id(course_id):

    course = Course.query.get_or_404(course_id)

    return jsonify(course.to_dict())
        
@courses_bp.route("/<int:course_id>/", methods=["PUT"])
def update_course(course_id):

    course = Course.query.get_or_404(course_id)

    data = request.get_json()

    course.title = data["title"]

    course.department_id = data["department_id"]

    db.session.commit()

    return jsonify(course.to_dict())

@courses_bp.route("/<int:course_id>/", methods=["DELETE"])
def delete_course(course_id):

    course = Course.query.get_or_404(course_id)

    db.session.delete(course)

    db.session.commit()

    return jsonify({
        "message":"Deleted Successfully"
    })
    
    
@courses_bp.route("/<int:id>/students/", methods=["GET"])
def get_students(id):

    students = (
        db.session.query(Student)
        .join(Enrollment)
        .filter(Enrollment.course_id == id)
        .all()
    )

    return jsonify([student.to_dict() for student in students])