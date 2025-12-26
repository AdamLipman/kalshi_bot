
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64
import datetime

def load_private_key(file_path):
    """Load your private key from a .key file."""
    with open(file_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )
    return private_key

def generate_signature(private_key, message):
    """Sign the message using RSA-PSS and encode it in Base64."""
    signature = private_key.sign(
        message.encode("utf-8"),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256(),
    )
    return base64.b64encode(signature).decode("utf-8")

def generate_auth_headers(private_key_path, api_key, method, path):
    """Generate authentication headers for Kalshi."""
    timestamp = int(datetime.datetime.now().timestamp() * 1000)  # Milliseconds timestamp
    private_key = load_private_key(private_key_path)
    message = f"{timestamp}{method}{path}"
    signature = generate_signature(private_key, message)

    return {
        "KALSHI-ACCESS-KEY": api_key,
        "KALSHI-ACCESS-TIMESTAMP": str(timestamp),
        "KALSHI-ACCESS-SIGNATURE": signature,
    }
