from django.shortcuts import render, render_to_response, RequestContext, HttpResponse
from threading import Thread
from .models import MQTTSimulatorTable
from django.utils import timezone
# from django.utils import simplejson
import numpy, json, time, datetime
# Create your views here.
dic = dict()
flag = False
tempFlag = False
class MQTTSimulator(object):
    def __init__(self, interval=100):
        self.interval = interval
        thread = Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    
    
    def run(self):
        """ Method that runs forever """
        global flag
        if not flag:
            while True:
                # Do something
                self.GenerateAndStoreData("BOX1")
                self.GenerateAndStoreData("BOX2")
                self.GenerateAndStoreData("BOX3")
                # print(jsonpayload)
                # print('Doing something imporant in the background')
                time.sleep(self.interval)

    
    def GenerateAndStoreData(self,hboxtype):
        global dic
        temperature = numpy.random.uniform(15,40)
        mq2 = numpy.random.uniform(0,2)
        mq3 = numpy.random.uniform(0,2)
        mq4 = numpy.random.uniform(0,2)
        mq5 = numpy.random.uniform(0,2)
        mq6 = numpy.random.uniform(0,2)
        mq7 = numpy.random.uniform(0,2)
        sound = numpy.random.uniform(50,100)
        humidity = numpy.random.uniform(20,70)
        # print("Hello1")
        # insertintotable = MQTTSimulatorTable(hboxtypedb=hboxtype,temperaturedb=temperature,mq2db=mq2,mq3db=mq3,mq4db=mq4,mq5db=mq5,mq6db=mq6,mq7db=mq7,sounddb=sound,humiditydb=humidity)
        # insertintotable.save()
        if temperature > 39.5:
            tempFlag = True
         # print(fetchhbox1.values())
        # print()
        # print()
        dic = { 'Temperature':temperature,'MQ2':mq2,'MQ3':mq3,'MQ4':mq4,'MQ5':mq5,'MQ6':mq6,'MQ7':mq7,'Sound':sound,'Humidity':humidity}
        # jsonpayload = json.dumps(dic)
        # return ""
def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

def home(request):
    tempFlag = False
    flag = True
    mqtt = MQTTSimulator()
    fetchhbox1 = MQTTSimulatorTable.objects.filter(hboxtypedb='BOX1').order_by('-timestampdb')[:10]
    fetchhbox2 = MQTTSimulatorTable.objects.filter(hboxtypedb='BOX2').order_by('-timestampdb')[:10]
    fetchhbox3 = MQTTSimulatorTable.objects.filter(hboxtypedb='BOX3').order_by('-timestampdb')[:10]
    
    box1 = list(fetchhbox1.values())
    box1 = json.dumps(box1, default=datetime_handler)
    box2 = json.dumps(list(fetchhbox2.values()),default=datetime_handler)
    box3 = json.dumps(list(fetchhbox3.values()),default=datetime_handler)
    data = {"HBOX1" :  box1 ,"HBOX2":  box2 ,"HBOX3": box3 }   
    # print(jsonpayload) 
    data = json.dumps(data) 
    return HttpResponse(data, content_type='application/json') 
    # return render(request, 'Base.html')
    # return render(request, 'Base.html')
    # return render_to_response('Base.html',locals(),context_instance=RequestContext(request))
    # while True:





