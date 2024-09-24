import streamlit as st 
import pandas as pd
import matplotlib.pyplot as pt


#This function creats the csv file for storing the form entries. 
csv = 'notes.csv'
def form():
    column = ["Date", "Amount", "Category", "Description"]#Specifiying the columns for the csv file.
    try:
        pd.read_csv(csv)
    except FileNotFoundError:
        df = pd.DataFrame(columns=column)   #Try and Except block  used for creating the file if it dosent exit, if it does it just reads the file.
        df.to_csv(csv,index=False)

#Function for opening and writing/appending the csv file(editing the file).
def enter(data1, data2, data3, data4):
    with open(csv, 'a+') as f: #Append and Reading the file.
        f.write(f"{data1},{data2},{data3},{data4}\n")



#Main body of the application.
st.title("Simple Finance Tracker")

st.subheader("You Can Either Upload a CSV file or Create your own!")


#allows for making use of anther CSV file with similar structure to the one being used in the application.
upload_file = st.file_uploader("Choose a CSV File", type="csv")

if upload_file is not None:
    st.write("File Uploaded....")
    df = pd.read_csv(upload_file)
    st.subheader("Data Preview") #Displays a Preview of the CSV file.
    st.write(df.head())

    st.subheader("Data Summery") #Displays a summary of the CSV file..
    st.write(df.describe())


#This section is for filtering the columns of the CSV file and their valuses. 
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select Columns to Filter by", columns) #Selecting the column in the form of a bropbox.
    unique_values = df[selected_columns].unique()
    selected_value = st.selectbox("Select value", unique_values)    #Selecting the values of the already selected column.

    filtered_df = df[df[selected_columns]== selected_value]
    st.write(filtered_df) #Displays the filtered values of the selected column.


#This Section is for plotting a graph by selecting the columns that will act as the X-axis and Y-axis respectively.
    st.subheader("Plot Data")
    x_axis = st.selectbox("Select the X-axis column", columns)
    y_axis = st.selectbox("Select the Y-axis", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_axis)[y_axis])



#This Sections contains the values for the Form in which users will have to manually input the datas for the CSV file.
else:
    form()  #Simply Calls the first function in order to access the CSV file.

    with st.form(key="My_form", clear_on_submit=True):  #Syntax for creating a form in streamlit.
        st.write("Entries")

        date = st.text_input("Date", key='date',placeholder="Enter date in the format (DD-MM-YYYY)")
        amount =  st.text_input('Amount', key='number', placeholder="Enter an Amount")
        category =  st.text_input('Category', key='ticker', placeholder="Income or Expense")
        description =  st.text_input('Description', key='note', placeholder="Enter a Discription")

        submit = st.form_submit_button('Submit')

        if submit:
            enter(date,amount,category,description)

    st.info('### APP, Show content of CSV file :point_down:...')


    #Simply displays the last vslues inputed into the foem. i.e Amount, Category, Description
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Amount", value=f"{amount}")
    col2.metric(label="Category", value=f"{category}")
    col3.metric(label="Description", value=f"{description}")



#Dsiplaying the summary.
    data = (pd.read_csv(csv))
    st.subheader("Data Preview")
    st.write(data.head())
    st.subheader("Data Summery")
    st.write(data.describe())



#Filtering the data.
    st.subheader("Filter Data")
    columns = data.columns.tolist()
    selected_columns = st.selectbox("Select Columns to Filter by", columns)
    unique_values = data[selected_columns].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = data[data[selected_columns]== selected_value]
    st.write(filtered_df)



    




