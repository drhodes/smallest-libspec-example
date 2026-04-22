"""
smallest example
"""

from libspec import Spec
from . import app

class SmallestExample(Spec):
    def modules(self):
        return [app]

if __name__ == "__main__":
    SmallestExample().write_xml("spec-build")
    
