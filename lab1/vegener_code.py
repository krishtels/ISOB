class VigenereCode:
    @staticmethod
    def get_code(letter):
        return ord('A') if 'A' <= letter <= 'Z' else ord('a')

    @staticmethod
    def code(s: str, k: str):
        ans = ""
        k *= len(s) // len(k) + 1
        for i in range(len(s)):
            if 'A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'z':
                ans += chr(VigenereCode.get_code(s[i]) + ((ord(s[i]) - VigenereCode.get_code(s[i]) + ord(k[i]) - VigenereCode.get_code(k[i])) % 26))
            else:
                ans += s[i]
        return ans

    @staticmethod
    def decode(s: str, k: str):
        ans = ""
        k *= len(s) // len(k) + 1
        for i in range(len(s)):
            if 'A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'z':
                ans += chr(VigenereCode.get_code(s[i]) + ((ord(s[i]) - VigenereCode.get_code(s[i]) - ord(k[i]) + VigenereCode.get_code(k[i]) + 26) % 26))
            else:
                ans += s[i]
        return ans