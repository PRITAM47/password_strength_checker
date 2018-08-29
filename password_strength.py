def check(data)-> bool:

    #Initializing variable to check for alphabets and numbers
    count_lower= False
    count_upper= False
    count_number = False
    
    #minimum 10 characters required
    if len(data)>= 10:
        for i in data:
            if i.islower():
                count_lower = True
            elif i.isupper():
                count_upper = True
            elif i.isdigit():
                count_number = True
        if count_lower == True and count_upper == True and count_number == True:
            return True
            
        else : return False
            
    else: return False
    

a=check("123456123456") # user can check their password strength by calling check function
print(a)
    
