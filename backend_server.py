from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Configuration
EMAIL_ADDRESS = "devanshibansal74@gmail.com"  # Your email
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')  # Store password in environment variable

# Store contact messages in JSON file (for demonstration)
MESSAGES_FILE = 'contact_messages.json'

def load_messages():
    """Load existing messages from file"""
    if os.path.exists(MESSAGES_FILE):
        with open(MESSAGES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_message(message_data):
    """Save a new message to file"""
    messages = load_messages()
    messages.append(message_data)
    with open(MESSAGES_FILE, 'w') as f:
        json.dump(messages, f, indent=2)

def send_email_notification(form_data):
    """Send email notification when someone submits the contact form"""
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"Portfolio Contact: {form_data['subject']}"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        
        # Create HTML email body
        html_body = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f4f4f4;">
                    <h2 style="color: #00ff9d; border-bottom: 2px solid #00ff9d; padding-bottom: 10px;">
                        New Contact Form Submission
                    </h2>
                    
                    <div style="background: white; padding: 20px; border-radius: 5px; margin-top: 20px;">
                        <p><strong style="color: #0a0e1a;">Name:</strong> {form_data['name']}</p>
                        <p><strong style="color: #0a0e1a;">Email:</strong> {form_data['email']}</p>
                        <p><strong style="color: #0a0e1a;">Subject:</strong> {form_data['subject']}</p>
                        
                        <div style="margin-top: 20px;">
                            <strong style="color: #0a0e1a;">Message:</strong>
                            <p style="background: #f9f9f9; padding: 15px; border-left: 3px solid #00ff9d; margin-top: 10px;">
                                {form_data['message']}
                            </p>
                        </div>
                        
                        <p style="margin-top: 20px; font-size: 12px; color: #666;">
                            Submitted on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
                        </p>
                    </div>
                    
                    <div style="margin-top: 20px; padding: 15px; background: #e8f5e9; border-radius: 5px;">
                        <p style="margin: 0; color: #2e7d32;">
                            <strong>Reply To:</strong> <a href="mailto:{form_data['email']}" style="color: #00ff9d;">{form_data['email']}</a>
                        </p>
                    </div>
                </div>
            </body>
        </html>
        """
        
        msg.attach(MIMEText(html_body, 'html'))
        
        # Send email (configure with your SMTP settings)
        # Uncomment and configure when ready to use
        # with smtplib.SMTP('smtp.gmail.com', 587) as server:
        #     server.starttls()
        #     server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        #     server.send_message(msg)
        
        return True
    except Exception as e:
        print(f"Email error: {str(e)}")
        return False

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        "status": "active",
        "message": "Portfolio Backend API is running",
        "endpoints": {
            "/api/contact": "POST - Submit contact form",
            "/api/messages": "GET - Retrieve all messages (admin)",
            "/api/stats": "GET - Get portfolio statistics"
        }
    })

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        if not all(field in data for field in required_fields):
            return jsonify({
                "success": False,
                "error": "Missing required fields"
            }), 400
        
        # Validate email format
        if '@' not in data['email']:
            return jsonify({
                "success": False,
                "error": "Invalid email format"
            }), 400
        
        # Create message object
        message_data = {
            "id": len(load_messages()) + 1,
            "name": data['name'],
            "email": data['email'],
            "subject": data['subject'],
            "message": data['message'],
            "timestamp": datetime.now().isoformat(),
            "status": "unread"
        }
        
        # Save message
        save_message(message_data)
        
        # Send email notification (if configured)
        email_sent = send_email_notification(data)
        
        return jsonify({
            "success": True,
            "message": "Message received successfully! I'll get back to you soon.",
            "email_notification": email_sent
        }), 200
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/messages', methods=['GET'])
def get_messages():
    """Get all contact messages (for admin use)"""
    try:
        messages = load_messages()
        return jsonify({
            "success": True,
            "count": len(messages),
            "messages": messages
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/messages/<int:message_id>', methods=['PATCH'])
def update_message_status(message_id):
    """Update message status (e.g., mark as read)"""
    try:
        data = request.get_json()
        messages = load_messages()
        
        for message in messages:
            if message['id'] == message_id:
                if 'status' in data:
                    message['status'] = data['status']
                break
        
        with open(MESSAGES_FILE, 'w') as f:
            json.dump(messages, f, indent=2)
        
        return jsonify({
            "success": True,
            "message": "Message updated successfully"
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get portfolio statistics"""
    try:
        messages = load_messages()
        
        stats = {
            "total_messages": len(messages),
            "unread_messages": len([m for m in messages if m.get('status') == 'unread']),
            "recent_messages": messages[-5:] if messages else [],
            "portfolio_stats": {
                "projects": 10,
                "hackathons": 5,
                "internships": 2,
                "cgpa": 8.2
            }
        }
        
        return jsonify({
            "success": True,
            "stats": stats
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }), 200

if __name__ == '__main__':
    print("🚀 Portfolio Backend Server Starting...")
    print("📧 Email:", EMAIL_ADDRESS)
    print("🌐 Server running on http://localhost:5000")
    print("\nAvailable endpoints:")
    print("  - POST   /api/contact      - Submit contact form")
    print("  - GET    /api/messages     - View all messages")
    print("  - GET    /api/stats        - Portfolio statistics")
    print("  - PATCH  /api/messages/:id - Update message status")
    print("\n" + "="*50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
