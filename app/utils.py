from fastapi import HTTPException


def matriz_14x14_validated(matriz_text_flat: str):
    matriz_clean = matriz_text_flat.strip()
    lines = matriz_clean.split("\n")
    matriz = []

    for line in lines:
        row = line.strip().split(",")

        matriz.append(row)

    if len(matriz) != 14:
        raise HTTPException(status_code=400, detail= "La matriz debe tener 14 filas")
    
    for line in matriz:
        if len(line) != 14:
            raise HTTPException(status_code=400, detail= "Cada fila debe tener 14 letras")
        


