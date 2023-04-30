Question 1 - 
Description - Create a small command-line program in Python to calculate the total invoice amount for the below purchases - 
Book - Introduction to Python Programming : Rs 499.00
Book - Python Libraries Cookbook : Rs. 855.00
Book - Data Science in Python : Rs. 645.00
Taxes and additional charges are described as details - 
GST : 12%
Delivery Charges : Rs. 250.00

code:

book1=int(input("Enter noof Introduction to python programming books you need: "))
book2=int(input("Enter noof python library copy books you need: "))
book3=int(input("Enter noof datascience in python books you need: "))
gst=0.12    #12%
total=(book1*499.0)+(book2*855.0)+(book3*645.0) # cost_book1=499.0,cost_book2=855.0,cost_book3=645.0
if total==0:
    print('please enter how many books you want')
else:
    total_invoice_amount=total+(total*gst)+250.0 #delivary_charges=250.0
    print('total invoice amount is: %.2f' % total_invoice_amount)


Question 2 - 
Description: Write a program in Python to print the number of unique letters in a string. Only new letters from the string should be counted and not duplicates.
Input : string1 = "India"
Output : uniqueLetters = i,n,d,a
Input : string1 = "Dedication"
Output : uniqueLetters = d,e,i,c,a,t,o,n

code:

string=input('Enter string: ')
string=string.lower()
se=list(set(string))
print("Unique letters are:",end=" ")
for i in string:
    if i in se:
        print(i,end=",")
        se.remove(i)
