from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'


class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='user_id')
    name = models.CharField(max_length=100)
    photo_url = models.URLField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    timezone = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    availability = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    performance_rating = models.FloatField(blank=True, null=True)
    on_time_percentage = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'profiles'


class Skills(models.Model):
    skill_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)  # Changed from skill_name to name to match schema

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'skills'


class ProfileSkills(models.Model):
    profile_id = models.ForeignKey('Profile', on_delete=models.CASCADE, db_column='profile_id')
    skill_id = models.ForeignKey('Skills', on_delete=models.CASCADE, db_column='skill_id')

    def __str__(self):
        return f"{self.profile_id.name} - {self.skill_id.name}"

    class Meta:
        db_table = 'profile_skills'
        unique_together = ('profile_id', 'skill_id')


class Portfolio(models.Model):
    portfolio_id = models.AutoField(primary_key=True)
    profile_id = models.ForeignKey('Profile', on_delete=models.CASCADE, db_column='profile_id')
    project_title = models.CharField(max_length=255)
    media_url = models.URLField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.project_title

    class Meta:
        db_table = 'portfolios'


class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='client_id')
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    budget_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    budget_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    delivery_type = models.CharField(max_length=50, blank=True, null=True)
    custom_deadline = models.DateTimeField(blank=True, null=True)
    require_rough_sketch = models.BooleanField(default=False)
    require_moodboard = models.BooleanField(default=False)
    auto_cancel_enabled = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='open')
    visibility_status = models.CharField(max_length=50, default='public')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'jobs'


class JobAttachments(models.Model):
    attachment_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey('Jobs', on_delete=models.CASCADE, db_column='job_id')
    file_url = models.URLField(max_length=255)

    def __str__(self):
        return f"Attachment for {self.job_id.title}"

    class Meta:
        db_table = 'job_attachments'


class Applications(models.Model):
    application_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey('Jobs', on_delete=models.CASCADE, db_column='job_id')
    freelancer_id = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='freelancer_id')
    status = models.CharField(max_length=50, default='pending')
    start_time = models.DateTimeField(blank=True, null=True)
    countdown_deadline = models.DateTimeField(blank=True, null=True)
    draft_url = models.URLField(max_length=255, blank=True, null=True)
    draft_submitted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Application by {self.freelancer_id.email} for {self.job_id.title}"

    class Meta:
        db_table = 'applications'


class Messages(models.Model):
    message_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey('Jobs', on_delete=models.CASCADE, db_column='job_id')
    sender_id = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='sender_id')
    content = models.TextField()
    message_type = models.CharField(max_length=50, default='text')
    timestamp = models.DateTimeField(auto_now_add=True)
    version_url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Message from {self.sender_id.email} in {self.job_id.title}"

    class Meta:
        db_table = 'messages'


class Bans(models.Model):
    ban_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='user_id')
    reason = models.TextField()
    issued_at = models.DateTimeField(auto_now_add=True)
    is_temporary = models.BooleanField(default=True)
    appeal_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Ban for {self.user_id.email}"

    class Meta:
        db_table = 'bans'


class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey('Jobs', on_delete=models.CASCADE, db_column='job_id')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='pending')
    released_at = models.DateTimeField(blank=True, null=True)
    tip = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Payment of ${self.amount} for {self.job_id.title}"

    class Meta:
        db_table = 'payments'


class ClientDashboard(models.Model):
    dashboard_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='user_id')
    job_id = models.ForeignKey('Jobs', on_delete=models.CASCADE, db_column='job_id')
    notes = models.TextField(blank=True, null=True)
    rehired_freelancer_id = models.ForeignKey(
        'Users', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='rehired_jobs',
        db_column='rehired_freelancer_id'
    )

    def __str__(self):
        return f"Client Dashboard for {self.user_id.email}"

    class Meta:
        db_table = 'client_dashboard'


class FreelancerDashboard(models.Model):
    dashboard_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='user_id')
    active_jobs = models.IntegerField(default=0)
    total_earnings = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    strike_count = models.IntegerField(default=0)
    availability = models.CharField(max_length=100, blank=True, null=True)
    category_preferences = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Freelancer Dashboard for {self.user_id.email}"

    class Meta:
        db_table = 'freelancer_dashboard'


class Ratings(models.Model):
    rating_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey('Jobs', on_delete=models.CASCADE, db_column='job_id')
    client_id = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='given_ratings', db_column='client_id')
    freelancer_id = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='received_ratings', db_column='freelancer_id')
    draft_quality = models.IntegerField()
    communication = models.IntegerField()
    average_rating = models.FloatField()
    review = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Rating for {self.freelancer_id.email} by {self.client_id.email}"

    class Meta:
        db_table = 'ratings'