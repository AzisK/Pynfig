```python
# config_local.py
EMAIL = "me_myself_and_i@gmail.com"

---

# config.py
EMAIL = "very_important_stakeholders@gmail.com"

try:
    import config_local import *
except ImportError:
    pass

===

# config.py
EMAIL = "very_important_person_1@mail.com very_important_person_1@mail.com very_important_person_1@mail.com".split()

===

# config_local.py
PASSWORD = "my_local_machine_password"

---

# config.py
PASSWORD = "dummy_password_for_code_navigation_and_easy_parsing"

try:
    import config_local import *
except ImportError:
    pass
```
