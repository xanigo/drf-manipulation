from rest_framework.fields import DateTimeField


class ManipulationSerializerMixin:
    inserted_at: DateTimeField = DateTimeField(read_only=True)
    updated_at: DateTimeField = DateTimeField(read_only=True)

    class Meta:
        fields = ["inserted_at", "updated_at"]
