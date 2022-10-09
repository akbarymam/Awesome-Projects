import contextlib
import io
import unittest

class TestResult(unittest.TestCase):
	def __init__(self, test_name, c):
		super(TestResult, self).__init__(test_name)
		self.c = c
	
	def test_score(self):
		score = self.c.prediction.score
		self.assertIsInstance(score, float, "Score Invalid")
		self.assertAlmostEqual(score, 50.0, msg="Score Invalid", delta=50)

	def test_prediction(self):
		x = str(self.c.prediction.predict([3,3,2,2,0,0])[0])
		self.assertEqual(x, 'unacc', "Incorrect Prediction")

	def test_not_none(self):
		self.assertIsNotNone(self.c.prediction, "Prediction Empty")
		self.assertIsNotNone(self.c.unacc, "Unacceptable Empty")
		self.assertIsNotNone(self.c.acc, "Acceptable Empty")
		self.assertIsNotNone(self.c.good, "Preferred Empty")
		self.assertIsNotNone(self.c.vgood, "Optimal Empty")
	
	def test_data_in(self):
		self.assertIn('acc', self.c.df['decision'].tolist(), "Valid data missing")
	
	def test_data_not_in(self):
		self.assertNotIn('ac', self.c.df['decision'].tolist(), "Invalid data present")

def tester(car_evaluation):
	# find all tests in this module
	test_loader = unittest.TestLoader()
	test_names = test_loader.getTestCaseNames(TestResult)
	suite = unittest.TestSuite()
	for test_name in test_names:
		suite.addTest(TestResult(test_name, car_evaluation))
	with io.StringIO() as buf:
		# run the tests
		with contextlib.redirect_stdout(buf):
			unittest.TextTestRunner(stream=buf).run(suite)
		# process (in this case: print) the results
		return buf.getvalue()