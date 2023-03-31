def addition(*args):  # beliebige Parameter, müssen als letztes in der Aufzählung der Parameter stehen
    result = 0
    for arg in args:
        result += arg
    return result


print(addition(3, 6, 88, 12, 34))

nums = [4, 7, 5, 9, 12, 34, 55]
print(addition(*nums))

