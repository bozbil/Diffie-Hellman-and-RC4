# Lab Assignment
Suppose that user A wishes to set up a connection with user B and use a
secret key to encrypt messages on that connection. The two users, each is
going to generates a one-time private key and calculates a public key. These
public values, together with global public values for q and a, are stored in
some central directory. Write a program in python and address the following
requirements:


- Generate two random numbers as the one-time private keys for users A
and B using combined linear congruential generator considering 


```bash
m1=2,147,483,563
a1= 40,014
m2= 2,147,483,399
a2= 20,692 
(for a new connection, a new private key should be be generated)
```



- Using the Diffie-Hellman algorithm and the private keys generated in (a),
generate the secret key for users A and B.
- Suppose that user A wishes to send a text file to user B. Break the
plaintext into 128 bits blocks and encrypt the last 128 bits block of the
plaintext based on RC4 algorithm using the secret key generated in (b).
- Decrypt the encrypted message generated in (c) for user B using the
secret key.
