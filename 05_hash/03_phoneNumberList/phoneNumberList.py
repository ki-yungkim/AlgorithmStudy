def solution(phone_book):
    
    phone_book.sort()
    for i in range(len(phone_book)-1):
        a = phone_book[i]
        b = phone_book[i+1][:len(a)] 
        if a in b:
            return False         
    return True
