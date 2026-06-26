import re

def validate_number(number):
    # Sadece rakam içerdiğini ve 10-12 basamak arası olduğunu doğrula
    pattern = r'^\d{10,12}$'
    return bool(re.match(pattern, number))