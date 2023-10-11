from django.shortcuts import render, redirect
from .models import Profile, ChatMessage, SoilData  
from .forms import SignUpForm, SoilPropertiesForm, ChatForm
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
import google.generativeai as palm


# Create your views here.

def index(request):
    profiles = Profile.objects.all()
    soils = SoilData.objects.all()

    context = {
        'profiles': profiles,
        'soils': soils,
    }
    return render(request, 'index.html', context=context)

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('index')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'login_form': form})

def logout_view(request):
    auth_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')

@login_required
def soil_data(request):
    if request.method == 'POST':
        form = SoilDataForm(request.POST)
        if form.is_valid():
            try:
                data = form.save(commit=False)
                data.user = request.user
                data.save()
                return redirect('user_dashboard')
            except Exception as e:
                return render(request, 'soil_data.html', {'form': form, 'error': e})
        else:
            return render(request, 'soil_data.html', {'form': form, 'error_message': 'Form validation failed.'})
    else:
        form = SoilDataForm()
    return render(request, 'soil_data.html', {'form': form})

@login_required
def user_dashboard(request):
    soil_data = SoilData.objects.filter(user=request.user)
    # Implement logic to calculate health assessments if needed
    return render(request, 'dashboard.html', {'soil_data': soil_data})



@login_required
def soil_properties_analysis(request):
    if request.method == 'POST':
        palm.configure(api_key='AIzaSyA2fSdNXmrkVRtxVECo-PjdtGAyntUMpW8')
        models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
        model = models[0].name
        form = SoilPropertiesForm(request.POST)
        if form.is_valid():
            # Construct the prompt using user input
            prompt = f"Analyze the soil with the following properties: Particle Size: {form.cleaned_data['particle_size']}, Soil pH: {form.cleaned_data['soil_ph']}, CEC: {form.cleaned_data['cec']}, Calcium: {form.cleaned_data['calcium']}, Magnesium: {form.cleaned_data['magnesium']} and then give a recommendation"

            # Use the text completion model to generate a response
            completion = palm.generate_text(
                model=model,
                prompt=prompt,
                temperature=0.7,  # Adjust temperature as needed
                max_output_tokens=800,  # Adjust max length as needed
            )

            # Get the generated response from the completion
            generated_response = completion.result

            return render(request, 'analysis_result.html', {'generated_response': generated_response})

    else:
        form = SoilPropertiesForm()

    return render(request, 'soil_properties_input_form.html', {'form': form})






@login_required
def chat_view(request):
    if request.method == 'POST':
        palm.configure(api_key='AIzaSyA2fSdNXmrkVRtx    VECo-PjdtGAyntUMpW8')
        form = ChatForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            if prompt == 'quit':
                return redirect('chat_view')  # Redirect to chat view when 'quit' is entered

            # Use your chat model here to generate a response
            response = palm.chat(
                context="Be a professional soil scientist with vast and accurate knowledge in soil science, agronomy, and general agriculture.",
                examples=[],
                messages=prompt
            )

            # Save the user's input and the model's response to your database
            ChatMessage.objects.create(user_input=prompt, model_response=response.last)
    else:
        form = ChatForm()

    # Fetch all chat messages from your database
    chat_messages = ChatMessage.objects.all()

    return render(request, 'chat_page.html', {'form': form, 'chat_messages': chat_messages})

