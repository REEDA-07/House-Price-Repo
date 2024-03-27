import streamlit as st
import pandas as pd
import joblib
import warnings
warnings.filterwarnings('ignore')



st.markdown("<h1 style = 'color: #FC819E; text-align: center; font-family: Copperplate Gothic'>HOUSE PRICE PREDICTOR</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #F7418F; text-align: center; font-family: Copperplate Gothic '>Built By AJAO FAREEDAH: DAINTREE COHORT</h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html= True)

st.image('19198806.jpg', use_column_width= True)

st.header('Project Background Information', divider = True)
st.write("The House Price predicted Project aims to provide accurate estimations of residential property prices to assist both homebuyers and sellers. By leveraging advanced algorithms and data analytics, the app streamlines real estate transactions, supports informed decision-making, enhances market transparency, and offers a user-friendly interface. Ultimately, the objective is to simplify the process of buying and selling residential properties, benefiting consumers and industry professionals in the real estate sector.")

st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)

# Show Dataframe
df = pd.read_csv('ajah_deploy.csv')
st.dataframe(df)

# Input User Image
st.sidebar.image('pngwing.com (1).png',caption = 'Welcome User')

# Apply space in the sidebar
st.sidebar.markdown("<br>", unsafe_allow_html= True)
st.sidebar.markdown("<br>", unsafe_allow_html= True)

# Declare user Input Variables
st.sidebar.subheader('Input Variables', divider = True)
loc = st.sidebar.selectbox('Location', ["Ajah"])
bedroom = st.sidebar.selectbox('Bedroom', df['Bedroom'].unique())
bathroom = st.sidebar.selectbox('Bathrooms', df['Bathrooms'].unique())
toilet = st.sidebar.selectbox('Toilet', df['Toilet'].unique())
loc_area = st.sidebar.selectbox('Location Area', df['Location Area'].unique())

# Display the user input
input_var = pd.DataFrame()
input_var['Location'] = [loc]
input_var['Bedroom'] = [bedroom]
input_var['Bathrooms'] = [bathroom]
input_var['Toilet'] = [toilet]
input_var['Location Area'] = [loc_area]


st.markdown("<br>", unsafe_allow_html= True)
# Display the users input variable
st.subheader('Users Input Variables', divider= True)
st.dataframe(input_var)

# Import the scalers
loc_area_encoder = joblib.load('Location Area_encoder.pkl')
loc_encoder = joblib.load('Location_encoder.pkl')

# Transform the users input with the imported scalers
input_var['Location Area'] = loc_area_encoder.transform(input_var[['Location Area']])
input_var['Location'] = loc_encoder.transform(input_var[['Location']])

# st.dataframe(input_var)

model = joblib.load('HousePriceModel.pkl')
predicted = model.predict(input_var)


# Creating predicted
if st.button('Predict Price'):
        st.snow()
        st.success(f'The predicted price for your desired house is: {predicted[0].round(2)}')


# if st.button('Predict Churn'):
#     if predicted == 0:
#         st.error('Customer Has CHURNED')
#     else:
#         st.success('Customer Is With Us')