import streamlit as st
import numpy as np
import joblib

# Load the saved model and scaler
model = joblib.load('parkinsons_model.pkl')
scaler = joblib.load('scaler.pkl')

# Title
st.title('Parkinson\'s Disease Prediction App')

st.write('Enter the required parameters to predict if the person has Parkinson\'s Disease.')

# Default values (example values or empty if no input)
default_values = {
    'MDVP_Fo_Hz': 119.99200,
    'MDVP_Fhi_Hz': 157.30200,
    'MDVP_Flo_Hz': 74.99700,
    'MDVP_Jitter_percent': 0.00784,
    'MDVP_Jitter_Abs': 0.00007,
    'MDVP_RAP': 0.00370,
    'MDVP_PPQ': 0.00554,
    'Jitter_DDP': 0.01109,
    'MDVP_Shimmer': 0.04374,
    'MDVP_Shimmer_dB': 0.42600,
    'Shimmer_APQ3': 0.02182,
    'Shimmer_APQ5': 0.03130,
    'MDVP_APQ': 0.02971,
    'Shimmer_DDA': 0.06545,
    'NHR': 0.02211,
    'HNR': 21.03300,
    'RPDE': 0.414783,
    'DFA': 0.815285,
    'spread1': -4.813031,
    'spread2': 0.266482,
    'D2': 2.301442,
    'PPE': 0.284654
}

# Input box for the user to paste the comma-separated values
user_input = st.text_area(
    'Paste the comma-separated values (e.g., 119.99200,157.30200,...)',
    height=100
)

# Button to auto-fill the input fields
if st.button('Fill'):
    try:
        # Split the input string by commas and convert to float
        input_values = [float(value.strip()) for value in user_input.split(',')]

        # Update the default values with the parsed input values
        for i, key in enumerate(default_values):
            default_values[key] = input_values[i]

        st.success('Values successfully filled!')
    except Exception as e:
        st.error('Invalid input format. Please make sure the input is in the correct comma-separated format.')

# Now, use the updated values in the number inputs
MDVP_Fo_Hz = st.number_input('MDVP-Fo(Hz)', format="%.5f", value=default_values['MDVP_Fo_Hz'])
MDVP_Fhi_Hz = st.number_input('MDVP-Fhi(Hz)', format="%.5f", value=default_values['MDVP_Fhi_Hz'])
MDVP_Flo_Hz = st.number_input('MDVP-Flo(Hz)', format="%.5f", value=default_values['MDVP_Flo_Hz'])
MDVP_Jitter_percent = st.number_input('MDVP-Jitter(%)', format="%.5f", value=default_values['MDVP_Jitter_percent'])
MDVP_Jitter_Abs = st.number_input('MDVP-Jitter(Abs)', format="%.5f", value=default_values['MDVP_Jitter_Abs'])
MDVP_RAP = st.number_input('MDVP-RAP', format="%.5f", value=default_values['MDVP_RAP'])
MDVP_PPQ = st.number_input('MDVP-PPQ', format="%.5f", value=default_values['MDVP_PPQ'])
Jitter_DDP = st.number_input('Jitter-DDP', format="%.5f", value=default_values['Jitter_DDP'])
MDVP_Shimmer = st.number_input('MDVP-Shimmer', format="%.5f", value=default_values['MDVP_Shimmer'])
MDVP_Shimmer_dB = st.number_input('MDVP-Shimmer(dB)', format="%.5f", value=default_values['MDVP_Shimmer_dB'])
Shimmer_APQ3 = st.number_input('Shimmer-APQ3', format="%.5f", value=default_values['Shimmer_APQ3'])
Shimmer_APQ5 = st.number_input('Shimmer-APQ5', format="%.5f", value=default_values['Shimmer_APQ5'])
MDVP_APQ = st.number_input('MDVP-APQ', format="%.5f", value=default_values['MDVP_APQ'])
Shimmer_DDA = st.number_input('Shimmer-DDA', format="%.5f", value=default_values['Shimmer_DDA'])
NHR = st.number_input('NHR', format="%.5f", value=default_values['NHR'])
HNR = st.number_input('HNR', format="%.5f", value=default_values['HNR'])
RPDE = st.number_input('RPDE', format="%.5f", value=default_values['RPDE'])
DFA = st.number_input('DFA', format="%.5f", value=default_values['DFA'])
spread1 = st.number_input('spread1', format="%.5f", value=default_values['spread1'])
spread2 = st.number_input('spread2', format="%.5f", value=default_values['spread2'])
D2 = st.number_input('D2', format="%.5f", value=default_values['D2'])
PPE = st.number_input('PPE', format="%.5f", value=default_values['PPE'])

# Button to Predict
if st.button('Predict'):

    # Making a prediction
    input_data = (
        MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs, MDVP_RAP,
        MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5,
        MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE
    )

    # Change input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the numpy array
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Standardize the data
    std_data = scaler.transform(input_data_reshaped)

    # Make prediction
    prediction = model.predict(std_data)

    if (prediction[0] == 0):
        st.success('The Person does NOT have Parkinson\'s Disease.')
    else:
        st.error('The Person HAS Parkinson\'s Disease.')
