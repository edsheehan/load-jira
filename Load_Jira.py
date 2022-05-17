import configparser
from jira.client import JIRA

def new_issue(jira, summ, desc, sp, epic):
    jira.create_issue(project='SF', summary=summ, description=desc, \
        issuetype={'name': 'Story'}, customfield_10013=epic, customfield_10020=sp, \
        assignee={'accountId':'557058:c8e45e29-55d3-434e-a2d1-fcf0770af621'})
    
def show_issue(jira, issue_id):
    print (jira.projects())
    issue = jira.issue(issue_id)
    print (issue.fields.project.key)             # 'JRA'
    print (issue.fields.issuetype.name)          # 'New Feature'
    print (issue.fields.reporter.displayName)    # 'Mike Cannon-Brookes [Atlassian]'
    print (issue.fields.customfield_10020)
    print (issue.fields.customfield_10013)

def read_auth():
    config = configparser.ConfigParser()
    config.read('D:/Temp/Jira_Auth.ini')
    auth_user = config['DEFAULT']['User']
    auth_key = config['DEFAULT']['Auth_Key']
    return auth_user, auth_key

def main():
    auth_user, auth_key = read_auth()
    options = {'server': 'https://navemagile.atlassian.net/'}
    jira = JIRA(options, basic_auth=(auth_user, auth_key))
    show_issue(jira, 'SF-45')
    quit()
    quit()

    new_issue(jira, 'Monday morning walk', 'Stay healthy', 1, 'SF-3')
    new_issue(jira, 'Tuesday morning walk', 'Stay healthy', 1, 'SF-3')
    new_issue(jira, 'Wednesday morning walk', 'Stay healthy', 1, 'SF-3')
    new_issue(jira, 'Thursday morning walk', 'Stay healthy', 1, 'SF-3')
    new_issue(jira, 'Friday morning walk', 'Stay healthy', 1, 'SF-3')
    new_issue(jira, 'Saturday morning walk', 'Stay healthy', 1, 'SF-3')
    new_issue(jira, 'Sunday morning walk', 'Stay healthy', 1, 'SF-3')
    new_issue(jira, 'Scan mail', 'Stay organised', 2, 'SF-24')
    new_issue(jira, 'Work-out session 1', 'Stay healthy', 2, 'SF-3')
    new_issue(jira, 'Work-out session 2', 'Stay healthy', 2, 'SF-3')
    new_issue(jira, 'Work-out session 3', 'Stay healthy', 2, 'SF-3')
    
    print('Finished')   
    quit()
        
main()