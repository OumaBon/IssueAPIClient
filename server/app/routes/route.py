from . import api
from ..import db
from flask import jsonify,request
from ..model import Issue
from ..exceptions import ValidationError


@api.route('/register', methods=["POST"])
def create_issue():
    if not request.is_json:
        raise ValidationError("Request must be JSON")
    data = request.get_json()
    if not data.get('title'):
        raise ValidationError("Title is required")
    if not data.get('description'):
        raise ValidationError("Description is required")
    issue = Issue(
        title=data.get('title'),
        description=data.get('description'),
    )
    db.session.add(issue)
    db.session.commit()
    return jsonify({"message": "Issue created successfully!"}), 201

    
@api.route('/issues', methods=["GET"])
def get_issues():
    issues = Issue.query.all()
    return jsonify([issue.to_dict() for issue in issues]), 200


@api.route('/issues/<int:id>', methods=["GET"])
def get_issue_by_id(id):
    issue = Issue.query.get_or_404(id)
    return jsonify(issue.to_dict()), 200



@api.route('/issues/<int:id>', methods=["PUT"])
def update_issue(id):
    issue = Issue.query.get_or_404(id)
    if request.is_json:
        data = request.get_json()
        issue.title = data.get('title', issue.title)
        issue.description = data.get('description', issue.description)
        db.session.commit()
        return jsonify({"message": "Issue updated successfully!", "issue": issue.to_dict()}), 200
    else:
        return jsonify({"error": "The request payload is not in JSON format"}), 400



@api.route('/issues/<int:id>', methods=["DELETE"])
def delete_issue(id):
    issue = Issue.query.get_or_404(id)
    db.session.delete(issue)
    db.session.commit()
    return jsonify({"message": "Issue deleted successfully!"}), 200

    