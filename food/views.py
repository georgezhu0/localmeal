from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from food.forms import CollegeForm, UserForm, ConsumerForm, TransactionForm, DriverForm
from food.models import College, Swarthmore_Service, Haverford_Service, Transaction, Driver
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.

#def index(request):
#    return HttpResponse("Help eliminate food waste niggas <br/> <a href='/clients/college'>College</a>")

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Please join us"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'food/index.html', context_dict)

def college(request):

	return HttpResponse("I am a college food producer <br/> <a href='/clients/''>Index</a>")

def add_college(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CollegeForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CollegeForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'food/add_college.html', {'form': form})

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        consumer_form = ConsumerForm(data=request.POST)
       

        # If the two forms are valid...
        if user_form.is_valid() and consumer_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            consumer = consumer_form.save(commit=False)
            consumer.user = user

            consumer.save()

           
            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, consumer_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        consumer_form = ConsumerForm()


    # Render the template depending on the context.
    return render(request,
            'food/register.html',
            {'user_form': user_form, 'consumer_form': consumer_form, 'registered': registered, 'type': 'consumer'} )

def driver_register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        driver_form = DriverForm(data=request.POST)
       
        if user_form.is_valid() and driver_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            driver = driver_form.save(commit=False)
            driver.user = user

            driver.save()

            registered = True
        else:
            print user_form.errors, driver_form.errors

    else:
        user_form = UserForm()
        driver_form = DriverForm()


    return render(request,
            'food/register.html',
            {'user_form': user_form, 'driver_form': driver_form, 'registered': registered, 'type': 'driver'} )

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/clients/menu/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Food account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'food/login.html', {'type':1})


def driver_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/drivers/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Driver's account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'food/login.html', {'type':2})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

def menu(request):

    swat = Swarthmore_Service.objects.all()[0]
    have = Haverford_Service.objects.all()[0]

    context_dict = {'boldmessage': "College Menus", 'swatnum':swat.meals, 'swatmenu':swat.menu, 'havnum':have.meals, 'havmenu':have.menu}

    return render(request, 'food/menu.html', context_dict)

def log(request):

    transactions = Transaction.objects.all()

    return render(request, 'food/log.html', {'transactions' : transactions})

@login_required
def order_swat(request):

    print request.user.consumer.addressline1
    if request.method == 'POST':
        order_form = TransactionForm(data=request.POST)
       

        if order_form.is_valid():
            # Save the transaction to the database.
            order = order_form.save(commit=False)

            order.school='Swarthmore'
            order.consumer = request.user.consumer
            order.name = order.consumer.name
            order.date = timezone.now()
            order.save()

            s=Swarthmore_Service.objects.all()[0]
            s.meals-=order.number_meals
            s.save()

            return HttpResponseRedirect('/clients/order/thankyou')

        else:
            print order_form.errors

    else:
        address = {'drop_off': request.user.consumer.addressline1, 
        'city': request.user.consumer.city, 
        'zipcode': request.user.consumer.zipcode}
        order_form = TransactionForm(initial=address)

    return render(request,
            'food/order.html',
            {'order_form': order_form, 'school': 'Swarthmore'} )

@login_required
def order_hav(request):

    if request.method == 'POST':
        order_form = TransactionForm(data=request.POST)
       

        if order_form.is_valid():
            # Save the transaction to the database.
            order = order_form.save(commit=False)

            order.school='Haverford'
            order.consumer = request.user.consumer
            order.name = order.consumer.name
            order.date = timezone.now()
            order.save()

            h=Haverford_Service.objects.all()[0]
            h.meals-=order.number_meals
            h.save()

            return HttpResponseRedirect('/clients/order/thankyou')

        else:
            print order_form.errors

    else:
        address = {'drop_off': request.user.consumer.addressline1, 
        'city': request.user.consumer.city, 
        'zipcode': request.user.consumer.zipcode}
        order_form = TransactionForm(initial=address)

    return render(request,
            'food/order.html',
            {'order_form': order_form, 'school': 'Haverford'})

@login_required
def thankyou(request):
    return render(request, 'food/thanks.html')

@login_required
def map(request):

    school = request.user.driver.school
    transactions = Transaction.objects.all()
    deliveries = []

    for transaction in transactions:
        if school == transaction.school:
            delivery = transaction.drop_off+', '+transaction.city+' '+str(transaction.zipcode)
            deliveries.append(delivery)

    return render(request, 'map.html', {'list': deliveries})