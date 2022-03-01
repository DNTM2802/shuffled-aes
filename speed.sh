for (( i=0; i<100000; i++ ))
do
   # 15 character alphanumeric keys from /dev/urandom
   key=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 15)
   skey=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 15)
   
   # My AES
   dd if=/dev/urandom bs=1 count=4K status=none | base64 | python3 encrypt.py $key --timeit | python3 decrypt.py $key --timeit > /dev/null

   # My SAES
   dd if=/dev/urandom bs=1 count=4K status=none | base64 | python3 encrypt.py $key $skey --timeit | python3 decrypt.py $key $skey --timeit > /dev/null

   # Python Cryptography AES
   dd if=/dev/urandom bs=1 count=4K status=none| base64 | python3 lib_cryptography.py $key
done

# Find the minimum speeds
for f in times/*_times.txt;
do
    min=1000
    type=$(echo $f | cut -d'/' -f 2 | cut -d'_' -f 1-2)
    while IFS= read -r line
    do
        if [[ "$(echo "$line < $min" | bc)" -eq "1" ]]
        then
            min=$line
        fi
    done < "$f"
    echo -e "${type}\t${min}"
done