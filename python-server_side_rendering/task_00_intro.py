import os;


def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print('template must be a string')
        return
    
    if not isinstance(attendees, list) or not all (isinstance(i, dict) for i in attendees):
        print('attendees must be a list of dictionaries')
        return
    
    if template == '':
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    i = 1
    for attendee in attendees:
        message = template
        message = message.replace("{name}", str(attendee.get("name", "N/A")))
        message = message.replace("{event_title}", str(attendee.get("event_title", "N/A")))
        message = message.replace("{event_date}", str(attendee.get("event_date", "N/A")))
        message = message.replace("{event_location}", str(attendee.get("event_location", "N/A")))

        filename = f"output_{i}.txt"
        with open (filename, "w", encoding="utf-8") as f:
            f.write(message)
            print(f"created file: {filename}")
            i += 1
    
