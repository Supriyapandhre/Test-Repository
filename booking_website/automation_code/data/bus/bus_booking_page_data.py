# Test data
travel_date = 20
source_location = "Pune"
source_area = "Swargate"

# Locators
source_element = ("txtSource", "id")
source_dropdown_option = (f"//li[contains(text(), '{source_area}, ')]/strong[text()='{source_location}']", "xpath")
destination_element = ("txtDestination", "id")
depart_date_element = (f"//span[text()='{travel_date}']", "xpath")
search_button = ("//button[@class='D120_search_btn searchBuses']", "xpath")
