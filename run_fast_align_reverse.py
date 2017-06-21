import os,sys

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "run_fast_align.py merge_file alignment_out prob_out"
		exit()

	os.system("fast_align -i %s -d -o -v -s -r -p %s > %s"%(sys.argv[1],sys.argv[3],sys.argv[2]))

