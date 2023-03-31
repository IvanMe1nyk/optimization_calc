from django import forms
from .models import MetGold, MetPolPod, MetSven, MetFib, MetKonfig,MetNap, MetRan, MetDef

class MetGoldForm(forms.ModelForm):
    class Meta:
        model=MetGold
        fields=['func','left','right','exp','dir']
        
class MetPolPodForm(forms.ModelForm):
    class Meta:
        model=MetPolPod
        fields=['func','left','right','exp','dir']
        
class MetSvenForm(forms.ModelForm):
    class Meta:
        model=MetSven
        fields=['func','x','exp','dir']
        
class MetFibForm(forms.ModelForm):
    class Meta:
        model=MetFib
        fields=['func','left','right','exp','dir']

class MetKonfigForm(forms.ModelForm):
    class Meta:
        model=MetKonfig
        fields=["func","x_start","delta","alpha","landa","exp","dir"]
        
class MetNapForm(forms.ModelForm):
    class Meta:
        model=MetNap
        fields=["func","x_start","n","exp","dir"]
        
class MetRanForm(forms.ModelForm):
    class Meta:
        model=MetRan
        fields=["func","x_start","nk","M","N","alpha","beta","t","R","dir"]
        
class MetDefForm(forms.ModelForm):
    class Meta:
        model=MetDef
        fields=["func","x_vershyny","n","alpha","beta","exp","hamma","dir"]