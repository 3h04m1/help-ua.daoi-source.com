from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('main','0006_alter_help_help_type_alter_help_mod_date_and_more')]
    operations = [
        migrations.RenameField(
            model_name='help',
            old_name='help_type',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='needhelp',
            old_name='help_type',
            new_name='title',
        ),
    ]