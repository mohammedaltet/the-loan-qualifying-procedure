import streamlit as st
import joblib 
import pandas as pd

Inputs = joblib.load("Inputs.pkl")
Model = joblib.load("Model.pkl")

def predict(Gender, Married, Dependents, Education, Self_Employed,
            ApplicantIncome, CoapplicantIncome, LoanAmount,
            Loan_Amount_Term, Credit_History, Property_Area):
    test_df = pd.DataFrame(columns = Inputs)
    test_df.at[0,"Gender"] = Gender
    test_df.at[0,"Married"] = Married
    test_df.at[0,"Dependents"] = Dependents
    test_df.at[0,"Education"] = Education
    test_df.at[0,"Self_Employed"] = Self_Employed
    test_df.at[0,"ApplicantIncome"] = ApplicantIncome
    test_df.at[0,"CoapplicantIncome"] = CoapplicantIncome
    test_df.at[0,"LoanAmount"] = LoanAmount
    test_df.at[0,"Loan_Amount_Term"] = Loan_Amount_Term
    test_df.at[0,"Credit_History"] = Credit_History
    test_df.at[0,"Property_Area"] = Property_Area
    result = Model.predict(test_df)[0]
    
def main():
    st.title("Loan Qualifying Procedure App")
    Gender = st.selectbox("Gender" , ['Male', 'Female'])
    Married = st.selectbox("Married" , ['Yes', 'No'])
    Dependents = st.selectbox("Dependents" , ['0', '1', '2', '3+'])
    Education = st.selectbox("Education" , ['Graduate', 'Not Graduate'])
    Self_Employed = st.selectbox("Self Employed or not" , ['Yes', 'No'])
    ApplicantIncome = st.slider("Applicant Income" , min_value=150, max_value=50000, value=0, step=1)
    CoapplicantIncome = st.slider("Coapplicant  Income" , min_value=0, max_value=20000, value=0, step=1)
    LoanAmount = st.slider("Loan  Amount" , min_value=5000, max_value=1000000, value=0, step=1)
    Loan_Amount_Term = st.selectbox("Loan Amount Term per day" , [360, 120, 240, 180,  60, 300, 480,  36,  84,  12])
    Credit_History = st.selectbox("Credit History" , ['Good', 'Bad'])
    Property_Area = st.selectbox("Property Area" , ['Urban', 'Rural', 'Semiurban'])
    
 
    if st.button('applicant is eligible for a loan or not?'):
        pridc = predict(Gender, Married, Dependents, Education, Self_Employed,
        ApplicantIncome, CoapplicantIncome, LoanAmount,
        Loan_Amount_Term, Credit_History, Property_Area)
        if pridc == 1:
            pridc = 'Yes'
        elif pridc == 0:
            pridc = 'No'
        st.success(f'{pridc}')
if __name__ == '__main__':
    main()
