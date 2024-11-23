text = "abcd e"
st = []
for i in text:
    st.append(i)
rev_text = ''
while st:
    rev_text += st.pop() 
print(rev_text)