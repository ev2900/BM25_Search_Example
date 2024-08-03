# BM25 Example

<img width="85" alt="map-user" src="https://img.shields.io/badge/views-1304-green"> <img width="125" alt="map-user" src="https://img.shields.io/badge/unique visits-711-green">

I based this example on the YouTube video - [How to Create a BM25 Index in Python with Rank BM25 (Search Engine)](https://www.youtube.com/watch?v=ysvpxiPAHLg). The example uses the [rank_bm25](https://github.com/dorianbrown/rank_bm25) Python library.

## What is BM25

BM25 is a formula used by search engines to figure out which documents are most relevant to a search query. BM25 looks at things like how often the words in the query appear in a document and how common those words are across all documents

## Example in Python

### Install rank_bm25 library

The [rank_bm25](https://github.com/dorianbrown/rank_bm25) Python library makes is easy to implement BM25 algorithms in Python

```pip install rank_bm25``` or in a Juypter notebook run ```!pip install rank_bm25```

To confirm that the installation was successful import the BM250kapi item from the rank_bm25 library run

```from rank_bm25 import BM25Okapi```

### Create corpus of documents

In this example we have a corpus of 3 documents

```
corpus = [
  "Hello there good man!",
  "It is quite windy in London",
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

### Create a BM25 index from the tokenized document corpus

``` bm25 = BM25Okapi(tokenized_corpus) ```

### Query the BM25 index

We can search for *windy London* . The document *It is quite windy in London* should be returned as the most relevant match to our search.

```
query = "windy London"
tokenized_query = query.split(" ")

doc_scores = bm25.get_scores(tokenized_query)
print(doc_scores)

---- result below ----

[0, 0.937, 0]
```

The ```get_scores``` method returns a score of how relevant each document is to the query. A score of 1 is very relevant a score of 0 is not relevant. Notice the second sentence in our document corpus has the highest score. This makes sense given the second sentence in our corpus is *It is quite windy in London* and our query is *windy London*

We can use the  ```get_top_n``` method to return the top relevant documents as opposed to just the relevancy scores the ```get_scores``` method returns

```
doc = bm25.get_top_n(tokenized_query, corpus, n=1)
print(doc)

---- result below ----

['It is quite windy in London']
```
