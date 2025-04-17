from typing import List

class EncodeDecode:
    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + '#' + word
        return result

    def decode(self, encodedStr: str) -> List[str]:
        result = []
        i = 0

        while i < len(encodedStr) - 1:

            numOfChars = ''
            # find num of characters in word
            while encodedStr[i] != '#':
                numOfChars += encodedStr[i]
                i += 1
            i += 1

            # create word
            numOfChars = int(numOfChars)
            word = encodedStr[i: i + numOfChars]

            # add word to list
            i += numOfChars
            result.append(word)
 
        return result

list1 = ["neet","code","love","you"]

encodeDecodeStr = EncodeDecode()
encoded = encodeDecodeStr.encode(list1)
decoded = encodeDecodeStr.decode(encoded)

print("Encoded str: ", encoded) # " Encoded str:  4#neet4#code4#love3#you "
print("Decoded string: ", decoded) # " ['neet', 'code', 'love', 'you'] "
