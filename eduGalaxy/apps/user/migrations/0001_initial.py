# Generated by Django 2.1.4 on 2019-07-08 10:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EduUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_email', models.EmailField(max_length=50, unique=True, verbose_name='이메일')),
                ('user_nickname', models.CharField(max_length=50, unique=True, verbose_name='닉네임')),
                ('user_age', models.IntegerField(default=0, verbose_name='나이')),
                ('user_job', models.CharField(max_length=30, verbose_name='직업')),
                ('user_gender', models.CharField(default='U', max_length=2, verbose_name='성별')),
                ('user_address1', models.CharField(max_length=100)),
                ('user_address2', models.CharField(max_length=100)),
                ('user_phone', models.CharField(max_length=15, verbose_name='핸드폰 번호')),
                ('user_receive_email', models.BooleanField(default=False, verbose_name='알림 동의 여부')),
                ('user_confirm', models.BooleanField(default=False, verbose_name='본인인증 여부')),
                ('user_signup_ip', models.CharField(max_length=20, verbose_name='가입 ip')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='가입날짜')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 여부')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자 리스트',
            },
        ),
    ]