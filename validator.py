def clean_text(value):
    if not isinstance(value, str):
        return ""
    return value.strip()[:8000]

def is_valid_question(value):
    return isinstance(value, str) and bool(value.strip())
