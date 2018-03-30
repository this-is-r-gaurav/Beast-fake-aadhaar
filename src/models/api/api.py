from flask import jsonify, request
from flask.blueprints import Blueprint
from flask_restplus import Resource, Api

from src.config import domain
from src.models.api.methods import APIMethods
from src.models.person.person import Person

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint, '1.0', 'Testing Beast Aadhaar Api', 'This is a Fake Aadhar Api for SIH Hackathon',
          default_label='Beast Fake Aadhaar', default='Beast')


@api.route('/users')
class ListAllUser(Resource):
    def get(self):
        cluster_data = APIMethods.get_cluster_user()
        return jsonify({'data': cluster_data})


@api.route('/aadhaar')
class GetUserInfo(Resource):
    @api.doc(params={
        'aadhaar_no': {'in': 'formData', 'description': 'User Aadhaar Number', 'required': 'True'}})
    def post(self):
        aadhaar_no = request.form['aadhaar_no']
        person = Person.get_by_aadhaar(aadhaar_no)
        if person:
            return jsonify(
                {
                    "aadhaar": person.aadhaar_no,
                    "name": person.name,
                    "gender": person.gender,
                    "address": person.address,
                    "dob": person.dob.strftime("%Y-%m-%d"),
                    "phone": person.phone,
                    "image": domain + "static/assets/images/" + person.image
                })
        else:
            return None


@api.route('/register')
class AddUser(Resource):

    @api.doc(params={
        'aadhaar_no': {'in': 'formData', 'description': 'User Aadhaar Number', 'required': 'True'},
        'name': {'in': 'formData', 'description': 'User Name', 'required': 'True'},
        'dob': {'in': 'formData', 'description': 'User Date of Birth', 'required': 'True'},
        'address': {'in': 'formData', 'description': 'User Address', 'required': 'True'},
        'mobile_no': {'in': 'formData', 'description': 'User Mobile Number', 'required': 'True'},
        'gender': {'in': 'formData', 'description': 'User Gender', 'required': 'True'},
    })
    def post(self):
        aadhaar_no = request.form['aadhaar_no']
        name = request.form['name']
        dob = request.form['dob']
        image ="x.jpeg"
        address = request.form['address']
        mobile_no = request.form['mobile_no']
        gender = request.form['gender']

        if Person.get_by_aadhaar(aadhaar_no):

            return {"msg": "User already exist"}
        else:
            if Person(aadhaar_no,image,name,address,gender,dob,mobile_no,"True").save_to_db():
                return {"msg":"user created successfuly"}, 201
            else:
                return {"msg":"user cant be created"}, 302

