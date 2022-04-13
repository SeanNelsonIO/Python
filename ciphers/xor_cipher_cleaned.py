
from __future__ import annotations


class XORCipher:
    def __init__(self, key: int = 0):
        

        
        self.__key = key

    def encrypt(self, content: str, key: int) -> list[str]:
        

        
        assert isinstance(key, int) and isinstance(content, str)

        key = key or self.__key or 1

        
        key %= 255

        return [chr(ord(ch) ^ key) for ch in content]

    def decrypt(self, content: str, key: int) -> list[str]:
        

        
        assert isinstance(key, int) and isinstance(content, list)

        key = key or self.__key or 1

        
        key %= 255

        return [chr(ord(ch) ^ key) for ch in content]

    def encrypt_string(self, content: str, key: int = 0) -> str:
        

        
        assert isinstance(key, int) and isinstance(content, str)

        key = key or self.__key or 1

        
        while key > 255:
            key -= 255

        
        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans

    def decrypt_string(self, content: str, key: int = 0) -> str:
        

        
        assert isinstance(key, int) and isinstance(content, str)

        key = key or self.__key or 1

        
        while key > 255:
            key -= 255

        
        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans

    def encrypt_file(self, file: str, key: int = 0) -> bool:
        

        
        assert isinstance(file, str) and isinstance(key, int)

        try:
            with open(file) as fin:
                with open("encrypt.out", "w+") as fout:

                    
                    for line in fin:
                        fout.write(self.encrypt_string(line, key))

        except OSError:
            return False

        return True

    def decrypt_file(self, file: str, key: int) -> bool:
        

        
        assert isinstance(file, str) and isinstance(key, int)

        try:
            with open(file) as fin:
                with open("decrypt.out", "w+") as fout:

                    
                    for line in fin:
                        fout.write(self.decrypt_string(line, key))

        except OSError:
            return False

        return True


























