password = "jhjd8901290"

password_length = len(password)

if password_length < 6:
    strength = "Week"
elif password_length <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Your Password is " + strength)