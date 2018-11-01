import numpy as np
from ..search import search

files = ['../../data/spec-4055-55359-0001.fits',
         '../../data/spec-4055-55359-0006.fits',
         '../../data/spec-4055-55359-0010.fits',
         '../../data/spec-4055-55359-0012.fits']

def test_search_return():
    '''test the search returns a list of strings'''
    result = search(files, 'ra', 0, 360)
    assert isinstance(result, (list,)), 'Your search is not returning a list.'

def test_search_return2():
    '''test the search returns a list of strings'''
    result = search(files, 'dec', -180, 180)
    assert isinstance(result, (list,)), 'Your search is not returning a list.'
    
def test_search_return3():
    '''test that spectrum_search returns a list'''
    result = search(files, 'ra', 0, 360)
    assert np.all([(r in files) for r in result]), 'Your file is not in the given files.'
    #assert result[0] in files, 'Your file is not in the given files.'
    
def test_search_return4():
    '''test that spectrum_search returns a list'''
    result = search(files, 'ra', -1e10, 1e10)
    assert len(result) == len(files), 'The search is not returning everything it is meant to.'
    
def test_search_return5():
    '''test that spectrum_search returns a list'''
    result = search(files, 'dec', -1e10, 1e10)
    assert len(result) == len(files), 'The search is not returning everything it is meant to.'
    
