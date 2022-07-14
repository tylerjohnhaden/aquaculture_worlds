#!/usr/bin/env python

import rospy
import smach
import smach_ros

class ChooseRestSpot(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success', 'error'])

    def execute(self, userdata):
        rospy.loginfo('Choosing rest spot for idle state')
        
        


class Bar(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAR')
        return 'outcome1'

def main():
    rospy.init_node('auv_state_machine')

    sm = smach.StateMachine(outcomes=['error'])

    with sm:
        smach.StateMachine.add('FOO', Foo(), 
                               transitions={'outcome1':'BAR', 'outcome2':'outcome4'})
        smach.StateMachine.add('BAR', Bar(), 
                               transitions={'outcome1':'FOO'})

    # Execute SMACH plan
    outcome = sm.execute()



if __name__ == '__main__':
    main()
