# -*- coding: utf-8 -*-
import hashlib
import base64
from Crypto import Random  # noqa
from Crypto.Cipher import AES
from .util import creat_timestamp
import uuid

BS = 16


def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()


def unpad(s):
    return s[:-ord(s[len(s) - 1:])]


def iv():
    """ 초기 백터 """
    return chr(0) * 16


class AESCipher(object):
    def __init__(self, key):
        self.key = key
        # self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, message):
        """
        암호화
        """
        message = message.encode()
        raw = pad(message)
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, enc):
        """ 복호화  """
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')


def passwd_crypt(value):
    """ 가입시/로그인시 암호화  """
    return hashlib.sha256(value.encode('ascii')).hexdigest()


def token_generator():
    """
    토큰 생성기
    총 문자열 길이(46)
    """
    gen_token = str(uuid.uuid4())
    expire_time = creat_timestamp() + 60
    return gen_token + str(expire_time)


if __name__ == '__main__':
    print(len(token_generator()))
    # message = '한글을 테스트 합니다.'
    # enc = AESCipher(CRYPTO_KEY).encrypt(message)
    # dec = AESCipher(CRYPTO_KEY).decrypt(enc)
