import joblib


model_in_disk = joblib.load("./src/web/data/model_20240730.pkl")


def predict(features):
    predictions = model_in_disk.predict(features)
    return predictions.tolist()