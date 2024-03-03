import pandas as pd

NAME_FILE = 'noticias.csv'

def load_data():
    try:
        return pd.read_csv(NAME_FILE, sep=',')
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{NAME_FILE}'. La ejecución se detendrá.")
        raise SystemExits
    
if __name__ == "__main__":
    df = load_data()
    df['title'] = df['title'].apply(lambda x: x.split(' '))

    #para obtener lista con listas de strings
    #columna_title_lista = df['title'].tolist() 
    