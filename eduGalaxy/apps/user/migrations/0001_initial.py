# Generated by Django 2.1.4 on 2019-08-26 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EdUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='이메일')),
                ('nickname', models.CharField(max_length=50, unique=True, verbose_name='닉네임')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 여부')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자')),
            ],
            options={
                'verbose_name_plural': '사용자',
                'verbose_name': '사용자',
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=20, verbose_name='학교')),
                ('grade', models.IntegerField(default=0, null=True, verbose_name='학년')),
                ('age', models.IntegerField(default=0, verbose_name='나이')),
                ('gender', models.CharField(default='U', max_length=2, verbose_name='성별')),
            ],
            options={
                'verbose_name_plural': '자녀',
                'verbose_name': '자녀',
            },
        ),
        migrations.CreateModel(
            name='EduLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=20, verbose_name='학교')),
                ('status', models.CharField(max_length=4, verbose_name='상태')),
                ('modified_cnt', models.IntegerField(default=0, verbose_name='수정 횟수')),
                ('child', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Child')),
            ],
        ),
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eduser', models.CharField(max_length=100, verbose_name='기본정보')),
                ('profile', models.CharField(max_length=100, verbose_name='프로필')),
                ('Parent', models.CharField(max_length=200, verbose_name='학부모정보')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('eduser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('signup_ip', models.CharField(max_length=20, verbose_name='가입 ip')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='가입날짜')),
                ('login_ip', models.CharField(max_length=20, verbose_name='로그인 ip')),
                ('log_file', models.FileField(null=True, upload_to='', verbose_name='로그 파일')),
            ],
            options={
                'verbose_name_plural': 'logs',
                'verbose_name': 'log',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('eduser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('group', models.CharField(max_length=30, verbose_name='직업')),
                ('phone', models.CharField(max_length=15, verbose_name='핸드폰 번호')),
                ('receive_email', models.BooleanField(default=False, verbose_name='이메일 수신 여부')),
                ('confirm', models.BooleanField(default=False, verbose_name='본인인증 여부')),
            ],
            options={
                'verbose_name_plural': '사용자 프로필',
                'verbose_name': '사용자 프로필',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.Profile')),
                ('address1', models.CharField(max_length=100, null=True, verbose_name='주소')),
                ('address2', models.CharField(max_length=100, null=True, verbose_name='상세주소')),
            ],
            options={
                'verbose_name_plural': '학부모',
                'verbose_name': '학부모',
            },
        ),
        migrations.CreateModel(
            name='SchoolAuth',
            fields=[
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.Profile')),
                ('school', models.CharField(max_length=20, null=True, verbose_name='소속/학교')),
                ('auth_doc', models.FileField(null=True, upload_to='', verbose_name='인증 서류')),
                ('tel', models.CharField(max_length=15, null=True, verbose_name='사무실 연락처')),
            ],
            options={
                'verbose_name_plural': '학교 관계자',
                'verbose_name': '학교 관계자',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.Profile')),
                ('school', models.CharField(max_length=20, verbose_name='학교')),
                ('grade', models.IntegerField(default=0, null=True, verbose_name='학년')),
                ('age', models.IntegerField(default=0, verbose_name='나이')),
                ('gender', models.CharField(default='U', max_length=2, verbose_name='성별')),
                ('address1', models.CharField(max_length=100, null=True, verbose_name='주소')),
                ('address2', models.CharField(max_length=100, null=True, verbose_name='상세주소')),
            ],
            options={
                'verbose_name_plural': '학생',
                'verbose_name': '학생',
            },
        ),
        migrations.AddField(
            model_name='edulevel',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Student'),
        ),
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Parent'),
        ),
    ]
