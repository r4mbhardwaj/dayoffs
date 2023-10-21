import calendar


class HolidayManager:
    def __init__(
        self, weekly_off_days, religious_holidays, country_locale, additional_holidays
    ):
        """Initializes the HolidayManager."""
        self.weekly_off_days = [
            day.lower() for day in weekly_off_days
        ]  # Convert to lowercase for comparison
        self.religious_holidays = religious_holidays
        self.country_locale = country_locale
        self.additional_holidays = additional_holidays
        # TODO: add error checks, e.g., verify that weekly_off_days are valid day names

    def is_weekly_off(self, date):
        """Checks if the given date is a weekly off day based on user's settings."""
        return calendar.day_name[date.weekday()].lower() in self.weekly_off_days

    def get_holidays(self, start_date=None, end_date=None):
        """Returns all holidays in the given date range."""
        # TODO: implement the logic to get public holidays, religious holidays, and weekly off days.
        # If start_date and end_date are None, return all holidays.

    def is_holiday(self, date):
        """Checks if the given date is a holiday."""
        # TODO: implement the logic to check if date is a public holiday, religious holiday, or weekly off day
        # Use the is_weekly_off method to check if the date is a weekly off day
