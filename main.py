# 초성 리스트 19
First_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트 21
Middle_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성 리스트 28
Last_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def korean_to_be_englished(korean_word):
    r_lst = []
    for w in list(korean_word.strip()):
        if '가'<=w<='힣':
            ## 588개 마다 초성이 바뀜. 
            ch1 = (ord(w) - ord('가'))//588
            ## 중성은 총 28가지 종류
            ch2 = ((ord(w) - ord('가')) - (588*ch1)) // 28
            ch3 = (ord(w) - ord('가')) - (588*ch1) - 28*ch2
            r_lst.append([First_LIST[ch1], Middle_LIST[ch2], Last_LIST[ch3]])
        else:
            r_lst.append([w])
    return r_lst

def abbreviation(separated_word):
    result_word.clear()
    put = 0
    for i in range(len(separated_word)-1):
        if(separated_word[i][2] == 'ㄱ' and separated_word[i+1][0] == 'ㅎ'):
            separated_word[i][2] = ' '
            separated_word[i+1][0] = 'ㅋ'
            put=1
        elif(separated_word[i][2] == 'ㄷ' and separated_word[i+1][0] == 'ㅎ'):
            separated_word[i][2] = ' '
            separated_word[i+1][0] = 'ㅌ'
            put=1
        elif(separated_word[i][2] == 'ㅈ' and separated_word[i+1][0] == 'ㅎ'):
            separated_word[i][2] = ' '
            separated_word[i+1][0] = 'ㅊ'
            put=1
        elif(separated_word[i][2] == 'ㅂ' and separated_word[i+1][0] == 'ㅎ'):
            separated_word[i][2] = ' '
            separated_word[i+1][0] = 'ㅍ'
            put=1
    for i in range(len(separated_word)):
        result_word.append(combine_data(separated_word[i]))
    if put == 1:
        print("자음 축약")
        print(result_word)
    return separated_word

def consonant_elimination(separated_word):
    result_word.clear()
    put=0
    for i in range(len(separated_word)):
        if(separated_word[i][2] == 'ㄳ' or separated_word[i][2] == 'ㄺ'):
            put=1
            separated_word[i][2]= 'ㄱ'
        elif(separated_word[i][2] == 'ㄵ' or separated_word[i][2] == 'ㄶ'):
            put=1
            separated_word[i][2] = 'ㄴ'
        elif(separated_word[i][2] == 'ㄼ' or separated_word[i][2] == 'ㄽ' or separated_word[i][2] == 'ㅀ' or separated_word[i][2] == 'ㄾ'):
            put=1
            separated_word[i][2] = 'ㄹ'
        elif(separated_word[i][2] == 'ㅄ'):
            put=1
            separated_word[i][2] = 'ㅂ'
        elif(separated_word[i][2] == 'ㄻ'):
            put=1
            separated_word[i][2] = 'ㅁ'
        elif(separated_word[i][2] == 'ㄿ'):
            put=1
            separated_word[i][2] = 'ㅍ'
        result_word.append(combine_data(separated_word[i]))
    if put == 1:
        print("자음 탈락(자음군 단순화)")
        print(result_word)
    return separated_word

def palatalize(separated_word):
    result_word.clear()
    put=0
    for i in range(len(separated_word)-1):
        if((separated_word[i][2] == 'ㄷ' or separated_word[i][2] == 'ㅌ') and separated_word[i+1][1] == 'ㅣ'):
            put = 1
            if(separated_word[i][2] == 'ㄷ'):
                separated_word[i+1][0] = 'ㅈ'
            else:
                separated_word[i+1][0] = 'ㅊ'
            separated_word[i][2] = ' '
    for i in range(len(separated_word)):
        result_word.append(combine_data(separated_word[i]))
    if put == 1:
        print("구개음화")
        print(result_word)
    return separated_word

def ending_rule(separated_word):
    result_word.clear()
    put = 0
    for i in range(len(separated_word)):
        if(separated_word[i][2] == 'ㄲ' or separated_word[i][2] == 'ㅋ'):
            put = 1
            separated_word[i][2] = 'ㄱ'
        elif(separated_word[i][2] == 'ㅌ' or separated_word[i][2] == 'ㅅ' or separated_word[i][2] == 'ㅆ' or separated_word[i][2] == 'ㅈ' or separated_word[i][2] == 'ㅊ' or separated_word[i][2] == 'ㅎ'):
            put = 1
            separated_word[i][2] = 'ㄷ'
        elif(separated_word[i][2] == 'ㅍ'):
            put = 1
            separated_word[i][2] = 'ㅂ'
        result_word.append(combine_data(separated_word[i]))
    if put == 1:
        print("음절 끝소리 규칙")
        print(result_word)
    return separated_word

def continue_sound(separated_word):
    result_word.clear()
    put = 0
    for i in range(len(separated_word)):
        if(i>0 and separated_word[i][0] == 'ㅇ' and separated_word[i-1][2] != ' ' and separated_word[i-1][2] != 'ㅇ'):
            separated_word[i][0] = separated_word[i-1][2]
            separated_word[i-1][2] = ' '
            put=1
    for i in range(len(separated_word)):
        result_word.append(combine_data(separated_word[i]))
    if put == 1:
        print("연음")
        print(result_word)
    return separated_word

