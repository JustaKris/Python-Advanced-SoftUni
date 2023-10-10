class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


EMAIL_MIN_LENGTH = 5
VALID_DOMAINS = ['.com', '.bg', '.org', '.net']

while True:
    email = input()
    if email == 'End':
        break

    if len(email.split('@')[0]) < EMAIL_MIN_LENGTH:
        raise NameTooShortError(f'Name must be more than {EMAIL_MIN_LENGTH} characters')

    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    if '.' + email.split('.')[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(VALID_DOMAINS)}')

    print('Email is valid')

'''
abc@abv.bg
'''
'''
peter@gmail.com
petergmail.com
'''
'''
peter@gmail.hotmail
'''
