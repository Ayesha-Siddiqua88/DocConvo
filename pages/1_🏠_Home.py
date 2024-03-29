import streamlit as st

# settings
page_title = "DocConvo"
page_icon = "📂"
layout = "centered"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

# with st.sidebar:
#     st.image("images/Logo.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-color: #527143;
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# styling
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .shadow-text {
              text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# body of page
st.title('📂 Welcome to DocConvo')

box_style = """
    background-color: #8da780;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
"""
st.markdown(
    f"""
    <br>
    <div style="{box_style}">
        <h4 style="shadow-text;">Empowering Your Health Journey – Navigate, Analyze, Thrive!</h4>
        <p>This platform is designed to help predict and analyze your health reports. Our platform leverages state-of-the-art machine learning models to provide swift and accurate predictions based on the data you input. Whether you're assessing your risk factors, monitoring your health journey, or seeking preventive measures, our user-friendly interface empowers you with valuable insights. Your well-being is our priority, and we are here to guide you through your health analysis journey. Analyze, understand, and thrive with our Health Analyzer!</p>
    </div>
    <br>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    f"""
    <div style="{box_style}">
        <h4 style='color: #0066cc;'>How it Works!</h4>
        <ul>
            <li>Choose a specific Analyser from the sidebar.</li>
            <li>Enter the relevant data for prediction or analysis.</li>
            <li>Get instant results based on our trained machine learning models!</li>
        </ul>
    </div>
    <br>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div style="{box_style}">
        <h4 style='color: #0066cc;'>Features</h4>
        <ul>
            <li>Safely store and manage your previous health reports, creating a comprehensive archive for easy reference and tracking.</li>
            <li>Experience a seamless and user-friendly interface designed to simplify your health journey.</li>
            <li>Also provides Guidelines for effective diabetes and heart disease control.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

def create_footer():
    footer= """
            background-color:#8da780 ;
            padding: 20px;
            text-align: center;
            bottom: 0;
            width: 100%;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        """

    button="""
            background-color: #e78b2c; 
            color: #fff;
            padding: 5px 5px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        """
    text="""
            font-size:11px
        """

    st.markdown(
        f"""
        <br>
        <br>
        <div style="{footer}">
            <a style="{button}" href="https://github.com/Ayesha-Siddiqua88" target="_blank">GitHub</a>
            <br>
            <br>
            <p>Privacy | Health | Terms</p>
            <p><i>Made with 💙 by Ayesha & Asma</i></p>
            <p style="{text}">2023 Copyright. All Rights Reserved.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

create_footer()