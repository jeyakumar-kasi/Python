import os


class FileMatcher:
	def _init_(self):
		self.max_count = 100
		
	def matchFileContents(self, filepath1, filepath2):
		with open(filepath1) as fh1:
			with open(filepath2) as fh2:
				
				for lineno1, line1 in enumerate(fh1.readlines(), 1):
					for lineno2, line2 in enumerate(fh2.readlines(), 1):
						if line1 != line2:
							# not matched
							print(line2)
	
	def matchFileNames(self, filepath1, filepath2):
		total = 0
		is_more = False
		missing_count = 0
		for root, dirs, files in os.walk(filepath1):
			if files:
				#filedir = os.path.dirname(os.path.join(root, files[0]))
				
				tmp_files = os.listdir(os.path.dirname(filepath2))
				for file in files:
					total += 1
					if file not in tmp_files:
						missing_count += 1
						filepath = os.path.join(root, file)
						print(f"{missing_count:>3} Missing <{filepath}>")
					# else:
					#	print(f"    [OK]    <{filepath}>")	
					
					if total >= self.max_count :
						is_more = True
						break
		if not is_more:		
			print(f"Total files: {total}")
		else:
			print(f"({self.max_count}+ more)..")
		
							
	def compare(self, filepath1, filepath2):
		if os.path.isfile(filepath1):
			return self.matchFileContents(filepath1, filepath2)
																		
		# Directory match
		return self.matchFileNames(filepath1, filepath2)
							
							
if _name_ == "_main_":
	filepath1 = r"/storage/emulated/0/Android"
	filepath2 = r"/storage/emulated/0/DCIM"
	
	
	fileMatcher = FileMatcher()
	fileMatcher.compare(filepath1, filepath2)
	
	# print(os.path.dirname(filepath2))
	# tmp_files = os.listdir(os.path.dirname(filepath2))
	# print(tmp_files)