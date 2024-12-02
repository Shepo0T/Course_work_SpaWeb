from rest_framework import serializers


class HabitsValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value['pleasant_habit']:
            if value['associated_habit'] or value['reward']:
                raise serializers.ValidationError(
                    'У приятной привычки не может быть связанной привычки или вознаграждения')
            if value['associated_habit'] and value['reward']:
                raise serializers.ValidationError(
                    'Может быть только связанная привычка или вознаграждение,')
            if value['time_to_complete'] > '00:02:00':
                raise serializers.ValidationError(
                    'Длительность привычки не может быть больше 2 минут')
            if value['associated_habit']:
                if not value['associated_habit'].is_good:
                    raise serializers.ValidationError('Связанные привычки = приятные привычки')
