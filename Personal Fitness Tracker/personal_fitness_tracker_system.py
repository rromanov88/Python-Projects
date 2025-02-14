# Personal Fitness Tracker System 🏋️‍♂️

# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal


def log_workout(workout_type, duration):
    """
    Log a workout.
    - Append the workout type and duration to the workouts list.
    - Print a confirmation message.
    """
    workouts.append((workout_type, duration))
    print(f"Workout logged: {workout_type} for {duration} minutes.")
    print(workouts)


def log_calorie_intake(calories_consumed):
    """
    Log calorie intake for a meal.
    - Append the calorie amount to the calories list.
    - Print a confirmation message.
    """
    calories.append(calories_consumed)
    print(f"Calorie intake logged: {calories_consumed} calories.")


def view_progress():
    """
    Display a summary of the user's progress for the day.
    - Calculate the total workout time and total calories.
    - Print motivational feedback.
    """
    total_workout_time = sum(duration for _, duration in workouts)
    total_calories = sum(calories)

    print("\n--- Today's Progress ---")
    print(f"Total workout time: {total_workout_time} minutes")
    print(f"Total calories consumed: {total_calories} calories")

    if total_workout_time >= workout_goal:
        print("Great job! You've met your workout goal! 💪")
    else:
        print(f"Keep going! You need {workout_goal - total_workout_time} more minutes to reach your workout goal.")

    if total_calories <= calorie_goal:
        print("Well done! You're within your calorie goal! 🎉")
    else:
        print(f"Watch out! You've exceeded your calorie goal by {total_calories - calorie_goal} calories.")


def reset_progress():
    """
    Clear all data from the workouts and calories lists.
    - Print a confirmation message.
    """
    global workouts, calories
    workouts = []
    calories = []
    print("Progress has been reset. Start fresh!")


def set_daily_goals(workout_minutes, calorie_limit):
    """
    Set daily goals for workout time and calorie intake.
    - Update the global variables workout_goal and calorie_goal.
    - Print a confirmation message.
    """
    global workout_goal, calorie_goal
    workout_goal = workout_minutes
    calorie_goal = calorie_limit
    print(f"Daily goals set: {workout_goal} minutes of workout, {calorie_goal} calories.")


def encouragement_system():
    """
    Provide motivational feedback based on progress and goals.
    - Compare current totals to the daily goals.
    - Print encouragement messages.
    """
    total_workout_time = sum(duration for _, duration in workouts)
    total_calories = sum(calories)

    if total_workout_time >= workout_goal and total_calories <= calorie_goal:
        print("Amazing work today! You've smashed your fitness goals! 🏋️‍♂️")
    elif total_workout_time >= workout_goal:
        print("Great job on your workout! Try to manage your calories better tomorrow. 🍑")
    elif total_calories <= calorie_goal:
        print("You're doing great with your calorie intake! Keep up the good work on workouts! 🙌")
    else:
        print("Don't give up! Tomorrow is a new day to hit those goals! ✨")
        print('Be stronger than your excuses')


def main():
    """
    Main function to interact with the user.
    """
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Display menu options
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")

        if choice == '1':
            # Prompt for workout type and duration
            workout_type = input("Enter workout type (e.g., Running): ")
            duration = float(input("Enter workout duration in minutes: "))
            log_workout(workout_type, duration)
        elif choice == '2':
            # Prompt for calories consumed
            calories_consumed = float(input("Enter calories consumed: "))
            log_calorie_intake(calories_consumed)
        elif choice == '3':
            # Call view_progress function
            view_progress()
        elif choice == '4':
            # Call reset_progress function
            reset_progress()
        elif choice == '5':
            # Prompt for daily goals
            workout_minutes = float(input("Set your daily workout goal (minutes): "))
            calorie_limit = float(input("Set your daily calorie intake goal: "))
            set_daily_goals(workout_minutes, calorie_limit)
        elif choice == '6':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
