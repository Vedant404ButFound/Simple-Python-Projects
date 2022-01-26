import hashlib

passl = int(input("Tell me your password length : "))
passw = input("Enter password hash : ")

for i in range(int("1"+"0"*passl)):
	i = str(i).rjust(passl,"0")
	passhash = hashlib.sha1(i.encode()).hexdigest()+hashlib.md5(i.encode()).hexdigest()
	if passhash == passw:
		print(f"\n=====================\nYour password is {i}\n=====================")