#rotterA
L1=[[13, 1, 2, 5, 12, 8, 9, 14, 3, 7, 16, 11, 4, 6, 15, 10, 19, 18, 17],
    [6, 8, 14, 20, 16, 1, 11, 13, 4, 5, 15, 10, 21, 3, 9, 12, 2, 19, 17, 7, 18],
    [15, 18, 11, 19, 4, 2, 12, 21, 5, 16, 10, 17, 25, 1, 13, 8, 22, 14, 27, 7, 26, 3, 20, 24, 23, 9, 28, 6]]

#rotterB
L2=[[3, 15, 11, 2, 17, 16, 18, 10, 8, 5, 14, 19, 1, 9, 12, 6, 7, 13, 4],
    [12, 17, 16, 5, 2, 15, 8, 6, 13, 10, 7, 20, 21, 14, 9, 1, 3, 11, 18, 4, 19],
    [2, 27, 18, 25, 8, 6, 21, 13, 10, 7, 1, 28, 23, 4, 17, 11, 20, 5, 3, 14, 15, 22, 12, 19, 9, 26, 24, 16]]
    

#rotterC
L3=[[15, 6, 3, 5, 4, 8, 12, 2, 14, 13, 19, 9, 10, 18, 1, 7, 17, 11, 16],
    [16, 5, 15, 20, 11, 8, 3, 9, 7, 21, 12, 6, 1, 19, 2, 13, 14, 18, 17, 4, 10],
    [1, 20, 23, 19, 10, 25, 22, 12, 17, 7, 21, 16, 27, 2, 15, 6, 24, 8, 26, 5, 13, 4, 11, 9, 14, 18, 28, 3]]

#reflectorA
R1=[[6, 3, 10, 9, 14, 1, 17, 18, 8, 5, 4, 7, 2, 13, 16, 11, 12, 19, 15],
    [11, 9, 4, 18, 7, 15, 1, 19, 13, 20, 21, 10, 12, 2, 5, 14, 17, 3, 8, 16, 6],
    [15, 10, 20, 3, 5, 28, 26, 11, 24, 12, 1, 14, 6, 25, 16, 9, 21, 22, 8, 2, 23, 17, 19, 4, 18, 27, 7, 13]]

#reflectorB
R2=[[17, 8, 9, 13, 7, 11, 18, 10, 3, 15, 19, 5, 4, 16, 12, 6, 14, 2, 1],
    [21, 13, 3, 7, 11, 9, 8, 17, 4, 1, 10, 12, 16, 19, 20, 14, 5, 6, 15, 2, 18],
    [2, 8, 1, 6, 13, 5, 19, 28, 25, 17, 22, 21, 12, 24, 7, 16, 3, 20, 23, 26, 27, 14, 9, 18, 4, 10, 11, 15]]


#rotter1
def rotter1(x,y):
   
    L=[L1,L2,L3]
    crotter=L[x][y]
    
    num2=crotter[num1-1]
    return ((num2))
    
#rotter2
def rotter2(x,y):

    L=[L1,L2,L3]
    crotter=L[x][y]
    num3=crotter[num2-1]
    return (num3)
    
#reflectorA
def reflectorA(x,y):
    R=[R1,R2]
    cref1=R[x][y]
    cref2=cref1[:]
    cref2.reverse()
        
    a=cref1.index(num3)
    b=cref2[a]
    return(b)
    
#rotter2역함수
def irotter2(x,y):
    L=[L1,L2,L3]
    crotter=L[x][y]
    num5=crotter.index(num4)
    num5+=1
    return(num5)
    
#rotter1역함수
def irotter1(x,y):
    L=[L1,L2,L3]
    crotter=L[x][y]
    num6=crotter.index(num5)
    num6+=1
    return(num6)



turn=eval(input("Today's number:"))
mun1=eval(input("Enter a rotter's number:"))
mun2=eval(input("Enter a rotter's number:"))
mun3=eval(input("Enter a reflector's number:"))

sentence=input('enter:')




Output=[]
OOutput=[]
# 초성 리스트. 00 ~ 18  
list초성=['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅍ','ㅌ','ㅎ']
# 중성 리스트. 00 ~ 20 
list중성=['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음) 
list종성=['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']


for pos1 in range(0,len(sentence)):
    word=sentence[pos1]
    import re

    # 유니코드 한글 시작 : 44032, 끝 : 55199  
    BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
  
    if __name__ == '__main__':  
        split_keyword_list = word
        result = []
    
        for keyword in split_keyword_list:  
            # 한글 여부 check 후 분리  
            if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', keyword) is not None:  
                char_code = ord(keyword) - BASE_CODE  
                char1 = int(char_code / CHOSUNG)  
                result.append(list초성[char1])  
              
                char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)  
                result.append(list중성[char2])  
            
                char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))  
                result.append(list종성[char3])  
            
            else:  
                result.append(keyword)  
        characterS="".join(result)

    
    for Acharacter in characterS:
        k=characterS.index(Acharacter)     

        #초성 중성 종성 선택
        L한글=[list초성,list중성,list종성]
        cList=L한글[k]

        
        num1=cList.index(Acharacter)+1


        #def rotter1
        num2=rotter1(mun1-1,k)+k+turn+pos1
        

        #List범위를 초과할 수 있으므로
        Lnum=len(cList)
        if num2>=Lnum:
            num2=num2%Lnum
        if num2==0:
            num2=Lnum   


        #def rotter2
            
        num3=rotter2(mun2-1,k)


        #def reflectorA
        num4=reflectorA(mun3-1,k)


        #def rotter2역함수
        num5=irotter2(mun2-1,k)-k-turn-pos1
        

        #List범위를 초과할 수 있으므로
        if num5<0:
            num5=num5%Lnum
        if num5==0:
            num5=Lnum

        
        #def rotter1역함수
        num6=irotter1(mun1-1,k)-1

        final=cList[num6]
        Output.append(final)
        fOutput=''.join(Output)

        #분리된 한글 합체
    print(fOutput)
        
print(fOutput)      
