from src.models.person.person import Person

class APIMethods:
    @staticmethod
    def get_cluster_user():
        users = Person.get_all_user()
        if users is not None:
            return [{
            "aadhaar_no": user.aadhaar_no,
            "name": user.name,
            "gender": user.gender,
            "address": user.address,
            "dob": user.dob,
            "phone": user.phone,
            "fingerprint": user.fingerprint,
            "image": user.image
            } for user in users]
        else:
            return None