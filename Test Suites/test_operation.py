import sys
sys.path.append('C:/Users/youse/Desktop/tkinter')

import sqlite3
import unittest
import utils

DB_PATH = 'C:/Users/youse/Desktop/tkinter/Database/pickbox.db'

class Test_Operation(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.c= self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_cancel(self):

        # Case 1
        shipment_id = 100001
        shipment = utils.get_shipment(shipment_id)
        prev_status =  shipment[0][1]
        prev_latest_update = shipment[0][2]
        # operation
        utils.cancel_shipment(shipment_id)
        updated_shipment = utils.get_shipment(shipment_id)
        new_status = updated_shipment[0][1]
        new_latest_update = updated_shipment[0][2]
        result =  (new_status == "Cancelled" and new_latest_update != prev_latest_update)
        expected = True
        self.assertEqual(result, expected)
        # restoring
        utils.restore_shipment_status_latest_update(shipment_id, prev_status, prev_latest_update)

        # Case 2
        shipment_id = 100002
        shipment = utils.get_shipment(shipment_id)
        prev_status =  shipment[0][1]
        prev_latest_update = shipment[0][2]
        # operation
        utils.cancel_shipment(shipment_id)
        updated_shipment = utils.get_shipment(shipment_id)
        new_status = updated_shipment[0][1]
        new_latest_update = updated_shipment[0][2]
        result =  (new_status == "Cancelled" and new_latest_update != prev_latest_update)
        expected = True
        self.assertEqual(result, expected)
        # restoring
        utils.restore_shipment_status_latest_update(shipment_id, prev_status, prev_latest_update)
      
    def test_update_locker(self):
        
        # Case 1
        shipment_id = 100001
        locker_id = 1006
        shipment = utils.get_shipment(shipment_id)
        prev_locker_id =  shipment[0][6]
        # operation
        utils.update_locker(locker_id, shipment_id)
        updated_shipment = utils.get_shipment(shipment_id)
        new_locker_id = updated_shipment[0][6]
        result =  new_locker_id == locker_id
        expected = True
        self.assertEqual(result, expected)
        # restoring
        utils.restore_shipment_locker_id(shipment_id, prev_locker_id)

        # Case 2
            
    def test_update_status(self):
        
        # Case 1: the status is Pending and it should update to Out For Delivery along side the latest_update
        shipment_id = 100001
        prev_status = "Pending"
        expected_status = "Out For Delivery"
        shipment = utils.get_shipment(shipment_id)
        prev_latest_update = shipment[0][2]
        # operation
        utils.update_shipment_status(shipment_id, prev_status)
        updated_shipment = utils.get_shipment(shipment_id)
        new_stuts = updated_shipment[0][1]
        new_latest_update = updated_shipment[0][2]
        result =  (expected_status == new_stuts and new_latest_update != prev_latest_update)
        expected = True
        self.assertEqual(result, expected)
        # restoring
        utils.restore_shipment_status_latest_update(shipment_id, prev_status, prev_latest_update)
        
        # Case 2: the status is Out For Delivery and it should update to Ready For Collection along side the latest_update
        shipment_id = 100003
        prev_status = "Out For Delivery"
        expected_status = "Ready For Collection"
        shipment = utils.get_shipment(shipment_id)
        prev_latest_update = shipment[0][2]
        # operation
        utils.update_shipment_status(shipment_id, prev_status)
        updated_shipment = utils.get_shipment(shipment_id)
        new_stuts = updated_shipment[0][1]
        new_latest_update = updated_shipment[0][2]
        result =  (expected_status == new_stuts and new_latest_update != prev_latest_update)
        expected = True
        self.assertEqual(result, expected)
        # restoring
        utils.restore_shipment_status_latest_update(shipment_id, prev_status, prev_latest_update)
        
if __name__ == '__main__':
    unittest.main()