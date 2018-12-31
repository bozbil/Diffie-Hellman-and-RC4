#kahramankostas
#Lab_Assignment_2.py


################COMBINED LINEAR CONGRUENTIAL GENERATOR  ###########
import random
m_1 = 2147483563
m_2 = 2147483399
a_1 = 40014
a_2 = 20692
y_1 = (random.randint(1, m_1 - 1))
y_2 = (random.randint(1, m_1 - 1))
one_time_private_keys=[]

for i in range (0,2):
    y_1 = a_1 * y_1%m_1
    y_2 = a_2 * y_2%m_2
    decision = (y_1-y_2)%(m_1-1)
    if decision > 0:
        one_time_private_keys+=[int((decision / m_1)  *  500)]
    elif decision < 0:
        one_time_private_keys+=[int((decision / m_1 + 1)  *  500)]
    else:
        one_time_private_keys+=[int(((m_1 - 1)/m_1)  *  500)]
print("COMBINED LINEAR CONGRUENTIAL GENERATOR")
for i in  one_time_private_keys:
    print("User %s Private Key= " %(chr(65+one_time_private_keys.index(i))) ,i)
print("\n")





###########################   DIFFIE-HELLMAN ALGORITHM    ##############
print("DIFFIE-HELLMAN ALGORITHM")
q,alpha=353,3
x,y=[],[]
for i in one_time_private_keys:
    x+=[i % q]
    y+=[(alpha ** i) % q]   
secretkey=(y[0] ** x[1]) % q

print(" Xa= %s\n Xb= %s\n Ya= %s\n Yb= %s  " %(x[0],x[1],y[0],y[1]))
print("Diffie-Hellman algorithm Secret Key  = %s" %(secretkey))
print("\n")






###########################   RC4 ALGORITHM ENCRYPTION   #############
print("RC4 ALGORITHM ENCRYPTION")

try:
    bookfile = open("book.txt")
    book=bookfile.read()
    bookfile.close()
except:
    print ("This program needs a data file (book.txt)")
    exit(1)

block_128_bits=[]

for i in range(0,len(book),16):
    block_128_bits += [book[ i : i + 16 ]]
    
book=block_128_bits[len(block_128_bits)-1]

keystream, s, t = [],[],[]
key =str(secretkey)


# Initialization
for i in range (0 , 256 ) :
    s+=[i]
    t+=[ key[i  %  len(key ) ]]
   
   
# Initial Permutation of S	
j = 0
for i in range (0,256 ) :
    j = (j + s[i]  + ord(t[i]  )  )  %  256
    s[i] ,s[j]  = s[j] ,s[i ]

	
# Stream Generation	
j = 0
for i in range (1,len(book )  + 1 ) :
    j = (j + s[i]  )   %  256
    s[i] , s[j]  = s[j] , s[i] 
    counter = (s[i]  + s[j]  )   %  256
    keystream+=[s[counter] ] 

	
encrypted_msg = ""
counter = 0
for i in book:
    temporary = ("%02X"  %  (ord( i )  ^ (keystream[counter]  )  )  ) 
    encrypted_msg = encrypted_msg + str(temporary) 
    counter += 1
print("Encrypted text with RC4 algorithm =  %s" %(encrypted_msg))    
      



                        
###################  RC4 ALGORITHM DECRYPTION   ##########################
print("\nRC4 ALGORITHM DECRYPTION")
counter = 0
decrypted_msg=""
for i in range(0,len(encrypted_msg)-1,2):
    temporary = (((int(encrypted_msg[i:i+2],16))  ^ (keystream[counter]  )  )  ) 
    decrypted_msg = decrypted_msg + chr(temporary) 
    counter += 1
      
print("Decrypted text with RC4 algorithm =  %s" %(decrypted_msg)  ) 



