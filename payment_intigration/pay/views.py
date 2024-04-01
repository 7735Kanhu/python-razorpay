from django.shortcuts import render
import razorpay
from payment_intigration.settings import RAZOR_KEY_ID ,RAZOR_KEY_SECRET

# Create your views here.
client = razorpay.Client(auth=(RAZOR_KEY_ID , RAZOR_KEY_SECRET))
 

def index(request):

    DATA = {
        "amount": 60000,
        "currency": "INR",
        "payment_capture": '1',
        # "receipt": "receipt#1",
        # "notes": {
        #     "key1": "value3",
        #     "key2": "value2"
        # }
    }
    payment_order = client.order.create(data=DATA)
    payment_order_id = payment_order['id']
    contex = {
        'amount': 600 ,'api_key': RAZOR_KEY_ID, 'order_id':payment_order_id
    }
    return render(request,'index.html',contex)