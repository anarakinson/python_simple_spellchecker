from turn_layout import turn_layout
from word_separate2 import split
import hunspell

# import pandas as pd
import re


hobj_ru = hunspell.Hunspell(
    "Russian",
    hunspell_data_dir='D:/Coding/jupy_notebooks/CP-2023/Dictionaries/',
    disk_cache_dir='D:/Coding/jupy_notebooks/CP-2023/hunspell_cache/'
)
hobj_eng = hunspell.Hunspell(
    "English (American)",
    hunspell_data_dir='D:/Coding/jupy_notebooks/CP-2023/Dictionaries/',
    disk_cache_dir='D:/Coding/jupy_notebooks/CP-2023/hunspell_cache/'
)



def spellcheck(data):

    variants = {
        0 : [], 
        1 : [],
        2 : [], 
        3 : [],
    }
    
    
    for word in data.split(" "):    

        if word.isnumeric():
            for i in range(4):
                variants[i].append(word)
            continue

        suggest = hobj_ru.suggest(f'{word}') 

        if hobj_ru.spell(f'{word}') == False:
            if len(re.findall(r'[A-z]+', word )) > 0:

                suggest = hobj_eng.suggest(f'{word}')
                word_turned = turn_layout(word)

                if hobj_eng.spell(f'{word}'):
                    for i in range(4):
                        variants[i].append(word)
                    continue

                elif hobj_ru.spell(word_turned):
                    for i in range(4):
                        variants[i].append(word_turned)
                    continue

                elif len(suggest) > 0:
                    for i in range(len(suggest)):
                        if i > 3:
                            break
                        variants[i].append(suggest[i])
                    continue
                
                else:
                    word = word_turned
                    
            elif len(suggest) == 0: 
                splitted_words = " ".join(split(word))        
                for i in range(4):
                    variants[i].append(splitted_words)
        
        if len(suggest) > 0:
            for i in range(len(suggest)):
                if i > 3:
                    break
                variants[i].append(suggest[i])

    for i in range(4):
        variants[i] = " ".join(variants[i])
    return variants


if __name__ == "__main__":
    data = "приветдрузья hello rfr ltkf дывочка"

    print(spellcheck(data))
    