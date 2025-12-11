import re

def clean(text):
    # Remove HTML tags and unwanted artifacts
    text = re.sub(r"<.*?>", "", text)
    return text.strip()
