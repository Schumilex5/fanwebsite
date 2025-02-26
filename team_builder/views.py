from django.shortcuts import render, redirect
from .models import Unit, Team, Strategy
from .forms import TeamForm, StrategyForm

# View for the home page
def home(request):
    return render(request, 'team_builder/home.html')

# View for team builder
def team_builder(request):
    units = Unit.objects.all()
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_builder')
    else:
        form = TeamForm()

    return render(request, 'team_builder/team_builder.html', {'form': form, 'units': units})

# View for strategy planner
def strategy_planner(request):
    strategies = Strategy.objects.all()
    if request.method == 'POST':
        form = StrategyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('strategy_planner')
    else:
        form = StrategyForm()

    return render(request, 'team_builder/strategy_planner.html', {'form': form, 'strategies': strategies})

# Voting function
def vote_strategy(request, strategy_id, vote_type):
    strategy = Strategy.objects.get(id=strategy_id)
    if vote_type == 'up':
        strategy.upvotes += 1
    elif vote_type == 'down':
        strategy.downvotes += 1

    # Hide strategy if it has too many downvotes
    if strategy.downvotes >= 5:
        strategy.hidden = True

    strategy.save()
    return redirect('strategy_planner')
