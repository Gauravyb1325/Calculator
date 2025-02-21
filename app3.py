from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Gaurav Yadav"  # Replace with your actual name
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    ist_time_str = ist_time.strftime("%Y-%m-%d %H:%M:%S IST")

    # Get top command output
    try:
        top_output = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True).stdout
    except Exception as e:
        top_output = f"Error retrieving top output: {str(e)}"

    return f"""
    <h1>HTOP Details</h1>
    <p><b>Name:</b> {full_name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {ist_time_str}</p>
    <pre><b>Top Output:</b><br>{top_output}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
