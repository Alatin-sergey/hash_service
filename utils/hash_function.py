import math
import random
import hashlib

class HashFunc:
    def __init__(self):
        self.a = None
        self.b = None

    def div_method(self, k : int, m : int = 19) -> str:
        if m == 0:
            raise ValueError('m не может быть меньше нуля')
        return str(k % m)
    
    def multi_method(self, k : int, m : int = 19) -> str:
        if m == 0:
            raise ValueError('m не может быть меньше нуля')
        A = (math.sqrt(5) - 1) / 2 
        return str(math.floor(m * ((A * k) % 1)))
    
    def universal_method(self, k : int, m : int = 19) -> str:
        if m == 0:
            raise ValueError('m не может быть меньше нуля')
        p = self.find_next_prime(m)
        if self.a is None or self.b is None:
            self.a = random.randint(1, p-1)
            self.b = random.randint(0, p-1)
        return str(((self.a*k + self.b) % p) % m)

    def hash_with_sha_256(self, k : int) -> str:
        
        k = str(k).encode('utf-8')
        hash_object = hashlib.sha256(k)
        return hash_object.hexdigest()


    def find_next_prime(self, start : int) -> int:
        """
        Находит следующее простое число после заданного числа start.
        """
        def is_prime(n: int) -> bool:
            """
            Проверяет, является ли число простым.
            """
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
    
        if start < 2:
            start = 2  # Начинаем с 2, если start меньше 2
        else:
            start += 1  # Ищем следующее число после start

        while True:
            if is_prime(start):
                return start
            start += 1

    