def flow_phoneme(separated_word):
    result_word.clear()
    put = 0
    for i in range(len(separated_word)-1):
        if(separated_word[i][2] == 'ㄴ' and separated_word[i+1][0] == 'ㄹ'):
            put=1
            separated_word[i][2] = 'ㄹ'
        elif(separated_word[i][2] == 'ㄹ' and separated_word[i+1][0] == 'ㄴ'):
            put=1
            separated_word[i+1][0] = 'ㄹ'
    for i in range(len(separated_word)):
        result_word.append(combine_data(separated_word[i]))
    if put == 1:
        print("유음화")
        print(result_word)
    return separated_word

def strong_phonme(separated_word):
    result_word.clear()
    put = 0
    for i in range(len(separated_word)-1):
        if((separated_word[i][2] == 'ㄱ' or separated_word[i][2] == 'ㄷ' or separated_word[i][2] == 'ㅂ') and separated_word[i+1][0] == 'ㄱ'):
            separated_word[i+1][0] = 'ㄲ'
            put=1
        elif((separated_word[i][2] == 'ㄱ' or separated_word[i][2] == 'ㄷ' or separated_word[i][2] == 'ㅂ') and separated_word[i+1][0] == 'ㄷ'):
            separated_word[i+1][0] = 'ㄸ'
            put=1
        elif((separated_word[i][2] == 'ㄱ' or separated_word[i][2] == 'ㄷ' or separated_word[i][2] == 'ㅂ') and separated_word[i+1][0] == 'ㅂ'):
            separated_word[i+1][0] = 'ㅃ'
            put=1
        elif((separated_word[i][2] == 'ㄱ' or separated_word[i][2] == 'ㄷ' or separated_word[i][2] == 'ㅂ') and separated_word[i+1][0] == 'ㅈ'):
            separated_word[i+1][0] = 'ㅉ'
            put=1
        elif((separated_word[i][2] == 'ㄱ' or separated_word[i][2] == 'ㄷ' or separated_word[i][2] == 'ㅂ') and separated_word[i+1][0] == 'ㅅ'):
            separated_word[i+1][0] = 'ㅆ'
            put=1
    for i in range(len(separated_word)):
        result_word.append(combine_data(separated_word[i]))
    if put == 1:
        print("경음화")
        print(result_word)
    return separated_word

def nose_phoneme(separated_word):
    result_word.clear()
    put = 0
    for i in range(len(separated_word)-1):
        if(separated_word[i][2] == 'ㅂ' and (separated_word[i+1][0] == 'ㄴ' or separated_word[i+1][0] == 'ㅁ' or separated_word[i+1][0] == 'ㄹ')):
            put=1
            if(separated_word[i+1][0] == 'ㄹ'):
                separated_word[i+1][0] = 'ㄴ'
            separated_word[i][2] = 'ㅁ'
        elif(separated_word[i][2] == 'ㄷ' and (separated_word[i+1][0] == 'ㄴ' or separated_word[i+1][0] == 'ㅁ' or separated_word[i+1][0] == 'ㄹ')):
            put=1
            separated_word[i][2] = 'ㄴ'
            if(separated_word[i+1][0] == 'ㄹ'):
                separated_word[i+1][0] = 'ㄴ'
        elif(separated_word[i][2] == 'ㄱ' and (separated_word[i+1][0] == 'ㄴ' or separated_word[i+1][0] == 'ㅁ' or separated_word[i+1][0] == 'ㄹ')):
            put=1
            separated_word[i][2] = 'ㅇ'
            if(separated_word[i+1][0] == 'ㄹ'):
                separated_word[i+1][0] = 'ㄴ'
        elif((separated_word[i][2] == 'ㅁ' or separated_word[i][2] == 'ㅇ') and separated_word[i+1][0] == 'ㄹ'):
            put=1
            separated_word[i+1][0] = 'ㄴ'
    for i in range(len(separated_word)):
        result_word.append(combine_data(separated_word[i]))
    if put == 1:
        print("비음화")
        print(result_word)
    return separated_word

def combine_data(separted_word):
    for i in range(19):
        if(First_LIST[i] == separted_word[0]):
            f1 = i
    for i in range(21):
        if(Middle_LIST[i] == separted_word[1]):
            f2 = i
    for i in range(28):
        if(Last_LIST[i] == separted_word[2]):
            f3 = i
    uni_word = 44032 + (f1 * 588) + (f2 * 28) + f3
    return chr(uni_word)

def process_data(separated_word):
    
    #자음 축약
    separated_word = abbreviation(separated_word)

    #자음 탈락(자음군 단순화)
    separated_word = consonant_elimination(separated_word)

    #구개음화
    separated_word = palatalize(separated_word)

    #연음
    separated_word = continue_sound(separated_word)

    #음절 끝소리 규칙
    separated_word = ending_rule(separated_word)

    #경음화
    separated_word = strong_phonme(separated_word)

    #비음화
    separated_word = nose_phoneme(separated_word)

    #유음화
    separated_word = flow_phoneme(separated_word)
    
    return result_word


str_data = input()
divided_data = []
result_word = []
divided_data = korean_to_be_englished(str_data)
print("결과 : " + ''.join(process_data(divided_data)))