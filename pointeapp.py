# Backend
# Importera nödvändiga bibliotek
import streamlit as st
import numpy as np
import logging
from sklearn.neighbors import KNeighborsClassifier

# Logginställningar
logging.basicConfig(level=logging.INFO)

# Värden för träningsdata
X_train = np.array([[240, 120], [230, 110], [220, 130], [250, 115], [240, 125]])
y_train = np.array(["Grecian feet", "Roman feet", "Egyptian feet", "Grecian feet", "Roman feet"])

# Skapa och träna KNN-modellen
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Funktion för att analysera fotform (baserat på fotlängd, fotbredd och tårnas form)
def analyze_foot_shape(foot_length, foot_width, toe_shape):
    if toe_shape == "Second toe longer than big toe":
        return "Grecian feet"
    elif toe_shape == "Toes gradually shorten from big toe":
        return "Egyptian feet"
    else:  # "First three toes are roughly the same length"
        return "Roman feet"

# Funktion för att rekommendera skomodeller baserat på fotform och nivå
def recommend_shoe(foot_shape, skill_level):
    if skill_level == "A few to a couple of years of experience":
        if foot_shape == "Grecian feet":
            return ["Bloch Sylphide", "Capezio Contempora"]
        elif foot_shape == "Roman feet":
            return ["Bloch Aspiration", "Mirelle Academie"]
        else:  # Egyptian feet
            return ["Bloch Balance European", "Bloch Suprima"]
    elif skill_level == "Many years of experience":
        if foot_shape == "Grecian feet":
            return ["Bloch Alpha", "Bloch Signature"]
        elif foot_shape == "Roman feet":
            return ["Bloch B Morph", "Mirella Professional"]
        else:  # Egyptian feet
            return ["Bloch Alpha", "Freed Classic"]
    return []

# Frontend
# Streamlit
st.image(r"C:\Users\mikae\Documents\ec\IMG_9368.jpg", caption="Image Credit: Mikaela Bennshagen", use_column_width=True)

st.markdown('<h1 style="text-align: center; color: #FFB6C1;">Pointe Shoe Analyzer</h1>', unsafe_allow_html=True)
st.markdown(
    '<div style="background-color: #FFDDDD; padding: 10px; border-radius: 5px;">'
    '<strong>IMPORTANT:</strong> This information is based on personal research and is not official advice. '
    'Please consult a professional pointe shoe fitter before trying or purchasing. </div>',
    unsafe_allow_html=True
)

# Användaren anger fotlängd och fotbredd manuellt
foot_length = st.number_input("The length of your foot (in mm)", min_value=200, max_value=300, value=240)
foot_width = st.number_input("The width of your foot (in mm)", min_value=80, max_value=150, value=120)

# Användaren får välja form på tårna
toe_shape = st.radio(
    "What is the shape of your toes?",
    ("Second toe longer than big toe", 
     "Toes gradually shorten from big toe", 
     "First three toes are roughly the same length")
)

# Välj nivå
skill_level = st.selectbox("Choose pointe shoe level:", ["Choose...", "A few to a couple of years of experience", "Many years of experience"], index=0)

if skill_level != "Choose...":
    # Analysera fotform baserat på användarens angivna fotmått och tårnas form
    foot_shape = analyze_foot_shape(foot_length, foot_width, toe_shape)
    st.markdown(f'<p style="color: #FFB6C1; font-size: 20px; text-align: center;">Your foot type: {foot_shape}</p>', unsafe_allow_html=True)

    # Rekommendera skomodeller baserat på fottyp och nivå
    recommended_shoes = recommend_shoe(foot_shape, skill_level)
    if recommended_shoes:
        st.markdown(f'<p style="color: #FFB6C1; font-size: 20px; text-align: center;">Recommended pointe shoes for {foot_shape}:</p>', unsafe_allow_html=True)
        for shoe in recommended_shoes:
            st.write(shoe)
    else:
        st.write("Couldn't find a recommended pointe shoe.")
else:
    st.write("Please choose your skill level.")

# Loggning av händelser
logging.info("Fotlängd: %s, Fotbredd: %s, Tårnas form: %s", foot_length, foot_width, toe_shape)







