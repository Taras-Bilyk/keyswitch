import rules

def get_text(text, mode):
    text_to_return = text
    if mode == "0":
        for x in rules.logic:
            text_to_return = text_to_return.replace(str(x), rules.logic[str(x)])
    if mode == "1":
        for x in rules.logic_eng:
            text_to_return = text_to_return.replace(str(x), rules.logic_eng[str(x)])
    return text_to_return



