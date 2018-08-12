
def RULE_MATCH(log_obj):
	result = False
	
	if "Locked" in log_obj["content"]:
		result = True
	return result
	
def RULE_ACTION(env_obj, rule_obj, log_obj):
	print(log_obj["line"], "\t", log_obj["content"].strip())
	rule_name = rule_obj["name"]
	log_line = str(log_obj["line"])
	env_obj[rule_name + "_" + log_line]={"rule": rule_obj, "log": log_obj}

def RULE_END(log):
	a=1+1