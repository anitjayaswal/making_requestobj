making a Request object:

class RequestObj(models.Model): #new
    user = None
    POST = {}
    GET = {}
    META = {}
    def __init__ (self,usr):
        self.user = usr

    def set_post_variable(self,post_var,key):
        self.POST[key] = post_var

    def set_get_variable(self,get_var):
        self.GET = get_var


request_obj = RequestObj
status = 'delivered'
d = s.deliveryoutscan_set.all().latest('id')
employee = EmployeeMaster.objects.get(employee_code=d.employee_code.employee_code)
user= employee.user
request_obj.user = user
request_obj.POST['data_entry_emp']= employee.employee_code
request_obj.POST['delivery_emp']= employee.employee_code
request_obj.POST['reason_code']= "999"
request_obj.POST['recieved_by']= "Self"
request_obj.POST['remarks']= ''
request_obj.POST['time']=time
request_obj.POST['date']=date
import time as tm
import random
num = str(int(tm.time() * 1000))
ran = str(math.floor((random.random() * 100) + 1))
ajax_num = num + ran
request_obj.POST['ajax_num']=ajax_num
if status=='delivered':
    request_obj.POST['awbd']=s.airwaybill_number
    request_obj.POST['awbu']=''
elif status=='undelivered':
    request_obj.POST['awbu']=s.airwaybill_number
    request_obj.POST['awbd']=''
