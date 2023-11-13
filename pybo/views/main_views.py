from flask import Blueprint, url_for
from pybo.models import Question
from werkzeug.utils import redirect

# 블루프린트 객체 생성
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello pybo !!!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))  # question 블루프린트에 정의된 _list 함수