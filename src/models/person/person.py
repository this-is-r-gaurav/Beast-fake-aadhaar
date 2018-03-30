import uuid
import datetime

import src.models.person.constants as PersonConstants

from src.common.database import Database
from src.common.Utility.Utility import CommonUtility as PersonUtility


class Person:
    def __init__(self, aadhaar_no, image, name, address, gender, dob, phone, fingerprint=None, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.aadhaar_no = PersonUtility.formating_aadhaar(aadhaar_no)
        self.name = PersonUtility.formating_name(name)
        self.address = address
        self.gender = gender
        self.dob = datetime.datetime.strptime(dob, "%Y-%m-%d") if isinstance(dob, str) else dob
        self.phone = PersonUtility.formating_phone(phone)
        self.fingerprint = fingerprint
        self.image = image

    def json(self):
        return {
            "_id": self._id,
            "aadhaar_no": self.aadhaar_no,
            "name": self.name,
            "gender": self.gender,
            "address": self.address,
            "dob": self.dob.strftime("%Y-%m-%d"),
            "phone": self.phone,
            "fingerprint": self.fingerprint,
            "image": self.image
        }

    def save_to_db(self):
        Database.update(PersonConstants.COLLECTION, {"_id": self._id}, self.json())

    @classmethod
    def get_by_id(cls, person_id):
        data = Database.find_one(PersonConstants.COLLECTION, {'_id': person_id})
        return cls(**data) if data is not None else False

    @classmethod
    def get_all_user(cls):
        cluster_data = Database.find(PersonConstants.COLLECTION, {})
        return [cls(**data) for data in cluster_data if cluster_data is not None] if cluster_data is not None else None

    @classmethod
    def get_by_aadhaar(cls, aadhaar_no):
        data = Database.find_one(PersonConstants.COLLECTION, {'aadhaar_no': aadhaar_no})
        return cls(**data) if data is not None else None
