# BM25 Example

I based this example on the YouTube video - [How to Create a BM25 Index in Python with Rank BM25 (Search Engine)](https://www.youtube.com/watch?v=ysvpxiPAHLg). The example uses the [rank_bm25](https://github.com/dorianbrown/rank_bm25) Python library.

## What is BM25

BM25 is a formula used by search engines to figure out which documents are most relevant to a search query. BM25 looks at things like how often the words in the query appear in a document and how common those words are across all documents

## Example in Python

### Install rank_bm25 library

The [rank_bm25](https://github.com/dorianbrown/rank_bm25) Python library makes is easy to implement BM25 algorithms in Python

```pip install rank_bm25``` or in a Juypter notebook run ```!pip install rank_bm25```

To confirm that the installation was successful import the BM250kapi item from the rank_bm25 library run

```from rank_bm25 import BM250kapi```

### Create corpus of documents

In this example we have a corpus of 3 documents

```
corpus = [
  "Hello there good man!",
  "It is quite windy in Londong",
  "How is the weather today?"
]
```

### Tokenize each document

Tokenization breaks down sentences into individual words. Each work is a token. Tokenization is an important preprocessing step because BM25 operates on the level of individual tokens

The code below tokenizes each document by breaking each sentence into a list of words

```
tokenized_corpus = []
for doc in corpus:
  doc_tokens = doc.split()
  tokenized_corpus.append(doc_tokens)
```

If you print the tokenized_corpus. The tokenized_corpus would looke like 

```
print(tokenized_corpus)

---- result below ----

[['Hello', 'there', 'good', 'man!'],
 ['It', 'is', 'quite', 'windy', 'in', 'London'],
 ['How', 'is', 'the', 'weather', 'today?']]
```

### Create object from tokenized document corpus

``` bm25 = BM250kapi(tokenized_corpus) ```


