from django import forms
from .models import Record

class InputRecord(forms.ModelForm):
	class Meta:
		model = Record
		fields = ['first_name','last_name','address','city','state','province','kode_pos','email','phone','created_by']

	def __init__(self, *args, **kwargs):
		super(InputRecord, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['class']="form-control"
		self.fields['first_name'].widget.attrs['required']="required"
		self.fields['first_name'].widget.label="First Name"

		self.fields['last_name'].widget.attrs['class']="form-control"
		self.fields['last_name'].widget.attrs['required']="required"
		self.fields['last_name'].widget.label="Last Name"

		self.fields['address'].widget.attrs['class']="form-control"
		self.fields['address'].widget.attrs['required']="required"
		self.fields['address'].widget.label="Address"

		self.fields['email'].widget.attrs['class']="form-control"
		self.fields['email'].widget.attrs['required']="required"
		self.fields['email'].widget.label="Email"

		self.fields['phone'].widget.attrs['class']="form-control"
		self.fields['phone'].widget.attrs['required']="required"
		self.fields['phone'].widget.label="Phone Number"

		self.fields['city'].widget.attrs['class']="form-control"
		self.fields['city'].widget.attrs['required']="required"
		self.fields['city'].widget.label="City"

		self.fields['state'].widget.attrs['class']="form-control"
		self.fields['state'].widget.attrs['required']="required"
		self.fields['state'].widget.label="State"

		self.fields['province'].widget.attrs['class']="form-control"
		self.fields['province'].widget.attrs['required']="required"
		self.fields['province'].widget.label="Province"

		self.fields['kode_pos'].widget.attrs['class']="form-control"
		self.fields['kode_pos'].widget.attrs['required']="required"
		self.fields['kode_pos'].widget.label="Postal Code"

		self.fields['created_by'].widget.attrs['class']="form-control"
		self.fields['created_by'].widget.attrs['readonly']="readonly"
		self.fields['created_by'].widget.label="Created By"

class UpdateRecord(forms.ModelForm):
	class Meta:
		model = Record
		fields = ['first_name','last_name','address','city','state','province','kode_pos','email','phone']

	def __init__(self, *args, **kwargs):
		super(InputRecord, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['class']="form-control"
		self.fields['first_name'].widget.attrs['required']="required"
		self.fields['first_name'].widget.label="First Name"
		self.fields['first_name'].widget.attrs['disabled']="disabled"

		self.fields['last_name'].widget.attrs['class']="form-control"
		self.fields['last_name'].widget.attrs['required']="required"
		self.fields['last_name'].widget.label="Last Name"
		self.fields['last_name'].widget.attrs['disabled']="disabled"

		self.fields['address'].widget.attrs['class']="form-control"
		self.fields['address'].widget.attrs['required']="required"
		self.fields['address'].widget.label="Address"

		self.fields['email'].widget.attrs['class']="form-control"
		self.fields['email'].widget.attrs['required']="required"
		self.fields['email'].widget.label="Email"

		self.fields['phone'].widget.attrs['class']="form-control"
		self.fields['phone'].widget.attrs['required']="required"
		self.fields['phone'].widget.label="Phone Number"

		self.fields['city'].widget.attrs['class']="form-control"
		self.fields['city'].widget.attrs['required']="required"
		self.fields['city'].widget.label="City"

		self.fields['state'].widget.attrs['class']="form-control"
		self.fields['state'].widget.attrs['required']="required"
		self.fields['state'].widget.label="State"

		self.fields['province'].widget.attrs['class']="form-control"
		self.fields['province'].widget.attrs['required']="required"
		self.fields['province'].widget.label="Province"

		self.fields['kode_pos'].widget.attrs['class']="form-control"
		self.fields['kode_pos'].widget.attrs['required']="required"
		self.fields['kode_pos'].widget.label="Postal Code"