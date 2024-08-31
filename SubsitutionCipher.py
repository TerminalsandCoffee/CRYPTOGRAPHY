from collections import Counter
import string

def decrypt(ciphertext, key):
    return ciphertext.translate(str.maketrans(key, string.ascii_lowercase))

ciphertext = "zorxv dzh yvtrmmrmt gl tvg evib grivw lu hrggrmt yb svi hrhgvi lm gsv yzmp zmw lu szermt mlgsrmt gl wl lmxv li gdrxv hsv szw kvvkvw rmgl gsv yllp svi hrhgvi dzh ivzwrmt yfg rg szw ml krxgfivh li xlmevihzgrlmh rm rg zmw dszg rh gsv fhv lu z yllp gslftsg zorxv drgslfg krxgfivh li xlmevihzgrlm hl hsv dzh xlmhrwvirmt rm svi ldm nrmw zh dvoo zh hsv xlfow uli gsv slg wzb nzwv svi uvvo evib hovvkb zmw hgfkrw dsvgsvi gsv kovzhfiv lu nzprmt z wzrhb xszrm dlfow yv dligs gsv gilfyov lu tvggrmt fk zmw krxprmt gsv wzrhrvh dsvm hfwwvmob z dsrgv Izyyrg drgs krmp vbvh izm xolhv yb svi"

# Frequency analysis
freq = Counter(ciphertext.replace(" ", "").lower())
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print("Most common letters:", sorted_freq[:6])

# Common English letters by frequency
eng_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ".lower()

# Initial mapping based on frequency
key = {cipher: plain for cipher, _ in sorted_freq[:26] for plain in eng_freq}

# Manual adjustments based on common words and patterns
key['v'] = 'e'
key['g'] = 't'
key['s'] = 'h'
key['r'] = 'i'
key['m'] = 'n'
key['w'] = 'd'
key['z'] = 'a'
key['l'] = 'o'
key['h'] = 's'
key['x'] = 'c'
key['e'] = 'v'
key['i'] = 'r'
key['y'] = 'b'
key['p'] = 'k'
key['n'] = 'm'
key['d'] = 'w'
key['u'] = 'f'
key['f'] = 'u'
key['b'] = 'y'
key['k'] = 'p'
key['I'] = 'R'

plaintext = decrypt(ciphertext, ''.join(key.keys()))
print("\nDecrypted text:")
print(plaintext)
