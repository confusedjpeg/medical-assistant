def train_model(data, labels):
    """
    Train the machine learning model using the provided data and labels.
    
    Parameters:
    - data: The input features for training the model.
    - labels: The corresponding labels for the input features.
    
    Returns:
    - model: The trained machine learning model.
    """
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    import joblib

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

    # Initialize the model
    model = RandomForestClassifier()

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model accuracy: {accuracy:.2f}")

    # Save the trained model
    joblib.dump(model, 'trained_model.pkl')

    return model