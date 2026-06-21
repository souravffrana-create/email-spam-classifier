#import-libraries
from pathlib import Path
import joblib
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import precision_score,confusion_matrix,classification_report,accuracy_score



#Load-Data
base_dir = Path(__file__).resolve().parent.parent
data_path = base_dir / "data"/ "spam_dataset.csv"
dataset = pd.read_csv(data_path)

#encoding
le = LabelEncoder()
dataset["label"] = le.fit_transform(dataset["label"])

#feature
X = dataset["text"]
#targt
y = dataset["label"]

#Build-pipeline
pipeline = Pipeline([
    ("tfidf",TfidfVectorizer(stop_words="english",max_features=5000)),
    ("model",LinearSVC(max_iter=10000))
])

#Train-Test_split
X_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)


#Model-Training
pipeline.fit(X_train,y_train)

#Predict-Test_data
y_pre = pipeline.predict(x_test)

#Model evaluation
score = accuracy_score(y_test,y_pre)*100

cr = classification_report(y_test,y_pre)


#save model
model_path = Path(__file__).parent.parent / "model"
model_path.mkdir(exist_ok=True)
#joblib.dump(pipeline,model_path / "spam_email_classification.pkl")