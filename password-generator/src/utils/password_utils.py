import secrets
import string
from config.constants import SPECIAL_CHARS, DEFAULT_LENGTH

def generate_password(length=DEFAULT_LENGTH, include_upper=True, include_lower=True, include_digits=True, include_special=True):
    chars = ""
    password = []
    
    if include_upper:
        chars += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))
    if include_lower:
        chars += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))
    if include_digits:
        chars += string.digits
        password.append(secrets.choice(string.digits))
    if include_special:
        chars += SPECIAL_CHARS
        password.append(secrets.choice(SPECIAL_CHARS))

    if not chars:
        raise ValueError("At least one character type must be selected")

    while len(password) < length:
        password.append(secrets.choice(chars))
    
    secrets.shuffle(password)
    return "".join(password)

def check_password_strength(pwd):
    score = 0
    if len(pwd) >= 8: score += 1
    if any(c.islower() for c in pwd): score += 1
    if any(c.isupper() for c in pwd): score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c in SPECIAL_CHARS for c in pwd): score += 1
    
    strength_levels = {
        0: ("Very Weak", "red"),
        1: ("Weak", "orange"),
        2: ("Medium", "yellow"),
        3: ("Strong", "yellowgreen"),
        4: ("Very Strong", "green"),
        5: ("Excellent", "darkgreen")
    }
    return score, strength_levels.get(score, ("Unknown", "grey"))
