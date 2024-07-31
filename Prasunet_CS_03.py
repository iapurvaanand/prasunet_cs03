import re

def password_strength(password):

    strength_score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be 8 characters or long.")
    elif len(password) >= 8:
        strength_score += 1
        feedback.append("Password length is good.")

    # uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1
        feedback.append("Password has uppercase letters.")
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1
        feedback.append("Password has lowercase letters.")
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # numbers
    if re.search(r'[0-9]', password):
        strength_score += 1
        feedback.append("Password has numbers.")
    else:
        feedback.append("Password should include at least one number.")

    # characters
    if re.search(r'[\W_]', password):
        strength_score += 1
        feedback.append("Password has special characters.")
    else:
        feedback.append("Password should include at least one special character.")

    # overall strength
    if strength_score == 5:
        feedback.append("Password strength: Strong")
    elif strength_score >= 3:
        feedback.append("Password strength: Moderate")
    else:
        feedback.append("Password strength: Weak")

    return feedback

# Example usage
password = input("Enter your password: ")
feedback = password_strength(password)
print("\n".join(feedback)