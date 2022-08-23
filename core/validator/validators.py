from django.core.validators import RegexValidator

phone_validator = RegexValidator(regex='^(\+\d{1,3})?,?\s?\d{8,13}',
                                         message="Phone number must be entered in the format: '+999999999'. "
                                                 "Up to 15 digits allowed.")
