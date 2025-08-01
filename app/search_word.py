from typing import List, Tuple
import string
import random

direcction_search = [
    (0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)
]

size = 14

def inside_limits(x:int, y:int, rows:int, columns:int)->bool:
    if (x < 0 or x >= rows) or (y < 0 or y >= columns):
        return False
    else:
        return True
    
def serchs_words(matriz: List[List[str]], word: str) ->bool:
    rows = len(matriz)
    columns = len(matriz[0])

    for i in range(rows):
        for j in range(columns):
            for dir_x , dir_y in direcction_search:
                x = i
                y = j
                firt_letter_word = 0

                while(firt_letter_word < len(word) and inside_limits(x=x, y=y, rows=rows, columns=columns) and
                      matriz[x][y].upper() == word[firt_letter_word].upper()):
                    x += dir_x
                    y += dir_y
                    firt_letter_word +=1 

                    if firt_letter_word == len(word):
                        return True
    return False

def process_serch(matriz_text_flat: str, words: List[str]) ->dict:
    matriz_clean = matriz_text_flat.strip()
    lines = matriz_clean.split("\n")
    matriz = []
    results = {"encontrados": [], "no encontrados": []}
    for line in lines:
        row = line.strip().split(",")

        matriz.append(row)

    for word in words:
        if serchs_words(matriz= matriz, word=word):
            results["encontrados"].append(word)
        else:
            results["no encontrados"].append(word)
    
    return results


def generate_soup_letter(words: List[str])->str:
    matriz = []

    for i in range(size):
        row = []

        for j in range(size):
            row.append("")
        
        matriz.append(row)
    
    for word in words:
        word = word.upper()
        inserted = False

        for r in range(14):
            dir_x,dir_y = random.choice(direcction_search)
            if dir_x == 0 and dir_y == 0:
                continue

            start_x = random.randint(0, size - 1)
            start_y = random.randint(0, size - 1)

            end_x = start_x + dir_x * (len(word) - 1)
            end_y = start_y + dir_y * (len(word) - 1)

            if not (0 <= end_x < size and 0 <= end_y < size):
                continue

            can_insert = True
            for i in range(len(word)):
                x = start_x + dir_x * i
                y = start_y + dir_y * i
                actual_word = matriz[x][y]
                
                if actual_word != "" and actual_word != word[i]:
                    can_insert = False
                    break
            
            if can_insert:
                for i in range(len(word)):
                    x = start_x + dir_x * i
                    y = start_y + dir_y * i
                    matriz[x][y] = word[i]
                inserted = True
                break

            if not inserted:
                print(f"no se pudo insertar la palabra: {word}")

    for f in range(size):
        for c in range(size):
            if matriz[f][c] == "":
                matriz[f][c] = random.choice(string.ascii_uppercase)

    row_text = []

    for r in matriz:
        letter_row = ",".join(r)

        row_text.append(letter_row)

    final_row = "\n".join(row_text)

    return final_row



