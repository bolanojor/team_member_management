from django import forms
from team_member.models import TeamMember

# Team member model form: notice admin_role label and widget are changed
class TeamMemberForm(forms.ModelForm):
    class Meta():
        model = TeamMember
        fields = ('picture', 'first_name', 'last_name',  'email',
                  'phone_number', 'admin_role')
        labels = {
            'admin_role': ''
        }
        widgets = {
            'admin_role': forms.RadioSelect
        }
