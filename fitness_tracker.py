import time

# Global dictionary to store user data (in memory)
user_data = {
    "name": "",
    "workouts": [],
    "goals": {"workout_duration": 0, "distance": 0},  # goals in minutes and miles
}

# Function to get user input
def get_input(prompt):
    return input(prompt).strip()

# Function to register a user
def register_user():
    user_data["name"] = get_input("Enter your name: ")
    print(f"Welcome, {user_data['name']}! Let's start tracking your fitness journey.")

# Function to log a workout
def log_workout():
    workout_type = get_input("Enter workout type (e.g., Running, Weightlifting, Yoga): ")
    workout_duration = float(get_input("Enter workout duration in minutes: "))
    distance_covered = float(get_input("Enter distance covered in miles (0 if not applicable): "))
    
    # Store workout data
    workout = {
        "type": workout_type,
        "duration": workout_duration,
        "distance": distance_covered,
    }
    user_data["workouts"].append(workout)
    print(f"Workout logged: {workout_type} - {workout_duration} mins, {distance_covered} miles")

# Function to set fitness goals
def set_goals():
    user_data["goals"]["workout_duration"] = float(get_input("Set your goal workout duration in minutes: "))
    user_data["goals"]["distance"] = float(get_input("Set your goal distance in miles: "))
    print(f"Goals set! Workout duration: {user_data['goals']['workout_duration']} mins, Distance: {user_data['goals']['distance']} miles.")

# Function to view progress
def view_progress():
    total_duration = sum(workout["duration"] for workout in user_data["workouts"])
    total_distance = sum(workout["distance"] for workout in user_data["workouts"])

    print("\n--- Progress Summary ---")
    print(f"Total workout duration: {total_duration} mins")
    print(f"Total distance covered: {total_distance} miles")

    # Goal progress
    print(f"Goal progress:")
    print(f"Workout duration: {total_duration}/{user_data['goals']['workout_duration']} mins")
    print(f"Distance: {total_distance}/{user_data['goals']['distance']} miles")

# Main menu loop
def main():
    if not user_data["name"]:
        register_user()

    while True:
        print("\n--- Fitness Tracker Menu ---")
        print("1. Log a workout")
        print("2. Set fitness goals")
        print("3. View progress")
        print("4. Exit")
        
        choice = get_input("Choose an option (1-4): ")

        if choice == "1":
            log_workout()
        elif choice == "2":
            set_goals()
        elif choice == "3":
            view_progress()
        elif choice == "4":
            print("Thanks for using the Fitness Tracker. Keep up the good work!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
