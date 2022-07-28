import sys
import json
import events
from datetime import date
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from mixpanelexportapi.mixpanelexportapi_client import MixpanelexportapiClient

global client


def get_dictionary_count(dictionary):
    count = 0
    for k in dictionary:
        count += len(dictionary[k])
    return count


def get_events_from_mixpanel_api(from_date, to_date):
    where = 'defined(properties["$username"])'
    project_id = 690335
    accept = 'text/plain'
    result = client.export_data.mixpanel_events_data(from_date, to_date, where, project_id, accept)

    return list(result.split("\n"))


# for debugging purpose
def get_events_from_local_file():
    with open('D:\\Hackathon\\output-username-signup.json', encoding="utf8") as json_file:
        json_list = list(json_file)
    return json_list


def get_signup_email_list_from_events(json_list):
    list = []
    for json_str in json_list:
        if json_str != '':
            event = json.loads(json_str)
            event_name = event['event']
            if event_name == events.CGaaSEvents.SignUp.value:
                list.append(event['properties'].get('$username'))
    return list

def get_counts(df):
    counts_list = []
    cgaas_events = df[((df.Event=='SignUp') & (df.SignUpProperty=='Anypoint')) |\
       ((df.Event=='TransformViaAPI')) |\
       ((df.Event=='Transform_Failed') & (df.EventProperty=='TransformViaAPI')) |\
       ((df.Event=='Failed: SDKGenerated_API')) |\
       ((df.Event=='SDKGenerated_API')) |\
       ((df.Event=='OnPremPortalGeneration')) |\
       ((df.Event=='OnPremPortalGenerationFailure'))].Email.nunique()
    
    commons_events = df[df.Event.str.contains("Transform")].Email.nunique()
    codegen_events = df[df.Event.str.contains("SDKGenerated")].Email.nunique()
    portal_events = df[df.Event.str.contains("Portal")].Email.nunique()
    
    counts_list.append(commons_events)
    counts_list.append(codegen_events)
    counts_list.append(portal_events)
    counts_list.append(cgaas_events)
    
    return counts_list

def get_filtered_event_count(week_number):
    commons_dict = {k: [] for k in events.CommonsEvents.list()}
    portal_dict = {k: [] for k in events.PortalEvents.list()}
    codegen_dict = {k: [] for k in events.CodeGenEvents.list()}
    cgaas_dict = {k: [] for k in events.CGaaSEvents.list()}

    events_list = []

    # populate events dictionary
    events_list.extend(events.CommonsEvents.list())
    events_list.extend(events.PortalEvents.list())
    events_list.extend(events.CodeGenEvents.list())
    events_list.extend(events.CGaaSEvents.list())

    events_dict = {k: [] for k in events_list}

    # -1 since our week is 1 week behind the iso calendar
    date_range = get_week_date_range(week_number - 1)
    print("Generating data for week {0}, from {1} to {2}.".format(week_number, date_range[0], date_range[1]))
    json_list = get_events_from_mixpanel_api(date_range[0], date_range[1])

    # get list of signup emails from the events
    signup_email_list = get_signup_email_list_from_events(json_list)
    
    # list to filter duplicate email values
    event_email_list = []

    for json_str in json_list:
        if json_str != '':
            event = json.loads(json_str)
            event_name = event['event']
            user_email = event['properties'].get('$username')
            event_property= event['properties'].get('InvokedFrom', 'NA')
            signup_property= event['properties'].get('SignUpType', 'NA')
            
            
            # if event is relevant and is for new signup users
            if (event_name in events_dict.keys()) and (user_email in signup_email_list):
                event_email = event_name +'-&-'+ user_email +'-&-'+ event_property +'-&-'+ signup_property
                # to remove the duplicate events for same user
                if event_email not in event_email_list:
                    events_dict[event_name].append(event)
                    event_email_list.append(event_email)
    
    
    fin_lists = []
    for row in event_email_list:
        fin_lists.append(row.split('-&-'))
        
    df = pd.DataFrame(fin_lists, columns = ['Event', 'Email', 'EventProperty', 'SignUpProperty'])
    df = df.drop_duplicates()
    
    return get_counts(df)



def get_week_date_range(week_number):
    # (year, week, day of week)
    start = date.fromisocalendar(2022, week_number - 1, 6)

    # (year, week, day of week)
    end = date.fromisocalendar(2022, week_number, 5)

    return [start, end]


def get_week_list_from_range(start, end):
    lst = []
    lst.extend(range(start, end))
    lst.append(end)
    return lst


def plot_graph(input_range_list):
    commons_count_per_week = []
    portal_count_per_week = []
    codegen_count_per_week = []
    cgass_count_per_week = []

    for event in events_per_week.values():
        commons_count_per_week.append(event[0])
        portal_count_per_week.append(event[1])
        codegen_count_per_week.append(event[2])
        cgass_count_per_week.append(event[3])

    plt.plot(input_range_list, commons_count_per_week, label="Commons")
    plt.plot(input_range_list, portal_count_per_week, label="Portal")
    plt.plot(input_range_list, codegen_count_per_week, label="CodeGen")
    plt.plot(input_range_list, cgass_count_per_week, label="CGAAS")
    # naming the x axis
    plt.xlabel('Week')
    # naming the y axis
    plt.ylabel('Count')
    plt.legend()
    # plt.show()
    now = datetime.now()
    plt.savefig("Activations-" + now.strftime("%H-%M-%S") + ".png")


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise TypeError("Invalid input. usage, app.py start_week_range end_week_range")

    # process command line 
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    # Initialize the Mixpanel client
    client = MixpanelexportapiClient(
        basic_auth_user_name='auth_user_name',
        basic_auth_password='auth_password',
    )

    events_per_week = {}
    input_range_list = []

    # create list using the range
    input_range_list = get_week_list_from_range(start, end)

    for i in input_range_list:
        
        events_per_week[i] = get_filtered_event_count(i)

    print(events_per_week)

    plot_graph(input_range_list)

