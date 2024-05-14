from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary data, replace with database integration
activities = [
    {"title": "Hiking", "points": 10, "member": ""},
    {"title": "Kayaking", "points": 15, "member": ""},
    {"title": "Cooking a new recipe", "points": 5, "member": ""}
]

activities_done = []

undergrad_members = [
    "Bordy Smoth", "Dawson Chapppp", "Austin Lowery"
]

alumni_members = [
    "Cameron Dunn", "Carey Jackson", "McKennon Wilson"
]

@app.route('/')
def index():
    return render_template('index.html', activities=activities, activities_done=activities_done, undergrad_members=undergrad_members, alumni_members=alumni_members)

@app.route('/add_activity', methods=['POST'])
def add_activity():
    title = request.form['title']
    points = None  # Initialize points as None
    
    # Determine member based on member type
    member_type = request.form['member_type']
    if member_type == 'Alumni':
        member = request.form['member_alumni']
    elif member_type == 'Undergrad':
        member = request.form['member_undergrad']
    else:
        member = ''  # Default value
    
    # Check if the entered title matches a pre-defined activity
    for activity in activities:
        if activity['title'] == title:
            points = activity['points']
            break  # Exit loop once the activity is found
    
    # Check if points have been determined
    if points is not None:
        new_activity = {"title": title, "points": points, "member": member}
        activities_done.append(new_activity)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
