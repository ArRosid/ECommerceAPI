import os
import random
from datetime import datetime


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