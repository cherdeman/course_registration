# Utility functions
from datetime import datetime

def current_term():
	year = datetime.now().year
	month = datetime.now().month
	if month < 7:
		term = "spr"
	else:
		term = "fall"

	return term + str(year)