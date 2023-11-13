import os

BASE_DIR = os.path.dirname(__file__)

#  데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# SQLAlchemy 이벤트 처리 옵션 비 활성화
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-WTF를 사용하기 위한 플라스크 환경변수
SECRET_KEY="dev"