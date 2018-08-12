import sys
import json
import os
import importlib

def apply_rules(log, json_obj):
	for item in json_obj:
		mod_en = item["enable"]
		mod_name = item["name"]
		mod_repo = item["repo"]
		if(mod_en == 1):
			mod = importlib.import_module(mod_repo + "." + mod_name)
			if mod.RULE_MATCH(log):
				if mod.RULE_ACTION:
					mod.RULE_ACTION(log)
				#if mod.RULE_END:
				#	mod.RULE_END(log)

def loadJson2Obj(json_file):
	data = None
	with open(json_file) as fd:
		data = json.load(fd)	
	return data
	
def load_log_with_json(log_file, json_obj):
	line_index = 1
	with open(log_file, 'r', encoding='UTF-8') as in_file:
		for line in in_file:
			log = {}
			log["filename"] = log_file
			log["line"] = line_index
			log["content"] = line
			apply_rules(log, json_obj)
			#if (line_index % 1000) == 0 :
			#	print(line_index)
			line_index+=1

def load_log_with_line_index(log_file, start_index, end_index):
	line_index = 1
	with open(log_file, 'r', encoding='UTF-8') as in_file:
		for line in in_file:
			if(line_index >= start_index) and (line_index <= end_index):
				print(line)
			line_index += 1

def help():
	print("parser_main <ops> ...")
	print("  ops : compare, lines")
	print("    parser_main compare <log_file> <json_rule> ")
	print("    parser_main line <log_file> <start_index> <end_index>")
	sys.exit(1)
	
if __name__ == '__main__':

	if len(sys.argv) < 3 :
		help()
	
	ops = sys.argv[1]
	log_file_path = sys.argv[2]

	if ops == "compare" :
		json_cfg = sys.argv[3]
		json_obj = loadJson2Obj(json_cfg)
		load_log_with_json(log_file_path, json_obj)
	if ops == "line" :
		start_index = int(sys.argv[3])
		end_index =  int(sys.argv[4])
		load_log_with_line_index(log_file_path, start_index, end_index)
