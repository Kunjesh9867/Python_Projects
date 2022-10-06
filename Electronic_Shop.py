import json
import datetime
import time
x = datetime.datetime.now()
print("Today's date is:",x)
print('*********************************************************************')
print('*                  WELCOME TO THE KUNJESH SALES!!!            *')
print('*                            SUMMER SALE                      *')
print('*            GET 20% OFF ON ANY PRODUCT WITH A GIFT VOUCHER   *')
print('*********************************************************************')
for i in [27,67,92,100]:
    print(i," % LOADED")
    time.sleep(1.00)
product={1:{'name':'Laptop','price':50000,'qty':10},
         2:{'name':'Phone','price':10000,'qty':85},
         3:{'name':'Washing machine','price':30000,'qty':34},
         4:{'name':'Cooking Stove','price':10000,'qty':102},
         5:{'name':'Computer','price':35000,'qty':32}
         }
print(json.dumps(product,indent=4))
kunjesh='kkr'
h=11
while(h!=0):
    print('1.Adminstration')
    print('2.User')
    print('0.Exit')
    h=eval(input('Enter the choice(1,2,0):'))
    if h==1:
        password=input('Enter The Password:')
        if password=='kunjesh':
            k=0
            while k!=5:
                print('You are in Adminstration mode:')
                print('   1.Add an item.')
                print('   2.Search an item.')
                print('   3.delete an item.')
                print('   4.modify an item.')
                print('   5.back to main menu:')
                k=eval(input('Enter your Choice(1,2,3,4,5):'))
                if k==1:
                    code=eval(input('Enter the Code of the Product:'))
                    name=input('Enter the Name of the Product:')
                    price=eval(input('Enter the price of the Product:'))
                    quantity=eval(input('Enter the Quantity of the Product:'))
                    kkr={code:{'name':name,'price':price,'qty':quantity}}
                    product.update(kkr)
                    print(json.dumps(product,indent=2))
                elif k==2:
                    search=eval(input('Enter the Code of The Product:'))
                    for keys in product:
                        if keys==search:
                            print("Code    :",keys)
                            print('Name    :',product[keys]['name'])
                            print('Price   :',product[keys]['price'])
                            print('Quantity:',product[keys]['qty'])
                            break
                    else:
                        print('Sorry! The Product Is Not Found In the Cart')
                elif k==3:
                    delete=eval(input('Enter the Code of the Product:'))
                    del product[delete]
                    print(json.dumps(product,indent=5))
                elif k==4:
                    code=eval(input('Enter the Code Of The Product:'))
                    new_name=input('Enter the New Name of the Product else + to Retain:')
                    if new_name=='+':
                        pass
                    else:
                        product[code]['name']=new_name
                    new_price=eval(input('Enter The New Price of the Product else 5 to Retain:'))
                    if new_price==5:
                        pass
                    else:
                        product[code]['price']=new_price
                    new_quantity=eval(input('Enter The New Quantity of the Product else 2 to Retain'))
                    if new_quantity==2:
                        pass
                    else:
                        product[code]['qty']=new_quantity   
                    print(json.dumps(product,indent=2))
                elif k==5:
                    print('Back to main menu')
        else:
            print('Incorrect Password!!!')
    if h==2:
        product_price=0
        kk='y'
        kkr='y'
        while kk=='y':
            print('     WELCOME TO OUR SHOP!!!\n     OUR SHOP HAS VARIETY OF CHOICES')
            print('1.Show Products')
            print('2.Buy Product')
            print('3.Exit')
            inp=eval(input('Enter your choice(1,2,0);)'))
            if inp==1:
                print(json.dumps(product,indent=4))
                kk=='n'   
            elif inp==2:
                kkr='y'
                while kkr=='y':
                    Enter_product=eval(input('Enter The Code of the Product:'))
                    for keys in product:
                        if Enter_product==keys:
                            print('          Name of the Product is:',product[keys]['name'])
                            print('          Price of the Product is:',product[keys]['price'])
                            qty=eval(input('Enter the Quantity of the Product:'))
                            print()
                            print('       ***Checking for your Quantity in our Cart:-)***')
                            if qty<=product[keys]['qty']:
                                print('         Items are available in the Cart!!!')
                                kunjesh={Enter_product:{'name':product[Enter_product]['name'],'price':product[Enter_product]['price'],'qty':product[Enter_product]['qty']-qty}}
                                product_price+=product[keys]['price']*qty
                                print()
                                kkr=input('Do you want to buy another product(y/n):')
                                if kkr=='n':
                                    kk!='y'
                            else:
                                print('The Required Quantity is not Available In The Cart:-(')
                                continue
                    else:
                        for keys in product:
                            if Enter_product==keys:
                                break
                        else:
                            print('not found')
                print('Total Amount to be Paid:',product_price)
                payment=input('PAYMENT OPTION are:\n1.COD\n2.Cheque\nEnter Your Payment Option:)')
                if payment=='1':
                    print("Thank You for your payment option.\nYour Receipt will be sent with our Delivery boy:)")
                    break
                if payment=='2':
                    print("Thank You for your payment option.\nYour Receipt will be sent at your Mobile Number:)")
                    print()
                    print('        THANK YOU!\n        PLEASE COME AGAIN')
                    break
            elif inp==0:
                break
        #print(json.dumps(product,indent=3))     
    if h==0:
        print('Terminating Program!!!')
        break
                
                
                
    




