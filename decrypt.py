from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import base64

with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

encryptedStr= "Vas/Tg5TFuJW7J2IdVLdixpqQ4frref66zH2xZvFehWIV+1VVKwWYTJTznovww9j30sUYzGxO21oGmbZRPqM531KTLMlH8ew7cAScdgciIIDBBcwBGrgBREibibqlSAXiRi++D+oi4/NWTdjgvnf9txqTiif1VaqxAhbXZBXyZbZoDPPQoo0EWhWUhBagelUwfAIT4LMNlp01Mjk/tUAlg/FKegF20JuIJezfSqISN0BbhpUC2lraUU6KCmPU91rLF/KZ7IAoclCo686AjhjZ9BUyeeTMOYG9MUvX5j7ro83aMXVklxZm6ACZWkqC4azZZLUR8nAnRTo+oKLmngxLw=="

encrypted = base64.b64decode(encryptedStr)

original_message = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(original_message)