# PA-2 Word Frequency (3/28)
# 최소원, 박영준

with open("alice_in_wonderland.txt") as f:
    page = f.read()
    # 반복성이 없는 단순 text 는 우선적으로 처리
    # '.' '-'로 구분됐지만 합쳐져야 단어의 의미를 나타내는 단어 변환
    page = page.replace("'em", "them")               # 'em은 them 의 축약형
    page = page.replace("Ma'am", "Madam")            # Madam 과 Miss 의 중간 의미 단어로 Madam 으로 변환
    page = page.replace("W. RABBIT", "W＇RABBIT")    # 사람 이름으로 나눠 쓰지 않도록 변환
    page = page.replace("o'clock", "o＇clock")       # o'clock으로 나눠지지 않도록 자연스럽게 변환
    page = page.replace("arm-chair", "arm－chair")
    page = page.replace("to-night", "to－night")          ##################################
    page = page.replace("pine-apple", "pine－apple")      # '-'가 있는 형태가 자연스러운 단어 #
    page = page.replace("low-spirited", "low－spirited")  ##################################
    page = page.replace("looking-glass", "looking－glass")
    page = page.replace("fairy-tales", "fairy－tales")
    page = page.replace("lesson-books", "lesson－books")
    page = page.replace("sky-rocket", "sky－rocket")
    page = page.replace("guinea-pigs", "guinea－pigs")
    page = page.replace("queer-shaped", "queer－shaped")
    page = page.replace("sea-shore", "sea－shore")
    page = page.replace("jury-box", "jury－box")
    page = page.replace("never-ending", "never－ending")
    page = page.replace("star-fish", "starfish")        #################################
    page = page.replace("jelly-fish", "jellyfish")      # '-'가 없어도 같은 뜻을 갖는 경우 #
    page = page.replace("note-book", "notebook")        #################################
    page = page.replace("to-day", "today")
    # 본문에서 '--' 글자를 이어서 처리해야 하는 경우
    page = page.replace('Beau--ootiful', 'beautiful')
    page = page.replace('beauti--FUL', 'beautiful')
    page = page.replace('Soo--oop', 'soup')
    page = page.replace('e--e--evening', 'evening')
    page = page.replace('beauti--ful', 'beautiful')
    ####### 'd는 문맥을 파악하고 변환해야 하기 때문에 하나씩 해석해서 처리함 #######
    ############################ 'd 중 would 변환 ############################
    page = page.replace("'d rather", "wolud rather")  # rather 앞 'd는 무조건 would
    page = page.replace("'d soon fetch", "wolud soon fetch")    # 해석할 경우 would가 적절함
    page = page.replace("'d let", "wolud let")                  # 해석할 경우 would가 적절함
    page = page.replace("they'd take", "they would take")       # 해석할 경우 would가 적절함
    page = page.replace("he'd do", "he would do")               # 해석할 경우 would가 적절함
    page = page.replace("'d only", "would only")                # 해석할 경우 would가 적절함
    page = page.replace("'d like", "would like")                # 해석할 경우 would가 적절함
    page = page.replace("'d have", "would have")                # 해석할 경우 would가 적절함
    page = page.replace("'d ", "would only")                    # 해석할 경우 would가 적절함
    ############################ 'd 중 had 변환 ############################
    page = page.replace("'d better", "had better")  # better 앞 'd는 무조건 had
    page = page.replace("'d nearly forgotten", "had nearly forgotten")
    page = page.replace("'d taken", "had taken")    ##################################
    page = page.replace("'d gone", "had gone")      ##### 과거분사 앞은 무조건 had #####
    page = page.replace("'d been", "had been")      ##################################
    page = page.replace("'d hardly finished", "had hardly finished")
    page = page.replace('-', " ")
    # 'd의 다른 경우는 아래에서 처리함
    # 'CHAPTER' 의 I V X는 영어 단어로 처리할 수 없어 특수문자로 변경
    page = page.replace('CHAPTER I', 'CHAPTER Ⅰ')
    page = page.replace('CHAPTER II', 'CHAPTER Ⅱ')
    page = page.replace('CHAPTER III', 'CHAPTER Ⅲ')
    page = page.replace('CHAPTER IV', 'CHAPTER Ⅳ')
    page = page.replace('CHAPTER V', 'CHAPTER Ⅴ')
    page = page.replace('CHAPTER VI', 'CHAPTER Ⅵ')
    page = page.replace('CHAPTER VII', 'CHAPTER Ⅶ')
    page = page.replace('CHAPTER VIII', 'CHAPTER Ⅷ')
    page = page.replace('CHAPTER IX', 'CHAPTER Ⅸ')
    page = page.replace('CHAPTER X', 'CHAPTER Ⅹ')
    page = page.replace('CHAPTER XI', 'CHAPTER ⅩⅠ')
    page = page.replace('CHAPTER XII', 'CHAPTER ⅩⅡ')



words_list = page.split()   # words_list 로 정리된 page 내용 넣기

# traslate, maketrans 함수 이용해 본문 Text 처리
intab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\"
outtab = "abcdefghijklmnopqrstuvwxyz                                          "
trantab = str.maketrans(intab, outtab)  # 텍스트에 문자 변환
trans_list = []

