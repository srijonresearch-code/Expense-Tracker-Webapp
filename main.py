import json
import streamlit as st
#loding data storage=>expenses.json
try:
    with open("expenses.json","r") as file:
        expense=json.load(file)
except:
    expense=[] #when the json file is not available        
st.title(f"📊 Expense-Tracker",text_alignment="center")

#Program menu design
"""
print(f"2. View Expenses")
print(f"3. View Total Spent")
print(f"4. View Total Expenses")
print(f"5. Delete Expense")
print(f"6. Clear Expenses")
print(f"7. Exit")
"""   
    #if else condition
with st.form("Add Expense"):
    st.header("Add Expense",text_alignment="center")
    category=st.text_input("Enter Category")
    amount=st.number_input("Enter Amount",min_value=100,max_value=1000)
    date=st.text_input("Enter Date",placeholder="DD/MM/YY")    
    if st.form_submit_button("Submit",icon=":material/check:",icon_position="right"):
        if expense==[] and (category =="" and amount ==100 and date==""):
            st.error("Error",icon=":material/error:")
            st.toast("Invalid input")
        elif (expense[len(expense)-1]["Category"]==category) and (expense[len(expense)-1]["Date"]==date) and (expense[len(expense)-1]["Amount"]==amount):
            st.error("Error",icon=":material/error:")
            st.toast("Value already exists")
        
        else:
            expense.append({"Category":category,"Amount":amount,"Date":date})
            with open("expenses.json","w") as file:
                json.dump(expense,file)
            st.success("Expense added successfully",icon=":material/data_check:")    
st.divider()
        
    
if st.button("View Expenses"):
    index=0
    st.write(f"{'Category':<15}{'Amount':<10}{'Date':<12}")
    print("-"*36)
    while index<len(expense):
        print(f"{index}. {expense[index]['Category']:<12}{expense[index]['Amount']:<10}{expense[index]['Date']:<12}")
        index+=1
    print("-"*20)    
"""
    elif option==3:
        total_spent=0
        index=0
        while index<len(expense):
            total_spent=total_spent+expense[index]["Amount"]
            index+=1
        print(f"Total spent: {total_spent}")
        print("-"*20)
    elif option==4:
        print(f"Total Expenses: {len(expense)}")
        print("-"*20)
    elif option==5:
        while True:
            index=0
            print(f"{'Category':<15}{'Amount':<10}{'Date':<12}")
            print("-"*36)
            while index<len(expense):
                print(f"{index}. {expense[index]['Category']:<12}{expense[index]['Amount']:<10}{expense[index]['Date']:<12}")
                index+=1
            print("-"*20)
            try:
                delete_index=int(input("Enter number to delete: "))
            except ValueError:
                print("Invalid input :(")
                print("-"*20)
                continue
            if 0<=delete_index<len(expense):    
                expense.pop(delete_index)
                with open("expenses.json","w") as file:
                    json.dump(expense,file)
                print("Expense deleted successfully! ^_^")
                break
            else:
                print("Invalid number! Please enter correct number :(")    
            print("-"*20)
    elif option==6:
        with open("expenses.json","w") as file:
            json.dump([],file)
            expense=[]
        print(f"Expenses cleared successfully! ^_^")
        print("-"*20)    
    elif option==7:
        print(f"Program exited successfully! ^_^")
        print("-"*20)
"""
      