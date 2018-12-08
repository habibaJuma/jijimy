from flask.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]