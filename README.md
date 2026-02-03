# 🚀 Devanshi Bansal - ML Engineer Portfolio

A modern, cyberpunk-inspired portfolio website showcasing Machine Learning and AI projects, with a fully functional backend for contact form handling.

![Portfolio Preview](https://img.shields.io/badge/Status-Production%20Ready-00ff9d?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Tech-HTML%20%7C%20CSS%20%7C%20JS%20%7C%20Python%20%7C%20Flask-00d4ff?style=for-the-badge)

## ✨ Features

### Frontend
- 🎨 **Modern Cyberpunk Design** - Tech-forward aesthetic with animated gradients and grid backgrounds
- 📱 **Fully Responsive** - Optimized for desktop, tablet, and mobile devices
- 🎭 **Smooth Animations** - Scroll-triggered reveals and micro-interactions
- 🎯 **Interactive Components** - Dynamic stats counter, hover effects, and smooth scrolling
- 🌟 **Distinctive Typography** - Using Orbitron and Rajdhani fonts for a futuristic feel
- ⚡ **Performance Optimized** - Fast loading with CSS-only animations

### Backend
- 📧 **Contact Form API** - Flask backend to handle form submissions
- 💾 **Message Storage** - JSON-based storage for contact messages
- 📨 **Email Notifications** - Automated email alerts for new messages
- 📊 **Analytics Dashboard** - API endpoints for portfolio statistics
- 🔒 **Input Validation** - Server-side validation for security
- 🌐 **CORS Enabled** - Ready for frontend-backend communication

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3 (Advanced animations, gradients, flexbox, grid)
- Vanilla JavaScript (ES6+)
- Google Fonts (Orbitron, Rajdhani)

### Backend
- Python 3.8+
- Flask (Web framework)
- Flask-CORS (Cross-origin resource sharing)
- SMTP (Email functionality)
- JSON (Data storage)

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Git (optional, for cloning)

### Quick Start

#### 1. Clone or Download the Project
```bash
# Using Git
git clone https://github.com/Devanshiiii28/portfolio.git
cd portfolio

# Or download and extract the ZIP file
```

#### 2. Set Up the Backend

**Install Python Dependencies:**
```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Configure Email (Optional):**

To enable email notifications, set up an environment variable:

```bash
# On Windows (Command Prompt)
set EMAIL_PASSWORD=your_app_password

# On Mac/Linux (Terminal)
export EMAIL_PASSWORD=your_app_password

# Or create a .env file
echo "EMAIL_PASSWORD=your_app_password" > .env
```

**For Gmail:**
1. Enable 2-factor authentication
2. Generate an "App Password" from Google Account settings
3. Use this app password as EMAIL_PASSWORD

#### 3. Run the Backend Server

```bash
python backend_server.py
```

The server will start on `http://localhost:5000`

You should see:
```
🚀 Portfolio Backend Server Starting...
📧 Email: devanshibansal74@gmail.com
🌐 Server running on http://localhost:5000

Available endpoints:
  - POST   /api/contact      - Submit contact form
  - GET    /api/messages     - View all messages
  - GET    /api/stats        - Portfolio statistics
  - PATCH  /api/messages/:id - Update message status
```

#### 4. Open the Frontend

Simply open `portfolio.html` in your web browser:

**Option 1: Direct File Open**
- Double-click `portfolio.html`
- Or right-click → Open with → Your Browser

**Option 2: Using Python HTTP Server**
```bash
# In a new terminal window
python -m http.server 8000

# Then visit: http://localhost:8000/portfolio.html
```

**Option 3: Using VS Code Live Server**
- Install "Live Server" extension
- Right-click `portfolio.html` → "Open with Live Server"

## 🌐 Deployment Guide

### Deploy Frontend (Free Options)

#### Option 1: GitHub Pages
1. Create a GitHub repository
2. Push your code
3. Go to Settings → Pages
4. Select branch and `/` root
5. Your site will be live at `https://username.github.io/portfolio`

#### Option 2: Netlify
1. Sign up at [netlify.com](https://netlify.com)
2. Drag and drop your project folder
3. Done! Get instant HTTPS domain

#### Option 3: Vercel
1. Sign up at [vercel.com](https://vercel.com)
2. Import your GitHub repository
3. Deploy with one click

### Deploy Backend (Free Options)

#### Option 1: Render
1. Sign up at [render.com](https://render.com)
2. Create new Web Service
3. Connect your GitHub repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python backend_server.py`
6. Add environment variables
7. Deploy!

#### Option 2: Railway
1. Sign up at [railway.app](https://railway.app)
2. New Project → Deploy from GitHub
3. Add environment variables
4. Deploy automatically

#### Option 3: PythonAnywhere
1. Sign up at [pythonanywhere.com](https://pythonanywhere.com)
2. Upload files via Files tab
3. Set up web app in Web tab
4. Configure WSGI file
5. Reload and go live

**Update API URL in portfolio.html:**
After deploying backend, update line ~1195 in `portfolio.html`:
```javascript
const API_URL = 'https://your-backend-url.com';  // Replace with your deployed backend URL
```

## 📁 Project Structure

```
portfolio/
│
├── portfolio.html              # Main portfolio webpage
├── backend_server.py          # Flask backend server
├── requirements.txt           # Python dependencies
├── README.md                  # This file
│
├── contact_messages.json      # Generated: Stores contact form submissions
└── .env                       # Optional: Environment variables (create this)
```

## 🎯 Features Breakdown

### Sections
1. **Hero Section** - Animated introduction with dynamic stats
2. **Skills Section** - Categorized technical skills with tags
3. **Projects Section** - Featured ML/AI projects with tech badges
4. **Experience Section** - Timeline of internships and achievements
5. **Contact Section** - Interactive form with backend integration

### Backend API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| POST | `/api/contact` | Submit contact form |
| GET | `/api/messages` | Get all messages (admin) |
| GET | `/api/stats` | Portfolio statistics |
| PATCH | `/api/messages/:id` | Update message status |
| GET | `/api/health` | Health check |

### API Examples

**Submit Contact Form:**
```bash
curl -X POST http://localhost:5000/api/contact \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "subject": "Collaboration Opportunity",
    "message": "I would like to discuss a project..."
  }'
```

**Get All Messages:**
```bash
curl http://localhost:5000/api/messages
```

**Get Statistics:**
```bash
curl http://localhost:5000/api/stats
```

## 🎨 Customization Guide

### Change Colors
Edit CSS variables in `portfolio.html` (around line 18):
```css
:root {
    --primary: #00ff9d;      /* Neon green */
    --secondary: #00d4ff;    /* Cyan */
    --tertiary: #ff00aa;     /* Pink */
    --dark: #0a0e1a;         /* Dark blue */
}
```

### Update Content
- **Personal Info:** Lines 950-1000 (Hero section)
- **Skills:** Lines 1020-1080 (Skills section)
- **Projects:** Lines 1095-1200 (Projects section)
- **Experience:** Lines 1230-1280 (Experience section)
- **Contact:** Lines 1320-1380 (Contact section)

### Add/Remove Sections
Each section follows this structure:
```html
<section id="section-name">
    <div class="container">
        <!-- Content here -->
    </div>
</section>
```

## 🔒 Security Best Practices

1. **Never commit sensitive data:**
   - Add `.env` to `.gitignore`
   - Use environment variables for passwords

2. **Input validation:**
   - Backend validates all form inputs
   - Frontend has required fields

3. **CORS configuration:**
   - Update CORS settings for production
   - Specify allowed origins

4. **Rate limiting:**
   - Consider adding rate limiting for production
   - Prevent spam and abuse

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Contact form not working
1. Check if backend is running (`http://localhost:5000`)
2. Check browser console for errors (F12)
3. Verify API_URL in portfolio.html matches backend URL
4. Check CORS settings if deployed

### Email notifications not sending
1. Verify EMAIL_PASSWORD environment variable is set
2. Use Gmail App Password (not regular password)
3. Check spam folder
4. Review backend console for error messages

### Port already in use
```bash
# Change port in backend_server.py (last line)
app.run(debug=True, host='0.0.0.0', port=5001)  # Use different port
```

## 📊 Analytics & Monitoring

The backend includes basic analytics:
- Total messages received
- Unread message count
- Recent submissions
- Portfolio statistics

Access via: `GET /api/stats`

## 🚀 Future Enhancements

### Planned Features
- [ ] Admin dashboard for managing messages
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Advanced email templates
- [ ] File upload capability
- [ ] Rate limiting and spam protection
- [ ] User authentication for admin panel
- [ ] Integration with Google Analytics
- [ ] Blog section with CMS
- [ ] Dark/Light theme toggle
- [ ] Multi-language support

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Devanshi Bansal**
- Email: devanshibansal74@gmail.com
- University: devanshi.2327cs1037@kiet.edu
- LinkedIn: [devanshi-bansal-9575412a5](https://linkedin.com/in/devanshi-bansal-9575412a5)
- GitHub: [Devanshiiii28](https://github.com/Devanshiiii28)
- LeetCode: [Devanshiiii28](https://leetcode.com/Devanshiiii28)
- Phone: +91-7456833267

## 🙏 Acknowledgments

- Font: Orbitron & Rajdhani from Google Fonts
- Icons: Unicode emojis
- Design inspiration: Cyberpunk and tech aesthetics
- Built with ❤️ for internship and placement opportunities

## 📞 Support

For questions, issues, or collaboration:
- Email: devanshibansal74@gmail.com
- Open an issue on GitHub
- Fill out the contact form on the portfolio

---

**Made with 💚 by Devanshi Bansal | ML Engineer & AI Developer**

⭐ Star this repo if you find it helpful!
