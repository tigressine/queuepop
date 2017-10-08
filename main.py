VERSION = '1.0'
responses = {
    'positive': ['accept',
                 'accept queue',
                 'yes',
                 'ye',
                 'go',
                 'lets go'],
    'negative': ['decline',
                 'decline queue',
                 'no',
                 'nah fam',
                 'cancel']
}

def build_response(
        session_attributes,
        title, 
        output, 
        reprompt, 
        end_session):
    return {
        'version' : VERSION,
        'sessionAttributes' : session_attributes,
        'response': {
            'outputSpeech' : {
                'type' : 'PlainText',
                'text' : output
                },
            'card' : {
                'type' : 'Simple',
                'title' : title,
                'content' : output
                },
            'reprompt' : {
                'outputSpeech' : {
                    'type' : 'PlainText',
                    'text' : reprompt
                    }
                },
            'shouldEndSession' : end_session
            }
        }

#FUNCTIONS: THIS WHERE THE CASH IS BOIS
def get_help():
    session_attributes = {}
    reprompt = None
    speech_output = "Please give a valid response"
    end_session = False
    
    return build_response(
            session_attributes,
            'QueuePop',
            speech_output,
            reprompt,
            end_session)
            
def start_countdown():
    session_attributes = {}
    reprompt = None
    speech_output = "Queue popped"
    end_session = False
    
    return build_response(
            session_attributes,
            'QueuePop',
            speech_output,
            reprompt,
            end_session)
    
def queue_accept():
    session_attributes = {}
    reprompt = None
    speech_output = "Accepting queue..."
    end_session = True

    return build_response(
            session_attributes,
            'QueuePop',
            speech_output,
            reprompt,
            end_session)

def queue_decline():
    session_attributes = {}
    reprompt = None
    speech_output = "Declining queue..."
    end_session = True
    
    return build_response(
            session_attributes,
            'QueuePop',
            speech_output,
            reprompt,
            end_session)

# EVENTS
def event_launch(request, session):
    return start_countdown()

def event_intent(request, session):
    if request['intent']['name'] == 'QueueIntent':
        #return queue_accept()
        if request['intent']['slots']['Response']['value'] in responses['positive']:
            return queue_accept()
        elif request['intent']['slots']['Response']['value'] in responses['negative']:
            return queue_decline()
        else:
            return get_help()
    elif request['intent']['name'] == 'AMAZON.HelpIntent':
        return get_help()
    else:
        raise ValueError("Invalid intent")

# HANDLER
def main_handler(event, context):
    if event['request']['type'] == 'LaunchRequest':
        return event_launch(event['request'], event['session'])
    elif event['request']['type'] == 'IntentRequest':
        return event_intent(event['request'], event['session'])
    elif event['request']['type'] == 'SessionEndedRequest':
        return event_end_session(event['request'], event['session'])
