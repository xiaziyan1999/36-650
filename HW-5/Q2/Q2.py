def remove_punctuations(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in string:
       if char not in punctuations:
           no_punct = no_punct + char

    return no_punct

remove_punctuations("Hello in 36-650, & other MSP courses")