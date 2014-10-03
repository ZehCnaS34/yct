from django.contrib.auth.models import User

def create_user(sender, **kwargs):
    password = User.objects.make_random_password()
    e = kwargs['instance']
    fn, ln = e.name.split(' ')
    uname = e.name + e.company.name
    user = User(username=uname,
                password=password,
                first_name=fn,
                last_name=ln,
                email=e.email)
    user.save()
    e.user_id = user.id

