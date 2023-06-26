import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import sys 
# 读取文本文件
with open(sys.argv[1], 'r') as f:
    text = f.read()

# 将文本转换为小写，并进行分词
tokens = set(word_tokenize(text.lower()))
print(word_tokenize(text.lower()))
# 去cet4—6
with open('reference/CET_4+6_edited.txt', 'r') as f:
    text = f.read()
cet_words = set(word_tokenize(text.lower()))
print (len(cet_words))

# 过滤停用词、标点符号等无关词汇，并进行词干化处理
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
print (len([lemmatizer.lemmatize(word) for word in tokens if word.isalpha() and word not in stop_words]))
print (len([lemmatizer.lemmatize(word) for word in tokens if word.isalpha() and word not in stop_words and word not in cet_words]))

filtered_tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalpha() and word not in stop_words and word not in cet_words] 

# 去重
unique_tokens = set(filtered_tokens)

# 将单词保存到新文件中
with open(sys.argv[2], 'w') as f:
    for word in unique_tokens:
        f.write(word + '\n')