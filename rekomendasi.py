# PACKAGES
import nltk #untuk tokenisasi
import re # mendeteksi karakter selain huruf dan angka kemudian dihilangkan
import numpy as np #cosine similiarity
from gensim import corpora, similarities 
from gensim.models import LsiModel #perhitungan LSI
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory #menghilangkan kata yang tidak bermakna
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory #mengubah ke kata dasar 
import sys
import warnings
import sqlite3 #database
from gensim.models import TfidfModel #tfidf

if not sys.warnoptions:
    warnings.simplefilter("ignore")
# FUNCTIONS

# inisialisasi function/ set stopword set, word stemmer and word tokenizer
word_tokenizer = nltk.tokenize.WordPunctTokenizer()
factory = StemmerFactory()
word_stemmer = factory.create_stemmer()
factory = StopWordRemoverFactory()
stopword_remover = factory.create_stop_word_remover()

# function untuk preprocessing
def filter_words_and_get_word_stems(document,
                                    word_tokenizer,
                                    word_stemmer,
                                    stopword_remover,
                                    pattern_to_match_words=r"[^\w]",
                                    word_length_minimum_n_chars=2):
 
    document = re.sub(pattern_to_match_words, r" ", document) #selain huruf dan angka diganti spasi
    document = re.sub(r"\s+", r" ", document) #selain huruf dan angka maka diganti dengan spasi
    # diproses dgn stopword remover(menghilangkan kata tak bermakna)diletakan di word filtered
    words_filtered = stopword_remover.remove(document) 
    word_stems = word_stemmer.stem(words_filtered) #nilai dari word filtered di proses dengn stemmer untuk mengembalikan ke kata dasar
    words = word_tokenizer.tokenize(word_stems) #nilai dari word stems diproses dengan tokenizer untuk menjadikan kalimat pertoken
    return (words) #setelah diproses nilai words akan dikembalikan


#function recommender dengan parameter query. query adalah pesan yang dikirim oleh pengguna line
def recommender(query):
    conn = sqlite3.connect('/var/www/helloworld/db_buku.db') #koneksi ke database

    
    cursor = conn.execute("SELECT id, judul, penulis, teks from BUKU")
    data = list(cursor)

    #data buku dimasukan ke document train
    documents_train =  [each_list[3] for each_list in data]
    judul_buku = [each_list[1] for each_list in data]
    conn.close()
    # print(documents_train)
    # print('\n')
    # print(judul_buku)

    # variabel document test di isi dgn chat dr pengguna
    document_test = query

    # melakukan proses preprocessing pada dokumen data buku
    word_stem_arrays_train = [ #untuk setiap document pada document train di lakukan proses filtering, hasilnya dimasukan 
    # variabel filter_words_and..
        filter_words_and_get_word_stems(str(document), word_tokenizer,
                                        word_stemmer, stopword_remover)
        for document in documents_train
    ]
    

    # melakukan preprocessing pada document test 
    word_stem_array_test = filter_words_and_get_word_stems(document_test,
                                                           word_tokenizer,
                                                           word_stemmer,
                                                           stopword_remover)
    

    # PROCESS

    # pembuatan dictionary (id) untuk setiap kata
   
    dictionary = corpora.Dictionary(
        word_stem_array_train for word_stem_array_train in word_stem_arrays_train)
    #pembuatan corpus (jumlah kata) per id dalam dokumen
    corpus = [
        dictionary.doc2bow(word_stem_array_train)
        for word_stem_array_train in word_stem_arrays_train
    ]



    # buat lsi model dari dictionary dan corpus
    # LSI model cisinya matrix  Singular Value Decomposition (SVD) 
   
    lsi_model = LsiModel(
        corpus=corpus,
        id2word=dictionary
    )
    
    # hitung cosine ssimilarity matrix
    cosine_similarity_matrix = similarities.MatrixSimilarity(lsi_model[corpus])


    # hitung lsi vector pada document test
    vector_lsi_test = lsi_model[dictionary.doc2bow(word_stem_array_test)]
    

    # lakukan perhitungan cosine similiarity pada semua dokumen
    cosine_similarities_test = cosine_similarity_matrix[vector_lsi_test]

    # OUTPUT
    # ambil dokumen dengan cosine similiarity tertinggi
    most_similar_document_test = judul_buku[np.argmax(
        cosine_similarities_test)]

    #mengembalikan judul buku dengan isi dokumen yang paling sesuai
    return most_similar_document_test


