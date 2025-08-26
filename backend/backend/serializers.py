from rest_framework import serializers
from .models import (
    Users, Profile, Skills, ProfileSkills, Portfolio, Jobs, JobAttachments,
    Applications, Messages, Bans, Payments, ClientDashboard, FreelancerDashboard, Ratings )

# Users Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(source="user_id", read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


# Skills Serializer
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


# ProfileSkills Serializer
class ProfileSkillSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(source="profile_id", read_only=True)
    skill = SkillSerializer(source="skill_id", read_only=True)

    class Meta:
        model = ProfileSkills
        fields = '__all__'


# Portfolio Serializer
class PortfolioSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(source="profile_id", read_only=True)

    class Meta:
        model = Portfolio
        fields = '__all__'


# Jobs Serializer
class JobSerializer(serializers.ModelSerializer):
    client = UserSerializer(source="client_id", read_only=True)

    class Meta:
        model = Jobs
        fields = '__all__'


# JobAttachments Serializer
class JobAttachmentSerializer(serializers.ModelSerializer):
    job = JobSerializer(source="job_id", read_only=True)

    class Meta:
        model = JobAttachments
        fields = '__all__'


# Applications Serializer
class ApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer(source="job_id", read_only=True)
    freelancer = UserSerializer(source="freelancer_id", read_only=True)

    class Meta:
        model = Applications
        fields = '__all__'


# Messages Serializer
class MessageSerializer(serializers.ModelSerializer):
    job = JobSerializer(source="job_id", read_only=True)
    sender = UserSerializer(source="sender_id", read_only=True)

    class Meta:
        model = Messages
        fields = '__all__'


# Bans Serializer
class BanSerializer(serializers.ModelSerializer):
    user = UserSerializer(source="user_id", read_only=True)

    class Meta:
        model = Bans
        fields = '__all__'


# Payments Serializer
class PaymentSerializer(serializers.ModelSerializer):
    job = JobSerializer(source="job_id", read_only=True)

    class Meta:
        model = Payments
        fields = '__all__'


# Client Dashboard Serializer
class ClientDashboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(source="user_id", read_only=True)
    job = JobSerializer(source="job_id", read_only=True)
    rehired_freelancer = UserSerializer(source="rehired_freelancer_id", read_only=True)

    class Meta:
        model = ClientDashboard
        fields = '__all__'


# Freelancer Dashboard Serializer
class FreelancerDashboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(source="user_id", read_only=True)

    class Meta:
        model = FreelancerDashboard
        fields = '__all__'


# Ratings Serializer
class RatingSerializer(serializers.ModelSerializer):
    job = JobSerializer(source="job_id", read_only=True)
    client = UserSerializer(source="client_id", read_only=True)
    freelancer = UserSerializer(source="freelancer_id", read_only=True)

    class Meta:
        model = Ratings
        fields = '__all__'
