import streamlit as st

st.write('Building own app')
st.title('Swastik College')
st.markdown('Sports')
st.header('1200ml')

st.checkbox('Pick  option',['Yes','No'])
st.button('Click')
st.radio('Gender',['Male','Female'])

st.selectbox('Pick a fruit',['Apple','Banana','Grapes'])
st.multiselect('Choose a planet',['Earth','Mars','Neptune'])

st.slider('Pick a number',0,50)
st.success("You did it!")
st.error("Error Occured")
st.warning("It's easy to build a Streamlit App")
st.info('Sujan is a xakka')

st.button('Click Here')

# INput Fields
st.number_input("Enter your Age:",0,100)


# SideBar and Container
st.sidebar.title('Here it comes:')
