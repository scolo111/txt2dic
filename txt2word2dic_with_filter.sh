#!/bin/bash
out=./OUTPUT

rm $out/*

chmod +x ./Script/txt2word.py
cat ./INPUT/*.txt > $out/input.txt
./Script/txt2word.py   $out/input.txt  $out/words.txt

#uniq -c 按照频率排序，每行 频率 单词
#sort 第一列(-k1)的数字形式(-n)的变量进行逆序(-r 从大到小)排列 , -k2表示在前面的排序基础上对重复次数一致的单词进行按字母顺序的排列
#head -n5000取前5000行
#tr -s把连续匹配的换成换行
uniq -c $out/words.txt | sort -k1nr -k2 | tr -d "[0-9 ]" | sort -u > ./$out/words_sorted.txt

egrep "^\w+" reference/CET_4+6_edited.txt -o | sort -u  > $out/ref.txt

python3 Script/stemmer.py $out/words_sorted.txt $out/stems.txt 

diff  $out/ref.txt $out/stems.txt | grep -E "^>" | sort -u | cut -c3- > $out/output_without_cet.txt

echo "Complete"
wc -l $out/*