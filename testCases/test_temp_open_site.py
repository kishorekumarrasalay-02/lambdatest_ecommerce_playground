def test_open_site(setup):
    driver = setup
    driver.get("https://ecommerce-playground.lambdatest.io/")
    assert "Your Store" in driver.title  # Correct page title

