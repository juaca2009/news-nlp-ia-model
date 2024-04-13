import logs
import logging
import emoji
import string
import re
import pandas as pd

ACCENT_MARKS = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
NAME_FILE = 'noticias.csv'

def load_data():
    try:
        logging.info('Carga de noticias desde el .csv')
        return pd.read_csv(NAME_FILE, sep='\t')
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{NAME_FILE}'. La ejecución se detendrá.")
        raise SystemExits

def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F700-\U0001F77F"  # alchemical symbols
                           u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                           u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                           u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                           u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                           u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                           u"\U00002702-\U000027B0"  # Dingbats
                           u"\U000024C2-\U0001F251" 
                           "]+", flags=re.UNICODE)
    return re.sub(emoji_pattern, '', text)

def lower_case(text):
    return text.lower()

def delete_symbols(text):
    return text.translate(str.maketrans("", "", string.punctuation + "¿¡‘’“”"))

def replace_unicode(text):
    return ''.join(ACCENT_MARKS.get(caracter, caracter) for caracter in text)

def clean_text(text):
    cleaned_text = text
    cleaned_text = remove_emoji(cleaned_text)
    cleaned_text = lower_case(cleaned_text)
    cleaned_text = delete_symbols(cleaned_text)
    cleaned_text = replace_unicode(cleaned_text)
    return cleaned_text

def execute():
    df = load_data()
    logging.info('Limpieza de las noticias')
    df['title'] = df['title'].apply(clean_text)
    return df['title'].tolist()