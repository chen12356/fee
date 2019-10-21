from rest_framework import serializers

from accountApp.models import account


class accountSerializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = ['id','real_name','idcard_no','login_name','status','create_date','pause_date','close_date']