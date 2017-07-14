# LUIDA

## 개발에 사용된 프로그램들
```
os: osx 10.12.5
python: 3.6.1
package: requirements.txt 참조
redis: 3.2.9
mariadb: 10.2.7-MariaDB Homebrew
```

### how to run luida
osx 기준으로 redis, mariadb 그리고 python관련 패키지를 <br>
설치및 실행한다.
```
brew services start redis
brew services start mariadb
source virtualenv/bin/activate
pip installl -r requirements.txt
export FLASK_APP=main.py
flask db upgrade
```