import unittest
import testing

class MyTest(unittest.TestCase):

	
	def setUp(self):
		""" Setting up for the test """
		print "FooTest:setUP_:begin"
		
		testName = self.shortDescription()
		if (testName == "Test routine A"):
			print "setting up for test A"
			
		print "FooTest:setUp_:end"
		
	def tearDown(self):
		""" Cleaning up after the test """
		print "FooTest:tearDown_:begin"
		
		testName = self.shortDescription()
		if (testName == "Test routine A"):
			print "cleaning up after test A"
			
		print "FooTest:tearDown_:end"
	
	def test_game(self):
		pass
		#deal_to_player = self.table.deal_to_player()
		
		#self.assertEqual(range(10), deal_to_player())

if __name__ == '__main__':
	unittest.main()