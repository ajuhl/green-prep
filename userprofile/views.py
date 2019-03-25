from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm

def profile(request):
    # return HttpResponse("Hello, world. You're at the user profile page.")
    # if request.method == 'POST':
    #     form = UserForm(request.POST, instance = request.user)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         message.error(request, _('Complete form.'))
    # else:
    #     form = UserForm(instance = request.user)
    # return render(request, 'profile.html', {
    #     'form' : form,
    # })
    form = UserForm()
    return render(request, 'profile.html', {'form': form})
    # if request.method == 'POST':
    #     form = UserForm(request.POST, instance = request.user.profile)
    #     if form.is_valid:
    #         form.save()
    #         return HttpResponseRedirect('returned')
    #     else:
    #         user = request.user
    #         profile = request.profile
    #         form = UserForm(instance=profile)
    #     args = {}
    #     args.update(csrf(request))
    #     args['form'] = form
    #     print (form)
    # else:
    #     form = UserForm(instance=request.user.profile)
    #     args = {}
    #     args.update(csrf(request))
    #     args['form'] = form
    #
    #     return render_to_response('profile.html', args)
