
def RULE_MATCH(log):
	result = False
	
	if "Locked" in log["content"]:
		result = True
	return result
	
def RULE_ACTION(log):
	print(log["line"], "\t", log["content"].strip())

def RULE_END(log):
	a=1+1