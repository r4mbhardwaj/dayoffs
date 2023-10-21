import pytest
from datetime import datetime
from dayoffs.holiday_manager import HolidayManager


def test_is_weekly_off():
    holiday_manager = HolidayManager(
        weekly_off_days=["monday"],
        religious_holidays=[],
        country_locale="US",
        additional_holidays=[],
    )
    assert holiday_manager.is_weekly_off(datetime(2023, 10, 22)) == False
    assert holiday_manager.is_weekly_off(datetime(2023, 10, 23))


def test_holiday_manager_initialization():
    holiday_manager = HolidayManager(
        weekly_off_days=["monday", "tuesday"],
        religious_holidays=["christian"],
        country_locale="US",
        additional_holidays=[datetime(2022, 12, 12)],
    )
    assert holiday_manager.weekly_off_days == ["monday", "tuesday"]
    assert holiday_manager.religious_holidays == ["christian"]
    assert holiday_manager.additional_holidays == [datetime(2022, 12, 12)]
