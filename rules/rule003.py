
def RULE_MATCH(log_obj):
	result = False
	
	if "deadlock" in log_obj["content"]:
		result = True
	return result
	
def RULE_ACTION(env_obj, rule_obj, log_obj):
	print(log_obj["line"], "\t", log_obj["content"].strip())