def removeNumbers(text):
    modified_string = ''.join([i for i in str(text) if not i.isdigit()])
    return modified_string

def leaveNumbers(text):
    modified_string = ''.join([i for i in str(text) if i.isdigit()])
    return modified_string
