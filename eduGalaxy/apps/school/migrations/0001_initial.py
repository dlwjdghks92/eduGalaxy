# Generated by Django 2.1.4 on 2019-08-09 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='admin/schoolCSV', verbose_name='파일 경로')),
                ('file_use', models.CharField(default='', max_length=25, verbose_name='파일 용도')),
                ('file_name', models.CharField(default='', max_length=25, verbose_name='파일명')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='파일 생성 날짜')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='관리자명')),
            ],
            options={
                'verbose_name_plural': '학교 csv파일 목록',
                'verbose_name': '학교 csv 파일',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ooe', models.CharField(max_length=30, verbose_name='시도교육청')),
                ('lea', models.CharField(max_length=20, verbose_name='지역교육청')),
                ('location', models.CharField(max_length=20, verbose_name='지역')),
                ('scode', models.CharField(max_length=20, verbose_name='정보공시 학교코드')),
                ('name', models.CharField(max_length=20, verbose_name='학교명')),
                ('gcode', models.IntegerField(default=0, verbose_name='학교급코드')),
                ('estab_div', models.CharField(max_length=4, verbose_name='설립구분')),
                ('char', models.CharField(max_length=15, verbose_name='학교특성')),
                ('has_branches', models.BooleanField(default=False, verbose_name='분교여부')),
                ('estab_type', models.CharField(max_length=4, verbose_name='설립유형')),
                ('day_n_night', models.CharField(max_length=4, verbose_name='주야구분')),
                ('anniversary', models.CharField(max_length=8, verbose_name='개교기념일')),
                ('estab_date', models.CharField(max_length=8, verbose_name='설립일')),
                ('dcode', models.CharField(max_length=10, verbose_name='법정동코드')),
                ('address1', models.CharField(max_length=40, verbose_name='주소')),
                ('address2', models.CharField(max_length=25, verbose_name='상세주소')),
                ('zip_code', models.CharField(max_length=6, verbose_name='우편번호')),
                ('zip_code_st', models.CharField(max_length=5, verbose_name='도로명 우편번호')),
                ('address1_st', models.CharField(max_length=40, verbose_name='도로명주소')),
                ('address2_st', models.CharField(max_length=25, verbose_name='도로명 상세주소')),
                ('lat', models.FloatField(default=0, verbose_name='위도')),
                ('lng', models.FloatField(default=0, verbose_name='경도')),
                ('tel', models.CharField(max_length=20, verbose_name='전화번호')),
                ('fax', models.CharField(max_length=20, verbose_name='팩스번호')),
                ('homepage', models.CharField(max_length=40, verbose_name='홈페이지주소')),
                ('gender_div', models.CharField(max_length=10, verbose_name='남녀공학 구분')),
                ('num_student', models.IntegerField(default=0, verbose_name='학생 수')),
                ('num_teacher', models.IntegerField(default=0, verbose_name='교직원 수')),
                ('modified_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='수정날짜')),
            ],
            options={
                'verbose_name_plural': '학교 목록',
                'verbose_name': '학교',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(max_length=100, null=True, verbose_name='학교로고 파일명')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성날짜')),
                ('created_ip', models.CharField(max_length=20, verbose_name='게시판 생성 ip')),
                ('modified_date', models.DateTimeField(blank=True, null=True, verbose_name='수정날짜')),
                ('modified_ip', models.CharField(max_length=20, verbose_name='게시판 수정 ip')),
                ('eduser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('school_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.Info')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성날짜')),
                ('created_ip', models.CharField(max_length=20, verbose_name='게시판 생성 ip')),
                ('modified_date', models.DateTimeField(blank=True, null=True, verbose_name='수정날짜')),
                ('modified_ip', models.CharField(max_length=20, verbose_name='게시판 수정 ip')),
                ('eduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Post')),
            ],
        ),
    ]
