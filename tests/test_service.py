from src.service import *
def test_generation():
 o=VisualAidService().generate(Request('deep breathing')); assert len(o['image_id'])==16 and o['latency_ms']>=0
def test_empty():
 import pytest
 with pytest.raises(ValueError): VisualAidService().generate(Request('  '))
