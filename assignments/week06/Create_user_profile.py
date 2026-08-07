def create_user_profile(username, age=18, premium=False):
    if premium == True:
        status = "Premium User"
    else:
        status = "Standard User"
    return f"{username} (age: {age}) - {status}"
print(create_user_profile("Boonchoo", 48))
print(create_user_profile("Manee"))
print(create_user_profile("Piti", 23, True))