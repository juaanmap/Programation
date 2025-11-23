def is_substring(text1, text2):
    return text2 in text1
def alphabetical_first(text1, text2):
    if text1 < text2:
        return text1
    else:
        return text2
