# creating a module for reuse in another script
# module is meant to reverse and mirror any word inserted.
def reverse():
    string = 'Manipulator'
    string2 = ''
    for i in string:
        string2 = i + string2
    print(string2)
    return reverse


def mirror():
    string = 'Gentility'
    string2 = ''
    for i in string:
        string2 = i + string2
    print(string, string2)
    return mirror

