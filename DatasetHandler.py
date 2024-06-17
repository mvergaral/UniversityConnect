import pandas as pd

def filter_chunk(chunk, column_name, value):
    if column_name in chunk.columns:
        chunk_filtered = chunk[chunk[column_name] == value]
        chunk_filtered = chunk_filtered[['mrun', 'nomb_inst', 'nomb_sede', 'comuna_sede']]
        return chunk_filtered
    else:
        print(f"'{column_name}' is not present in the columns of the current chunk.")
        return None

def normalize_column_names(chunk):
    chunk.columns = chunk.columns.str.lower()
    return chunk

def select_columns(chunk, columns):
    return chunk[columns]

def merge_dataframes(df_a, df_b, on):
    return pd.merge(df_a, df_b, on=on)

def save_dataframe(df, filename):
    df.to_csv(filename, index=False)
    print("The file has been created successfully.")

def main():
    archivo_a = "20230802_Matrícula_Ed_Superior_2023_PUBL_MRUN.csv"
    archivo_b = "20240404_Notas_y_Egresados_EnseñanzaMedia_2022_WEB.csv"
    archivo_c = "20240404_Notas_y_Egresados_EnseñanzaMedia_2021_WEB.csv"
    archivo_d = "20240404_Notas_y_Egresados_EnseñanzaMedia_2020_WEB.csv"
    chunk_size = 100000

    resultados_a = []
    resultados_b = []

    for chunk_a in pd.read_csv(archivo_a, chunksize=chunk_size, delimiter=';', header=0, encoding="utf-8"):
        try:
            chunk_a_filtered = filter_chunk(chunk_a, 'comuna_sede', 'VALPARAISO')
            chunk_a_filtered = filter_chunk(chunk_a_filtered , 'nomb_inst', 'PONTIFICIA UNIVERSIDAD CATOLICA DE VALPARAISO')
            if chunk_a_filtered is not None:
                resultados_a.append(chunk_a_filtered)
        except UnicodeDecodeError as e:
            print("Error in chunk:", e)
            print("Chunk contents:", chunk_a)
            print("Error occurred in row:", chunk_a.index)

    df_a_filtered = pd.concat(resultados_a, ignore_index=True)

    for chunk_b in pd.read_csv(archivo_b, chunksize=chunk_size, delimiter=';', header=0):
        try:
            chunk_b_normalized = normalize_column_names(chunk_b)
            chunk_b_filtered = select_columns(chunk_b_normalized, ['mrun', 'nom_com_rbd'])
            chunk_b_filtered = filter_chunk(chunk_b_filtered, 'nom_reg_rbd_a', 'VALPO')
            resultados_b.append(chunk_b_filtered)
        except UnicodeDecodeError as e:
            print("Error in chunk:", e)
            print("Chunk contents:", chunk_b)
            print("Error occurred in row:", chunk_b.index)

    for chunk_c in pd.read_csv(archivo_c, chunksize=chunk_size, delimiter=';', header=0):
        try:
            chunk_c_normalized = normalize_column_names(chunk_c)
            chunk_c_filtered = select_columns(chunk_c_normalized, ['mrun', 'nom_com_rbd'])
            resultados_b.append(chunk_c_filtered)
        except UnicodeDecodeError as e:
            print("Error in chunk:", e)
            print("Chunk contents:", chunk_c)
            print("Error occurred in row:", chunk_c.index)

    for chunk_d in pd.read_csv(archivo_d, chunksize=chunk_size, delimiter=';', header=0):
        try:
            chunk_d_normalized = normalize_column_names(chunk_d)
            chunk_d_filtered = select_columns(chunk_d_normalized, ['mrun', 'nom_com_rbd'])
            resultados_b.append(chunk_d_filtered)
        except UnicodeDecodeError as e:
            print("Error in chunk:", e)
            print("Chunk contents:", chunk_d)
            print("Error occurred in row:", chunk_d.index)

    df_b_filtered = pd.concat(resultados_b, ignore_index=True)

    df_resultado = merge_dataframes(df_a_filtered, df_b_filtered, 'mrun')

    save_dataframe(df_resultado, 'PUCV20222023.csv')

if __name__ == "__main__":
    main()