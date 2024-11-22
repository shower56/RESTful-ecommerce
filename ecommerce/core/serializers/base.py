from rest_framework import serializers


class CustomModelSerializer(serializers.ModelSerializer):
    """
    serializer 내부에 업데이트가 되어야 하지 말아야 팔드가 있다면 class Meta 내부에 `up_update_fields 를 구성하여 업데이트시 제외한다.
    """

    def to_internal_value(self, data):
        if self.instance and hasattr(self.Meta, "no_update_fields"):
            for field in self.Meta.no_update_fields:
                if field in data:
                    data.pop(field)
        return data
