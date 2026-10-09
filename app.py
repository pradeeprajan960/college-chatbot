from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_msg = data.get('message', '').lower()

    if 'hi' in user_msg or 'hello' in user_msg or 'vanakam' in user_msg:
        reply = "Vanakam! 👋 College pathi enna theriyanum?"
    elif 'fees' in user_msg or 'fee' in user_msg or 'evlo' in user_msg:
        reply = "CSE ku 1.2L per year, ECE ku 1.1L. Office la confirm pannikalam."
    elif 'hostel' in user_msg or 'hostel eruka' in user_msg:
        reply = "Hostel iruku da! Boys ku separate, girls ku separate. Fees 70k per year, food included."
    elif 'library' in user_msg:
        reply = "Library timing 11 AM - 3 PM. 2 books 15 days ku eduthukalam."
    elif 'hod' in user_msg:
    if 'AIDS' in user_msg:
        reply = "AIDS HOD Archana Mam."
    elif 'Cyber' in user_msg:
        reply = "Cyber HOD Priyanka Mam."
    elif 'AIDS A' in user_msg and 'adviser' in user_msg:
    reply = "AIDS A class adviser Gowtham Sir."
elif 'AIDS B' in user_msg and 'adviser' in user_msg:
    reply = "AIDS B class adviser Archana Mam."
    elif 'college Principal' in user_msg:
        reply = "baskaran sir." 
    elif 'exam' in user_msg:
        reply = "Internal exam next month. Timetable website la varum."
    elif 'timing' in user_msg or 'time' in user_msg:
        reply = "College timing 9:30 AM - 4 PM."
    else:
        reply = "Sorry, athu pathi enakku therila. Timing, admission, fees, hostel, placement, library, HOD, exam pathi kelu."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
