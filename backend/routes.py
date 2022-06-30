from flask import Blueprint


simple_page = Blueprint('simple_page', __name__)

# all of Flask routes go in here
@simple_page.route('/')
def home():
    return "testing"