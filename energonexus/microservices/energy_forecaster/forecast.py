from django.core.management.base import BaseCommand
from celery import shared_task
from sklearn.ensemble import GradientBoostingRegressor
from energonexus.core.models import EnergyConsumption

@shared_task
def forecast_energy_consumption():
    energy_data = EnergyConsumption.objects.all()
    X = energy_data.drop(['energy_consumption'], axis=1)
    y = energy_data['energy_consumption']

    model = GradientBoostingRegressor(n_estimators=100)
    model.fit(X, y)

    forecast_data = []
    for i in range(30):  # forecast for the next 30 days
        forecast_data.append(model.predict(X.iloc[-1:] + i))

    return forecast_data

class Command(BaseCommand):
    def handle(self, *args, **options):
        forecast_energy_consumption.delay()
