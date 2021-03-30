import string    
import random 


def random_code(value):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = value))    
    return ran
