# You should observe the Python PEP 8 recommendation on named constants.
#  - The name should be capitalized.
#  - The variable should be at "module scope", meaning that it is visible and
#    usable in all the functions in this file.  You can accompish this by placing
#    the variable at the start of the file, before any function.
#
#    This means the variable will be set only once, when the file is imported.
#    If the variable is in a function, it will be set everytime the function is
#    called.

def fen(s):
    '''
    Your docstring goes here.
    '''
    pass

#---------------------------------------------------------------------------------------------------------------
# Test code for pytest.
# You would be wise to create test instances of your own.

    def test_01(self):
        ans = '8  r  .  .  .  .  .  .  .\n7  .  p  .  .  .  p  k  .\n6  p  .  .  p  b  .  .  r\n5  .  .  p  .  p  .  p  .\n4  .  .  P  b  P  .  p  .\n3  .  N  .  Q  .  .  P  .\n2  P  P  .  .  .  P  P  .\n1  .  R  R  .  .  .  K  .\n   a  b  c  d  e  f  g  h'
        b = 'r7/1p3pk1/p2pb2r/2p1p1p1/2PbP1p1/1N1Q2P1/PP3PP1/1RR3K1'
        board = fen.fen(b)
        assert board == ans

#---------------------------------------------------------------------------------------------------------------
# Pure python test code.
# You would be wise to create test instances of your own.

if (__name__ == '__main__'):
    ans = '8  r  .  .  .  .  .  .  .\n7  .  p  .  .  .  p  k  .\n6  p  .  .  p  b  .  .  r\n5  .  .  p  .  p  .  p  .\n4  .  .  P  b  P  .  p  .\n3  .  N  .  Q  .  .  P  .\n2  P  P  .  .  .  P  P  .\n1  .  R  R  .  .  .  K  .\n   a  b  c  d  e  f  g  h'
    b = 'r7/1p3pk1/p2pb2r/2p1p1p1/2PbP1p1/1N1Q2P1/PP3PP1/1RR3K1'
    board = fen.fen(b)
    assert board == ans
