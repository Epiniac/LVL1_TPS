import re

def check_length(password):
    """Check the length of the password."""
    if len(password) < 8:
        return False, "Password should be at least 8 characters long."
    return True, None

def check_common_patterns(password):
    """Check if password contains common patterns like '123456'."""
    common_passwords = ["123456", "password", "123456789", "qwerty", "abc123"]
    for common in common_passwords:
        if common in password.lower():
            return False, "Password is too common."
    return True, None

def check_complexity(password):
    """Check for character complexity: uppercase, lowercase, numbers, special chars."""
    lower = re.compile(r'[a-z]')
    upper = re.compile(r'[A-Z]')
    digit = re.compile(r'\d')
    special = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    
    if not lower.search(password):
        return False, "Password should contain at least one lowercase letter."
    if not upper.search(password):
        return False, "Password should contain at least one uppercase letter."
    if not digit.search(password):
        return False, "Password should contain at least one digit."
    if not special.search(password):
        return False, "Password should contain at least one special character."
    
    return True, None

def password_strength(password):
    """Evaluate password strength."""
    checks = [
        check_length(password),
        check_common_patterns(password),
        check_complexity(password)
    ]
    
    complexity = ["Very Weak","Weak", "Medium", "Strong"]
    
    point = 0
    for check, message in checks:
        if not check:
            return complexity[point], message
        point += 1
    
    return complexity[point], "Great Job!"
    
    

def main():
    """Main function to test password strength."""
    password = input("Enter password: ")
    strength, message = password_strength(password)
    print(f"Password strength: {strength}")
    print(f"Suggestions: {message}")

if __name__ == "__main__":
    main()
