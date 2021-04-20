


##constraints
#- every muscle group gets worked at most twice per week and at least once per week.

## all muscle groups must be worked out before any group repeats.

#No muscle groups can be worked out on consecutive days.

##nums parameter is length of workout in minutes. Workout time must not exceed nums (DONE)

##if an exercise has been used, it can't be used again on the same day (DONE)

#variables:
##count = integer, keeps track of minutes spent during workout. cannot exceed num.
## num = integer. Parameter given as input for maximum desired workout time.
# workout = String. Prints each day's workouts and workout time.
# day = integer. Keeps track of day.


##create one version with dict, one with list. Use dict.update method to change values.


dicts_dict = {"Back":{"Deadlift (Entire Back)": 20, "Lat-Pull Downs (Mid-back)": 20, "Barbell Shrugs(Upper back)": 15, "Standing Barbell Row (Middle back)": 20,
                       "Pull ups (Middle Back)": 15, "T-Bar Row (Middle Back)": 20, "Seated Row (Middle Back)": 20},
            "Legs":{"Barbell Squats(Legs)": 30, "Barbell Lunges(Legs/Glutes)": 25, "Calf Raises(Legs)": 20,"Hamstring Curls- Machine (Legs)" : 20,
                        "Seated Leg Press (Legs)": 20},
             "Arms":{"Preacher Curls (Arms)": 20, "Bicep Dumbbell Curls (Arms)":20, "Tricep Extensions (Arms)" :15,
                        "Farmer Walks - (Arms - forearms)" : 15,  "Forearm curls (Arms - Forearms)": 20, "Machine dips (Arms - Triceps)": 20, "Wavy bar' curls (Arms - Biceps)": 15},
            "Abs/Core":{"Planks (Abs/Core)":25, "Sit-ups (Abs/Core)": 20, "Incline Sit-ups (Abs/Core": 20,
                        "Bicycle Kicks (Core/abs)": 10, "Bosu ball sit-ups (Core/abs)": 20, "Mountain Climbers (Core/abs)": 15},
            "Shoulders":{"Overhead Barbell Press (Shoulders)": 20, "Military Press (Shoulders)": 20, "Machine Shoulder Press (Shoulders)": 15,
                        "Lateral Dumbell Raises (Shoulders)": 15, "Dumbell Front Raises (Shoulders)": 15},
            "Chest":{"Flat Bench (Chest)": 25,"Dumbbell Bench (Chest)": 20, "Barbell Flys (Chest)": 20, "Machine Press (Chest)": 15,
                        "Incline Bench (Chest)": 20, "Push-ups (Chest)": 15}}




def random_workout(num):
    day, workout = (1, "")
    available = ['Back', 'Legs', 'Arms', 'Abs/Core', 'Shoulders', 'Chest']
    import random
    while day < 7:
        if day !=3:
            workout += "Day" + " " + str(day) + ": "
        else:
            available = ['Back', 'Legs', 'Arms', 'Abs/Core', 'Shoulders', 'Chest']
            workout += "Day " + str(day) + ":" + " Rest day" + "\n"
            workout += "Day 4: "
            day +=1
            pass
        x, y = random.sample(available, 2)
        available.remove(x)
        available.remove(y)
        y_dictionary = dicts_dict.get(x)
        x_dictionary = dicts_dict.get(y)
        count = 0
        for i in y_dictionary:
            if y_dictionary.get(i) + count <= ((num / 2) + (num/7)): ## adds buffer, balances workout groups.
                workout += i + ", "
                count += y_dictionary.get(i)
        for i in x_dictionary:
            if x_dictionary.get(i)  + count <= num:
                workout += i + ", "
                count += x_dictionary.get(i)
        if day < 6:
            if day == 3:
                groups.clear()
                workout += "Day " + str(day) + ":" + " Rest day" + "\n"
            else:
                workout.rstrip(",")
                workout += " || Total workout time = " + " " + str(count) + " minutes" + "\n"
        elif day == 6:
            workout += " || Total workout time = " + " " + str(count) + " minutes"

        day += 1
    workout += "\n" + "Day 7: Rest day"
    print(workout)

random_workout(120)

    #.random will be needed to select 2 muscle groups from muscle lists to initiate the week#
    #.random will be needed to select exercise from muscle group list, then pop once used

##user input:
    ## Weighlifting experience (Beginner, Novice, Intermediate, Advanced, Professional)
    ## I'd like to (Get bigger, Get Stronger, Get more toned)
    ## Workout time (30 min, 60 min, 90 min, 120 min)

##user output:
    ## "Your ideal weekly workout schedule is..."
    ##Want another workout? Try again!##
    # Link to Wikihow explaining all excercises#
    ## disclaimer that they should use Devin for better results
