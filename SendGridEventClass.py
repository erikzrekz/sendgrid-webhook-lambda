import datetime

event_set = set(['processed', 'dropped', 'delivered', 'deferred', 'bounce', 'open', 'click', 'spamreport', 'unsubscribe', 'group_unsubscribe', 'group_resubscribe'])

class SendGridEvent:
    """A class for SendGrid's event objects"""
    def __init__(self):
        self.TableName='EmailEvents'
        self.Item= {}
    
    def add_event(self, payload):
        timestamp = payload.get('timestamp')
        stringTimestamp = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
        
        self.Item['timestamp'] = {
            'S': stringTimestamp
        }
        
        email = payload.get('email')
        self.Item['email'] = {
            'S': email
        }
        
        smtp_id = payload.get('smtp-id')
        self.Item['smtp-id'] = {
            'S': smtp_id
        }
        
        sg_event_id = payload.get('sg_event_id')
        self.Item['sg_event_id'] = {
            'S': sg_event_id
        }
        
        sg_message_id = payload.get('sg_message_id')
        self.Item['sg_message_id'] = {
            'S': sg_message_id
        }
        
        event = payload.get('event')
        if (event in event_set):
            self.Item['event'] = {
                'S': event
            }
        else:
            self.Item['event'] = {
                'S': 'unknown'
            }
        
        if (event in ('open', 'click', 'group_resubscribe', 'group_unsubscribe')):
            ip = payload.get('ip')
            useragent = payload.get('useragent')
            
            self.Item['ip'] = {
                'S': ip
            }
            
            self.Item['useragent'] = {
                'S': useragent
            }
        
        if (event in ('dropped', 'bounce')):
            reason = payload.get('reason')
            status = payload.get('status')
            
            self.Item['reason'] = {
                'S': reason
            }
            
            self.Item['status'] = {
                'S': status
            }
            
        if (event in ('delivered', 'deferred')):
            response = payload.get('response')

            self.Item['response'] = {
                'S': response
            }
        
        if (event in ('click', 'group_resubscribe', 'group_unsubscribe')):
            url = payload.get('url')

            self.Item['url'] = {
                'S': url
            }
        
        if (event in ('group_resubscribe', 'group_unsubscribe')):
            asm_group_id = payload.get('asm_group_id')

            self.Item['asm_group_id'] = {
                'S': str(asm_group_id)
            }
        
        if (event in ('deferred')):
            attempt = payload.get('attempt')

            self.Item['attempt'] = {
                'S': attempt
            }
        
        if (event in ('processed')):
            pool = payload.get('pool', "unknown")

            self.Item['pool'] = {
                'S': pool
            }
        
        