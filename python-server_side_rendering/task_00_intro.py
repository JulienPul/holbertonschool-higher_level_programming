import os;


def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print('template must be a string')
        return
    
    if not isinstance(attendees, list) or not all (isinstance(i, dict) for i in attendees):
        print('attendees must be a list of dictionaries')
        return
    
    if template == '':
        print('template must not be empty')
        return
    
    if not attendees:
        print('attendees must not be empty')
        return
