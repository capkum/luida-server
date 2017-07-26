# -*- coding: utf-8 -*-

import re

regx = {
    'email': r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',
    'name': r'(^[A-Za-z가-힣\s?]{3,60})+$',
    'nickName': r'(^[A-Za-z가-힣]{3,20})+$',
    'passwd': r'^(?=.*[a-zA-Z])((?=.*\d)|(?=.*\W)).{6,20}$'
}


def validate_param(key, value):
    ''' 유효성검사
    email: 형식검사
    name: 3자이상 60자 이하 한글, 영문
    nickName: 3자이상 20자 이하
    passwd: 6자 이상 20자 이하 영문, 숫자, 한글 그리고 특수문자 필수입력
    '''
    if value:
        pattern = re.compile(regx[key])
        rt = pattern.match(str.strip(value))

        return True if rt else False

    else:
        return False


if __name__ == '__main__':
    pass
    # email = 'test1'
    # email1 = 'sj.kim@test'
    # email2 = 'sj.kim@test.com'
    # email3 = 'sj.kim@test.co.kr'
    # name = 'ki'
    # name1 = '2ki'
    # name2 = 'kim '
    # name3 = 'kim Seoung'
    # print(validate_param('email', email2))
    # print(validate_param('name', name3))
