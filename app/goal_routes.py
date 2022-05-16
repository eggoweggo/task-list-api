from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.goal import Goal
from datetime import datetime

goals_bp = Blueprint("goals_bp", __name__, url_prefix="/goals")

# helper functions
def validate_goal(goal_id):
    try:
        goal_id = int(goal_id)
    except:
        abort(make_response({"error": f"Goal id invalid"}, 400))

    goal = Goal.query.get(goal_id)
    if not goal:
        abort(make_response({"error":f"Goal not found"}, 404))
    return goal


# ----------------- END POINTS -------------------
# creates new goal to the database
@goals_bp.route("", methods=["POST"])
def create_goal():
    request_body = request.get_json()
    if "title" not in request_body:
        return make_response(jsonify({"details": "Invalid data"}), 400)

    new_goal = Goal(
        title=request_body["title"])

    db.session.add(new_goal)
    db.session.commit()
    response_body = {
        "goal": new_goal.make_dict()}
    return make_response(jsonify(response_body), 201)


# get all saved goals
@goals_bp.route("", methods=["GET"])
def get_all_goals():
    goals = Goal.query.all()
    response_body = [goal.make_dict() for goal in goals]
    return make_response(jsonify(response_body), 200)


# get one goal by task id 
@goals_bp.route("/<goal_id>", methods=["GET"])
def get_one_goal(goal_id):
    goal = validate_goal(goal_id)
    response_body = {"goal": goal.make_dict()}
    return make_response(jsonify(response_body), 200)


# update goal 
@goals_bp.route("/<goal_id>", methods=["PUT"])
def update_goal(goal_id):
    request_body = request.get_json()
    goal = validate_goal(goal_id)
    goal.title = request_body["title"]
    response_body = {"goal": goal.make_dict()}
    return make_response(jsonify(response_body), 200)


# delete goal
@goals_bp.route("/<goal_id>", methods=["DELETE"])
def delete_goal(goal_id):
    goal = validate_goal(goal_id)
    db.session.delete(goal)
    db.session.commit()
    response_body = {
        "details":f'Goal {goal.goal_id} "{goal.title}" successfully deleted'}
    return make_response(jsonify(response_body), 200)