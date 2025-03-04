#streamlit library install krengy
#pip install streamlit

import streamlit as st
st.st_page_config(page_title="growth mind set project",project_icon="⭐")
st.title("Growth_Mindset Challange : Web App with Streamlit ")
st.header("Welcome to YUour Growth Journey! ")
st.write("Embrace challenges, learn from mistakes ,and unlock your full potential. This AI-powerd app helps you build a growth mindset weth reflection, challenges,and achievements!⍣")
#quote section
st.header("Today's Growth Mindset Quote")
st.write("Success is not final, failur is not fatal: it is the courage to continue that counts.- Winston Churchill")
st.header("What's Your Challenge Todayt?")
user-input = st.text-input("Describea challenge you're facing:")

#condition
if User-input:
     st.success(f"you're facing : {user_input}. keep pushing forward towards your goal!")
     else:
        st.warning("Tell us about your  challenge to get started!")
        #reflexing
        st.header("Reflcting on Your Learning")
        reflection =st.text_area("Write upur reflection here:")
        if reflection:
              st.success("Greate Insight! Your reflection: {reflection}")
              else:
                  st.info("Reflection on past experience help you frow! Share your difficulties")
                  
                  #achievements
            st.header("Celebrate Your Wins!")
            acheivement=st.text_input("Share something you've recently accomplished:")

if acheivements:
     st.success(f"Amazing! You achieved: {acheivement}")
     else:
        st.info("Big or small, ever y acheivement counts! Share one now 🤩")

        #footer
        st.write("- - -")
        st.write("🌠 keep believing in yourself. Growth is a journey, not a destination!🌟")
        st.write("**⛔ Created by Saima Riaz**")


