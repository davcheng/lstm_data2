import subprocess
from subprocess import PIPE, Popen

word_list = ['great', 'good', 'love', 'works', 'price', 'excellent', 'fast', 'nice', 'fair', 'far', 'perfect', 'easy', 'best', 'well', 'awesome', 'amazing', 'happy', 'everything']


def main(word):
	generated_result = subprocess.Popen(['python', 'sample.py', '--prime', word], stderr=subprocess.STDOUT, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	out = generated_result.communicate()[0]
	print out
	write_to_file(out)
#	cleanse("generated_list.txt")

def write_to_file(text):
	with open("generated_list.txt", "a") as output_file:
		output_file.write(text)
		# output_file.write("\n")


def cleanse(file):
        input = open(file, "r")
        for line in input:
            if not line.startswith('I') and not line.startswith('Total') and not line.startswith('Free') and not line.startswith('pci') and not line.startswith('major') and not line.startswith('name'):
                with open("cleansed_generated_list.txt", "a") as output_file:
                        output_file.write(line)


if __name__ == "__main__":
	for x in word_list: 
		for y in xrange(5):
			main(x)
	cleanse("generated_list.txt")
