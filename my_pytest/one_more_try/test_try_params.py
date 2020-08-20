def test_e2e(platform, dsn):
    print(platform)
    assert platform == "Android"
    print(dsn)
    assert dsn == "A12345"