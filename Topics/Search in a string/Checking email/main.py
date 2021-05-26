def check_email(email):
    spaces = " " not in email
    arobase = "@" in email
    dot1 = "@." not in email
    dot2 = "." in email
    if arobase and dot2:
        dot3 = email.rindex("@") < email.rindex(".")
    else:
        dot3 = False
    return spaces and arobase and dot1 and dot2 and dot3
