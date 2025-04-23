import re

_comma_number_re = re.compile(r"(\d)(,)(\d)")
_decimal_number_re = re.compile(r"(\d)\.(\d)")
_pounds_re = re.compile(r"\£([0-9\,]*[0-9]+)")
_dollars_re = re.compile(r"\$([0-9\,]*[0-9]+)")
_ordinal_re = re.compile(r"([0-9]+)(st|nd|rd|th)")
_number_re = re.compile(r"[0-9]+")

def normalize_numbers(text):
    text = _comma_number_re.sub(r"\1\3", text)
    text = _pounds_re.sub(r"\1 pounds", text)
    text = _dollars_re.sub(r"\1 dollars", text)
    text = _ordinal_re.sub(lambda m: _expand_ordinal(m.group(1)), text)
    text = _number_re.sub(lambda m: _expand_number(m.group()), text)
    return text

def _expand_ordinal(match):
    num = int(match)
    suffix = 'th' if 11 <= num % 100 <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(num % 10, 'th')
    return f"{num}{suffix}"

def _expand_number(match):
    try:
        return str(int(match))
    except:
        return match
