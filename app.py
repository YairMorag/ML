import streamlit as st
import joblib

# טעינת המודל שאומן
model = joblib.load('loan_risk_model.pkl')

# כותרת ראשית
st.title("חיזוי סיכון הלוואות")

# קלטים למשתמש
age = st.number_input("גיל:", min_value=18, max_value=100, step=1, help="הכנס את גילך")
debt_amount = st.number_input("סכום חוב:", min_value=0.0, step=1000.0, help="הכנס את סכום החוב שלך")
payment_history = st.selectbox("היסטוריית תשלומים:", ['Excellent', 'Good', 'Fair', 'Poor'])
family_income = st.number_input("הכנסה משפחתית:", min_value=0.0, step=1000.0, help="הכנס את ההכנסה המשפחתית שלך")
profession = st.selectbox("מקצוע:", ['Teacher', 'Doctor', 'Engineer', 'Other'])
num_children = st.number_input("מספר ילדים:", min_value=0, step=1, help="הכנס את מספר ילדיך")

# כפתור לחישוב
if st.button("חשב סיכון"):
    # מיפוי הערכים לנתוני המודל
    payment_history_map = {'Excellent': 4, 'Good': 3, 'Fair': 2, 'Poor': 1}
    profession_map = {'Teacher': 1, 'Doctor': 2, 'Engineer': 3, 'Other': 0}
    
    # הכנת הנתונים
    input_data = [[
        age,
        debt_amount,
        payment_history_map[payment_history],
        family_income,
        profession_map[profession],
        num_children
    ]]
    
    # חיזוי בעזרת המודל
    risk_score = model.predict(input_data)[0]
    
    # תוצאה
    st.write(f"ציון הסיכון החזוי שלך הוא: {risk_score}")

