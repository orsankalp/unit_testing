from django.contrib import admin
from .models import MVRS_Category
from .models import MVRS_Cars
from .models import Booking
from .models import contact
from django import forms
# Register your models here.
admin.site.register(MVRS_Category)
admin.site.register(MVRS_Cars)

#admin.site.register(Booking,BookingAdmin)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('client_id','client_phone','client_problem', 'raised_on' )
    search_fields = ('client_phone',)
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        class HelpMessageAdminForm(form):
            client_phone = forms.CharField()
            client_id = forms.CharField(widget=forms.Textarea)
            client_problem = forms.CharField(widget=forms.Textarea)

        return HelpMessageAdminForm

    def save_model(self, request, obj, form, change):
        #Fetch booking details based on the entered booking ID
        client_phone = form.cleaned_data['booking_id']
        booking = Booking.objects.get(client_phone=client_phone)

        #Save the help message along with the booking details
        obj.client_phone = booking.client_phone
        #Add other fields as needed
        obj.save()
admin.site.register(contact,ContactAdmin)


