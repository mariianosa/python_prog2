from worker import Worker
from workerdb import WorkerDB
import unittest
from unittest.mock import patch

class TestWorkerAndWorkerDB(unittest.TestCase):
    def setUp(self):
        self.collection = WorkerDB()

    def test_add_worker(self):
        input_data = 'Max ,Olefir, IT, 3000'
        with patch('builtins.input', side_effect=input_data.split(',')):
            self.collection.add_worker()
        self.assertEqual(len(self.collection.collection), 1)
        
    def test_delete_worker(self):
        example_worker = Worker(worker_id="15", name="Anton", surname="Ivankiv", department="OLA", salary="8000")
        self.collection.collection.append(example_worker)
        input_data = "15"
        with patch('builtins.input', side_effect=input_data.split(',')):
            self.collection.delete(15)
        self.assertEqual(len(self.collection.collection), 0)

    def test_d_sorted(self):

        worker1 = Worker(worker_id="20", name="Anna", surname="Doe", department="IT", salary="5000")
        worker2 = Worker(worker_id="1", name="Ivan", surname="Boniuk", department="HR", salary="6000")
        worker3 = Worker(worker_id="17", name="Lina", surname="Smich", department="ITHouse", salary="5500")

        self.collection.collection.extend([worker1, worker2, worker3])

        expected_order = [worker2, worker3, worker1]
        with patch('builtins.input', side_effect=["ID"]):
            self.collection.d_sorted("ID")

        self.assertEqual(self.collection.collection, expected_order, "Lists are not equal")
   