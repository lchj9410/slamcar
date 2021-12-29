import rospy
from pynput.keyboard import Key, Listener
from geometry_msgs.msg import Twist
rospy.init_node('manual_drive')
rosrate=rospy.Rate(1000)
vel_command=rospy.Publisher('/cmd_vel',Twist,queue_size=100)
keyboard_input=Twist()

def press(key): 
    key_string=str(key)
    if key_string == "'w'": 
        keyboard_input.linear.x=0.25
    if key_string == "'W'": 
        keyboard_input.linear.x=0.55
    if key_string == "'s'": 
        keyboard_input.linear.x=-0.25
    if key_string == "'S'": 
        keyboard_input.linear.x=-0.55
    if key_string == "'a'": 
        keyboard_input.angular.z=3.5
    if key_string == "'A'": 
        keyboard_input.angular.z=7
    if key_string == "'d'": 
        keyboard_input.angular.z=-3.5
    if key_string == "'D'": 
        keyboard_input.angular.z=-7
    if key == Key.delete: 
        # Stop listener 
        return False
    vel_command.publish(keyboard_input)
    rospy.sleep(0.01)
def release(key):
    key_string=str(key)
    if key_string == "'w'" or key_string == "'W'" or key_string == "'s'" or key_string == "'S'": 
        keyboard_input.linear.x=0
    if key_string == "'a'" or key_string == "'A'" or key_string == "'d'" or key_string == "'D'": 
        keyboard_input.angular.z=0
    vel_command.publish(keyboard_input)
# Collect all event until released 
print(" press w-a-s-d-shift to drive, press 'del' to exit")
with Listener(on_press = press, on_release= release) as listener:    
    listener.join() 




