
import datetime
#welcome message function

def welcome():
    print("-----------------------------------------------")
    print("\t\t\t Welcome TO The Bike Management System\t\t\t")
    print("-----------------------------------------------")
#option funtion
def option():
    print("-----------------------------------------------")
    print("1.Sell Bike")
    print("2.Buy Bike")
    print("3.Exit")
    print("-----------------------------------------------")
#choosing option function
def choosing():
    
    loop=True
    s=True
    while loop==True:
        option()
        try:
            num=int(input("Enter the number from above option :  "))
            s=False
        except:
            print("Enter valid number!!")
        if s==False:
            if num==1:
                sellingbike()
            elif num==2:
                buyingbike()
                
            elif num==3:
                loop=False

                print("Thank you!!! Have a Good Day")
            else:
                print("Enter a number from above option")
#text file function
def csv():
    file=open("bikes.txt")
    list_=[]

    for line in file:
        line=line.replace("\n","")
        words=line.split(",")
        list_.append((words[0:]))
    return list_
#get date time function
def gettime():
    dt=datetime.datetime.now()
    hours=str(dt.hour)
    minutes=str(dt.minute)
    seconds=str(dt.second)
    years=str(dt.year)
    months=str(dt.month)
    days=str(dt.day)
    dates=years+"-"+months+"-"+days+"-"+hours+"-"+minutes+"-"+seconds
    return dates

#selling stock bike

def sellingbike():
    list_=csv()
    idstore=[]
    total=0
    dates=gettime()
    pa=True
    dt=datetime.datetime.now()
    hours=str(dt.hour)
    minutes=str(dt.minute)
    seconds=str(dt.second)
    years=str(dt.year)
    months=str(dt.month)
    days=str(dt.day)
    datess=years+"/"+months+"/"+days+" "+hours+":"+minutes+":"+seconds
    

    
    
    print(f"{'Id':<25} {'Name':<25} {'Brand':<30} {'color':<20} {'Quantity':<10} {'price':>20}")
    for v in list_:
     Id,name,brand,color,quantity,price = v
     detail= "{:<25} {:<25} {:<30} {:<20} {:<10} {:>20}".format(Id,name,brand,color,quantity,price)
     price=price.replace("\n","")
     print(detail)
    

    customern=input("Enter customer name : ")
    customera=input("Enter customer Address : ")
    customerm=input("Enter customer contact number : ")
    try:
        qnty=int(input("Enter number of bike you want to purchase : "))
        pa=False

    except:
        print("Enter valid number from the above option!!")
    if pa==False:
        for i in range(1,qnty+1):
            s=str(i)
            bikeid=input("Enter "+s+" Bike Id : ")
            for v in list_:
                Id,name, brand, color, quantity, price = v
                if(Id==bikeid):

              
                    idstore.append(bikeid)
                
    set_=set(idstore)
    store=[]
    store2=[]

    

    for f in set_:
      qtn=idstore.count(f)
      
      for v in list_:
        store=[]
        Id,name, brand, color, quantity, price = v
        price= price.replace("\n","")
        if(Id==f):
            dd=int(Id)
            if(int(quantity)>=1):
                final_list_after_sell(dd,qtn)
                prices=int(price)*qtn
                total=total+prices
                store.append(name)
                store.append(str(qtn))
                store.append(price)
                store.append(str(prices))
                store.append(brand)
                
                store2.append(store)

                k=customern+dates
    
                billf=open(k+".txt","w")
        
                billf.write("-----------------------------------------------------------------------------------------------------------------------------""\n")
        
    
                billf.write(f"{'Name':<25} {'brand':<25}{'unit price':<30}{'Quantity':<20}{'Amount':>20}\n")
                for s in store2:
                    nameb, qtnb,priceb , pricesb, brandb = s
                    detail= "{:<25} {:<25} {:<30} {:<20} {:>20}".format(nameb, brandb,priceb,qtnb, pricesb.replace(',',''))
                    billf.write(detail+"\n")
                billf.write("-----------------------------------------------------------------------------------------------------------------------------"+"\n")
                billf.write(f"{'Total : ':>100}""{:<100}".format(total)+"\n")
                billf.write(f"{'date time : ':>100}""{:<100}".format(datess)+"\n")
                billf.close()
                print("-----------------------------------------------------------------------------------------------------------------------------""\n")
            
            
    
                print(f"{'Name':<25} {'brand':<25}{'unit price':<30}{'Quantity':<20}{'Amount':>20}")
                for e in store2:
                    nameb, qtnb,priceb , pricesb, brandb = e
                    detail= "{:<25} {:<25} {:<30} {:<20} {:>20}".format(nameb, brandb,priceb,qtnb, pricesb.replace(',',''))
                    print(detail)
                print("-----------------------------------------------------------------------------------------------------------------------------"+"\n")
                print(f"{'Total : ':>100}""{:<100}".format(total))
                print(f"{'date time : ':>100}""{:<100}".format(datess)+"\n")
            else:
                print("-----------------------------------------------------------------------------------------------------------------------------""\n")
                if(Id==bikeid):
                    a=list_[int(bikeid)-1][2]
               
                print(a," is out of stock")
                

