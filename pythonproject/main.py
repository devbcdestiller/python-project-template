from config.secure_properties import secure_properties
from utils.decryption import Decryption

# Set your key as an environment variable in production
KEY = b'password12345678'


def main():
    properties = Decryption(cipher_dict=secure_properties.get('dev'), key=KEY)
    print(properties.decrypt_properties())


if __name__ == "__main__":
    main()
