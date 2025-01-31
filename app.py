from flask import Flask, render_template, url_for, send_from_directory
import os

app = Flask(__name__)

# Add this route to directly serve static files (for debugging)
@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/')
@app.route('/index.html')
def index():
    # Debug: Print the constructed URL for the logo
    logo_url = url_for('static', filename='images/logo/logo1.jpg')
    print(f"Logo URL: {logo_url}")
    return render_template('index.html')

@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html')

# Add error handlers
@app.errorhandler(404)
def not_found_error(error):
    print(f"404 Error: {error}")  # This will show in your logs
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    print(f"500 Error: {error}")  # This will show in your logs
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.debug = True
    # Print static folder location on startup
    print(f"Static folder path: {app.static_folder}")
    print(f"Static folder exists: {os.path.exists(app.static_folder)}")
    app.run()
