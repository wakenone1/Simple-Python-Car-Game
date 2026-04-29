#Simple Car Game...

engine_running = False
speed = 0 
user_input = ""

while True:
    user_input = input("""Input(Type "help" for instruction): """).lower()
    if user_input.lower() == "help":
        print("""Start the car : Start
Stop the car : Stop
Increase throttle : Faster
Decrease throttle : Slower
Max throttle : max throttle
Doom stop : doom stop
Quit Game : Quit""")
    if user_input.lower() == "start":
        if engine_running:
            print("Car already started", f"{speed}")
        else:
            engine_running = True
            print("Car has started", f"{speed}mph")
    elif user_input.lower() == "stop":
        if engine_running:
            print("Car stopped", f"{speed}mph")
        else:
            engine_running = False
            print("Car already stopped", f"{speed}mph")
    elif user_input.lower() == "faster":
        if speed < 280:
            speed = speed + 10
            print("10 units increased!", f"{speed}mph")
        else:
            print("IT'S THE MAX SPEED!!!")
    elif user_input.lower() == "max throttle":
        while speed < 280:
            speed = speed + 1
            print(f"{speed}mph")
        else:
            print("IT'S THE MAX SPEED!!!!")
            
    elif user_input.lower() == "slower":       
        if speed > 0:
            speed = speed - 10
            print("10 units decreased!", f"{speed}mph")
        else:
            print("Your car stopped. You can't go slower than that. DUH!!!")
    elif user_input.lower() == "doom stop":
        while speed > 0:
            speed = speed - 1
            print(f"{speed}mph")
    elif user_input.lower() == "quit":
        print("Thanks for playing!")
        break
    else:
        print("Type help if you need again.")
