---
marp: true
theme: leet
---

# crypto

- ancient ciphers
- xor
- rsa basics
- aes basics
- signatures?
- dh kex?

---

- motivation
- goals
  - encrypt network traffic
  - encrypt messages
  - encrypt data at rest
  - maintain integrity
  - allow verifying properties (zk)
  - digital signatures
  - …
- politics and controversy

<!-- plug hist 449 -->

---

![munitions t-shirt](https://upload.wikimedia.org/wikipedia/commons/9/96/Munitions_T-shirt_%28front%29.jpg)

---

> never roll your own crypto*
>   —folk wisdom

---

## ancient ciphers

- caesar cipher
- substitution cipher
- …

---

## xor

$$0 \oplus 0 = 0$$
$$0 \oplus 1 = 1$$
$$1 \oplus 0 = 1$$
$$1 \oplus 1 = 0$$

---

### xor properties

$$x \oplus x = 0$$
$$x \oplus y = y \oplus x$$
$$(x \oplus y) \oplus z = x \oplus (y \oplus z)$$
$$(x \oplus y) \oplus y = x$$

---

### basic xor ciphers

- single-byte xor
- repeating key xor
- one-time pad

---

## rsa

public-key cryptography

- alice wants to send bob a message
- alice uses bob's public key $(n, e)$ and encrypts the message
- only someone with the corresponding private key $(n, d)$ will be able to decrypt it

advantage: no need to already have a shared secret

---

- $n = pq$
- $e = \dots$ (coprime to $\lambda = (p - 1)(q - 1)$)
- $d = e^{-1} \pmod{\lambda}$

public key: $(n, e)$

private key: $(n, d)$

- $c = m^e \mod n$
- $m = c^d \mod n = {(m^e)}^d \mod n = m^{ed} \mod n = m \mod n$

---

### repeated plaintext under naive rsa

$$c_1 = m^e \mod n_1$$
$$c_2 = m^e \mod n_2$$
$$c_3 = m^e \mod n_3$$

can use the chinese remainder theorem to find $m^e$. next, for small $e$ we can just take the $e$-th root.

---

## demo: sha256 rainbow table

```sh
cat students.json | jq -r '.[].name' | while read name
    echo $name '=' (echo -n $name | tr '[:upper:]' '[:lower:]' | sha256sum)
end
```

---

## diffie-hellman key exchange

share a common secret over an insecure channel

principle: dlp hard

variants used in tls.

---

- public params: $p, g$
- private params
  - alice's $a$
  - bob's $b$
- alice calculates $A$ based on $g$ and $a$; sends it to bob
- bob calculates $B$ based on $g$ and $b$; sends it to alice
- alice combines $B$ and $a$ to get shared $k$
- bob combines $A$ and $b$ to get shared $k$

---

$$A = g^a \mod{p}$$
$$B = g^b \mod{p}$$
$$B^a \mod{p} = A^b \mod{p} = g^{ab} \mod{p}$$

---

## aes

- block cipher (block size 128)
- symmetric-key
- key size ∈ {128, 192, 256}
- "pretty good" (?)

---

### aes modes of operation

- ecb
- cbc
- …
- ctr

---

### ecb
