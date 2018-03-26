import re
class Utils:
    @staticmethod
    def allowed_file(filename):
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    @staticmethod
    def is_phone_valid(phone):
        """
        Recieve phone Number as parameter and returns
        true if number has format as +91xxxxx-xxxxx, +91xxxxxxxxxx, or xxxxxxxxxx
        or xxxxx-xxxxx
        :param phone:Client Phone Number
        :return:True if Phone number has right format otherwise False
        """
        phone_validator = re.compile('^(\+91[\d]{10})$|^([\d]{10})$|^(\+91[\d]{5}\-[\d]{5})$|^([\d]{5}\-[\d]{5})$')
        return True if phone_validator.match(phone) else False

    @staticmethod
    def is_adhaar_valid(adhaar):
        """
        Recieve adhaar Number as parameter and returns
        true if number has format as xxxx xxxx xxxx xxxx
        :param adhaar: Client Adhaar Number
        :return:True if Adhaar number has right Format
        """
        adhaar_validator = re.compile('^([\d]{4}\ ){3}[\d]{4}$')
        return True if adhaar_validator.match(adhaar) else False