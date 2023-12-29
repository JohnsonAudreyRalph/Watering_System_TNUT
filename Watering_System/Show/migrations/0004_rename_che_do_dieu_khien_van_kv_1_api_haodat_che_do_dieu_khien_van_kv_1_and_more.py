# Generated by Django 4.2.8 on 2023-12-25 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Show', '0003_api_haodat_api_khecoc_api_thaiminh'),
    ]

    operations = [
        migrations.RenameField(
            model_name='api_haodat',
            old_name='che_do_dieu_khien_van_kv_1',
            new_name='che_do_dieu_khien_van_KV_1',
        ),
        migrations.RenameField(
            model_name='api_haodat',
            old_name='che_do_dieu_khien_van_kv_2',
            new_name='che_do_dieu_khien_van_KV_2',
        ),
        migrations.RenameField(
            model_name='api_haodat',
            old_name='che_do_dieu_khien_van_kv_3',
            new_name='che_do_dieu_khien_van_KV_3',
        ),
        migrations.RenameField(
            model_name='api_haodat',
            old_name='che_do_hang_ngay_dieu_khien_kv_1',
            new_name='che_do_hang_ngay_dieu_khien_KV_1_1',
        ),
        migrations.RenameField(
            model_name='api_haodat',
            old_name='che_do_hang_ngay_dieu_khien_kv_2',
            new_name='che_do_hang_ngay_dieu_khien_KV_1_2',
        ),
        migrations.RenameField(
            model_name='api_haodat',
            old_name='che_do_hang_ngay_dieu_khien_kv_3',
            new_name='che_do_hang_ngay_dieu_khien_KV_1_3',
        ),
        migrations.RenameField(
            model_name='api_haodat',
            old_name='che_do_hang_ngay_xac_nhan_lan_5',
            new_name='che_do_hang_ngay_dieu_khien_KV_2_1',
        ),
        migrations.RenameField(
            model_name='api_haodat',
            old_name='che_do_hang_ngay_xac_nhan_lan_6',
            new_name='che_do_hang_ngay_dieu_khien_KV_2_2',
        ),
        migrations.RenameField(
            model_name='api_haodat',
            old_name='che_do_hang_ngay_gio_bat_dau_tuoi_5',
            new_name='che_do_tu_dong_cai_dat_do_am',
        ),
        migrations.RenameField(
            model_name='api_haodat',
            old_name='che_do_hang_ngay_gio_bat_dau_tuoi_6',
            new_name='che_do_tu_dong_do_am_max_1',
        ),
        migrations.RenameField(
            model_name='api_haodat',
            old_name='che_do_hang_ngay_phut_bat_dau_tuoi_6',
            new_name='che_do_tu_dong_do_am_max_2',
        ),
        migrations.RenameField(
            model_name='api_haodat',
            old_name='che_do_hang_ngay_phut_bat_dau_tuoi_5',
            new_name='che_do_tu_dong_do_am_max_3',
        ),
        migrations.RenameField(
            model_name='api_haodat',
            old_name='che_do_hang_ngay_thoi_gian_tuoi_5',
            new_name='che_do_tu_dong_do_am_max_4',
        ),
        migrations.RenameField(
            model_name='api_haodat',
            old_name='che_do_hang_ngay_thoi_gian_tuoi_6',
            new_name='che_do_tu_dong_do_am_min_1',
        ),
        migrations.RenameField(
            model_name='api_khecoc',
            old_name='che_do_dieu_khien_van_kv_1',
            new_name='che_do_dieu_khien_van_KV_1',
        ),
        migrations.RenameField(
            model_name='api_khecoc',
            old_name='che_do_dieu_khien_van_kv_3',
            new_name='che_do_dieu_khien_van_KV_3',
        ),
        migrations.RenameField(
            model_name='api_khecoc',
            old_name='che_do_hang_ngay_dieu_khien_kv_1',
            new_name='che_do_hang_ngay_dieu_khien_KV_1_1',
        ),
        migrations.RenameField(
            model_name='api_khecoc',
            old_name='che_do_hang_ngay_dieu_khien_kv_2',
            new_name='che_do_hang_ngay_dieu_khien_KV_1_2',
        ),
        migrations.RenameField(
            model_name='api_khecoc',
            old_name='che_do_hang_ngay_dieu_khien_kv_3',
            new_name='che_do_hang_ngay_dieu_khien_KV_1_3',
        ),
        migrations.RenameField(
            model_name='api_khecoc',
            old_name='che_do_hang_ngay_xac_nhan_lan_5',
            new_name='che_do_hang_ngay_dieu_khien_KV_2_1',
        ),
        migrations.RenameField(
            model_name='api_khecoc',
            old_name='che_do_hang_ngay_xac_nhan_lan_6',
            new_name='che_do_hang_ngay_dieu_khien_KV_2_2',
        ),
        migrations.RenameField(
            model_name='api_khecoc',
            old_name='che_do_hang_ngay_gio_bat_dau_tuoi_5',
            new_name='che_do_tu_dong_cai_dat_do_am',
        ),
        migrations.RenameField(
            model_name='api_khecoc',
            old_name='che_do_hang_ngay_gio_bat_dau_tuoi_6',
            new_name='che_do_tu_dong_do_am_max_1',
        ),
        migrations.RenameField(
            model_name='api_khecoc',
            old_name='che_do_hang_ngay_phut_bat_dau_tuoi_5',
            new_name='che_do_tu_dong_do_am_max_2',
        ),
        migrations.RenameField(
            model_name='api_khecoc',
            old_name='che_do_hang_ngay_phut_bat_dau_tuoi_6',
            new_name='che_do_tu_dong_do_am_max_3',
        ),
        migrations.RenameField(
            model_name='api_khecoc',
            old_name='che_do_hang_ngay_thoi_gian_tuoi_5',
            new_name='che_do_tu_dong_do_am_max_4',
        ),
        migrations.RenameField(
            model_name='api_khecoc',
            old_name='che_do_hang_ngay_thoi_gian_tuoi_6',
            new_name='che_do_tu_dong_do_am_min_1',
        ),
        migrations.RenameField(
            model_name='api_thaiminh',
            old_name='che_do_dieu_khien_van_kv_1',
            new_name='che_do_dieu_khien_van_KV_1',
        ),
        migrations.RenameField(
            model_name='api_thaiminh',
            old_name='che_do_dieu_khien_van_kv_2',
            new_name='che_do_dieu_khien_van_KV_2',
        ),
        migrations.RenameField(
            model_name='api_thaiminh',
            old_name='che_do_dieu_khien_van_kv_3',
            new_name='che_do_dieu_khien_van_KV_3',
        ),
        migrations.RenameField(
            model_name='api_thaiminh',
            old_name='che_do_hang_ngay_dieu_khien_kv_1',
            new_name='che_do_hang_ngay_dieu_khien_KV_1_1',
        ),
        migrations.RenameField(
            model_name='api_thaiminh',
            old_name='che_do_hang_ngay_dieu_khien_kv_2',
            new_name='che_do_hang_ngay_dieu_khien_KV_1_2',
        ),
        migrations.RenameField(
            model_name='api_thaiminh',
            old_name='che_do_hang_ngay_dieu_khien_kv_3',
            new_name='che_do_hang_ngay_dieu_khien_KV_1_3',
        ),
        migrations.RenameField(
            model_name='api_thaiminh',
            old_name='che_do_hang_ngay_xac_nhan_lan_5',
            new_name='che_do_hang_ngay_dieu_khien_KV_2_1',
        ),
        migrations.RenameField(
            model_name='api_thaiminh',
            old_name='che_do_hang_ngay_xac_nhan_lan_6',
            new_name='che_do_hang_ngay_dieu_khien_KV_2_2',
        ),
        migrations.RenameField(
            model_name='api_thaiminh',
            old_name='che_do_hang_ngay_gio_bat_dau_tuoi_5',
            new_name='che_do_tu_dong_cai_dat_do_am',
        ),
        migrations.RenameField(
            model_name='api_thaiminh',
            old_name='che_do_hang_ngay_gio_bat_dau_tuoi_6',
            new_name='che_do_tu_dong_do_am_max_1',
        ),
        migrations.RenameField(
            model_name='api_thaiminh',
            old_name='che_do_hang_ngay_phut_bat_dau_tuoi_5',
            new_name='che_do_tu_dong_do_am_max_2',
        ),
        migrations.RenameField(
            model_name='api_thaiminh',
            old_name='che_do_hang_ngay_phut_bat_dau_tuoi_6',
            new_name='che_do_tu_dong_do_am_max_3',
        ),
        migrations.RenameField(
            model_name='api_thaiminh',
            old_name='che_do_hang_ngay_thoi_gian_tuoi_5',
            new_name='che_do_tu_dong_do_am_max_4',
        ),
        migrations.RenameField(
            model_name='api_thaiminh',
            old_name='che_do_hang_ngay_thoi_gian_tuoi_6',
            new_name='che_do_tu_dong_do_am_min_1',
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_hang_ngay_dieu_khien_KV_2_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_hang_ngay_dieu_khien_KV_3_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_hang_ngay_dieu_khien_KV_3_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_hang_ngay_dieu_khien_KV_3_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_hang_ngay_dieu_khien_KV_4_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_hang_ngay_dieu_khien_KV_4_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_hang_ngay_dieu_khien_KV_4_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_hang_ngay_dieu_khien_KV_4_4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_tu_dong_do_am_min_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_tu_dong_do_am_min_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_tu_dong_do_am_min_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_tu_dong_gio_bat_dau_tuoi_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_tu_dong_gio_bat_dau_tuoi_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_tu_dong_gio_bat_dau_tuoi_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_tu_dong_gio_bat_dau_tuoi_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_tu_dong_phut_bat_dau_tuoi_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_tu_dong_phut_bat_dau_tuoi_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_tu_dong_phut_bat_dau_tuoi_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_tu_dong_phut_bat_dau_tuoi_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_tu_dong_thoi_gian_tuoi_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_tu_dong_thoi_gian_tuoi_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_tu_dong_thoi_gian_tuoi_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_tu_dong_thoi_gian_tuoi_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_xac_nhan_khu_vuc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_xac_nhan_lan_tuoi_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_xac_nhan_lan_tuoi_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_xac_nhan_lan_tuoi_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_haodat',
            name='che_do_xac_nhan_lan_tuoi_4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_hang_ngay_dieu_khien_KV_2_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_hang_ngay_dieu_khien_KV_3_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_hang_ngay_dieu_khien_KV_3_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_hang_ngay_dieu_khien_KV_3_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_hang_ngay_dieu_khien_KV_4_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_hang_ngay_dieu_khien_KV_4_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_hang_ngay_dieu_khien_KV_4_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_hang_ngay_dieu_khien_KV_4_4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_tu_dong_do_am_min_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_tu_dong_do_am_min_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_tu_dong_do_am_min_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_tu_dong_gio_bat_dau_tuoi_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_tu_dong_gio_bat_dau_tuoi_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_tu_dong_gio_bat_dau_tuoi_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_tu_dong_gio_bat_dau_tuoi_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_tu_dong_phut_bat_dau_tuoi_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_tu_dong_phut_bat_dau_tuoi_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_tu_dong_phut_bat_dau_tuoi_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_tu_dong_phut_bat_dau_tuoi_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_tu_dong_thoi_gian_tuoi_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_tu_dong_thoi_gian_tuoi_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_tu_dong_thoi_gian_tuoi_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_tu_dong_thoi_gian_tuoi_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_xac_nhan_khu_vuc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_xac_nhan_lan_tuoi_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_xac_nhan_lan_tuoi_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_xac_nhan_lan_tuoi_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_khecoc',
            name='che_do_xac_nhan_lan_tuoi_4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_hang_ngay_dieu_khien_KV_2_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_hang_ngay_dieu_khien_KV_3_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_hang_ngay_dieu_khien_KV_3_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_hang_ngay_dieu_khien_KV_3_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_hang_ngay_dieu_khien_KV_4_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_hang_ngay_dieu_khien_KV_4_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_hang_ngay_dieu_khien_KV_4_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_hang_ngay_dieu_khien_KV_4_4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_tu_dong_do_am_min_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_tu_dong_do_am_min_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_tu_dong_do_am_min_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_tu_dong_gio_bat_dau_tuoi_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_tu_dong_gio_bat_dau_tuoi_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_tu_dong_gio_bat_dau_tuoi_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_tu_dong_gio_bat_dau_tuoi_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_tu_dong_phut_bat_dau_tuoi_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_tu_dong_phut_bat_dau_tuoi_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_tu_dong_phut_bat_dau_tuoi_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_tu_dong_phut_bat_dau_tuoi_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_tu_dong_thoi_gian_tuoi_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_tu_dong_thoi_gian_tuoi_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_tu_dong_thoi_gian_tuoi_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_tu_dong_thoi_gian_tuoi_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_xac_nhan_khu_vuc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_xac_nhan_lan_tuoi_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_xac_nhan_lan_tuoi_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_xac_nhan_lan_tuoi_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='api_thaiminh',
            name='che_do_xac_nhan_lan_tuoi_4',
            field=models.BooleanField(default=False),
        ),
    ]