import nltk
from nltk.stem import PorterStemmer
import sys 

# 下载 Porter Stemmer 的数据
#nltk.download('punkt')

# 创建 Porter Stemmer 的实例
stemmer = PorterStemmer()

# 读取文件中的所有单词
with open(sys.argv[1], 'r') as f:
    words = f.read().split()

# 提取每个单词的词根部分
stems = [stemmer.stem(word) for word in words]

stems = list(set(stems))
stems = sorted(stems)

# 将词根部分保存到一个新文件中
with open(sys.argv[2], 'w') as f:
    f.write('\n'.join(stems))