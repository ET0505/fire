import math
from django.http import JsonResponse
from django.shortcuts import *
from .forms import MyForm


def home(request):
    if request.method == 'GET':
        return render(request, 'myapp/home.html')


def ajax_form_submission(request):
    if request.method == 'POST':
        form = MyForm(request.POST)

        if form.is_valid():
            start = int(form.cleaned_data['initial_amount'])
            stop = int(form.cleaned_data['final_amount'])
            steps = int(form.cleaned_data['invest_amount'])
            freq_option = form.cleaned_data['frequency_option']
            growth = float(form.cleaned_data['growth']) / 100

            # Set the milestones as one tenth, one quarter, one third, one half, three quarters, and the final amount 
            milestones_amounts = [stop/10, stop/4, stop/3, stop/2, stop*3/4, stop]
            
            # Empty array to store (milestone amount, years, months)
            milestones = []

            # Empty array to store the interest, contribution, and total amounts
            exponent_graph = []
            linear_graph = []
            total_graph = []

            # Calculating the growth rate, adjusted based on the frequency of investment 
            if freq_option == 'per-week':
                rate = growth / 52

            elif freq_option == 'per-month':
                rate = growth / 12

            elif freq_option == 'per-year':
                rate = growth 


            # Calculate the time periods for each milestone using the formula F = P + ([A(r + 1)^t - 1] / r)
            for milestone in milestones_amounts:
                # If milestone has already been reached 
                if milestone < start:
                    years = 0
                    months = 0

                else:
                    time_period = math.log( (((milestone - start) * rate) / steps ) + 1) / math.log(1 + rate)

                    if freq_option == 'per-week':
                        years = time_period / 52
                        months = (years - math.floor(years)) * 12

                    elif freq_option == 'per-month':
                        years = time_period / 12
                        months = (years - math.floor(years)) * 12
                    
                    elif freq_option == 'per-year':
                        years = time_period
                        months = (years - math.floor(years)) * 12
                    
                milestones.append((math.floor(milestone), math.floor(years), math.floor(months)))


            # Caclulate the total amount accrued after each year 
            # Add 2 to account for Year 0 and Year to reach the desired amount
            for year in range(milestones[5][1] + 2):
                exponent_amount = start + ((steps * ((rate + 1)**(year * 12) - 1)) / rate)
                linear_amount = start + (steps * (year * 12))

                interest_amount = exponent_amount - linear_amount

                exponent_graph.append(interest_amount)
                linear_graph.append(linear_amount)
                total_graph.append(exponent_amount)

            # Print statements here ensure the graph data have the right numbers 
            # print(linear_graph)
            # print(exponent_graph)
            # print(total_graph)
            
            return JsonResponse({'milestone_1': milestones[0],
                                 'milestone_2': milestones[1],
                                 'milestone_3': milestones[2],
                                 'milestone_4': milestones[3],
                                 'milestone_5': milestones[4],
                                 'milestone_6': milestones[5],
                                 'exponent_graph': exponent_graph,
                                 'linear_graph': linear_graph,
                                 'total_graph': total_graph})

        return JsonResponse({'Error': 'Invalid form submission. Please try again.'})
