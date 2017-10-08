#import random
#import time

VERSION = '1.0'

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
def gen_queue_pop():
    pop_time = random.randint(1,5)
    time.sleep(pop_time)
    
def start_countdown():
    #gen_queue_pop()
    session_attributes = {}
    reprompt = None
    speech_output = "Queue popped"
    end_session = False
    return build_response(
            session_attributes,
            'welcome',
            speech_output,
            reprompt,
            end_session)
    
    
def queue_accept(intent, session):
    session_attributes = {}
    reprompt = None
    speech_output = "Accepting queue..."
    end_session = True

    return build_response(
            session_attributes,
            intent['name'],
            speech_output,
            reprompt,
            end_session)

# EVENTS
def event_new_session(request, session):
    pass

def event_launch(request, session):
    return queue_accept(intent, session)

def event_intent(request, session):
    if request['intent']['name'] == 'CheckQueueIntent':
        return funct_to_check()
    elif request['intent']['name'] == 'AcceptQueueIntent':
        return queue_accept(intent, session)
    elif request['intent']['name'] == 'DeclineQueueIntent':
        return funct_to_decline()
    elif request['intent']['name'] == 'AMAZON.HelpIntent':
        return funct_to_help()
    elif (request['intent']['name'] == 'AMAZON.CancelIntent' or
          request['intent']['name'] == 'AMAZON.StopIntent'):
        return funct_to_cancel()
    else:
        raise ValueError("Invalid intent")

def event_end_session(request, session):
    pass


# HANDLER
def main_handler(event, context):
    if event['session']['new']:
        pass

    if event['request']['type'] == 'LaunchRequest':
        return event_launch(event['request'], event['session'])
    elif event['request']['type'] == 'IntentRequest':
        return event_intent(event['request'], event['session'])
    elif event['request']['type'] == 'SessionEndedRequest':
        return event_end_session(event['request'], event['session'])
