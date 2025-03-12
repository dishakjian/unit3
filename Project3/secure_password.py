from passlib.context import CryptContext

pwd_config = CryptContext(schemes=["pbkdf2_sha256"], default="pbkdf2_sha256")

def check_hash(input_str: str, hash: str) -> bool:
    """Verify if the input string matches the hash."""
    print(f"Input: '{input_str}'")  # Debugging
    print(f"Hash: '{hash}'")  # Debugging
    return pwd_config.verify(input_str, hash)

def hash_password(in_password: str) -> str:
    """Hash a password using pbkdf2_sha256."""
    return pwd_config.hash(in_password)
