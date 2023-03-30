def reverse_sp_word(st, l):
    st = st.split()
    return ' '.join(word[::-1] if word.startswith('l') else word for word in st)