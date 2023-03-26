# import openpyxl
# import Test
import unittest


class TestMethods(unittest.TestCase):

    def test_Wb_bill(self):
        print("test for opening workbook")

    def test_eBill_total(self):
        print("test for total calculation of electric Bill")

    def test_wBill_total(self):
        print("test for total calculation of water Bill")

    def test_gBill_total(self):
        print("test for total calculation of gas Bill")

    def test_clear_value(self):
        print('test for clearing all the values in the row')

    def test_total_monthly_bill(self):
        print("test for total monthly bill")

    def test_saveB(self):
        print("test for saving file of bill excel file")

    def test_loadWb_flat(self):
        print("test for opening workbook")

    def test_delete_row(self):
        print("Test of Deleting a row")

    def test_saveF(self):
        print("test for saving file of flat excel")
