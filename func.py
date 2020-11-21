def get_sum(one, two, delimiter='&'):
    return f'{str(one.upper())} {delimiter} {str(two.upper())}'
x = get_sum('Learn', 'Python')
print(x)
