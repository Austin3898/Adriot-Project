from .models import Customer, Payment
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import JsonResponse

import stripe
stripe.api_key = 'sk_test_51J3oFkCitZGeZ3SITK39zquvb3yiaM33aCeSrKrT5Xo8wsmnMoxTNXuTXiRkjzk1zbCGr9IrxBMh1Avgr4PvHaDj00n4ne9GBg'

# Create your views here.
def index(request):
    return render(request, 'payment_api/index.html')

def charge(request):
    amount = 5
    if request.method == 'POST':
        print('Data: ', request.POST)

        amount = int(request.POST['amount'])
        email=request.POST['email']
        name=request.POST['nickname']
        rec_name = request.POST['recipient_name']
        rec_acct_no = request.POST['recipient_acct_no']
        phone = request.POST['phone']
        source=request.POST['stripeToken']

        # Create stripe customer
        customer = stripe.Customer.create(
            email=email,
            name=name,
            source=source,
        )

        # Create stripe charge
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency= 'usd',
            description='Payment',
        )

        # After the success we add the payment to the database
        customer_details, created = Customer.objects.get_or_create(name=name, email=email, phone=phone)
        payment_details = Payment(customer=customer_details, status='Pending', recipients_name=rec_name, recipients_account_number=rec_acct_no, amount=amount)
        payment_details.save()
        
    return redirect(reverse('success', args=[amount]))

def successMsg(request, args):
    amount = args
    return render(request, 'payment_api/success.html', {'amount': amount})

def view_all_payments(request):
    all_payments = Payment.objects.filter(status='Pending')
    all_customers = Customer.objects.all()

    context = {'payments': all_payments, 'customers': all_customers}
    return render(request, 'payment_api/view.html', context)