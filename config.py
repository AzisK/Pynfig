EMAIL = "very_important_stakeholders@gmail.com"

PASSWORD = "dummy_password_for_code_navigation_and_easy_parsing"

try:
    from config_local import EMAIL, PASSWORD
    # or
    # from config_local import *
except ImportError:
    pass
