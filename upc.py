import crypt

def testPass(cryptPass):
	salt = cryptPass[0:2]

dictFile = open('dictionary.txt','r')

for word in dictFile.readline():
	word = word.strip('\n')
	cryptWord = crypt.crypt(word,salt)
	if (cryptWord == cryptPass):
		print('found password: ')+ word + '\n'
	else:
		print('password not found ')+ '\n'

def main():
	passFile = open('passwords.txt')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(":")[0]
			cryptPass = line.split(":")[1].strip('')
			print ("cracking password for: ")+user
			testPass(cryptPass)

if __name__=="__main__":
	main()