# BM25 Example

I based this example on the YouTube video - [How to Create a BM25 Index in Python with Rank BM25 (Search Engine)](https://www.youtube.com/watch?v=ysvpxiPAHLg). The example uses the [rank_bm25](https://github.com/dorianbrown/rank_bm25) Python library.

## What is BM25

BM25 is a formula used by search engines to figure out which documents are most relevant to a search query. BM25 looks at things like how often the words in the query appear in a document and how common those words are across all documents.

## Example in Python

### Install rank_bm25 library

The [rank_bm25](https://github.com/dorianbrown/rank_bm25) Python library makes is easy to implement BM25 algorithms in Python.

```pip install rank_bm25``` or in a Juypter notebook run ```!pip install rank_bm25```

To confirm that the installation was successful import the BM250kapi item from the rank_bm25 library run

```from rank_bm25 import BM250kapi```

## Create corpus of documents

```corpus = [
  "Hello there good man!",
  "It is quite windy in Londong",
  "How is the weather today?"
]```

In this example we have a courpus of 3 documents.

## Tokenize each documents in the corpus of documents
