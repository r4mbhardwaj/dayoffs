import datetime


def is_valid_date(date_string, format="%Y-%m-%d"):
    """
    Checks if the provided string is a valid date in the provided format.
    """
    try:
        datetime.datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False
