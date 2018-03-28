from flask import jsonify,request
from flask.blueprints import Blueprint
from flask_restplus import Resource, Api

from src.config import domain
from src.models.api.methods import APIMethods
from src.models.person.person import Person

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint,'1.0','Testing Beast Aadhaar Api', 'This is a Fake Aadhar Api for SIH Hackathon', default_label='Beast Fake Aadhaar',default='Beast')


@api.route('/users')
class ListAllUser(Resource):
    def get(self):
        cluster_data = APIMethods.get_cluster_user()
        return jsonify({'data': cluster_data })

@api.route('/adhaar')
class GetUserInfo(Resource):
    @api.doc(params={
        'aadhaar_no': {'in': 'formData', 'description': 'User Aadhaar Number', 'required': 'True'}})
    def post(self):
        aadhaar_no=request.form['aadhaar_no']
        person = Person.get_by_aadhaar(aadhaar_no)
        return jsonify(
            {
            "aadhaar": person.aadhaar_no,
            "name": person.name,
            "gender": person.gender,
            "address": person.address,
            "dob": person.dob,
            "phone": person.phone,
            "image": domain+"static/assets/images/"+person.image
             })

