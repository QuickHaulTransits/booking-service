import pytest
from app import validate_phone, validate_date_time, calculate_booking_amount, get_estimated_delivery
from datetime import datetime, timedelta

def test_validate_phone():
    assert validate_phone("9876543210") is True
    assert validate_phone("6123456789") is True
    assert validate_phone("1234567890") is False
    assert validate_phone("987654321") is False
    assert validate_phone("98765432100") is False

def test_validate_date_time():
    future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    past_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    
    assert validate_date_time(future_date, "10:00") is True
    assert validate_date_time(past_date, "10:00") is False

def test_calculate_booking_amount():
    # Test bike light weight
    res = calculate_booking_amount("bike", 10, "light")
    # base_rate (30) + per_km (2) * 10 = 50
    # gst = 50 * 0.18 = 9
    # total = 59
    assert res["base_amount"] == 50.0
    assert res["gst_amount"] == 9.0
    assert res["total_amount"] == 59.0

    # Test truck heavy weight
    res = calculate_booking_amount("truck", 100, "heavy")
    # base_rate (500) + per_km (40) * 100 = 4500
    # gst = 4500 * 0.18 = 810
    # total = 5310
    assert res["base_amount"] == 4500.0
    assert res["gst_amount"] == 810.0
    assert res["total_amount"] == 5310.0

def test_get_estimated_delivery():
    assert get_estimated_delivery("bike") == "2-4 hours"
    assert get_estimated_delivery("van") == "4-6 hours"
    assert get_estimated_delivery("truck") == "6-8 hours"
    assert get_estimated_delivery("unknown") == "4-6 hours"
