import hashlib, uuid, pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='ye2121br',
                             password='Olympia1!',
                             db='ye2121br_',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

password = input("What is your password? ")


# this creates a brand new guaranteed unique salt every time you run it
salt = uuid.uuid4().hex


print ("password + salt is: " + password + str(salt))

# this is an open-source method to ONE-WAY hash a password
hashed_password = hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


print ("the hashed password is: ", hashed_password)
print ("Now lets insert into the database!")

try:
   with connection.cursor() as cursor:
       sql = "INSERT INTO `userPass` (`hashed_password`, `password`, `salt`) VALUES (`%s`, `%s`,`%s`)"
      # to_sql = (hashed_password, password, salt)
       cursor.execute(sql)
        
finally:
    connection.commit()
    #connection.close()
    
print("Now lets retrieve from the database!")
try:
    sql_query = "SELECT `salt` FROM `userPass` WHERE `password` LIKE `%s`"
    #cursor.execute(sql_query)
        
    #returnSalt = password['%s']
    #print(returnSalt)
    print(hashed_password)
    
finally:
    connection.commit()
   

    


password1 = input ("Please re-enter your password: ")
if password1 == password:
    print ("Match!")
elif password1 != password: 
    print ("No Match")
    
