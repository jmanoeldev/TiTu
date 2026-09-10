from django import forms
from .models import  Experimento, Titulacao, SolucaoTitulante

class ExperimentoForm(forms.ModelForm):
    class Meta:
        model = Experimento
        fields = ['nome', 'tipo', 'data_realizacao']
        widgets = {
            'data_realizacao': forms.DateInput(attrs={'type': 'date'}),
        }

class TitulacaoForm(forms.ModelForm):
    class Meta:
        model = Titulacao
        fields = ['solucao_titulante', 'volume_titulante', 'volume_amostra',
                  'coeficiente_titulante', 'coeficiente_analito',]

    def __init__(self, *args, usuario = None, **kwargs):
        super().__init__(*args, **kwargs)
        if usuario is not None:
            #so mostra no select as soluções titulantes desse user
            self.fields['solucao_titulante'].queryset = (
                SolucaoTitulante.objects.filter(usuario = usuario)
            )

class SolucaoTitulanteForm(forms.ModelForm):
    class Meta:
        model = SolucaoTitulante
        fields = ['nome', 'concentracao_nominal']