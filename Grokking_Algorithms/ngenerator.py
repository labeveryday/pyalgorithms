from faker import Faker
from itertools import repeat

def get_names(number):
    """
    Generates a list of Names 
    (First Name, Last Name, both, Male, or Female)
    Args:
        number (int): Number of names
    """
    name_list = []
    faker = Faker()
    for _ in repeat(None, int(number)):
        name_list.append(faker.first_name())
    return name_list

def get_random_numbers(number):
    """
    Generates a random list of Numbers
    Args:
        number (int): Number of numbers
    """
    number_list = []
    faker = Faker()
    for _ in repeat(None, int(number)):
        number_list.append(faker.random_number())
    return number_list

def get_number_list(number):
    """
    Generates a random list of Numbers
    Args:
        number (int): Number of numbers
    """
    number_list = []
    for i in range(1, number + 1):
        number_list.append(i)
    return number_list 

def get_ipaddress(number, ip_type=None):
    """
    Generates a list of IP Addresses 
    Args:
        number (int): Number of ip addresses
        ip_type (string): Optional - public, private
    """
    ip_list = []
    faker = Faker()
    for _ in repeat(None, int(number)):
        ip_list.append(faker.ipv4_private() if ip_type == 'private'
        else faker.ipv4_public() if ip_type == 'public' else faker.ipv4())
    return ip_list
