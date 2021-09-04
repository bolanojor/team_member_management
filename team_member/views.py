from team_member.models import TeamMember
from team_member.forms import TeamMemberForm
from django.shortcuts import render, redirect, get_object_or_404

# List view: Shows all team members
def list(request):
    team_members_list = TeamMember.objects.all()
    content = {'team_members': team_members_list}
    return render(request, 'team_member/list.html', context=content)

# Add view: Adds a team member
def add(request):

    # On POST request gather form information and save a new team member
    if request.method == 'POST':
        team_member_form = TeamMemberForm(request.POST)

        if team_member_form.is_valid():
            team_member = team_member_form.save()

            if 'picture' in request.FILES:
                team_member.picture = request.FILES['picture']
                team_member.save()
            return redirect('/team_member/')
    else:
        # On GET request display empty form
        team_member_form = TeamMemberForm()
        content = {'form': team_member_form}
        return render(request, 'team_member/add.html', context=content)

# Edit view: Edits any team member's information
def edit(request, team_member_id):
    team_member = get_object_or_404(TeamMember, id=team_member_id)

    # On POST request gather form information and update team member
    if request.method == 'POST':
        team_member_form = TeamMemberForm(request.POST, instance=team_member)

        if team_member_form.is_valid():
            team_member = team_member_form.save()

            if 'picture' in request.FILES:
                team_member.picture = request.FILES['picture']
                team_member_form.save()
            return redirect('/team_member/')
    else:
        # On GET request display form with team member information
        team_member_form = TeamMemberForm(instance=team_member)
        content = {'form': team_member_form,
                   'team_member_id': team_member_id}
        return render(request, 'team_member/edit.html', context=content)

# Delete view: Deletes a team member
# Notice there's no HTML associated
def delete(request, team_member_id):
    team_member = get_object_or_404(TeamMember, id=team_member_id)
    team_member.delete()
    return redirect('/team_member/')
