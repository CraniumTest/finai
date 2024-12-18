import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def analyze_trends(data):
    data['Date'] = pd.to_datetime(data['date'])
    data.sort_values('Date', inplace=True)
    data['Return'] = data['close'].pct_change()
    
    features = data[["open", "high", "low", "volume"]]
    target = data["close"].shift(-1)
    
    X_train, X_test, y_train, y_test = train_test_split(features[:-1], target[:-1], test_size=0.2, random_state=42)
    
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    
    return model.predict(X_test)
