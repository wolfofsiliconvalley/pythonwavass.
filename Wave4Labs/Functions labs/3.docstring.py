def readable_timedelta(days):
    """convert days into weeks and days
    Args:
    days (int): number of days to convert

    Parameters:
    days -- number of days to convert (int)

    Returns:
    string of the number of weeks and days included in days"""

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {}  day(s)".format(weeks, remainder)
