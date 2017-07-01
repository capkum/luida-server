# -*- coding: utf-8 -*-

from flask import Blueprint
from .auth_proc import login_proc

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    """ 로그인 """
    return login_proc()


@auth.route('/signout', methods=['DELETE'])
def signout():
    """
    회원 탈퇴
    ToDo
    1. 탈퇴시 업로드어있던 파일을들 삭제
    2. 거래정보는 삭제하면 안된다
    3. 토큰 유효성 검사후 토큰 정보로 삭제
    """
    pass
    # try:
    #     _email = request.values.get('email')
    #     _passwd = request.values.get('passwd')

    #     user_token = request.headers.get('token')
    #     userid = jwt.decode(
    #         user_token, settings.SECURET_KEY, algorithm='HS256')

    #     user = Accounts.query.filter_by(
    #         id=userid['id'], passwd=_passwd).first()

    #     if type(user) is not 'NoneType':
    #         db.session.delete(user)
    #         db.session.commit()

    #         rt = jsonify(email=_email, passwd=_passwd,
    #                      status='delete success')
    #         return rt

    # except jwt.ExpiredSignatureError as e:
    #     print(str(e))
    #     return jsonify({'status': '토큰 기간 만료'})

    # except Exception as e:
    #     print(str(e))
    #     return 'delete fail'
