# from flask import Flask,render_template

# import pickle
# popular_df = pickle.load(open('popular.pkl', 'rb'))


# app=Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html',
#                            book_name=list(popular_df['book-Title'].values),
#                            author=list(popular_df['book-Author'].values),
#                            image=list(popular_df['Image-URL-M'].values),
#                            votings=list(popular_df['num_ratings'].values),
#                            ratings=list(popular_df['avg_ratings'].values))

# if __name__=='__main__':
#     app.run(debug=True)

from flask import Flask, render_template,request
import numpy as np

try:
    import pandas as pd
except ModuleNotFoundError:
    print("Pandas module not found. Please install it using 'pip install pandas'.")

try:
    import pickle
    popular_df = pickle.load(open('popular.pkl', 'rb'))
except FileNotFoundError:
    print("The file 'popular.pkl' does not exist.")
    popular_df = pd.DataFrame()  # Create an empty DataFrame if the file doesn't exist

try:
    import pandas as pd
except ModuleNotFoundError:
    print("Pandas module not found. Please install it using 'pip install pandas'.")

try:
    import pickle
    pt = pickle.load(open('pt.pkl', 'rb'))
except FileNotFoundError:
    print("The file 'popular.pkl' does not exist.")
    pt = pd.DataFrame()  # Create an empty DataFrame if the file doesn't exist

##hiiiii
print('hiiii')
try:
    import pandas as pd
except ModuleNotFoundError:
    print("Pandas module not found. Please install it using 'pip install pandas'.")

try:
    import pickle
    books = pickle.load(open('books.pkl', 'rb'))
except FileNotFoundError:
    print("The file 'popular.pkl' does not exist.")
    books = pd.DataFrame()  # Create an empty DataFrame if the file doesn't exist

try:
    import pandas as pd
except ModuleNotFoundError:
    print("Pandas module not found. Please install it using 'pip install pandas'.")

try:
    import pickle
    similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))
except FileNotFoundError:
    print("The file 'popular.pkl' does not exist.")
    similarity_scores = pd.DataFrame()  # Create an empty DataFrame if the file doesn't exist



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votings=list(popular_df['num_ratings'].values),
                           ratings=list(popular_df['avg_rating'].values))

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['POST'])
def recommend():
    user_input=request.form.get('user_input')
    index = np.where(pt.index==user_input)[0][0]
    similar_items=sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:9]  #sorting in terms of similarity score cuz it got sorted based on index

    data=[]
    for i in similar_items:
        item=[]
        # print(pt.index[i[0]])
        temp_df=books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)
    print(data)
    return render_template('recommend.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)
