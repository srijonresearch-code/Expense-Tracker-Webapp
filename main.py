import streamlit as st
import pandas as pd
st.set_page_config(layout="wide",page_title="Expense-Tracker",page_icon="📊")
st.markdown("""
<style>
.title-box {
    background-color: #1f3b5c;
    padding: 20px;
    border-radius: 8px;
    text-align: center;        
}

.title-text {
    color: white;
    font-size: 36px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""<div class="title-box"><div class="title-text">Expense-Tracker</div></div>""",unsafe_allow_html=True)
expenses=pd.read_csv("expenses.csv",index_col=False)
col1,col2,col3=st.columns([1,2,1])
col1.subheader("Add New Expense",text_alignment="left")
col2.subheader("Your Expenses",text_alignment="center")
col3.subheader("Track Summary",text_alignment="right")
with col1.form("Add_New_Expense"):
    expense_name=st.text_input("Expense Name",placeholder="example: coffee")
    amount=st.number_input("Amount ($)")
    date=st.date_input("Date")
    if st.form_submit_button("Add Expense"):      
        if (expense_name==""):
            st.error("Error",icon=":material/error:")
            st.toast("Invalid Input")
        else:
            if amount==0:
                st.error("Error",icon=":material/error:")
                st.toast("Amount can't be 0") 
            else:
                row_df={"Name":expense_name,"Amount":amount,"Date":date}
                expenses=pd.concat([expenses,pd.DataFrame([row_df])],ignore_index=True)
                expenses.to_csv("expenses.csv",index=False)
                st.rerun()
col2.dataframe(expenses)
delete_expense=col2.number_input("Enter Number to Delete",min_value=0)
if col2.button("Delete",type="primary"):
    try:
        expenses=expenses.drop(delete_expense)
        expenses.to_csv("expenses.csv",index=False)
    except:
        pass
    st.rerun()    

col3.metric("Total Spent ($)",expenses["Amount"].sum())
col3.metric("Total Expenses",len(expenses))
if "confirm" not in st.session_state:
    st.session_state["confirm"]=False
if col3.button("Reset",type="primary"):
    st.session_state["confirm"]=True     
if st.session_state["confirm"]:
    col3.warning("All data will be lost")
    if col3.button("confirm"):
        expenses=pd.DataFrame(columns=["Name", "Amount", "Date"])
        expenses.to_csv("expenses.csv",index=False)
        st.session_state["confirm"]=False    
        st.rerun()
        




