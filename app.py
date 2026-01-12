from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

print("--- STARTING APP ---")

app = Flask(__name__)

# This acts as our temporary database. 
# In a real app, this would connect to SQL or MongoDB.
community_posts = [
    {
        'id': 1,
        'type': 'Offer',
        'title': '10 Winter Coats Available',
        'organization': 'Downtown Hope Center',
        'description': 'We have received a donation of XL coats. Available for pickup.',
        'contact': 'sarah@hopecenter.org',
        'timestamp': '2023-10-27 09:30'
    },
    {
        'id': 2,
        'type': 'Request',
        'title': 'Urgent: Insulin Storage Needed',
        'organization': 'Street Medic Team',
        'description': 'We have a client needing refrigeration for medication near 5th St.',
        'contact': '555-0199',
        'timestamp': '2023-10-27 10:15'
    }
]

@app.route('/')
def home():
    # Show the homepage and pass the posts to it
    return render_template('index.html', posts=community_posts)

@app.route('/add_post', methods=['POST'])
def add_post():
    # Get data from the form
    title = request.form.get('title')
    post_type = request.form.get('type') # Offer or Request
    org = request.form.get('organization')
    desc = request.form.get('description')
    contact = request.form.get('contact')
    
    # Create the new post object
    new_post = {
        'id': len(community_posts) + 1,
        'type': post_type,
        'title': title,
        'organization': org,
        'description': desc,
        'contact': contact,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    # Add to our list (at the top)
    community_posts.insert(0, new_post)
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

