import emoji

def remove_emoji(text):
    return ''.join(c for c in text if c not in emoji.UNICODE_EMOJI)