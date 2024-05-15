from django.test import TestCase
from .models import Machine, ProductionLog
from .serializers import MachineSerializer, ProductionLogSerializer

class MachineModelTestCase(TestCase):
    def setUp(self):
        self.machine = Machine.objects.create(
            machine_name="Test Machine",
            machine_serial_no="123456",
        )

    def test_machine_model(self):
        machine = Machine.objects.get(machine_name="Test Machine")
        self.assertEqual(machine.machine_name, "Test Machine")
        self.assertEqual(machine.machine_serial_no, "123456")

class ProductionLogModelTestCase(TestCase):
    def setUp(self):
        self.machine = Machine.objects.create(
            machine_name="Test Machine",
            machine_serial_no="123456",
        )
        self.production_log = ProductionLog.objects.create(
            cycle_no="1",
            unique_id="123",
            material_name="Test Material",
            machine=self.machine,
            start_time="2024-05-15T00:00:00Z",
            end_time="2024-05-15T01:00:00Z",
            duration=1,
            ideal_cycle_time=0.5,
            actual_output=10,
            good_products=9,
            total_products=10,
        )

    def test_production_log_model(self):
        production_log = ProductionLog.objects.get(cycle_no="1")
        self.assertEqual(production_log.cycle_no, "1")
        self.assertEqual(production_log.unique_id, "123")
        self.assertEqual(production_log.material_name, "Test Material")
        self.assertEqual(production_log.machine, self.machine)
        self.assertEqual(production_log.start_time.strftime('%Y-%m-%dT%H:%M:%SZ'), "2024-05-15T00:00:00Z")
        self.assertEqual(production_log.end_time.strftime('%Y-%m-%dT%H:%M:%SZ'), "2024-05-15T01:00:00Z")
        self.assertEqual(production_log.duration, 1)
        self.assertEqual(production_log.ideal_cycle_time, 0.5)
        self.assertEqual(production_log.actual_output, 10)
        self.assertEqual(production_log.good_products, 9)
        self.assertEqual(production_log.total_products, 10)

class MachineSerializerTestCase(TestCase):
    def setUp(self):
        self.machine = Machine.objects.create(
            machine_name="Test Machine",
            machine_serial_no="123456",
        )

    def test_machine_serializer(self):
        serializer = MachineSerializer(self.machine)
        self.assertEqual(serializer.data['machine_name'], "Test Machine")
        self.assertEqual(serializer.data['machine_serial_no'], "123456")

class ProductionLogSerializerTestCase(TestCase):
    def setUp(self):
        self.machine = Machine.objects.create(
            machine_name="Test Machine",
            machine_serial_no="123456",
        )
        self.production_log = ProductionLog.objects.create(
            cycle_no="1",
            unique_id="123",
            material_name="Test Material",
            machine=self.machine,
            start_time="2024-05-15T00:00:00Z",
            end_time="2024-05-15T01:00:00Z",
            duration=1,
            ideal_cycle_time=0.5,
            actual_output=10,
            good_products=9,
            total_products=10,
        )

    def test_production_log_serializer(self):
        serializer = ProductionLogSerializer(self.production_log)
        self.assertEqual(serializer.data['cycle_no'], "1")
        self.assertEqual(serializer.data['unique_id'], "123")
        self.assertEqual(serializer.data['material_name'], "Test Material")
        self.assertEqual(serializer.data['machine'], self.machine.id)
        self.assertEqual(serializer.data['start_time'], "2024-05-15T00:00:00Z")
        self.assertEqual(serializer.data['end_time'], "2024-05-15T01:00:00Z")
        self.assertEqual(serializer.data['duration'], 1.0)
        self.assertEqual(serializer.data['ideal_cycle_time'], 0.5)
        self.assertEqual(serializer.data['actual_output'], 10)
        self.assertEqual(serializer.data['good_products'], 9)
        self.assertEqual(serializer.data['total_products'], 10)

