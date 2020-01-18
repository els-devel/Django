from django.db import models
from safe_api.safe_api_helpers import Fernet128
from safe_api.safe_api_helpers import AES256


class MyEncryptedField(models.TextField):

    def to_python(self, value):
        """overriding from TextField to encrypt text"""

        # algorithm = Fernet128()
        algorithm = AES256()

        if value is not None:
            value = str(value)
            value = algorithm.encrypt_(value)
            return str(value.decode())
        return value