def update_the_stock(bike_list):
    file = open("bikes.txt", "w")
    for i in bike_list:
        file.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+"\n")
    file.close()



def final_list_after_sell(motor_bike_id,the_bike_quantity):
     bike_list = csv()
     bike_list[motor_bike_id-1][4] = int(bike_list[motor_bike_id-1][4]) - the_bike_quantity   
     update_the_stock(bike_list)
def update_recent_the_stock(bike_list):
    file = open("bikes.txt", "w")
    for i in bike_list:
        file.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+"\n")
    file.close()

def recent_bike(motor_bike_id,the_bike_quantity):
     bike_list = csv()
     bike_list[motor_bike_id][4] = int(bike_list[motor_bike_id][4]) + the_bike_quantity   
     update_recent_the_stock(bike_list)
def newbike(list2):
    list_=csv()
    list_.append(list2)
    fadd=open("bikes.txt","w")
    for i in list_:
       fadd.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+"\n")
    fadd.close()

def buyingbike():
    list_=csv()
    ids=[]
    names=[]
    new=[]
    add_=[]
    ad=True
    coo=1
    loop=True
    print(f"{'Id':<25} {'Name':<25} {'Brand':<30} {'color':<20} {'Quantity':<10} {'price':>20}")
    for v in list_:
     Id,name,brand,color,quantity,price = v
     detail= "{:<25} {:<25} {:<30} {:<20} {:<10} {:>20}".format(Id,name,brand,color,quantity,price)
     price=price.replace("\n","")
     print(detail)
    fid=open("bikes.txt")
    for bid in fid:
        ids.append(bid[0])
    fid.close()
    
    count=len(ids)
    
    fname=open("bikes.txt")
    for nameb in fname:
        word=nameb.split(",")
    
        names.append(word[2])
        
    
    while ad==True:
        try:
           bikeadd=int(input("Enter number of bike  you want to add : "))
           ad=False
        except:
            print("Enter a valid input!!")
        
    while coo<=bikeadd:
        loop=True
        bikeb=input("Enter bike Brand : ")
        for name in names:
            if(bikeb==name):
                nid=names.index(name)
                q=int(input("Enter the quantity of bike you want to add : "))
                if(q<0):
                    print("Invalid quantity!!! Please Enter Valid quantity")
                    loop=False
                    break
                else:
                    recent_bike(nid,q)
                    loop=False

                
        if loop==True:    
            biken=input("Enter bike name : ")
            bikec=input("Enter bike color : ")
            qu=True
            pu=True
            while qu==True:
               try:
                  bikeq=int(input("Enter bike quantity : "))
                  qu=False
               except:
                print("Enter a valid quntatity : ")
            while pu==True:
                try:
                  bikep=int(input("Enter a bike price : "))
                  pu=False
                except:
                    print("Enter valid price : ")
            count+=1
                    
            add_.append(count)
            add_.append(biken)
            add_.append(bikeb)
            add_.append(bikec)
            add_.append(bikeq)
            add_.append(bikep)
            newbike(add_)
            add_.clear()
        coo+=1
              
               
    
                
                
                
                


                    
            
    


    
    



