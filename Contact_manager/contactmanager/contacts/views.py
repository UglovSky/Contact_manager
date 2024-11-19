from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def contact_add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})


def contact_delete(request, id):
    contact = get_object_or_404(Contact, pk=id)
    contact.delete()
    return redirect('contact_list')
