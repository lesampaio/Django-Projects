from django.http import JsonResponse

# Defining a function which will receive request and perform task depending upon function definition
def alunos(request):
    # This will return a string as HttpResponse
    if request.method == 'GET':
        aluno = {'id': 1, 'nome': 'Guilherme'}
        return JsonResponse(aluno)