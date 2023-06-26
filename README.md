# 说明
1. python脚本参考自(https://github.com/cndaqiang/txt2dic)<br>
2. 此程序目的在于提取相关专业文献中的单词，导入欧陆词典生词本进行背诵，再看文献时能减少自己的生词数
3. 新增 txt2word2dic_with_filter.sh 
- 过滤 cet4+6 的单词库
- 过滤重复词干
- 依赖 python 库 nltk 
- 依赖  [Punkt Tokenizer Models](https://www.nltk.org/nltk_data/)<br>库，解压缩到根目录

## 结构
```
.
├── INPUT
│   ├── VASP the GUIDE.txt
│   ├── example_UTF8.txt
│   └── html
│       ├── VASP the GUIDE.html
│       └── example.html
├── OUTPUT
│   ├── input.txt               # all txt merged from INPUT
│   ├── output_without_cet.txt  # output without cet4+6 
│   ├── ref.txt                 
│   ├── stems.txt               
│   ├── words.txt
│   └── words_sorted.txt
```
## 使用
1. 使用Adobe DC等程序将文献pdf导出为txt格式<br>
2. 使用记事本打开,另存为UTF8编码(Adobe DC可以直接导出UTF8编码的txt)<br>
3. 原始txt还可以来自网页等多种格式,最后保存或转码成UTF8的txt都可以
3. 将文件保存到./INPUT目录<br>
4. 运行`txt2word2dic_with_filter.sh`<br>
5. 结果输出在OUTPUT目录<br>
使用欧陆词典网页版在线导入生词



