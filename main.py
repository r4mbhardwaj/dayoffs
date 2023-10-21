from dayoffs.holiday_manager import HolidayManager
from datetime import datetime


def main():
    # Initialize HolidayManager
    holiday_manager = HolidayManager(
        weekly_off_days=[
            "saturday",
            "sunday",
        ],  # assuming you're using lowercase day names consistently,
        # when providing the day names, be consistent in using either all lowercase or all title case
        religious_holidays=["christian"],
        country_locale="US",
        additional_holidays=[datetime(2023, 12, 31), datetime(2023, 1, 1)],
    )

    # Get all holidays
    all_holidays = holiday_manager.get_holidays()
    print(f"All holidays: {all_holidays}")

    # Check a specific date for holiday
    is_holiday = holiday_manager.is_holiday(date=datetime(2023, 12, 25))
    print(f"Is Dec 25, 2023 a holiday? {'Yes' if is_holiday else 'No'}")

    # Get holidays for a specific period
    period_holidays = holiday_manager.get_holidays(
        start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31)
    )
    print(f"Holidays in 2023: {period_holidays}")

    # check if a specific date is a weekly off day
    is_weekly_off = holiday_manager.is_weekly_off(date=datetime.now())
    print(
        f"Is today ({datetime.now().today()}) a weekly off? {'Yes' if is_weekly_off else 'No'}"
    )


if __name__ == "__main__":
    main()
