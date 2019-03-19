from .models import FileData
import random

def generate_token():
    for _ in range(10):
        token = str(random.randint(1000, 9999))
        if not FileData.objects.filter(token=token):
            return token
    else:
        raise ValueError('Too many attempts to generate the code')