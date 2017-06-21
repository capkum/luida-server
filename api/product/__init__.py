from flask import Blueprint, jsonify
from flask import request
from werkzeug.exceptions import RequestEntityTooLarge
import os
from settings import UPLOAD_FOLDER

productor_profile = Blueprint('prodoct', __name__)
# UPLOAD_FOLDER = '/Users/hubmediadev/Desktop/luida-server/upload/'


@productor_profile.route('/p_profile', methods=['POST'])
def create_profile():

    try:
        img_fils = request.files.getlist("uploadedfile")

        for file in img_fils:
            img_name = file.filename
            try:
                file.save(os.path.join(UPLOAD_FOLDER, img_name))

            except Exception as e:
                print(str(e))
                return jsonify({
                    'status': 'upload fialed',
                    'upload_filename': img_name,
                })

        return jsonify({'status': 'upload success'})

    except RequestEntityTooLarge as e:
        return jsonify({'status': 'request too large'})

    except Exception as e:
        print(str(e))
        return jsonify({'status': 'upload fialed'})


def allowed_file(filename):
    """ 확장자 검색 """
    ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
