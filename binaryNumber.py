#-------------------------------------------------------------------------------
# Name:        binaryNumber.py
# Purpose:  A linked list implementation of a binary number.
#
# Author:      Assignment concept by pearcej, converted to Python by nakazawam
#
# Created:     21/09/2014
#-------------------------------------------------------------------------------

from bit import Bit

class BinaryNumber(object):

    #------------------------------------------------------------

    def __init__( self ):
        '''Initialize this binary number is empty  with no bits in it.'''
        self.leastSignificantBit = None
        self.numBits = 0

    def __len__(self):
        '''post: returns number of items in the list'''
        return self.numBits

    def get_least_significant_bit( self ):
	    return self.leastSignificantBit

    def convert_decimal_to_binary( self, decimal ):
        '''pre: The decimal input >= 0, leastSignificantBit = None
            If there IS a number in this object already, it will be clobbered.
        post: leastSignificantBit will point to the first link
        of a linked list representing the "decimal" number in reverse
        order (least to most significant bit)'''

        if( decimal < 0 ):
            return

        # Now use an algorithm to convert a decimal number to binary.
        # Repeatedly divide the number by 2 and keep the remainder.
        # It will build the binary number this way.

        # Start the process with the first binary number.
        if decimal%2 == 1:
            self.leastSignificantBit = Bit(True)
        else:
            self.leastSignificantBit = Bit(False)
        self.numBits += 1

        # Now loop through the decimal and convert to binary.
        bitRef = self.leastSignificantBit
        remainder = 0
        quotient = decimal // 2 # needs to be integer division

        while quotient > 0:
            remainder = quotient % 2
            quotient = quotient // 2 # needs to be integer division

            bitRef.add_next_bit( remainder == 1 )
            bitRef = bitRef.get_next_bit()	# Advance the reference
            self.numBits += 1

    def __str__( self ):
        ''' returns the string representation of this binary number.
        post: The string representation of this BinaryNumber will be returned.
            if there is no linked list, a blank string, "" is returned '''
        bitRef = self.leastSignificantBit
        output = ""

        if( bitRef == None ):
            return output

        for i in range(self.numBits):
            output = str(bitRef)+output
            bitRef = bitRef.get_next_bit()
        return output

    def remove_all( self ):
        '''pre: none
        post: All the links in the linked list started by leastSignificantBit
            will be de-allocated.'''

        if( self.leastSignificantBit == None ):
            return

        trailingBit = self.leastSignificantBit
        leadingBit = trailingBit.get_next_bit()

        for i in range(self.numBits-1):
            trailingBit.clear_next_bit()
            trailingBit = leadingBit
            leadingBit = leadingBit.get_next_bit()

        self.leastSignificantBit = None
        self.numBits = 0

    def increment( self ):
        '''TODO'''
        # You are to implement this function that will increment the binary
        # number stored in a linked list by one, making sure to propogate any
        # carries that are generated.

        # For example, if the number 15 is stored as "1111" and this
        # function is called,the result would be "10000" (really
        # represented as 0->0->0->0->1, where the carry "rippled" up the
        # bits, and an additional bit was added at the end because the 4th
        # 1 really became a "10"

        pass


    #------------------------------------------------------------


##     def __iter__(self):

##         # generator version works in both Python2 and Python3
##         node = self.head
##         while node is not None:
##             yield node.item
##             node = node.link

    #------------------------------------------------------------

    def __iter__(self):

        return BNIterator(self.head)

#------------------------------------------------------------

class BNIterator(object):

    #------------------------------------------------------------

    def __init__(self, head):
        self.currnode = head

    #------------------------------------------------------------
    # Python2 version
    def next(self):
        if self.currnode is None:
            raise StopIteration
        else:
            item = self.currnode.item
            self.currnode = self.currnode.link
            return item

    #------------------------------------------------------------
    # Python3 version
    def __next__(self):
        if self.currnode is None:
            raise StopIteration
        else:
            item = self.currnode.item
            self.currnode = self.currnode.link
            return item
