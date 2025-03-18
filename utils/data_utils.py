import pandas as pd
import pytz

def encode_features(df: pd.DataFrame) -> pd.DataFrame:
    # Encode boolean features
    df['verified'] = df['verified'].apply(lambda x : 1 if x == True else 0)
    df['protected'] = df['protected'].apply(lambda x : 1 if x == True else 0)

    # Encode label, which bot is 1 and human is 0
    df['label'] = df['label'].apply(lambda x : 1 if x == 'bot' else 0)

    return df


def extract_features(df: pd.DataFrame) -> pd.DataFrame:
    # Encode object features: have value is 1 and NaN is 0
    object_features = ['pinned_tweet_id', 'entities', 'url', 'location', 'description']
    for feature in object_features:
        df[feature] = df[feature].apply(lambda x : 0 if pd.isna(x) else 1)

    # Change created_at to datetime format
    df['created_at'] = pd.to_datetime(df['created_at'], format = "%Y-%m-%d %H:%M:%S%z")

    # Change timezone
    df['created_at'] = df['created_at'].dt.tz_convert(pytz.UTC)

    # Get publish time
    publish_time = pd.Timestamp(year=2022, month=8, day=20, hour=0, minute=0, second=0, tz=pytz.UTC)

    # Count existed time
    df['time_existed'] = publish_time - df['created_at']

    # Convert existed time to days
    df = df.drop('created_at', axis=1)
    df['time_existed'] = df['time_existed'].dt.total_seconds() / (24 * 3600)

    return df


def select_features(df: pd.DataFrame) -> pd.DataFrame:
    # Droping unnecessary features
    df = df.drop(['id', 'withheld', 'profile_image_url', 'name', 'username'], axis = 1)

    # Drop collinearity feature
    df = df.drop('url', axis=1)
    numerical_data = numerical_data.drop('url', axis=1)

    return df


if __name__ == '__main__':
    pass
