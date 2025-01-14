from flask import Blueprint, render_template, request
from repositories.ecommerce_repository import EcommerceRepository

main_bp = Blueprint('main', __name__)


@main_bp.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        options = EcommerceRepository.get_all()
        return render_template('index.html', options=options)
    elif request.method == 'POST':
        print(request.form)
        pass