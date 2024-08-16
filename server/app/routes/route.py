from . import api
from ..import db
from flask import jsonify,request
from ..model import Issue
from ..exceptions import ValidationError



@api.route('/register', methods=['POST'])
def create_issue():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if Issue.query.filter_by(title=title).first():
        return jsonify({"message": "Issue with this title already exists."}), 400

    new_issue = Issue(title=title, description=description)
    db.session.add(new_issue)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Issue could not be created."}), 500

    return jsonify({"id": new_issue.id, "message": "Issue created successfully."}), 200



    
@api.route('/issues', methods=["GET"])
def get_issues():
    issues = Issue.query.all()
    return jsonify([issue.to_dict() for issue in issues]), 200


@api.route('/issues/<int:issue_id>', methods=['GET'])
def get_issue(issue_id):
    issue = Issue.query.get(issue_id)
    if issue is None:
        return jsonify({"message": "Issue not found."}), 404

    return jsonify({
        'id': issue.id,
        'title': issue.title,
        'description': issue.description
    })





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

    