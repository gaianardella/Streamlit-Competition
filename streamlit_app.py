# import pickle
# from pathlib import Path

# import pandas as pd  # pip install pandas openpyxl
# import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
# import streamlit_authenticator as stauth  # pip install streamlit-authenticator


# Define the logout function
def logout():
    # Add logout logic here
    # For example, you can clear session data or redirect to a login page
    st.write("Logout clicked")

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="A Cloud Closet", page_icon=":dress:", layout="wide", sidebar_bg_color='blue')


# --- USER AUTHENTICATION ---

# Define username and password
CORRECT_USERNAME = "username"
CORRECT_PASSWORD = "password"

# Create a title and subheader
st.title("Login Page")
st.subheader("Enter your credentials to log in.")
# st.header("Enter your credentials to log in.") #is bigger


# Create input fields for username and password
username = st.text_input('Username')
password = st.text_input('Password', type='password')

if st.button("Login"):
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        st.success("You have successfully logged in.")
        show_question = True
    else:
        st.error('Invalid username or password')
        show_question = False
else:
    show_question = False
    
# Define the format function
def format_option(option):
    return "• " + option

if show_question:
    # ---- SIDEBAR ----
    # Add widgets to the sidebar
    st.sidebar.header("Sidebar")
    if st.sidebar.button("Logout"):
        logout()
    
        
# Add other widgets to the sidebar here
    st.sidebar.title(f"Welcome {CORRECT_USERNAME}")
    st.sidebar.header("Please Filter Here:")
    choice = st.sidebar.radio(
        "Select choice:",
        options=["Upload Clothes", "Pick me an outfit", "Give me some stats", "I need help"] #,
#         format_func=format_option
#         index=0
    )
    
    if choice =="Upload Clothes":
        st.subheader("Welcome to the Upload Clothes page")
    elif choice =="Pick me an outfit":
        st.subheader("Welcome to the Pick me an outfit page")
    elif choice =="Give me some stats":
        st.subheader("Welcome to the Give me some stats page")
    else:
        st.subheader("How to use the app")
        
        
# # --- USER AUTHENTICATION ---
# names = ["Peter Parker", "Rebecca Miller"]
# usernames = ["pparker", "rmiller"]

# # load hashed passwords
# file_path = Path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("rb") as file:
#     hashed_passwords = pickle.load(file)

# authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
#     "sales_dashboard", "abcdef", cookie_expiry_days=30)

# name, authentication_status, username = authenticator.login("Login", "main")

# if authentication_status == False:
#     st.error("Username/password is incorrect")

# if authentication_status == None:
#     st.warning("Please enter your username and password")

# if authentication_status:
#     # ---- READ EXCEL ----
#     @st.cache
#     def get_data_from_excel():
#         df = pd.read_excel(
#             io="supermarkt_sales.xlsx",
#             engine="openpyxl",
#             sheet_name="Sales",
#             skiprows=3,
#             usecols="B:R",
#             nrows=1000,
#         )
#         # Add 'hour' column to dataframe
#         df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
#         return df

#     df = get_data_from_excel()

#     # ---- SIDEBAR ----
#     authenticator.logout("Logout", "sidebar")
#     st.sidebar.title(f"Welcome {name}")
#     st.sidebar.header("Please Filter Here:")
#     city = st.sidebar.multiselect(
#         "Select the City:",
#         options=df["City"].unique(),
#         default=df["City"].unique()
#     )

#     customer_type = st.sidebar.multiselect(
#         "Select the Customer Type:",
#         options=df["Customer_type"].unique(),
#         default=df["Customer_type"].unique(),
#     )

#     gender = st.sidebar.multiselect(
#         "Select the Gender:",
#         options=df["Gender"].unique(),
#         default=df["Gender"].unique()
#     )

#     df_selection = df.query(
#         "City == @city & Customer_type ==@customer_type & Gender == @gender"
#     )

#     # ---- MAINPAGE ----
#     st.title(":bar_chart: Sales Dashboard")
#     st.markdown("##")

#     # TOP KPI's
#     total_sales = int(df_selection["Total"].sum())
#     average_rating = round(df_selection["Rating"].mean(), 1)
#     star_rating = ":star:" * int(round(average_rating, 0))
#     average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

#     left_column, middle_column, right_column = st.columns(3)
#     with left_column:
#         st.subheader("Total Sales:")
#         st.subheader(f"US $ {total_sales:,}")
#     with middle_column:
#         st.subheader("Average Rating:")
#         st.subheader(f"{average_rating} {star_rating}")
#     with right_column:
#         st.subheader("Average Sales Per Transaction:")
#         st.subheader(f"US $ {average_sale_by_transaction}")

#     st.markdown("""---""")

#     # SALES BY PRODUCT LINE [BAR CHART]
#     sales_by_product_line = (
#         df_selection.groupby(by=["Product line"]).sum()[["Total"]].sort_values(by="Total")
#     )
#     fig_product_sales = px.bar(
#         sales_by_product_line,
#         x="Total",
#         y=sales_by_product_line.index,
#         orientation="h",
#         title="<b>Sales by Product Line</b>",
#         color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
#         template="plotly_white",
#     )
#     fig_product_sales.update_layout(
#         plot_bgcolor="rgba(0,0,0,0)",
#         xaxis=(dict(showgrid=False))
#     )

#     # SALES BY HOUR [BAR CHART]
#     sales_by_hour = df_selection.groupby(by=["hour"]).sum()[["Total"]]
#     fig_hourly_sales = px.bar(
#         sales_by_hour,
#         x=sales_by_hour.index,
#         y="Total",
#         title="<b>Sales by hour</b>",
#         color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
#         template="plotly_white",
#     )
#     fig_hourly_sales.update_layout(
#         xaxis=dict(tickmode="linear"),
#         plot_bgcolor="rgba(0,0,0,0)",
#         yaxis=(dict(showgrid=False)),
#     )


#     left_column, right_column = st.columns(2)
#     left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
#     right_column.plotly_chart(fig_product_sales, use_container_width=True)


#     # ---- HIDE STREAMLIT STYLE ----
#     hide_st_style = """
#                 <style>
#                 #MainMenu {visibility: hidden;}
#                 footer {visibility: hidden;}
#                 header {visibility: hidden;}
#                 </style>
#                 """
#     st.markdown(hide_st_style, unsafe_allow_html=True)
    
    
    
    
    
    
#     ###############################
#     # # import snowflake.connector

# # # Define username and password
# # CORRECT_USERNAME = "username"
# # CORRECT_PASSWORD = "password"

# # # Create a title and subheader
# # st.title("Login Page")
# # st.subheader("Enter your credentials to log in.")
# # # st.header("Enter your credentials to log in.") #is bigger


# # # Create input fields for username and password
# # username = st.text_input('Username')
# # password = st.text_input('Password', type='password')

# # if st.button("Login"):
# #     if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
# #         st.success("You have successfully logged in.")
# #         show_question = True
# #     else:
# #         st.error('Invalid username or password')
# #         show_question = False
# # else:
# #     show_question = False

# # # Show Question
# # if show_question:
# #     question_placeholder = st.empty()
# #     options = ['Option A', 'Option B', 'Option C']
# #     selected_option = st.selectbox('Select an option', options)

# # #     if question_placeholder.button('Refresh'):
# # #         selected_option = None

# #     if selected_option:
# #         question_placeholder.write('You selected:', selected_option)
