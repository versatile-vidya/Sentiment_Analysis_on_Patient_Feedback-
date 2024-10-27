import string as st
import pandas as pd

#   Extracting postive and negitive words  
df = pd.read_csv("/home/vidi/leetcode/project/sentiment_analysis/Positive_Negative_Word_List.csv",encoding='ISO-8859-1')
negative = df['Negative Sense Word List'].dropna().tolist()       # neagtive words 
positive = df['Positive Sense Word List'].dropna().tolist()       # positive words

"""    encoding='ISO-8859-1': This specifies the character encoding used to read the file.
            Here, ISO-8859-1 (Latin-1) is used, which is a common encoding for Western languages
            and ensures compatibility with special characters in the file. If not specified,
            pandas uses utf-8 encoding by default.

    low_memory=False: This argument controls how pandas reads large files.
            When low_memory=True (the default), pandas reads the data in chunks,
            which can lead to data type inconsistencies if columns contain mixed
            data types (e.g., text and numbers).
            Setting low_memory=False reads the entire file into memory at once, 
            allowing pandas to infer the correct data types for each column, reducing the risk of DtypeWarnings.

"""

#   extracting  feedbacks 

##df = pd.read_csv("/home/vidi/leetcode/project/sentiment_analysis/HCAHPS_Hospital_11_2023.csv" ,encoding='cp1252')
#df = pd.read_csv("/home/vidi/leetcode/project/sentiment_analysis/patient_review.csv" ,encoding='ISO-8859-1', low_memory=False)
df = pd.read_csv("/home/vidi/leetcode/project/sentiment_analysis/HCAHPS_Hospital_07_2024.csv" ,encoding = 'ISO-8859-1', low_memory =False)

#feedback list
#feedback_list = df['reviews'].unique().tolist()
feedback_list = df['HCAHPS Answer Description'].unique().tolist()

# Preprocess the text (lowercase, remove punctuation, tokenize)
def preprocess_text(feedback):
    feedback = feedback.lower()     # converting feedback to lowercase
    feedback = feedback.translate(str.maketrans('', '',st.punctuation))  # removing punctuations 
    words = feedback.split()    #tokenizing the lines
    return words


#calculating sentiment score based on postive and negative words

def cal_sentiment_score(words):
    positive_cnt = 0
    negative_cnt = 0
    negation_words = {"not", "no", "never", "cannot", "wouldn't", "couldn't", "won't", "shouldn't"}


##  enumerate function : is used to loop through an iterable (like a list or tuple) while keeping track
#                       of the index of each item in the loop. It provides a counter (index) along with each item, making it easy to 
#                       reference both the position and the value of items in the loop.
    for i,word in enumerate(words) :
        if word in positive:
            # Check if a negation word appears directly before this word
            if i > 0 and words[i - 1] in negation_words:
                negative_cnt += 1  # Negated positive becomes negative
            else:
                positive_cnt += 1
        elif word in negative:
            if i > 0 and words[i - 1] in negation_words:
                positive_cnt += 1  # Negated negative becomes positive
            else:
                negative_cnt += 1
    sentiment_score = positive_cnt - negative_cnt
    return sentiment_score


#classify sentiment  based on the score 
def classify_sentiment(score):
    if score > 0:
        return "Postive"
    elif score <0 :
        return "Negative"
    else:
        return "Netural"

#creating a  dataframe to store feedback and results
df = pd.DataFrame(feedback_list , columns=["HCAHPS Answer Description"])
#df = pd.DataFrame(feedback_list , columns=["reviews"])

# analyzing  sentiment for each feedback

#df['Words'] = df['reviews'].apply(preprocess_text)
df['Words'] = df['HCAHPS Answer Description'].apply(preprocess_text)
df['Sentiment Score'] = df['Words'].apply(cal_sentiment_score)
df['Sentiment Label'] = df['Sentiment Score'].apply(classify_sentiment)

#saving reults to CSV  file for the use of Power BI

df.drop(columns='Words', inplace=True)  # Drop unnecessary 'Words' column
df.to_csv("/home/vidi/leetcode/project/sentiment_analysis/patient_feedback_sentiment.csv", index=False)





