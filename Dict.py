
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    length = request.args.get("length", "")
    if length:
        length = int(length)
        final = random_workout(length)
    else:
        final = ""
    return (
        """<form action="" method="get">
                <name="length"/>
                <label for="length">Choose a workout length (in minutes)</label>
                <select name="length" id="length">
                    <option value="">Select</option>
                    <option value="60">60</option>
                    <option value="90">90</option>
                    <option value="120">120</option>
                <input type="submit" value="Submit">
                <br><br>
                <workout>Based on your goals, here's possible weekly workout schedule for you:</workout> 
                <br><br>
                <br><br>
            </form>"""

            + final



    )



## To-do: render 3rd line of app to bold
## Add refresh button or string message to bottom of page
## Add section for



dicts_dict = {"Back":{"Deadlift (Entire Back)": 20, "Lat-Pull Downs (Mid-back)": 20, "Barbell Shrugs (Upper back)": 15, "Standing Barbell Row (Middle back)": 20,
                       "Pull ups (Middle Back)": 15, "T-Bar Row (Middle Back)": 20, "Seated Row (Middle Back)": 20},
            "Legs":{"Barbell Squats (Legs)": 30, "Barbell Lunges (Legs/Glutes)": 25, "Calf Raises (Legs)": 20,"Hamstring Curls- Machine (Legs)" : 20,
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
    workout += "\n" + "Day 7: Rest day" + "\n"
    workout1 = workout.replace("\n", "<br /><br />\n")
    return workout1


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
