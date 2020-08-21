x = int(input("Do you want to decrypt(1), or encrypt(2)?"))
message = input("enter the message:")


letters = "abcdefghijklmnopqrstuvwxyz12345678910ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+=/.,<>:;""[]{}\\"


encrypt = ''

decrypt = ''



key = 635472354892748774872687264823648712364892374682173648723648723649274921748927490827498217498217490821791827917

for i in message:
    position = letters.find(i)
    newposition = (position+key)%26
    encrypt += letters[newposition]

   


for i in encrypt:
    pos = letters.find(i)
    newpos = (pos-key*2)%26
    decrypt += letters[newpos]


if x == 1:
    print(decrypt)

if x == 2:
    print(encrypt)




 



    
    
    
    
    
    
    
    