# 제거된 구두점의 공백을 처리하는 for 반복문
index = 0
for word in words_list:
    word = word.translate(trantab)
    if word.strip() == '':
        continue
    trans_list.append(word.strip())     # trans_list에 변환된 문자 삽입
    if trans_list[index][-2:] == ' t':  # not 축약형 : n't
        if trans_list[index] == 'can t':
            trans_list.remove('can t')
            trans_list.append('can')
            trans_list.append("not")
        elif trans_list[index] == 'won t':
            trans_list.remove('won t')
            trans_list.append('will')
            trans_list.append("not")
        elif trans_list[index] == 'ain t':
            trans_list.remove('ain t')
            trans_list.append('am')
            trans_list.append("not")
        elif trans_list[index] == 'shan t':
            trans_list.remove('shan t')
            trans_list.append('shall')
            trans_list.append("not")
        else:   # don t, didn t, doesn t, isn t, aren t, hasn t, hadn t,  haven t
                # wouldn t, couldn t, shouldn t, wasn t, weren t, mayn t,
            temp = trans_list[index]
            trans_list.remove(trans_list[index])
            trans_list.append(temp[:-3])
            trans_list.append("not")
        # 's는 예외사항으로 처리하지 않음
        index += 1
    elif trans_list[index][-2:] == ' m':  # am 축약형 : 'm
        trans_list.remove(trans_list[index])
        trans_list.append('i')
        trans_list.append("am")
        index += 1
    elif trans_list[index][-3:] == ' ll':  # will 축약형 : 'll
        temp = trans_list[index]
        trans_list.remove(trans_list[index])
        trans_list.append(temp[:-3])
        trans_list.append("will")
        index += 1
    elif trans_list[index][-3:] == ' re':  # are 축약형 : 're
        temp = trans_list[index]
        trans_list.remove(trans_list[index])
        trans_list.append(temp[:-3])
        trans_list.append("are")
        index += 1
    elif trans_list[index][-3:] == ' ve':  # have 축약형 : 've
        temp = trans_list[index]
        trans_list.remove(trans_list[index])
        trans_list.append(temp[:-3])
        trans_list.append("have")
        index += 1
    elif trans_list[index][-2:] == ' d':  # could 축약형 : 'd
        temp = trans_list[index]
        trans_list.remove(trans_list[index])
        trans_list.append(temp[:-2])
        trans_list.append("could")
        index += 1
        # 본문 txt에서 would와 had를 예외로 모두 처리하여 나머지만 could로 변경
        # 영어 해석 상 should가 나오는 내용은 없다고 판단
    index += 1


# list 에서 단어의 사용 빈도를 count
def count(list, dict):
    for word in list:
        if word in dict:
            dict[word] += 1
    return dict


# translist 를 받아서 dictionary 로 바꿔줌
def chage_dict(list):
    dict_words = {}
    for word in list:
        dict_words[word] = 0
    return dict_words


def sort_dict(dic):  # Value 기준 sort
    import operator
    return sorted(dic.items(), key=operator.itemgetter(1), reverse=True)


def sort_dict2(dic):  # Key 기준 sort (사용 안함)
    import operator
    return sorted(dic.items(), key=operator.itemgetter(0), reverse=True)


dict_words = chage_dict(trans_list)     # chage_dict 으로 dictionary 형태로 만들어줌
count(trans_list, dict_words)           # 단어의 사용 빈도 수 계산
sorted_dict = sort_dict(dict_words)     # sorted 함수 이용 Value 기준으로 정렬


print('\n#################################################################')
print('Q1. How many different words are used in the Alice in Wonderland?')
print('#################################################################\n')

different_word = []
different_word = list(set(trans_list))  # 중복 제거
print(">>> 총 단어의 개수 : ", len(trans_list))
print(">>> 사용된 다른 단어의 개수 : ", len(different_word))
print(">>> 사용된 다른 단어 : ", different_word)


print('\n######################################################################################')
print('Q2. List top 20 frequently used words and their frequencies in the Alice in Wonderland.')
print('######################################################################################\n')
# 위에서 정의한 sorted_dict 으로 사용 빈도 순으로 정렬 됨
print(">>> 많이 사용된 단어 20개 : ", sorted_dict[:20])
for i in range(20):     # '사용 단어 - 사용된 빈도'로 출력
    print("Frequency of the word [", sorted_dict[i][0], "] is [", sorted_dict[i][1], "]")


print('\n###############################################################################')
print('Q3. which words in this book are not in the expected vocabulary at this level?')
print('###############################################################################\n')

with open("vocab.txt") as t:    # vocab.txt 파일 열기
    page = t.read()             # 읽어와서 page 에 저장
el_words_list = page.split()    # page 단어 el_words_list 로 저장
difficult_words = []            # 어려운 영단어 담을 words 리스트

# 어려운 단어장 만드는 for 반복문
# 어린이 단어장 리스트는 difficult_words
for word in dict_words.keys():
    if word not in el_words_list:       # vocab.txt 에 없는 경우
        difficult_words.append(word)    # 없는 단어인 경우 append

# 고유명사 - 이름은 단어장에 들어갈 단어가 아니므로 제외시키기 위해 name 을 만듬
# CHAPTER 에 있던 로마숫자도 단어장에서 제외시킴
name = ['alice', 'lory', 'W.rabbit' 'mary', 'ann', 'dinah', 'lewis', 'carroll', 'ada', 'mabel', 'william',
        'dodo', 'bill', 'elsie', 'lacie', 'tillie', 'paris', 'london', 'rome', 'new zealand', 'australia',
        'Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ', 'Ⅹ']

# 어린이 수준 이상이 되는 단어들을 찾아내기 위해 동화책 단어 리스트에서 고유명사, 로마숫자를 빼는 작업
for i in difficult_words:
    if i in name:
        difficult_words.remove(i)

print(">>> 어려운 단어의 개수 : ", len(difficult_words))
print(">>> 어려운 단어 목록 : ", difficult_words)

# 190502 Local Repository 변경 사항 확인해보기
