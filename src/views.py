from flask import Blueprint, render_template, request
from repositories.ecommerce_repository import EcommerceRepository

main_bp = Blueprint('main', __name__)


@main_bp.route("/", methods=['GET', 'POST'])
def index():
    options = EcommerceRepository.get_all()    
    if request.method == 'POST': 
        search_query = request.form.get('search_query') 
        category = request.form.get('category') 
    else: 
        search_query = ""
        category = ""

    return render_template('index.html', search_query=search_query, category=category, options=options)