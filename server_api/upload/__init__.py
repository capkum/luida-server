# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify
from flask import request
from api.database import db
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug import secure_filename
from settings import UPLOAD_FOLDER
from common.util import rename_upload_file
import os

from .models import Products

productor_profile = Blueprint('prodoct', __name__)


@productor_profile.route('/p_profile', methods=['POST'])
def create_profile():

    try:
        img_fils = request.files.getlist("uploadedfile")

        for file in img_fils:
            img_name = rename_upload_file(secure_filename(file.filename))

            try:
                file.save(os.path.join(UPLOAD_FOLDER, img_name))
                insert_data = Products(img_name)
                db.session.add(insert_data)
                db.session.commit()

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
