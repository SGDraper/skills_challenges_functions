from datetime import datetime

def check_date_for_access(date):
    dob = datetime.strptime(date, "%Y-%m-%d")
    age = (datetime.now() - dob).days // 365
    # message = f"Access denied, you are {age}, you must be at least 16"
    if age < 16:
        return f"Access denied, you are {age}, you must be at least 16"
    elif age > 16:
        return "Access granted"
    else:
        try:
            datetime.strptime(date,"%Y-%m-%d")
            return "Invalid format"
        except ValueError:
            return False