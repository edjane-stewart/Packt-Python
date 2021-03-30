def format_customer(first, last, location=None):
    full_name = '{} {}'.format(first, last)
    if location:
        return '{} ({})'.format(full_name, location)
    else:
        return full_name

print(format_customer("John", "Smith"))
print(format_customer("Jane", "Stewart", "New York"))