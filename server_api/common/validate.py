# -*- coding: utf-8 -*-

import re

regx = {
    'email': r'(\w+[\w\.]*)@(\w+[\w\.]*)\.([A-Za-z]+)',
    'name': r'[A-Za-z\s?]{3,20}',
    'nickName': r'[A-Za-z0-9_-]{3,20}'
}


def validate_param(key, value):
    pattern = re.compile(regx[key])
    rt = pattern.match(value)
    return True if rt is not None else False


if __name__ == '__main__':
    email = 'test1'
    email1 = 'sj.kim@test'
    email2 = 'sj.kim@test.com'
    email3 = 'sj.kim@test.co.kr'
    name = 'ki'
    name1 = '2ki'
    name2 = 'kim '
    name3 = 'kim Seoung'
    print(validate_param('email', email2))
    print(validate_param('name', name3))
