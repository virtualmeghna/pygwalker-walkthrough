import pygwalker as pyg
import streamlit.components.v1 as components
import pandas as pd
import streamlit as st

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Pygwalker: Power of Tableau, Convenience of Python",
    layout="wide"
)

# Add Title
st.title("Pygwalker: Power of Tableau, Convenience of Python")

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
st.sidebar.subheader("Or Use an Example Dataset :point_down:")

st.markdown('''When you work with data in data science, one of the essential things you do is create visual representations of that data, like charts and graphs. These visualizations help you understand the data better and communicate your findings effectively to others. 
            Now, there are different tools available for making these charts. Some are like fancy software you need to pay for, such as Tableau. Others are free and use a programming language called Python. The catch is, some of these tools can be quite complex, and you might need to invest a lot of time and effort to create your charts.

**One of these Python libraries is called PyGWalker. It's like having a super handy tool in your data analysis toolkit. It's specifically designed to work within Jupyter notebooks, which are a popular environment for data analysis in Python. PyGWalker is all about making your data analysis and chart creation faster and more interactive, similar to how Tableau works.** ''')
# st.write('---')

if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Access the Dashboard**')
    pyg_html = pyg.walk(df, return_html=True, env='Streamlit')
    components.html(pyg_html, height=1000, scrolling=True)


else:
    if st.sidebar.button('Press to use Example Dataset'):
        # Example data
        @st.cache_data
        def load_data():
            df = pd.read_csv('pokemon.csv')
            return df
        df = load_data()

        with   st.sidebar.expander("About the example Dataset"):
            st.write("This data set includes 721 Pokemon, including their number, name, first and second type, and basic stats: HP, Attack, Defense, Special Attack, Special Defense, and Speed.")
        st.subheader('**Input DataFrame**')
        with st.expander("Preview the Dataset"):
            st.write(df)
        # st.write('---')
        st.header('**Access the Dashboard**')
        pyg_html = pyg.walk(df, return_html=True, hideDataSourceConfig=False)
        components.html(pyg_html, height=1000, scrolling=True)
        

# # Generate the HTML using Pygwalker
# pyg_html = pyg.walk(df, return_html=True, hideDataSourceConfig=False)

# # Embed the HTML into the Streamlit app
# components.html(pyg_html, height=1000, scrolling=True)
