from cryptography.fernet import Fernet
from safe_web import settings
import base64
import hashlib
from os import urandom
from Crypto.Cipher import AES


class Fernet128:

    def __init__(self):
        self.key = settings.FERNET_KEY
        # get key from settings.py

    def encrypt_(self, secret):
        f = Fernet(self.key)
        # encrypt value
        encoded_text = secret.encode()
        encrypted_text = f.encrypt(encoded_text)
        return encrypted_text

    def decrypt_(self, secret):
        f = Fernet(self.key)
        # decrypt value
        if not isinstance(secret, bytes):
            secret = secret.encode()
        secret = f.decrypt(secret)
        return str(secret.decode())


class AES256:

    def __init__(self):
        aes_key = settings.AES_KEY
        # retrieves key from settings.py
        self.block_size = AES.block_size
        # 16 bytes
        self.key = hashlib.sha256(aes_key.encode()).digest()
        # gives 32 bytes for 256 bit encryption
        self.padding = "{"

    def encrypt_(self, secret):
        secret = self._pad(secret)
        iv = urandom(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(secret.encode()))

    def decrypt_(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.block_size - len(s) % self.block_size) * chr(self.block_size - len(s) % self.block_size)
        # return s + (self.block_size - len(s) % self.block_size) * self.padding

    def basic_encrypt(self, secret):
        # without initialization vector
        cipher = AES.new(self.key)
        encoded = base64.b64encode(cipher.encrypt(self._pad(secret)))
        return encoded

    def basic_decrypt(self, enc):
        # no initialization vector
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key)
        return self._unpad(cipher.decrypt(enc).decode('utf-8'))

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

