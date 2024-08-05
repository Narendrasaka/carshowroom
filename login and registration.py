import carshowroom
class LandR:
    def registration(self,username,password,phoneno,pincode,city):
        self.unmae=username
        self.pwd=password
        self.phoneno=phoneno
        self.pin = pincode
        self.city = city
        with open('user_reg.csv','a',newline='') as file:
            store = csv.writer(file)
            store.writerow([self.uname,self.pwd,self.phoneno,self.pin,self.city])  
        #Resgistration done successfully
    def login(self,username,password):

        with open('user_reg.csv','r',newline='') as file:
            read = csv.DictReader(file)
            for row in read:
                if row['uname'] == username and row['password'] == password:
                    print("yes")
            else:
                print("no")

