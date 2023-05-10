class CaesarCode:
    @staticmethod
    def get_code(letter):
        return ord('A') if 'A' <= letter <= 'Z' else ord('a')

    @staticmethod
    def code(s: str, k: int):
        ans = ""
        for letter in s:
            if 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':
                ans += chr(CaesarCode.get_code(letter) + ((ord(letter) - CaesarCode.get_code(letter) + k) % 26))
            else:
                ans += letter
        return ans

    @staticmethod
    def decode(s: str, k: int):
        ans = ""
        for letter in s:
            if 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':
                ans += chr(CaesarCode.get_code(letter) + ((ord(letter) - CaesarCode.get_code(letter) - k + 26) % 26))
            else:
                ans += letter
        return ans