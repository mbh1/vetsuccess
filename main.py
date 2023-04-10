import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="VetSuccess", layout="wide")


# Load the image file
logo = Image.open("Media\VetSuccess Logo White.jpg.png")

# Add the logo to the app and center it
st.image(logo, width=300)

#creating two columns for dropdown
col1,col2 = st.columns(2)

#font size for subheaders since its slightly too big
st.markdown(
    """
    <style>
    .subtitle {
        background-color: #0e1117;
        color: lightgrey;
        font-size:18px;
    }
    </style>
    """,unsafe_allow_html=True,
)


selected = option_menu(
    menu_title=None,
    options=["Home", "Resources", "About Us"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0px!important"},
        "icon": {"color": "#000000", "font-size": "25px"},
        "nav-item": {"padding": "3px 3px", "background-color": "#aea429"},
        "nav-link": {"font-size": "25px", "text-align": "center", "margin": "0px", "--hover-color": "#FEFBCF", "color": "#000000"},
        "nav-link-selected": {"background-color": "#fded29"},
    }

)

image_style = """
    position: fixed;
    top: 0;
    right: 0;
    margin-top: 10px;

    margin-right: 10px;
"""

page_bg_color = """
<style>
 [data-testid="stSidebar"] > div:first-child {
    background-color: #FFFFFF;}
 [data-testid="stHeader"] {
    background-color: #fded29;
    color: #000000;}
 </style>
"""

st.markdown(page_bg_color, unsafe_allow_html=True)

#creating chosen variable for drop down
chosen = None


# Home Page Content
if selected == "Home":
    st.title("Welcome to VetSuccess!")
    st.write("We are a non-profit organization that provides resources to veterans and their families. We are dedicated to helping veterans transition into civilian life and find success in their new careers. We provide resources such as job listings, resume templates, and interview tips. We also provide information on how to access VA benefits and how to get help with PTSD and other mental health issues. We are here to help you find success in your new life!")
    st.write("Please select a page from the menu above to get started!")
    st.header("News")
    st.write("Here are some recent news articles that we think you might find interesting!")
    st.subheader("New VA Benefits for Veterans")
    st.write("The VA has recently announced that they will be providing free mental health services to veterans who have been diagnosed with PTSD. This is a great step forward for veterans who have been struggling with mental health issues. We are excited to see what the future holds for veterans! [Read More](https://www.va.gov/opa/pressrel/pressrelease.cfm?id=5776)")
    st.subheader("New Job Listings")
    st.write("We have recently added some new job listings to our website. We are always adding new listings, so be sure to check back often! [Read More](https://www.va.gov/opa/pressrel/pressrelease.cfm?id=5776)")
    st.subheader("New Interview Tips")
    st.write("We have recently added some new interview tips to our website. We are always adding new tips, so be sure to check back often! [Read More](https://www.va.gov/opa/pressrel/pressrelease.cfm?id=5776)")


   
# About Us Page Content
elif selected == "About Us": 

    st.title("About Us")
    st.write("We are a group of veterans who are passionate about helping other veterans transition into civilian life. We know how difficult it can be to find a job after leaving the military, and we want to help you find success in your new career. We have all been there, and we want to help you avoid the same mistakes that we made. We are here to help you find success in your new life!")
    st.write("Please select a page from the menu above to get started!")

    st.subheader("Our Team")
    st.write("Here are the members of our team!")
    st.markdown(
        """
        - **Robin Obregon** - Team Lead
        - **Carlos Ramos** - Content Manager
        - **Saraid Pinto** - UI Designer
        - **Pablo Flores Lugo** - Developer
        - **Jonathan Oviedo** - Developer
        - **Michael Harari** - Developer
        """,
        unsafe_allow_html=True,
    )
#Resource page

elif selected == "Resources":
    
  chosen = option = st.selectbox(
         "Browse our available resources",
         ("Health","Education", "Housing", "Discounts"))
     
