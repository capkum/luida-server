# -*- coding: utf-8 -*-
from datetime import datetime
from time import mktime


def creat_timestamp():
    t = datetime.now()
    return int(mktime(t.timetuple()))


def rename_upload_file(filename):
    """
    업로드파일 이름변경
    업로드파일명을 timestamp로 변경
    """
    ext = filename.rsplit('.', 1)[1]
    return str(creat_timestamp()) + ext


def allowed_file(filename):
    """ 확장자 체크 """
    ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def check_upload_folder(userid):
    """
    유저 업로드 폴더 유무 검사
    ToDo
    1. profile potho
    2. gallery
    """
    pass


def lr_trim(value):
    """
    문자열의 양옆끝의 공백을 제거
    value 공백제거해야될 문자열
    """
    return str.strip(value)
