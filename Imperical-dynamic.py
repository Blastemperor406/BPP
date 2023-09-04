def branch_predictor(history):
    if history[-1] == 0 and history[-2] == 0:
        return 0
    elif history[-1] == 0 and history[-2] == 1:
        return 1
    elif history[-1] == 1 and history[-2] == 0:
        return 1
    else:
        return 0

# Define the main program
def main():
    # Initialize the history to all zeros
    history = [0, 0]

    # Define the instruction sequence
    instructions = [0, 1, 0, 0, 1, 1, 1, 0, 1, 1]

    # Initialize the correct predictions and total predictions to zero
    correct_predictions = 0
    total_predictions = 0

    # Loop through each instruction
    for instruction in instructions:
        # Predict the branch
        prediction = branch_predictor(history)

        # Update the history with the current instruction and prediction
        history.append(instruction)
        history.pop(0)
        history[-1] = prediction

        # Compare the prediction to the actual result and update the counters
        if prediction == instruction:
            correct_predictions += 1
        total_predictions += 1

    # Print the results
    print(f"Correct predictions: {correct_predictions}")
    print(f"Total predictions: {total_predictions}")
    print(f"Accuracy: {correct_predictions / total_predictions:.2%}")

main()