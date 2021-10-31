import unittest
import builtins
import pytest
import io
import unittest.mock
from unittest.mock import patch
from assignment import Switcher


class TestMethods(unittest.TestCase):     
        
    def testhelp(self):
        swicther = Switcher()
        self.assertEqual(swicther.Operation('helpCmd'), "Press 1 for creating new user \n Press 2 to update user \n Press 3 to delete user \n Press 4 to print all users \n Press 5 for weather information \n --help for help command")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self,operation,expected_output, mock_stdout):
        swicther = Switcher()
        swicther.Operation(operation) 
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testReadUsers(self):
        self.assert_stdout('readAll','User Entries:\ntestUser\t\n\n')
    
    def testDeleteUsers(self):
        swicther = Switcher()
        original_input = builtins.input
        builtins.input = lambda: 'testUser'
        swicther.Operation('delete')
        self.assertEqual(swicther.users,{})

    def testWeatherInfo(self):
        original_input = builtins.input
        builtins.input = lambda: 'goa'
        self.assert_stdout('weatherInfo','Enter City Name or Longitude and Latitude in following manner: Longitude/Latitude\nhumidity : 5\nPressure : 6\nAverage Temperature : 30\nWind Speed : 5\nWind Degree : 9\nUI index : 12\n')
     
    def testUpdateUser(self):
         mock_args = ['testUser','y','testUser1','234','123','y','123','123']
         with unittest.mock.patch('builtins.input', side_effect=mock_args):
            swicther = Switcher()
            swicther.Operation('update')
         
    def testCreateUser(self):
        mock_args = ['testUser1','123']
        with unittest.mock.patch('builtins.input', side_effect=mock_args):
            swicther = Switcher()
            swicther.Operation('create')
        

if __name__ == '__main__':
    unittest.main()