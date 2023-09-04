import numpy as np

class BranchPerceptron:
    def __init__(self, learning_rate=0.1, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
    
    def fit(self, X, y):
        # Add a bias term to the input data
        X = np.insert(X, 0, 1, axis=1)
        
        # Initialize weights randomly
        self.weights = np.random.rand(X.shape[1])
        
        # Iterate over the data n_iterations times
        for _ in range(self.n_iterations):
            # Make a prediction for each input
            y_pred = np.dot(X, self.weights)
            
            # Update the weights based on the prediction error
            error = y - np.where(y_pred > 0, 1, 0)
            self.weights += self.learning_rate * np.dot(X.T, error)
    
    def predict(self, X):
        # Add a bias term to the input data
        X = np.insert(X, 0, 1, axis=1)
        
        # Make a prediction for each input
        y_pred = np.dot(X, self.weights)
        
        # Return the predicted branch choices
        return np.where(y_pred > 0, 1, 0)
# Define the input data matrix X and target values y
X = np.array([[7, 8, 3], [7, 8, 11], [7, 8, 12], [7, 9, 10], [7, 9, 11], [7, 9, 12], [7, 10, 11], [7, 10, 12], [7, 11, 12], [8, 9, 10], [8, 9, 11], [8, 9, 12], [8, 10, 11], [8, 10, 12], [8, 11, 12], [9, 10, 11], [9, 10, 12], [9, 11, 12]])
y=np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0,1,0,0,1,1,1,0,0])
# Create an instance of the BranchPerceptron class
perceptron = BranchPerceptron()

# Train the perceptron using the fit method
perceptron.fit(X, y)
# Make predictions for new input examples
X_new = np.array([[3, 7, 8], [3, 7, 9], [3, 7, 10], [3, 7, 11], [3, 7, 12]]
)
y_pred = perceptron.predict(X_new)

# Print the predicted branch choices
print(y_pred,type(y_pred))

