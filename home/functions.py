import re


def change_link(old):
    text =  old

    m = re.search('d/(.+?)/view', text)
    if m:
        found = m.group(1)
        final = "https://drive.google.com/uc?export=view&id=" + found
        return final
    else:
        return 1


def check_email(mail):
    regex =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, mail)):
        return True
    else: 
        return False

def check_phone(phone):
    regex = r'\b[0-9]{10}\b'
    if(re.fullmatch(regex, phone)):
        return True
    else:
        return False

def check_pin(pin):
    regex = r'\b[0-9]{6}\b'
    if(re.fullmatch(regex, pin)):
        return True
    else:
        return False