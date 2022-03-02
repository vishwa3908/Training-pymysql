from flask import Blueprint
from src.services.login.customer_entry import Login

log_in = Blueprint("log_in",__name__)

@log_in.route("/login",methods = ["POST"])
def old_login():
    return Login.old_customer_login()

@log_in.route("/login/new",methods=["POST"])
def new_login():
    return Login.new_customer()

@log_in.route("/login/delete",methods=["DELETE"])
def delete_account():
    return Login.delete_my_account()