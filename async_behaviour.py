import anki_vector
from anki_vector.util import degrees

"""
This program is to test my understanding of Vector's asynchronous behaviour.
It turns out it is not as complicated as I first thought (I think!).
The most important finding is to control the flow of the program so it doesn't
start then immediately finish before any task has completed.

This program asks Vector to spin around twice whilst speaking.
"""

#Define main program
def main():
    
    #Get Vectors serial number
    args = anki_vector.util.parse_command_args()
    
    #Create an AsyncRobot instance
    with anki_vector.AsyncRobot(args.serial) as robot:
        
        #Move Vector off his charger. The .result() is a blocking function ensuring
        #this action is completed before moving on to the next step
        print("Driving off charger...")
        robot.behavior.drive_off_charger().result()        
        
        #Two asynchronous actions... Chew gum and walk;)
        #1
        print("Turn in place...")
        action = robot.behavior.turn_in_place(degrees(720), speed=degrees(80))

        #2
        print("Speak text...")        
        robot.say_text("Weee! This is fun")

        #This step ensures the actions complete before the program has ended
        while True:
                print("Running...")

                #Break out of loop and end program once Vector has finished spinning
                if action.done():
                        print("Action complete!")
                        break
                
                #Or touch Vectors back to stop him mid spin
                if robot.touch.last_sensor_reading.is_being_touched:
                        print("Has been touched!")
                        break
        
        print("Complete")

#Run main program
main()