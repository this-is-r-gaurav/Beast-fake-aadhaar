from flask import render_template, request, flash, redirect, url_for
from flask.blueprints import Blueprint
from werkzeug.utils import secure_filename

from src.common.Utility.utils import Utils
from src.models.person.person import Person

import os

person_blueprint = Blueprint('person',__name__)

@person_blueprint.route('/register', methods = ["POST", "GET"])
def register_user():
    if request.method == "POST":
        aadhaar_no = request.form['aadhaar_no']
        name = request.form['name']
        address = request.form['address']
        gender = request.form['gender']
        dob = request.form['dob']
        phone = request.form['phone']
        fingerprint = request.form['fingerprint']
        fileName = None
        if not Utils.is_adhaar_valid(aadhaar_no):
            flash('Incorrect format of Aadhaar Number')
            return request.url
        if not Utils.is_adhaar_valid(aadhaar_no):
            flash('Incorrect format of Mobile Number')
            return request.url
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        image = request.files['image']
        # if user does not select file, browser also
        # submit a empty part without filename
        if image.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if image and Utils.allowed_file(image.filename):
            filename = secure_filename(image.filename)
            fileName = filename
            image.save(os.path.join((url_for('static')+'/assets/images/',filename))

        Person(
            aadhaar_no=aadhaar_no,
            image = fileName,
            gender= gender,
            name = name,
            address = address,
            dob = dob,
            fingerprint=fingerprint,
            phone = phone).save_to_db()

    return render_template('users/get-records.html')
