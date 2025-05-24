from django.core.management.base import BaseCommand
from faker import Faker
import random
from django.utils.timezone import now

from MyApps.clientes.models import Clientes
from MyApps.empeños.models import Empeños
from MyApps.abonos.models import Abonos
from MyApps.prendas.models import Prendas
from MyApps.PrendasPerdidas.models import PrendasPerdidas

fake = Faker()

class Command(BaseCommand):
    help = 'Llena la base de datos con datos falsos usando Faker'

    def handle(self, *args, **kwargs):
        clientes = self.create_clientes()
        prendas = self.create_prendas(clientes)
        empeños = self.create_empeños(clientes)
        self.create_abonos(empeños)
        self.create_prendas_perdidas(empeños, prendas)
        self.stdout.write(self.style.SUCCESS("¡Base de datos poblada con éxito!"))

    def create_clientes(self, n=10):
        clientes = []
        for _ in range(n):
            cliente = Clientes.objects.create(
                nombre=fake.name(),
                documento=fake.unique.random_number(digits=8),
                telefono=str(fake.random_number(digits=10)),
                direccion=fake.street_name()[:10],
                correo=fake.email()
            )
            clientes.append(cliente)
        return clientes

    def create_prendas(self, clientes, n=20):
        prendas = []
        for _ in range(n):
            prenda = Prendas.objects.create(
                PesoGramos=round(random.uniform(1.0, 500.0), 2),
                ValorEstimado=round(random.uniform(1000, 10000), 2),
                Descripcion=fake.word() + " " + fake.color_name(),
                fk_clientes=random.choice(clientes)
            )
            prendas.append(prenda)
        return prendas

    def create_empeños(self, clientes, n=15):
        empeños = []
        for _ in range(n):
            fecha = fake.date_between(start_date="-6M", end_date="today")
            empeño = Empeños.objects.create(
                FechaEmpeño=fecha,
                PlazoMeses=random.choice([3, 4, 6]),
                InteresMensual=round(random.uniform(5.0, 15.0), 2),
                Estado=random.choice(['A', 'R', 'P']),
                fk_cliente=random.choice(clientes)
            )
            empeños.append(empeño)
        return empeños

    def create_abonos(self, empeños, n=30):
        for _ in range(n):
            Abonos.objects.create(
                fecha=fake.date_between(start_date="-3M", end_date="today"),
                monto=round(random.uniform(100, 2000), 2),
                tipoabono=random.choice(['I', 'C']),
                fk_empeño=random.choice(empeños)
            )

    def create_prendas_perdidas(self, empeños, prendas):
        # Solo crear una PrendasPerdidas por cada empeño
        for empeño in empeños:
            prenda = random.choice(prendas)
            PrendasPerdidas.objects.create(
                Fk_empeño=empeño,
                fk_prenda=prenda,
                FechaPerdida=now()
            )