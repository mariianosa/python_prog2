from worker import Worker
from workerdb import WorkerDB
import unittest
from unittest.mock import patch

class TestWorkerAndWorkerDB(unittest.TestCase):
    def setUp(self):
        self.collection = WorkerDB()

    def test_add_worker(self):
        input_data = 'Max, Olefir, IT, 3000'
        with patch('builtins.input', side_effect=input_data.split(',')):
            self.collection.add_worker()
        self.assertEqual(len(self.collection.collection), 1)
        
    def test_delete_worker(self):
        example_worker = Worker(worker_id = "15", name="Anton", surname="Ivankiv", department="OLA", salary="8000")
        self.collection.collection.append(example_worker)
        input_data = "15"
        with patch('builtins.input', side_effect=input_data.split(',')):
            self.collection.delete(15)
        self.assertEqual(len(self.collection.collection), 0)