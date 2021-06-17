from ie_utils import tokenize, remove_punctuation, remove_stopwords
import pytest 

@pytest.mark.parametrize("sentence, expected_tokens",[("first test sentence", ["first","test","sentence"]), ("a word",["a","word"])])
def test_tockenize_returns_expected_token(sentence, expected_tokens):
    tokens = tokenize(sentence)
    
    assert tokens == expected_tokens 
    
@pytest.mark.parametrize("sentence, expected_tokens",[("first test sentence", ["First","test","sentence"]), ("a word",["a","word"])])
def test_tockenize_returns_lower(sentence, expected_tokens):
    tokens = tokenize(sentence)
    for el in range(0, len(expected_tokens)):
        expected_tokens[el] =  expected_tokens[el].lower()
    assert tokens == expected_tokens

@pytest.mark.parametrize("sentence, expected_tokens",[("first . test , sentence !", ["First","test","sentence"])])
def test_tockenize_returns_no_punctation(sentence, expected_tokens):
    tokens = remove_punctuation(sentence)
    for el in range(0, len(expected_tokens)):
        expected_tokens[el] =  expected_tokens[el].lower()
    assert tokens == expected_tokens
    
@pytest.mark.parametrize("sentence, expected_tokens",[("the first test and sentence", ["First","test","sentence"])])
def test_tockenize_returns_no_stopwords(sentence, expected_tokens):
    tokens = remove_stopwords(sentence)
    for el in range(0, len(expected_tokens)):
        expected_tokens[el] =  expected_tokens[el].lower()
    assert tokens == expected_tokens
    
    

    