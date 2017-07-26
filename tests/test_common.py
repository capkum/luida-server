# -*- coding: utf-8 -*-
''' 유효성검사
    email: 형식검사
    name: 3자이상 60자 이하 한글, 영문
    nickName: 3자이상 20자 이하
    passwd: 6자 이상 20자 이하 영문, 숫자, 한글 그리고 특수문자 필수입력
'''
import pytest  # noqa
from server_api.common.validate import validate_param


def gen(key, objs):
    objs_len = 0
    while objs_len < len(objs):
        yield validate_param(key, objs[objs_len])
        objs_len += 1


def test_valid_email():
    emails = ['capnaver@naver.com', 'capnaver@naver.co.kr']
    for rt in gen('email', emails):
        assert rt


def test_invalid_email():
    emails = ['capnaver.com', 'capnaver@naver', '', None]
    for rt in gen('email', emails):
        assert not rt


def test_valid_passwd():
    pwds = ['furumee#1', '김성진#123dd']
    for rt in gen('passwd', pwds):
        assert rt


def test_invalid_passwd():
    '''
    ToDo 연속된 문자도 금지 해야되는데 지금 안되어있음
    '''
    pwds = ['dddddd', '김성진', 'fu@22', 'd' * 20]
    for rt in gen('passwd', pwds):
        assert not rt


def test_valid_name():
    names = ['김성진', 'json snow', 'king jons snow']
    for rt in gen('name', names):
        assert rt


def test_invalid_name():
    names = ['김', 'json2', '2 jons snow', 'json  snow#', '   ']
    for rt in gen('name', names):
        assert not rt


def test_valid_nickName():
    nicknames = ['김성진', 'jsonsnow', 'kingjonssnow']
    for rt in gen('nickName', nicknames):
        assert rt


def test_invalid_nickName():
    nicknames = ['김 진', ' j', 'json_snow', 'js', 'z' * 21]
    for rt in gen('nickName', nicknames):
        assert not rt
