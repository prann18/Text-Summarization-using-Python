# 📝 Text Summarization Project - V2 

## 📌 Overview
This project implements an **extractive text summarization pipeline** in Python.
It reads text from different file formats (`.txt`, `.docx`, `.pdf`), computes sentence similarities, and selects the most important sentences using a graph-based ranking approach.
The summarizer can be used for research papers, project proposals, or any long-form document to quickly extract the main points.
--------------------------------------------------------------------------------------
## ⚙️ Features

* Reads text from **multiple file formats**:
  * `.txt`
  * `.docx`
  * `.pdf`
  
* **Preprocessing**:
  * Sentence tokenization (NLTK)
  * Normalization (lowercasing, stopword removal)

* **Sentence Similarity**:
  * Cosine similarity on tokenized sentences
    
* **Graph-based Ranking**:
  * Build similarity matrix
  * Apply ranking (PageRank / MMR)

* **Anti-redundancy filtering** with tunable λ parameter
* Summarization with **user-defined number of sentences**
* Visualization of sentence graph
--------------------------------------------------------------------------------------
## 🏗️ Project Structure

Main functions defined in the notebook:
* `read_file(path)` → Read `.txt`, `.docx`, `.pdf` files
* `_normalize_sentence(sentence)` → Clean & tokenize sentences
* `_sentence_similarity(s1, s2, stop_words)` → Compute similarity between two sentences
* `_build_similarity_matrix(sentences, stop_words)` → Build matrix for ranking
* `mmr_rank(indices, sentences, sim_mat, top_n, lambda_)` → Maximal Marginal Relevance ranking
* `summarize(text, top_n, language)` → Summarize given text
* `summarize_from_file(path, top_n, language)` → Convenience wrapper for files
* `plot_summary_graph_pretty(...)` → Visualize similarity graph
* `summary_stats(text, summary)` → Report summary statistics
--------------------------------------------------------------------------------------
## 🚀 Usage

### 1️⃣ Install dependencies
```bash
pip install nltk python-docx PyPDF2 networkx numpy matplotlib
```

### 2️⃣ Run the notebook
Open `TextSummarization.ipynb` in Jupyter Notebook or JupyterLab.

### 3️⃣ Summarize a document
```python
(text, results) = summarize_from_file("Project_Proposal.docx")

summary, sentences, graph, scores, ranked_ind, sim_mat = results
print("\n".join(summary))
```
You’ll be prompted to enter the number of sentences for the summary if not provided.
--------------------------------------------------------------------------------------
## 🔮 Future Improvements
* Add support for `.csv` and `.xlsx` files
* Improve similarity calculation with word embeddings (Word2Vec, BERT)
* Implement abstractive summarization
* Deploy as a web app with Flask/Streamlit
--------------------------------------------------------------------------------------
## 👩‍💻 Author: Swamini Sontakke, Pranali Jamdade

Developed as part of a **volutary project** for exploring NLP techniques Pune University.
