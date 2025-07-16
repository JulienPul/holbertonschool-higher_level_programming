import os;


def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print('template must be a string')
        return
    
    if not isinstance(attendees, list) or not all (isinstance(i, dict) for i in attendees):
        print('attendees must be a list of dictionaries')
        return
    