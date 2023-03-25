# Initialize the starting state by creating a list with some random integers
def initialize():
    state = [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]
    return state

# Define a function to calculate the cost of the current state
# The cost is calculated using the number of inversions in the list


def calculate_cost(state):
    cost = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] > state[j]:
                cost += 1
    return cost

# Define a function to generate new states by swapping elements and shifting to the right


def state_generation(current_state):
    while True:
        # Calculate the cost of the current state
        current_state_cost = calculate_cost(current_state)
        print("Current state: ", current_state, "Cost: ", current_state_cost)

        # Initialize variables to keep track of the minimum cost and state
        min_next_cost = float('inf')
        min_next_state = None

        # Generate all possible next states by swapping each element with its next neighbor
        for i in range(len(current_state)-1):
            next_state = current_state.copy()
            # Swap the elements
            next_state[i], next_state[i+1] = next_state[i+1], next_state[i]
            # Shift the list to the right
            next_state = [next_state[-1]] + next_state[:-1]
            # Calculate the cost of the next state
            next_state_cost = calculate_cost(next_state)

            # Update the minimum cost and state if necessary
            if next_state_cost < min_next_cost:
                min_next_cost = next_state_cost
                min_next_state = next_state

        # If the minimum cost is less than the current cost, move to the next state
        # Otherwise, print the final state and cost and exit the loop
        if min_next_cost < current_state_cost:
            current_state = min_next_state
        else:
            print("Final state: ", current_state, "Cost: ", current_state_cost)
            break

# Define the main function to initialize the state and generate new states


def main():
    state = initialize()
    state_generation(state)


# Call the main function to start the program
main()
