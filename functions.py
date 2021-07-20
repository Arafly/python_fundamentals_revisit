from datetime import datetime

# Print the current time
def print_time():
    print('Task completed')
    print(datetime.now())
    print()
    
print_time()

# Functions that accept s dingle parameter
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)
last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)

print ('Your initials are: '+ first_name_initial \
    + last_name_initial)

print('Your initials are: ' \
    + get_initial(first_name) \
    + get_initial(last_name))


# Functions that accept multiple parameters
def get_initial(name, force_uppercae):
    if force_uppercae:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name, False)

print ('Your initials are: '+ first_name_initial)

print('Your initials are: ' \
    + get_initial(first_name, False))


# Named notation function
def error_logger(error_code, error_severity, log_to_db, \
    error_message, source_module):
    print('Oh no error: '+ error_message)
    
first_number = 10
second_number = 5
if (first_number > second_number):
    error_logger(error_code=45, error_severity=1, log_to_db=True, error_message='Second number is greater than first', source_module='my_math_method') 
    