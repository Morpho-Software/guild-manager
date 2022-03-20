1.	Help.py (static)
    a.	User click :1_:
        i.	Sends user raid_howtojoin.py (sign up instructions)
    b.	User click :2_:
        i.	Sends user raid_ptsummary.py (characters with raid point)

2.	Help_leader.py (static)
    a.	Schedule a raid code displayed
    b.	Editing a raid code displayed
    c.	Marking absences code displayed

    Leader types into #bot-operating:
        [2a.] Sends a raid.py (preview)
            i.	Click :Done:
                1.	Sends raid.py (completed) to #outland-raids or #azeroth-raids
            ii.	Click :Cancel:
                1.	Deletes the raid.py (preview)
        [2b.] Edits the raid.py (preview or completed) based on the raid ID
        [2c.] Gives all signed-up for raid ID 1 point for that raid type; Removes 1 point from the highest tier raid for those who are marked absent; reacts with a :Done: to message
            i.	Sends absent user raid_ptpenalty.py


3.	[2ai1.] Raid.py (completed) sent to raid channels
    a.	User clicks :Class Icon: :Spec: :Done:
        i.	If recognized, sends user signup_confirmation.py
            1.	User types different character name
                a.	If character is new, logs them with class and spec
                b.	If character is logged, changes class and spec
                c.	Sends user (updated character name) signup.py
            2.	Sends user reminder_raid.py 12 hours before raid start time
        ii.	If unrecognized, sends user raid_newcharacter.py
            1.	User types character name
                a.	Logs new character with class and spec
                b.	Sends user signup_confirmation.py
        iii.If attempted sign up failed, sends user signup_error.py
                (more than 1 class, 1 spec, and done clicked; less than those clicked)
        iv.	If raid is full, sends user signup_full.py
            1.	When 10+ or 25+ receive this message, raid.py (complete duplicate) created
                a.	Sends users who received signup_full.py; sign up_overflow.py
    b.	Click :Cancel:
        i.	User’s name is removed

4.	Reminder_raid.py sent to #raid-notices
    a.	Deletes 3 hours after raid start time

5.	Reminder_absent.py sent to raid creator at raid time and 6 hours after if incomplete
