import requests
import uuid
import smtplib

def getMyCourses(accessToken):
    URL = r'https://canvas.instructure.com/api/v1/courses?access_token='+accessToken
    PARAMS = {'enrollment_type':'student', 'enrollment_state':'active', 'state':'available'}
    courses = requests.get(url = URL, params = PARAMS).json()
    courseIDS = []
    courseNames = []
    for course in courses:
        #print(course['name']+': '+str(course['id']))
        courseIDS.append(course['id'])
        courseNames.append(course['name'])
    return (courseNames, courseIDS)
def getCourseStudents(courseID):
    pass

if __name__ == '__main__':
    #CANVAS DATA -----------------------------------------
    ACCESS_TOKEN = r"9957~tRs1L5UWx9pPhC21lM9m09LvkyQtdWE2jhMuICXiErkqXc4NxQ9DwGbGAdMgXyv2"
    (courseNames, courseIDS) = getMyCourses(ACCESS_TOKEN)
    
    URL = r'https://canvas.instructure.com/api/v1/courses/'+str(courseIDS[1])+'/users?access_token='+ACCESS_TOKEN
    PARAMS = {'enrollment_type':'student', 'enrollment_state':'active'}
    students = requests.get(url = URL, params = PARAMS).json()
    #for student in students:
        #print(student['name']+': '+str(student['id']))



    #GMAIL INFORMATION ---
    # =============================================================================
    # SET EMAIL LOGIN REQUIREMENTS
    # =============================================================================
    gmail_user = 'hackingtemplecanvas@gmail.com'
    gmail_app_password = '123Password'

    # =============================================================================
    # SET THE INFO ABOUT THE SAID EMAIL
    # =============================================================================
    sent_from = gmail_user
    sent_to = ['tuf08803@temple.edu']
    sent_subject = "Where are all my Robot Women at?"
    sent_body = ("Hey, what's up? friend!\n\n"
                 "I hope you have been well!\n"
                 "\n"
                 "Here is our slack please join!!"
                "https://hackingtemplecanvas.slack.com/"
                  "\n"
                 "Cheers,\n"
                 "Jay\n")

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

    # =============================================================================
    # SEND EMAIL OR DIE TRYING!!!
    # Details: http://www.samlogic.net/articles/smtp-commands-reference.htm
    # =============================================================================

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()

        #print('Email sent!')
    #except Exception as exception:
        #print("Error: %s!\n\n" % exception)    





    #SLACK INVITATION --------------------------------------------
    SLACKTOKEN = 'xoxp-595260197703-595262257863-595773860102-948a26bf7867f55488eba910c830464d'
    URL = 'https://slack.com/api/channels.create'
    DATA = {'token':SLACK_TOKEN, 'name': 'test1'}
    requests.post(url = URL, data = DATA)

    channels = requests.get(url = 'https://slack.com/api/conversations.list', params = {'token':SLACK_TOKEN}).json()
    channels = channels['channels']
    channelIDS = []
    for channel in channels:
        #print(channel['name']+': '+str(channel['id']))
        channelIDS.append(channel['id'])

    members = requests.get(url = 'https://slack.com/api/conversations.members', params = {'token':SLACK_TOKEN, 'channel':'CHHJCNBP0'}).json()
    #print(members)

    for member in members['members']:
        users = requests.get(url = 'https://slack.com/api/users.profile.get', params = {'token':SLACK_TOKEN, 'user':member}).json()
        if users['profile']['email'] == 'tui98107@temple.edu':        
            URL = 'https://slack.com/api/channels.invite'
            DATA = {'token':SLACK_TOKEN, 'channel': str(channelIDS[0]), 'user':member}
            response = requests.post(url = URL, data = DATA)
            #print(response.json())
