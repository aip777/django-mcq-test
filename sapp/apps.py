from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
    menu = (
        ParentItem('Students', children=[
            ChildItem('Students', url='/admin/sapp/studentinformation/'),
        ], icon='fa fa-leaf'),

        ParentItem('Users', children=[
            ChildItem(model='auth.user'),
            ChildItem('User groups', 'auth.group'),
        ], icon='fa fa-users'),

        ParentItem('Answers', children=[
            ChildItem(model='sapp.Answers'),
            ChildItem('Answers', url='/admin/sapp/answers/'),
        ], icon='fa fa-users'),

        ParentItem('Make Questions', children=[
            ChildItem(model='sapp.Makequestion'),
            ChildItem('Make Questions', url='/admin/sapp/makequestion/'),
        ], icon='fa fa-users'),

        ParentItem('Change Password', children=[
            ChildItem('Password change', url='admin:password_change'),
            # ChildItem('Open Google', url='http://google.com', target_blank=True),

        ], align_right=True, icon='fa fa-cog'),
    )

    def ready(self):
        super(SuitConfig, self).ready()

        # DO NOT COPY FOLLOWING LINE
        # It is only to prevent updating last_login in DB for demo app
        self.prevent_user_last_login()

    def prevent_user_last_login(self):
        """
        Disconnect last login signal
        """
        from django.contrib.auth import user_logged_in
        from django.contrib.auth.models import update_last_login
        user_logged_in.disconnect(update_last_login)