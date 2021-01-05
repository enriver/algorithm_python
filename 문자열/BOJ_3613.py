# java vs c++ - S5

import sys

# long_and_mnemonic_identifier -> longAndMnemonicIdentifier
def to_java(word):
    if '__' in word: # 언더바가 2개 이상 나오면 에러
        return 'Error!'
    
    if word[0]=='_' or word[-1]=='_' : # 언더바가 맨앞 또는 맨뒤에 나오면 에러
        return 'Error!'
    
    if word.islower()==False : # 언더바가 있지만 대문자를 포함할경우 에러
        return 'Error!'

    word=word.replace('_', ' ').title().replace(' ','')
    word=word.replace(word[0],word[0].lower(),1)

    return word

# longAndMnemonicIdentifier -> long_and_mnemonic_identifier
def to_cpp(word): 
    if word[0].isupper()==True: # 첫글자가 대문자면 에러
        return 'Error!'

    result=''

    for i in word:
        if i.isupper()==True:
            result+='_'+i.lower()
        else:
            result+=i

    return result


val=sys.stdin.readline().strip()

if '_' in val :
    print(to_java(val))

else:
    print(to_cpp(val))