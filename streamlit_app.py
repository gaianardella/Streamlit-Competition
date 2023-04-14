import streamlit as st
# # import snowflake.connector

# # Define username and password
# CORRECT_USERNAME = "username"
# CORRECT_PASSWORD = "password"

# # Create a title and subheader
# st.title("Login Page")
# st.subheader("Enter your credentials to log in.")
# # st.header("Enter your credentials to log in.") #is bigger


# # Create input fields for username and password
# username = st.text_input('Username')
# password = st.text_input('Password', type='password')

# if st.button("Login"):
#     if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
#         st.success("You have successfully logged in.")
#         show_question = True
#     else:
#         st.error('Invalid username or password')
#         show_question = False
# else:
#     show_question = False

# # Show Question
# if show_question:
#     question_placeholder = st.empty()
#     options = ['Option A', 'Option B', 'Option C']
#     selected_option = st.selectbox('Select an option', options)

# #     if question_placeholder.button('Refresh'):
# #         selected_option = None

#     if selected_option:
#         question_placeholder.write('You selected:', selected_option)




# ---- SIDEBAR ----
st.sidebar.title(f"Welcome {name}")
st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique(),
)

gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)
