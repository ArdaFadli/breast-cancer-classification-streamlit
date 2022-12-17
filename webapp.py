import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Load the data
loaded_model = pickle.load(open('trained_breastcancer_model.sav', 'rb'))

# create a function to predict

def breast_cancer_prediction(data_to_test):

    knn_predict = loaded_model.predict(data_to_test)

    print(knn_predict)
    if (knn_predict[0] == 'M'):
        return 'Predicted class: Malignant'
    else:
        return 'Predicted class: Benign'    


def main(): 

    # Create a title and sub-title
    st.title("Breast Cancer Prediction")

    # getting the input from the user
    global radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst
     
    radius_mean = st.number_input(label="radius_mean",step=1.,format="%.2f")
    texture_mean = st.number_input(label="texture_mean",step=1.,format="%.2f")
    perimeter_mean = st.number_input(label="perimeter_mean",step=1.,format="%.2f")
    area_mean = st.number_input(label="area_mean",step=1.,format="%.2f")
    smoothness_mean = st.number_input(label="smoothness_mean",step=1.,format="%.2f")
    compactness_mean = st.number_input(label="compactness_mean",step=1.,format="%.2f")
    concavity_mean = st.number_input(label="concavity_mean",step=1.,format="%.2f")
    concave_points_mean = st.number_input(label="concave_points_mean",step=1.,format="%.2f")
    symmetry_mean = st.number_input(label="symmetry_mean",step=1.,format="%.2f")
    fractal_dimension_mean = st.number_input(label="fractal_dimension_mean",step=1.,format="%.2f")
    radius_se = st.number_input(label="radius_se",step=1.,format="%.2f")
    texture_se = st.number_input(label="texture_se",step=1.,format="%.2f")
    perimeter_se = st.number_input(label="perimeter_se",step=1.,format="%.2f")
    area_se = st.number_input(label="area_se",step=1.,format="%.2f")
    smoothness_se = st.number_input(label="smoothness_se",step=1.,format="%.2f")
    compactness_se = st.number_input(label="compactness_se",step=1.,format="%.2f")
    concavity_se = st.number_input(label="concavity_se",step=1.,format="%.2f")
    concave_points_se = st.number_input(label="concave_points_se",step=1.,format="%.2f")
    symmetry_se = st.number_input(label="symmetry_se",step=1.,format="%.2f")
    fractal_dimension_se = st.number_input(label="fractal_dimension_se",step=1.,format="%.2f")
    radius_worst = st.number_input(label="radius_worst",step=1.,format="%.2f")
    texture_worst = st.number_input(label="texture_worst",step=1.,format="%.2f")
    perimeter_worst = st.number_input(label="perimeter_worst",step=1.,format="%.2f")
    area_worst = st.number_input(label="area_worst",step=1.,format="%.2f")
    smoothness_worst = st.number_input(label="smoothness_worst",step=1.,format="%.2f")
    compactness_worst = st.number_input(label="compactness_worst",step=1.,format="%.2f")
    concavity_worst = st.number_input(label="concavity_worst",step=1.,format="%.2f")
    concave_points_worst = st.number_input(label="concave_points_worst",step=1.,format="%.2f")
    symmetry_worst = st.number_input(label="symmetry_worst",step=1.,format="%.2f")
    fractal_dimension_worst = st.number_input(label="fractal_dimension_worst",step=1.,format="%.2f")

    # code to predict
    diagnosis = ''

    # create a button
    if st.button("Predict"):
        diagnosis = breast_cancer_prediction([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]])
        st.success(diagnosis)


if __name__ == '__main__':
    main()

