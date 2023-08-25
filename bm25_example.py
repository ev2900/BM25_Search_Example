from rank_bm25 import BM25Okapi

# Create corpus of documents
corpus = [
  "Hello there good man!",
  "It is quite windy in London",
  "How is the weather today?"
]

# Tokenize each document
tokenized_corpus = []
for doc in corpus:
  doc_tokens = doc.split()
  tokenized_corpus.append(doc_tokens)

#print(tokenized_corpus)

# Create a BM25 index from the tokenized document corpus
bm25 = BM25Okapi(tokenized_corpus)

# Query the BM25 index
query = "windy London"
tokenized_query = query.split(" ")

#doc_scores = bm25.get_scores(tokenized_query)
#print(doc_scores)

doc = bm25.get_top_n(tokenized_query, corpus, n=1)
print(doc)
