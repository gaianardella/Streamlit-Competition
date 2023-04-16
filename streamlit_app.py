import streamlit as st
# from streamlit_option_menu import option_menu
import pandas as pd
from io import StringIO
from PIL import Image

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="A Cloud Closet", page_icon=":dress:", layout="wide")

my_color_list=["Blue", "Red", "White", "Black", "Green", "Yellow", "Purple", "Pink"]
my_item_list=["Sweater", "Trousers", "T-Shirt", "Shorts"]
# my_color_list = my_color_list.set_index('Color')

# Define the logout function
def logout():
    # Add logout logic here
    # For example, you can clear session data or redirect to a login page
    st.write("Logout clicked")

# --- USER AUTHENTICATION ---

# Define username and password
CORRECT_USERNAME = "username"
CORRECT_PASSWORD = "password"


if 'login' not in st.session_state:
   # Create a title and subheader
    st.title("Login Page")
    st.subheader("Enter your credentials to log in.")
    login_form = st.form(key='login_form')
    username = login_form.text_input(label='username')
    password = login_form.text_input(label='password', type='password')
    submit_button = login_form.form_submit_button(label='submit')


    if submit_button:
        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            st.session_state.username = username
            st.session_state['login'] = True
            st.success("You have successfully logged in.")
            # show_question = True
            st.experimental_rerun()
        else:
            st.error('Invalid username or password')
            # show_question = False
    # else:
    #     show_question = False

if 'login' in st.session_state:
    st.empty()
    # st.write(f"hello, {CORRECT_USERNAME}")
    # if show_question:
    # Display the main page
    # st.title("Hello world!")
    # st.write("Welcome to the main page.")
    
    # Display the sidebar menu
    with st.sidebar:
        option_icons = {
            "Home": "house",
            "Upload Clothes": "box-arrow-in-up",
            "Pick me an outfit": "palette-fill",
            "Give me some stats": "bar-chart-fill",
            "Settings": "gear"
        }
        option = st.selectbox("Main Menu", options=list(option_icons.keys()), index=0, format_func=lambda option: f"<i class='bi bi-{option_icons[option]}'></i> {option}", unsafe_allow_html=True)

#         selected = option_menu("Main Menu", ["Home", "Upload Clothes", "Pick me an outfit", "Give me some stats", "Settings"], 
#             icons=['house', 'box-arrow-in-up', 'palette-fill', 'bar-chart-fill', 'gear'], menu_icon="cast", default_index=0)
          

    # Display the selected page
    if selected == "Home":
        st.title("Home page")
        st.header("This is the Home page.")
        st.subheader("1) Upload your photos")
        st.write("Upload your clothes photos in the app")
        st.subheader("2) Generate an outfit")
        st.write("Click to generate an outfit")
        st.subheader("3) Manage your wardrobe")
        st.write("See which clothes you never wear")
    elif selected == "Upload Clothes":
        st.title("Upload your clothes")
        st.subheader("This is the Upload Clothes page.")

        # Let's put a pick list here so they can pick the fruit they want to include 
        item_selected = st.multiselect("Pick item:", list(my_item_list), ['Sweater','Shorts'])
        # colors_to_show = my_color_list[colors_selected] #pandas.dataFrame.loc[source] Access a group of rows and columns by label(s) or a boolean array.
        # Display the table on the page.
        # st.dataframe(colors_to_show)
        
        show_upload=False
        if st.button("Submit Item"):
            show_upload=True
    
        if show_upload:
            colors_selected = st.multiselect("What color is the item:", list(my_color_list), ['Blue','Red'])
            #single file uploader (doesn't accept more than one file)
            uploaded_file = st.file_uploader("Choose a file")
            if uploaded_file is not None:
                # To read file as bytes:
                bytes_data = uploaded_file.getvalue()
                st.write(bytes_data)
                # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                # st.write(stringio)
                # # To read file as string:
                # string_data = stringio.read()
                # st.write(string_data)

            # # Can be used wherever a "file-like" object is accepted:
            # dataframe = pd.read_csv(uploaded_file)
            # st.write(dataframe)

    elif selected == "Pick me an outfit":
        st.title("Generate an outfit")
        st.subheader("This is the Pick me an outfit page.")
        temperature = st.radio("What\'s the temperature?",('Hot', 'Cold'))

        if temperature == 'Hot':
            st.write('You selected hot.')
        else:
            st.write('You selected cold.')

        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Top")
            top = Image.open('sweater.jpeg')
            st.image(top, width=340)
            

        with col2:
            st.header("Bottom")
            bottom = Image.open('trousers.jpeg')
            st.image(bottom, width=340)

      
        with col3:
            var=-1
            # if st.button("I don't like it", key="dislike"):
            #     show_generate=True
            # if st.button("I like it", key="like"):
            #     show_generate=False

            st.markdown("""
                <style>
                    div.stButton > button:first-child {
                        text-align:center;
                        background-color: #FF6347;
                        padding-left: 20px;
                        padding-right: 20px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        height: 100%; /* set the height of the container to 100% */
                    }
                </style>
            """, unsafe_allow_html=True)
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            if st.button("Disike"):
                var = 0

            st.markdown("""
                <style>
                    div.stButton > button:first-child {
                        text-align:center;
                        background-color: #00FF00;
                        padding-left: 20px;
                        padding-right: 20px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        height: 100%; /* set the height of the container to 100% */
                    }
                </style>
            """, unsafe_allow_html=True)
            if st.button("Like"):
                var = 1
        
        if var==1:
            st.write("Cool!")
        elif var == 0:
            st.write("generate again")
            

     
    elif selected == "Give me some stats":
        st.title("Stats")
        st.subheader("This is the Give me some stats page.")
    elif selected == "Settings":
        st.title("Settings")
        st.subheader("This is the Settings page.")
