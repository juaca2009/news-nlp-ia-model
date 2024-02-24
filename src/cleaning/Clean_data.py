import pandas as pd

NAME_FILE = 'noticias.csv'
CLEAN_FILE = '../model/noticias.csv'


def load_data():
    try:
        return pd.read_csv(NAME_FILE, sep='\t')
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{NAME_FILE}'. La ejecución se detendrá.")
        raise SystemExits
    
def save_data(data_frame):
    try:
        data_frame.to_csv(CLEAN_FILE, index=False)
    except FileNotFoundError:
        print(f"Error: No se encontró la ruta '{CLEAN_FILE}'. La ejecución se detendrá.")
        raise SystemExits
    

if __name__ == "__main__":
    df = load_data()