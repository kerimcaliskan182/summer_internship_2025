from django.db import models
from django.core.exceptions import ValidationError
import ipaddress

class User(models.Model):
    first_name = models.CharField(max_length=50)           
    last_name = models.CharField(max_length=50)            
    email = models.EmailField(unique=True)                  
    phone_number = models.CharField(max_length=20, blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)   
    username = models.CharField(max_length=100, blank=True, null=True) 
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def set_username_from_email(self, email):
        if '@' in email:
            self.username = email.split('@')[0]

    def clean(self):
        if '@' not in self.email:
            raise ValidationError("Email adresi '@' karakteri içermelidir.")
        
        if self.phone_number:
            if not self.phone_number.isdigit():
                raise ValidationError("Telefon numarası yalnızca rakamlardan oluşmalıdır.")
            if len(self.phone_number) != 10:
                raise ValidationError("Telefon numarası 10 haneli olmalıdır.")
       
class Device(models.Model):
    hostname = models.CharField(max_length=100, blank=True, null=True)
    device_name = models.CharField(max_length=100)         
    device_type = models.CharField(max_length=50)          
    serial_number = models.CharField(max_length=100, blank=True, null=True) 
    ip_address = models.GenericIPAddressField(protocol="IPv4", blank=True, null=True)
    mac_address = models.CharField(max_length=17, blank=True, null=True) 
    os_type = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hostname} - {self.device_name} ({self.device_type})"

def validate_ipv4_address(value):
    try:
        ipaddress.IPv4Address(value)
    except ValueError:
        raise ValidationError("Geçerli bir IPv4 adresi giriniz.")
    
def clean(self):
    if self.mac_address:
            if len(self.mac_address) != 17 or ':' not in self.mac_address:
                raise ValidationError("MAC adresi geçerli formatta olmalıdır (örn: AA:BB:CC:DD:EE:FF).")

