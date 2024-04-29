import pyHolidays as ph

def test_nyd():
    assert ph.calculate_new_years_observed(2024) == '2024-01-01'

def test_mlk():
    assert ph.calculate_mlk_day(2025) == '2025-01-20'

def test_wash():
    assert ph.calculate_washington_bday(2026) == '2026-02-16'

def test_gf():
    assert ph.calculate_good_friday(2024) == '2024-03-29'

def test_mem():
    assert ph.calculate_memorial_day(2025) == '2025-05-26'

def test_june():
    assert ph.calculate_juneteenth_observed(2026) == '2026-06-19'

def test_ind():
    assert ph.calculate_independence_day_observed(2026) == '2026-07-03'

def test_lab():
    assert ph.calculate_labor_day(2025) == '2025-09-01'

def test_thank():
    assert ph.calculate_thanksgiving(2024) == '2024-11-28'

def test_xmas():
    assert ph.calculate_christmas(2025) == '2025-12-25'

def test_vet():
    assert ph.calculate_veterans_day_observed(2024) == '2024-11-11'

def test_col():
    assert ph.calculate_columbus_day(2024) == '2024-10-14'
    