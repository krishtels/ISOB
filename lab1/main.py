from caesar_code import CaesarCode
from vegener_code import VigenereCode



# print(VigenereCode.code('The quick brown fox jumps over 13 lazy dogs.', 'cryptii'))
# print(VigenereCode.decode('Vyc jcqeb qkwep ddq rwdnh wdgi 13 tcqw wwou.', 'cryptii'))
# print(VigenereCode.decode('abababab bababa ababababab', 'ab'))
#

# print('Caesar Code')
# s = input('Enter string')
# k = int(input('Enter k for Caesar code'))
# res = CaesarCode.code(s, k)
# res_dec = CaesarCode.decode(res,k)
# print('Encrypted string: ' + res)
# print('Decrypted string: '+ res_dec)

print('Vigener Code')
s = input('Enter string')
k = input('Enter string k for Vigener code')
res = VigenereCode.code(s, k)
res_dec = VigenereCode.decode(res,k)
print('Encrypted string: ' + res)
print('Decrypted string: '+ res_dec)