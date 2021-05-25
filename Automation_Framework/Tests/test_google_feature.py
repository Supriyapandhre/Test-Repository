from Automation_Framework.Modules.google_search_page import GoogleSearch

def test_search_content_on_google(setup):
    gc = GoogleSearch(setup)
    gc.search_content()