if chosen == "Health":
   st.title("Health") 
   st.write("Current Available Health benefits offered to you")
   st.markdown('<p class="subtitle"><u>Veteran health care eligibility</u></p>',unsafe_allow_html=True)
   st.write("https://www.va.gov/health-care/eligibility/")
   st.markdown('<p class="subtitle"><u>Veteran with disability benefits</u></p>',unsafe_allow_html=True)
   st.write("https://www.va.gov/disability/dependency-indemnity-compensation/")
   st.markdown('<p class="subtitle"><u>Veteran Crisis Line and Therapy</u></p>',unsafe_allow_html=True)
   st.write("https://www.va.gov/health-care/health-needs-conditions/mental-health/")
   st.write("Call 988.")
   st.write("Text 838255.")
   st.write("Chat Online: https://www.veteranscrisisline.net/get-help-now/chat/")
   



elif chosen == "Housing":
   st.title("Housing")
   st.write("Current Available housing benefits offered to you")
   st.markdown('<p class="subtitle"><u>VA Homeless Programs</u></p>',unsafe_allow_html=True)
   st.write("https://www.va.gov/homeless/nationalcallcenter.asp")
   st.write(" 1-877-4AID VET (877-424-3838)")
   st.markdown('<p class="subtitle"><u>VA Home Loan Eligibility</u></p>',unsafe_allow_html=True)
   st.write("https://www.va.gov/housing-assistance/home-loans/eligibility/")
   st.markdown('<p class="subtitle"><u>Veteren housing grant</u></p>',unsafe_allow_html=True)
   st.write("https://www.va.gov/housing-assistance/disability-housing-grants/how-to-apply/")

elif chosen == "Education":
    st.title("Education")
    st.write("Current Available Education benefits offered to you")
    st.markdown('<p class="subtitle"><u>GI Bill Eligebility</u></p>',unsafe_allow_html=True)
    st.write("https://www.va.gov/education/about-gi-bill-benefits/post-9-11/")
    st.markdown('<p class="subtitle"><u>Employment and Readiness</u></p>',unsafe_allow_html=True)
    st.write("https://www.va.gov/careers-employment/vocational-rehabilitation/")
    st.markdown('<p class="subtitle"><u>Education and career counseling</u></p>',unsafe_allow_html=True)
    st.write("    https://www.va.gov/careers-employment/education-and-career-counseling/")

elif chosen == "Discounts":
    st.title("Discounts")
    st.write("Current Available Discounts offered to you")
    st.markdown('<p class="subtitle"><u>43% off AARP Membership</u></p>',unsafe_allow_html=True)
    st.write("https://www.military.com/discounts/veterans-and-military-members-save-43-off-aarp")
    st.markdown('<p class="subtitle"><u>Military Discount for Theme Tickets</u></p>',unsafe_allow_html=True)
    st.write("https://disneyworld.disney.go.com/special-offers/military-multi-day-tickets-2023/")
    st.markdown('<p class="subtitle"><u>10% off Nike purchases for Militray personnel</u></p>',unsafe_allow_html=True)
    st.write("https://www.nike.com/help/a/military-discount")



st.text("")
st.text("")
st.text("")
st.text("")   
st.text("") 
st.title("Resources")
st.write("Here are some resources that we think you might find helpful!")
st.markdown(
       """
       - [Job Listings](https://www.va.gov/opa/pressrel/pressrelease.cfm?id=5776)
       - [Resume Templates](https://www.va.gov/opa/pressrel/pressrelease.cfm?id=5776)
       - [Interview Tips](https://www.va.gov/opa/pressrel/pressrelease.cfm?id=5776)
       - [VA Benefits](https://www.va.gov/opa/pressrel/pressrelease.cfm?id=5776)
       - [Mental Health Resources](https://www.va.gov/opa/pressrel/pressrelease.cfm?id=5776)
       """,
       unsafe_allow_html=True,
   )
st.write("Please select a page from the menu above to get started!")
    
 # Define options for the dropdown menu

  
   
# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #fded29;
        color: black;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="footer">
        <p>© 2023 VetSuccess - All Rights Reserved</p>
    </div>
    """,
    unsafe_allow_html=True,
)
