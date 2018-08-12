
def RULE_MATCH(log):
	result = False
	
	if "userimport" in log["content"]:
		result = True
	return result
	
def RULE_ACTION(log):
	print(log["line"], "\t", log["content"].strip())