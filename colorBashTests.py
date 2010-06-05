# coding: utf-8

# version 1.0
# 6.5.2010
# Michal Horejsek

import unittest
from colorBash import *

class ColoredTextTest( unittest.TestCase ):

	def setUp( self ):
		self.coloredText = ColoredText( 'Hello World' )

	def tearDown( self ):
		self.coloredText = ColoredText( 'Hello World' )

	def testColor( self ):
		self.coloredText.setColor( 'green' )
		self.assertEqual( self.coloredText.get(), '\033[0;32mHello World\033[0m' )

	def testBackground( self ):
		self.coloredText.setBackground( 'blue' )
		self.assertEqual( self.coloredText.get(), '\033[44mHello World\033[0m' )

	def testColorAndBackground( self ):
		self.coloredText.set( 'dark black', 'gray' )
		self.assertEqual( self.coloredText.get(), '\033[2;30;47mHello World\033[0m' )

	def testColorBySlice( self ):
		self.coloredText.setColor( 'yellow', slice( 6, 11 ) )
		self.assertEqual( self.coloredText.get(), 'Hello \033[1;33mWorld\033[0m' )

	def testBackgroundBySlice( self ):
		self.coloredText.setBackground( 'purple', slice( 5 ) )
		self.assertEqual( self.coloredText.get(), '\033[45mHello\033[0m World' )

	def testColorAndBackgroundBySlice( self ):
		self.coloredText.setColor( 'dark cyan', slice( 6, 11 ) )
		self.coloredText.setBackground( 'cyan', slice( 8 ) )
		self.assertEqual( self.coloredText.get(), '\033[46mHello \033[2;36;46mWo\033[2;36mrld\033[0m' )

	def testCurrentColor( self ):
		self.coloredText.setColor( 'purple' )
		self.coloredText.setCurrentColor( 'light red' )
		self.assertEqual( self.coloredText.get(), '\033[0;35mHello World\033[1;31m' )

	def testCurrentColorCombinate( self ):
		self.coloredText.setColor( 'black', slice( 2 ) )
		self.coloredText.setColor( 'red', slice( 6, 8 ) )
		self.coloredText.setCurrentColor( 'light red' )
		self.assertEqual( self.coloredText.get(), '\033[0;30mHe\033[1;31mllo \033[0;31mWo\033[1;31mrld' )

	def testCurrentBackground( self ):
		self.coloredText.setColor( 'dark gray' )
		self.coloredText.setCurrentBackground( 'brown' )
		self.assertEqual( self.coloredText.get(), '\033[1;30;43mHello World\033[43m' )

	def testCurrentColorAndBackground( self ):
		self.coloredText.setColor( 'white' )
		self.coloredText.setCurrentColor( 'dark green' )
		self.coloredText.setCurrentBackground( 'black' )
		self.assertEqual( self.coloredText.get(), '\033[1;37;40mHello World\033[2;32;40m' )

	def testBadColor( self ):
		self.assertRaises( ColorError, self.coloredText.setColor, 'color' )

	def testBadBackground( self ):
		self.assertRaises( ColorError, self.coloredText.setBackground, 'dark black' )

	def testBadCurrentColor( self ):
		self.assertRaises( ColorError, self.coloredText.setCurrentColor, 'colour' )

	def testBadCurrentBackground( self ):
		self.assertRaises( ColorError, self.coloredText.setCurrentBackground, 'white' )

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase( ColoredTextTest )
	unittest.TextTestRunner( verbosity=2 ).run( suite )
