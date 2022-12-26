import io
import sys


def salute(name):
    """Says hi to someone."""
    print('Hi, {}!'.format(name))

text_trap = io.StringIO()
sys.stdout = text_trap

# execute our now mute function
salute('Anne')

# now restore stdout function
sys.stdout = sys.__stdout__

salute('Markel')

