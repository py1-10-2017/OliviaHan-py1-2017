import time
class Call(object):
    def __init__(self, caller_name, caller_num, reason):
        self.call_id = id(self)
        self.caller_name = caller_name
        self.caller_num = caller_num
        self.time_stamp = time.strftime('%c')
        self.reason = reason

    def display(self):
        print self.call_id
        print '{} is called at {} from {} regarding {}'.format(self.caller_name,self.time_stamp, self.caller_num, self.reason )

        return self



class CallCenter(object):
    def __init__(self):
        self.call = []
        self.queue = len(self.call)

    def add_new(self,call):
        self.call = self.call.append(call)
        return self

    def remove(self):
        self.call.pop(0)
        return self

    def info(self):
        for i in self.call:
            print i.display()
        return self


call1 = Call('olivia','425-638-7251','question')

callcenter1 = CallCenter()
callcenter1.add_new(call1).info()
