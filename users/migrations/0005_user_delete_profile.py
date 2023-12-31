# Generated by Django 4.2.9 on 2024-01-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("business", "0003_alter_review_owner"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("users", "0004_alter_profile_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("username", models.CharField(max_length=255, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user_groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to.",
                        related_name="users",
                        to="auth.group",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="users",
                        to="auth.permission",
                    ),
                ),
            ],
            options={"ordering": ["created_at"],},
        ),
        migrations.DeleteModel(name="Profile",),
    ]
