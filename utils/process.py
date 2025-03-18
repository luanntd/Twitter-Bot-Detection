import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from imblearn.under_sampling import EditedNearestNeighbours
from data_utils import encode_features, extract_features, select_features

def process(path):
    pd.set_option('display.max_colwidth', None)

    # Read data from .csv file
    df = pd.read_csv(path, low_memory=False)

    df = encode_features(df)   
    df = extract_features(df)
    df = select_features(df)

    # Split data
    X = df.drop('label', axis=1)
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42, stratify=y)

    # Min max scale
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Under sample data
    sampler = EditedNearestNeighbours()
    X_train_resampled, y_train_resampled = sampler.fit_resample(X_train_scaled, y_train)
    
    # Standard scale 
    scaler = StandardScaler()
    X_train_final = scaler.fit_transform(X_train_resampled)
    X_test_final = scaler.transform(X_test_scaled)

    return X_train_final, X_test_final, y_train_resampled, y_test

if __name__ == '__main__':
    pass
