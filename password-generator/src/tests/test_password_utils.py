from utils.password_utils import generate_password, check500_password_strength

def test_generate_password():
    pwd = generate_password()
    assert len(pwd) == 12
    assert any(c.isupper() for c in pwd)
    assert any(c.islower() for c in pwd)
    assert any(c.isdigit() for c in pwd)
    assert any(c in "!@#$%^&*()" for c in pwd)

def test_check_password_strength():
    score, (strength, color) = check_password_strength("Aa1!Bb2@Cc3#")
    assert score >= 4
    assert strength in ["Very Strong", "Excellent"]
