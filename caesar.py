#determine a lettrs position in the alpahbet
def alphabet_position(letter):
    if ord(letter) <= 90:
        new_letter = ord(letter) - 65
    if ord(letter) >= 97:
        new_letter = ord(letter) -97
    return new_letter

#takes a letter and encrypt it by rotating a certain number of spaces forward.

def rotate_character(s, rotation):
    s_rotated = ""
    for i in s:
        if i.isalpha():
            s_encrypt = ord(i) + rotation
            if s_encrypt in range(91, 97):
                s_encrypt = s_encrypt - 26
                s_encrypt = chr(s_encrypt)
                s_rotated = s_rotated + s_encrypt
            elif rotation == 26:
                s_rotated = s_rotated + i
            elif ord(i) < 91 and s_encrypt > 90:
                s_encrypt = s_encrypt - 26
                s_encrypt = chr(s_encrypt)
                s_rotated = s_rotated + s_encrypt
            elif s_encrypt > ord("z"):
                s_encrypt = s_encrypt - 26
                s_encrypt = chr(s_encrypt)
                s_rotated = s_rotated + s_encrypt
            elif s_encrypt < ord("z"):
                s_encrypt = s_encrypt
                s_encrypt = chr(s_encrypt)
                s_rotated = s_rotated + s_encrypt

        else:
            s_rotated = s_rotated + i
    return s_rotated

def encrypt(text, rot):
        x = rotate_character(text, rot)
        return x
