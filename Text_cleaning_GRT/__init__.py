from Text_cleaning_GRT import utils

___version___ = '0.0.1'

def get_wordcounts(x):
	return utils._get_wordcounts(x)

def get_charcounts(x):
	return utils._get_charcounts(x)

def get_avg_wordlength(x):
	return utils._get_avg_wordlength(x)

def get_stopwords_counts(x):
	return utils._get_stopwords_counts(x)

def get_urls(x):
	return utils._get_urls(x)	

def remove_urls(x):
	return utils._remove_urls(x):
	
def remove_special_chars(x):
	return utils._remove_special_chars(x):		

def remove_html_tags(x):
	return utils._remove_html_tags(x)
	
def remove_accented_chars(x):
	return utils._remove_accented_chars(x)

def remove_stopwords(x):
	return utils._remove_stopwords(x)
	
def remove_short_long_words(x):
    return str(utils._remove_short_long_words(x))

def lemmatize(x):
    return str(utils._lemmatize(x))

def preprocess_data(x):
    return utils._preprocess_data(x)