import pyContributions as pc

def test_401k():
    assert pc.contribution_max("401k", "2022") == '20500'

def test_401kCatchUp():
    assert pc.contribution_max("401kCatchUp", '2022') == '6500'

def test_SIMPLE():
    assert pc.contribution_max("SIMPLE", '2022') == '20500'

def test_SIMPLECatchUp():
    assert pc.contribution_max("SIMPLECatchUp", '2022') == '3000'

def test_bad_value():
    assert pc.contribution_max("Foo", '2022') is None