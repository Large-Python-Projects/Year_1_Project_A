import sys

def main_programme():
    
    option = input("Enter whether you'd like to only encode your message with 'e' or decode as well with 'd': ")

    while ((option != "e") and (option != "d") and (option != "E") and (option != "D")):
    
        option = input("You can only input 'e' or 'd', please re-enter: ")
    
    i = str(input("Please input a value to encode your sentence: "))
    sentence = str(input("Please input your sentence: "))
    option = option.lower()
    shift_val_error_check(sentence, i, option)
    sentence_error_check(sentence, i, option)
    
def shift_val_error_check(sentence, i, option):
    
    i_index = 0
    i_list = list(i)
    print(i_list)
    while (i_index < len(i_list) or i == ""):
        
        while(i == ""):
            
            i = str(input("Input required, please enter a value to encode your data: "))
            i_index = 0
            i_list = list(i)
            
        index = i_list[i_index]
        
        if((ord(index) <= 57 and ord(index) >= 49) or ord(index) == 45):
            
            if(float(i)%26 == 0):
                
                i = str(input("Input mustn't be a multiple of 26, please re-enter: "))
                i_index = 0
                i_list = list(i)
            
            else:
                
                i_index = i_index + 1
            
        else:
        
            i = str(input("Input must be an integer and non-zero, please re-enter: "))
            i_index = 0
            i_list = list(i)
            
    i = float(i)
            
    if(i > 0):
    
        i = int(i%26)
        
    elif(i < 0):
        
        i = int(i%-26)
          
    sentence_error_check(sentence ,i, option)      

def sentence_error_check(sentence, i, option):
    
    s_index = 0
    s_list = list(sentence)
    nothing = ""
    
    while ((s_index < len(s_list)) or (sentence == nothing)):
        
        while(sentence == nothing):
            
            sentence = str(input("Input must contain only letters and spaces, please re-enter: "))
            s_index = 0
            s_list = list(sentence)
        
        index = s_list[s_index]

        if(index.isalpha() == True):
            
            s_index = s_index + 1
            
        elif(ord(index) == 32):
            
            s_index = s_index + 1
            
        elif((index.isalpha() == False) and (ord(index) != 32)):
            
            sentence = str(input("Input must contain only letters and spaces, please re-enter: "))
            s_index = 0
            s_list = list(sentence)
            
    encrypt(s_list, i, option)
    
def encrypt(s_list, i, option):

    shift = int(i)
    n = 0
    result = 0
    resulting_list = []
    
    while(n < len(s_list)):
    
        n = int(n)
        index = s_list[n]
        ord_val = int(ord(index))
        
        if(ord_val <= 122 and ord_val >= 97):
        
            if((ord_val + shift) > 122):
                
                result = chr(ord_val + shift - 26)
                resulting_list.append(result)
                
            elif((ord_val + shift) <= 122 and (ord_val + shift) >= 97):
                
                result = chr(ord_val + shift)
                resulting_list.append(result)
                
            elif((ord_val + shift) < 97):
                
                result = chr(ord_val + shift + 26)
                resulting_list.append(result)
                
        elif(ord_val <= 90 and ord_val >= 65):
            
            if((ord_val + shift) > 90):
                
                result = chr(ord_val + shift - 26)
                resulting_list.append(result)
                
            elif((ord_val + shift) <= 90 and (ord_val + shift) >= 65):
                
                result = chr(ord_val + shift)
                resulting_list.append(result)
                
            elif((ord_val + shift) < 65):
                
                result = chr(ord_val + shift + 26)
                resulting_list.append(result)
                
        elif(ord_val == 32):
            
            resulting_list.append(" ")
            
        n = n + 1
        
    encrypted_sentence = "".join(resulting_list)
    
    print("\nYour encoded message is: "+encrypted_sentence+"\n")
    
    if(option == "e"):
    
        sys.exit("Programme finished")
    
    elif(option == "d"):    
        
        decrypt(resulting_list, i)

def decrypt(s_list, shift):
    
    shift = int(shift)
    n = 0
    result = ""
    resulting_list2 = []
    
    while(n < len(s_list)):
    
        n = int(n)
        index = s_list[n]
        ord_val = int(ord(index))
        
        if(ord_val <= 122 and ord_val >= 97):
        
            if((ord_val - shift) > 122):
                
                result = chr(ord_val - shift - 26)
                resulting_list2.append(result)
            
            elif((ord_val - shift) <= 122 and (ord_val - shift) >= 97):
                
                result = chr(ord_val - shift)
                resulting_list2.append(result)
            
            elif((ord_val - shift) < 97):
                
                result = chr(ord_val - shift + 26)
                resulting_list2.append(result)
            
        elif(ord_val <= 90 and ord_val >= 65):
            
            if((ord_val - shift) > 90):
                
                result = chr(ord_val - shift - 26)
                resulting_list2.append(result)
               
            elif((ord_val - shift) <= 90 and (ord_val - shift) >= 65):
                
                result = chr(ord_val - shift)
                resulting_list2.append(result)
                
            elif((ord_val - shift) < 65):
                
                result = chr(ord_val - shift + 26)
                resulting_list2.append(result)
               
        elif(ord_val == 32):
            
            resulting_list2.append(" ")
            
        n = n + 1
    
    decrypted_sentence = "".join(resulting_list2)
    print("Your decoded message is: "+decrypted_sentence+"\n")
    sys.exit("Programme finished")
    
main_programme()


