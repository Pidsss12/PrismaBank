import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bank_queue.settings')
django.setup()

from django.contrib.auth.models import User
from queues.models import ServiceCategory, Counter, BankConfig

def setup():
    # Create Superuser
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Created superuser: admin / admin123")
    
    # Create Staff Teller
    if not User.objects.filter(username='teller').exists():
        u = User.objects.create_user('teller', 'teller@example.com', 'admin123')
        u.is_staff = True
        u.save()
        print("Created staff teller: teller / admin123")

    # Create Staff CS
    if not User.objects.filter(username='cs').exists():
        u = User.objects.create_user('cs', 'cs@example.com', 'admin123')
        u.is_staff = True
        u.save()
        print("Created staff cs: cs / admin123")

    # Create regular Nasabah/Customer
    if not User.objects.filter(username='nasabah').exists():
        User.objects.create_user('nasabah', 'nasabah@example.com', 'admin123')
        print("Created regular customer: nasabah / admin123")
    
    # Create Categories
    teller, _ = ServiceCategory.objects.get_or_create(
        name='Teller', 
        prefix='A', 
        color='blue',
        icon='banknote'
    )
    cs, _ = ServiceCategory.objects.get_or_create(
        name='Customer Service', 
        prefix='B', 
        color='indigo',
        icon='user-cog'
    )
    
    # Create Counters
    Counter.objects.get_or_create(name='Loket 1', service_category=teller)
    Counter.objects.get_or_create(name='Loket 2', service_category=teller)
    Counter.objects.get_or_create(name='CS 1', service_category=cs)
    
    # Create Config
    BankConfig.objects.get_or_create(bank_name='Antigravity Bank')
    
    print("Initial data created successfully!")

if __name__ == '__main__':
    setup()
