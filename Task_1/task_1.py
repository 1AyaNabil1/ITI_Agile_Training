def check_length(Password):
    if len(Password) <= 5:
        raise ValueError(
            "Password is too short. It must be at least 6 characters long."
        )


def check_special(Password):
    if not ("&" in Password and "_" in Password):
        raise ValueError("Password must contain both '&' and '_'.")


def check_numbers(Password):
    if not any(c.isdigit() for c in Password):
        raise ValueError("Password must contain at least one number.")


def test_password(Password):
    try:
        check_length(Password)
        check_special(Password)
        check_numbers(Password)
        print("Valid password:", Password)
    except ValueError as e:
        print("Invalid password:", Password, "-", str(e))


# Test cases
test_password("_ayanabil7")  # Valid password
test_password("abc&1")  # Too short, invalid
test_password("abcdef")  # Missing '&', '_', and numbers
test_password("&_abcdef")  # Missing numbers
test_password("&_12345")  # Valid password
