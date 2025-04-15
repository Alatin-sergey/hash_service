from fastapi import FastAPI, HTTPException
from utils.hash_function import HashFunc

import json

app = FastAPI()
hash = HashFunc()



hash_dict : dict[str, object] = {
    'div' : hash.div_method,
    'multi' : hash.multi_method,
    'universal' : hash.universal_method,
    'sha_256' : hash.hash_with_sha_256
}

@app.get("/hash/{method}/{number}")
def hashing(method : str, number : int):
    try:
        return {
            'method' : method,
            'number' : number,
            'hash' : hash_dict[method](number)
            }
    
    except KeyError as e:
        # Обработка ошибок, которые могут возникнуть в методах хеширования
        raise HTTPException(status_code=400, detail='The hashing method is specified incorrectly. Choose from 4 options: div, multi, universal, sha_256.')
    except TypeError as e:
        # Обработка ошибок, которые могут возникнуть в методах хеширования
        raise HTTPException(status_code=422, detail='Enter a number.')
    except Exception as e:
        # Обработка других непредвиденных ошибок
        raise HTTPException(status_code=500, detail='An internal server error has occurred')

