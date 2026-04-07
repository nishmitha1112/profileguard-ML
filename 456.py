import pandas as pd

fusers = pd.read_csv("../data/fusers.csv")
users = pd.read_csv("../data/users.csv")

print(fusers.columns)
print(users.columns)
df = pd.concat([fusers, users], ignore_index=True)
df.head()
df['dataset'].unique()
df = pd.concat([fusers, users], ignore_index=True)
df['dataset'].unique()
df['dataset'].value_counts()
df['dataset'].value_counts()
df[df['dataset'] == 'INT'].head()
df[df['dataset'] == 'E13'].head()
df[df['dataset'] == 'INT'].head()
df[df['dataset'] == 'E13'].head()
df[df['dataset'] == 'INT'].head()
df['label'] = df['dataset'].apply(lambda x: 0 if x == 'INT' else 1)
df_clean = df.copy()

columns_to_drop = [
    'id', 'name', 'screen_name', 'url', 'profile_image_url', 'profile_banner_url',
    'profile_background_image_url', 'profile_background_image_url_https',
    'profile_image_url_https', 'description', 'location', 'time_zone',
    'profile_sidebar_border_color', 'profile_sidebar_fill_color', 'profile_text_color',
    'profile_background_color', 'profile_link_color', 'created_at', 'updated',
    'dataset'
]

df_clean = df_clean.drop(columns=columns_to_drop)
df_clean.head()
bool_cols = [
    'default_profile', 'default_profile_image', 'geo_enabled',
    'profile_use_background_image', 'profile_background_tile',
    'protected', 'verified'
]

for col in bool_cols:
    df_clean[col] = df_clean[col].fillna(False).astype(int)

df_clean.head()
import warnings
warnings.filterwarnings('ignore')
# Followers–Friends Ratio
df_clean['ff_ratio'] = df_clean['followers_count'] / (df_clean['friends_count'] + 1)

# Activity Score
df_clean['activity_score'] = df_clean['statuses_count'] / (df_clean['friends_count'] + 1)

# Engagement Score
df_clean['engagement_score'] = df_clean['favourites_count'] / (df_clean['followers_count'] + 1)
df_fe = df_clean.copy()
df_fe.head()
df_clean.columns
df.columns
df['label'] = df['dataset'].apply(lambda x: 0 if x == 'INT' else 1)
df_clean['label'] = df['label']
df_fe = df_clean.copy()
df_fe.columns
features = [
    'followers_count',
    'friends_count',
    'verified',
    'default_profile',
    'ff_ratio'
]

X = df_fe[features]
y = df_fe['label']

X.shape, y.shape
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

print("Random Forest")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
import pickle

with open("../models/fake_profile_model.pkl", "wb") as f:
    pickle.dump(rf, f)

print("5-feature model saved successfully")












