import os
import random
from datetime import datetime
import string

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 6

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    random_name = random.randint(1,5911999129)
    name, ext = get_filename_ext(filename)
    final_filename = f'{name}_{random_name}{ext}'

    today = datetime.now()
    today_path = today.strftime("%Y/%m/%d")

    return f'products/{today_path}/{final_filename}'

def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))