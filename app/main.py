from fastapi import FastAPI
from .schemas import SearchWordRequest
from .search_word import process_serch, generate_soup_letter
from .utils import matriz_14x14_validated

app = FastAPI(title= "Sopa de Letras")

@app.post("/letterSoup")
def look_words(data: SearchWordRequest):
    if not data.matriz:
        data.matriz = generate_soup_letter(words = data.words)

    matriz_14x14_validated(matriz_text_flat=data.matriz)
    results = process_serch(matriz_text_flat=data.matriz, words=data.words)
    return {"matriz utilizada": data.matriz, "Resultado": results}