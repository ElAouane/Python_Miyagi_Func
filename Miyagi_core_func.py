def sensei(string):
    return 'sensei' not in string

def block_blocking(string):
    return 'block' in string or 'blocking' in string

def question(string):
    return '?' in string

def exit_(string):
    return 'sensei, i am at peace' in string