# Shuffled AES (S-AES) using Python

Implemention of a shuffed version of AES (S-AES), which is similar to AES but with an extra 128-bit key (shuffing key, SK).
S-AES operates as AES, but with one modified round. That round is pseudo-randomly selected with SK, and exclusively among the first 9 (encryption) rounds.

The modified round operates as follows:
- In the AddRoundKey step, the SK is used to rotate the bytes of the Round Key used in this round.
- The S-Box used in the SubBytes step is a shuffled variant of the original S-Box wich depends on the SK. The shuffling is done using a variation of the Fisher–Yates shuffle Algorithm.
- In the ShiftRows step, the byte shifts applied to each row are permuted with the SK.
- In the MixColumns step, the SK is used to add an offset to the index used to select the column in one of the matrices.

If a SK is not used, the program operates with the normal AES.

---
The required files are:
- SAES.py (library)
- encrypt.py
- decrypt.py
- speed.sh

---
To encrypt something, use:
```shell
echo some_plain | python3 encrypt.py [--timeit] key [skey]
```

To decrypt something, use:
```shell
echo some_cipher | python3 decrypt.py [--timeit] key [skey]
```

To test the performance (will take long), run:
```shell
chmod +x speed.sh
./speed.sh > times/overall_100k_best_times.txt
```
---

To check the profiler results (need to install snakeviz), run:
```shell
snakeviz profiler/<profiler_file>
```

To run any test, do:
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```