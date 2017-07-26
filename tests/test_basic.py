# -*- coding: utf-8 -*-

import os  # noqa
import unittest
from server_api.common.validate import validate_param


class BasicTests(unittest.TestCase):
    ''' 유효성검사
    email: 형식검사
    name: 3자이상 60자 이하 한글, 영문
    nickName: 3자이상 20자 이하
    passwd: 6자 이상 20자 이하 영문, 숫자, 한글 그리고 특수문자 필수입력
    '''

    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_validate(self):
        false_case = validate_param('email', 'test')
        true_case = validate_param('email', 'cap@naver.com')
        self.assertAlmostEqual(false_case, False)
        self.assertAlmostEqual(true_case, True)


if __name__ == '__main__':
    unittest.main()
