from flask import Flask, render_template, request, url_for

# Creating the app
app = Flask(__name__)

# Global Variables
notes_list = []
temp_notes_list = []
notes_list_title = []
temp_notes_list_title = []
final_list = []

# Creating the main page


@app.route("/", methods=['GET', 'POST'])
def main():
    global notes_list, temp_notes_list, notes_list_title, temp_notes_list_title, final_list

    if request.method == "POST":
        webpage = request.form
        # print(webpage)
        notes_inp = str(webpage['notesInp'])
        print(notes_inp)
        temp_notes_list.append(notes_inp)
        [notes_list.append(x) for x in temp_notes_list if x not in notes_list]

    return render_template("index.html", notes_list=notes_list)


# Running the app
if __name__ == '__main__':
    app.run(debug=True)
