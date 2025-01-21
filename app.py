import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title('Please enter your credentials to see if you are a high accesibility user or not')

feature_used_input = st.selectbox('Select feature from following choices', ['Colorblind Mode',
                                                                            'High Contrast Mode',
                                                                            'Multilingual',
                                                                            'Text-to-Speech',
                                                                            'Visual Aid'])

engagement_score_input = st.selectbox('Select Engagement Score', [1, 2, 3, 4, 5])
engagement_score_input_2 = int(engagement_score_input)

age_group_input = st.selectbox('What is your age group', ['Adult',
                                                          'Professional',
                                                          'Young Adult',
                                                          'Senior',
                                                          'Teenager'])

gender_input = st.selectbox('Select Gender', ['Male',
                                              'Female',
                                              'Non-Binary'])

additional_attributes_input = st.selectbox('How do you identify?', ['LGBTQ+',
                                                                    'Straight',
                                                                    'Person of Color'])

class User:
    def __init__(self, feature_used, engagement_score, age_group, gender, additional_attributes):
        self.feature_used = feature_used
        self.engagement_score = engagement_score
        self.age_group = age_group
        self.gender = gender
        self.additional_attributes = additional_attributes

user = User(feature_used_input, engagement_score_input_2, age_group_input, gender_input, additional_attributes_input)

feature_used_data = user.feature_used
engagement_score_data = user.engagement_score
age_group_data = user.age_group
gender_data = user.gender
additional_attributes_data = user.additional_attributes

dic = {'feature_used': feature_used_data,
       'engagement_score': engagement_score_data,
       'age_group': age_group_data,
       'gender': gender_data,
       'additional_attributes': additional_attributes_data}

inputed_data = pd.DataFrame(dic, index=[0])
num = inputed_data['engagement_score']
number = pd.DataFrame(num, index=[0])

def if_elif_feature_used():
    if feature_used_data == 'Colorblind Mode':
        fu_values = {'feature_used_Colorblind Mode': 1,
                     'feature_used_High Contrast Mode': 0,
                     'feature_used_Multilingual': 0,
                     'feature_used_Text-to-Speech': 0,
                     'feature_used_Visual Aid': 0}
        
    elif feature_used_data == 'High Contrast Mode':
        fu_values = {'feature_used_Colorblind Mode': 0,
                     'feature_used_High Contrast Mode': 1,
                     'feature_used_Multilingual': 0,
                     'feature_used_Text-to-Speech': 0,
                     'feature_used_Visual Aid': 0}
        
    elif feature_used_data == 'Multilingual':
        fu_values = {'feature_used_Colorblind Mode': 0,
                     'feature_used_High Contrast Mode': 0,
                     'feature_used_Multilingual': 1,
                     'feature_used_Text-to-Speech': 0,
                     'feature_used_Visual Aid': 0}
        
    elif feature_used_data == 'Text-to-Speech':
        fu_values = {'feature_used_Colorblind Mode': 0,
                     'feature_used_High Contrast Mode': 0,
                     'feature_used_Multilingual': 0,
                     'feature_used_Text-to-Speech': 1,
                     'feature_used_Visual Aid': 0}
        
    elif feature_used_data == 'Visual Aid':
        fu_values = {'feature_used_Colorblind Mode': 0,
                     'feature_used_High Contrast Mode': 0,
                     'feature_used_Multilingual': 0,
                     'feature_used_Text-to-Speech': 0,
                     'feature_used_Visual Aid': 1}
        
    feature_values = pd.DataFrame(fu_values, index=[0])
    return feature_values

feat = if_elif_feature_used()

def if_elif_age_group_data():
    if age_group_data == 'Adult':
        a_values = {'age_group_Adult': 1,
                    'age_group_Professional': 0,
                    'age_group_Senior': 0,
                    'age_group_Teenager': 0,
                    'age_group_Young Adult': 0}

    elif age_group_data == 'Professional':
        a_values = {'age_group_Adult': 0,
                    'age_group_Professional': 1,
                    'age_group_Senior': 0,
                    'age_group_Teenager': 0,
                    'age_group_Young Adult': 0}

    elif age_group_data == 'Senior':
        a_values = {'age_group_Adult': 0,
                    'age_group_Professional': 0,
                    'age_group_Senior': 1,
                    'age_group_Teenager': 0,
                    'age_group_Young Adult': 0}

    elif age_group_data == 'Teenager':
        a_values = {'age_group_Adult': 0,
                    'age_group_Professional': 0,
                    'age_group_Senior': 0,
                    'age_group_Teenager': 1,
                    'age_group_Young Adult': 0}

    elif age_group_data == 'Young Adult':
        a_values = {'age_group_Adult': 0,
                    'age_group_Professional': 0,
                    'age_group_Senior': 0,
                    'age_group_Teenager': 0,
                    'age_group_Young Adult': 1}

    age_values = pd.DataFrame(a_values, index=[0])
    return age_values

age = if_elif_age_group_data()

def if_elif_gender():
    if gender_data == 'Female':
        g_values = {'gender_Female': 1,
                    'gender_Male': 0,
                    'gender_Non-Binary': 0}

    elif gender_data == 'Male':
        g_values = {'gender_Female': 0,
                    'gender_Male': 1,
                    'gender_Non-Binary': 0}

    elif gender_data == 'Non-Binary':
        g_values = {'gender_Female': 0,
                    'gender_Male': 0,
                    'gender_Non-Binary': 1}

    gender_values = pd.DataFrame(g_values, index=[0])
    return gender_values

gend = if_elif_gender()

def if_elif_add_attributes():
    if additional_attributes_data == 'LGBTQ+':
        add_values = {'additional_attributes_LGBTQ+': 1,
                      'additional_attributes_Person of Color': 0,
                      'additional_attributes_Straight': 0}

    elif additional_attributes_data == 'Person of Color':
        add_values = {'additional_attributes_LGBTQ+': 0,
                      'additional_attributes_Person of Color': 1,
                      'additional_attributes_Straight': 0}

    elif additional_attributes_data == 'Straight':
        add_values = {'additional_attributes_LGBTQ+': 0,
                      'additional_attributes_Person of Color': 0,
                      'additional_attributes_Straight': 1}

    additional_att = pd.DataFrame(add_values, index=[0])
    return additional_att

attributes = if_elif_add_attributes()

join1 = number.join(feat)
join2 = join1.join(age)
join3 = join2.join(gend)
final_join = join3.join(attributes)

def deploy_model():
    with open('model_pickle', 'rb') as file:
        pkl = pickle.load(file)

    return pkl

model = deploy_model()

np_dataframe = np.array(final_join)

predicted_data = model.predict(np_dataframe)

pred_comp = pd.DataFrame(predicted_data, index=[0])

dic_true_false = {'No': pred_comp[0],
                  'Yes': pred_comp[1]}

this_data = pd.DataFrame(dic_true_false)

my_data = this_data.idxmax(axis=1).item()

button = st.button('Click Here to Find Out')
if button:
    st.write('Your credentials', inputed_data)

    yes_ = 'You are a high accessibility user'
    no_ = 'You are not a high accessibility user'
    if my_data == 'Yes':
        st.write(yes_)

    elif my_data == 'No':
        st.write(no_)
