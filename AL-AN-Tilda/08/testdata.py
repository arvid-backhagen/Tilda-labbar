from lab8 import *
import unittest

class Test(unittest.TestCase):

	def testMolekyl(self):

		self.assertEqual(checksyntax("H"), "Följer syntaxen!")
		
		self.assertEqual(checksyntax("Ha2"), "Följer syntaxen!")
		self.assertEqual(checksyntax("H2"), "Följer syntaxen!")
		self.assertEqual(checksyntax("Ha"), "Följer syntaxen!")
		self.assertEqual(checksyntax("1"), "Följer inte syntaxen!")
		self.assertEqual(checksyntax("aa"), "Följer inte syntaxen!")
		self.assertNotEqual(checksyntax("c"), "Följer syntaxen!")

	def testAtom(self):

		self.assertEqual(checksyntax("HH"), "Följer inte syntaxen!")
		self.assertEqual(checksyntax("a"), "Följer inte syntaxen!")
		self.assertEqual(checksyntax("H"), "Följer syntaxen!")
		self.assertEqual(checksyntax("Hh"), "Följer syntaxen!")
		self.assertNotEqual(checksyntax("H"),"Följer inte syntaxen!")
		

if __name__ == '__main__':
	unittest.main()
