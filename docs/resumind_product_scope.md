# Resumind Product Scope

## 🌟 Overview

**Resumind** is an AI-powered job application manager designed to help job seekers streamline their search, track progress, and generate tailored application materials. The app combines intuitive tracking features with powerful AI tools for resume and cover letter generation, enabling users to apply more effectively and stay organized.

---

## 👤 Target Users

### 1. **Recent Graduates**

* Need structure and clarity in job searches
* May lack experience in resume and cover letter writing

### 2. **Career Switchers**

* Need to tailor materials to new industries
* Track multiple job applications with varied roles

### 3. **Tech Professionals**

* Apply to dozens of roles
* Need automation and insights to maximize job hunting efficiency

---

## 🧩 Core MVP Features (Must-Have)

### 1. **Authentication (Firebase or Supabase)**

* Email/password or OAuth login
* User account creation and secure session management

### 2. **Job Tracker Dashboard**

* Add/Edit/Delete job applications
* Track status (Applied, Interviewing, Offer, Rejected)
* Columns for: Company, Role, Location, Applied Date, Notes, Resume Used, Tags

### 3. **Resume Builder**

* Create and edit resume(s) with simple editor
* Option to import past data or generate suggestions via AI
* Export as PDF

### 4. **Cover Letter Generator**

* Input job info → output custom-tailored letter using OpenAI
* Allow manual editing before saving/export

---

## ✨ Future Features (Nice-to-Have)

### 1. **AI Job Match Insights**

* Suggest which resumes to use based on job description
* Score or rank job matches

### 2. **Chrome Extension**

* Auto-fill and track applications from job boards like LinkedIn, Indeed

### 3. **Smart Notifications**

* Reminders for follow-ups, interviews, deadlines

### 4. **Calendar Integration**

* Visual timeline of applications and interview dates

### 5. **Resume/Cover Letter Feedback**

* AI-powered suggestions to improve tone, length, and keywords

---

## 🔧 Tech Stack (Tentative)

* **Frontend:** React or Next.js
* **Backend:** Flask (Python)
* **Auth & DB:** Supabase or Firebase
* **AI Integration:** OpenAI API (GPT-4)
* **Deployment:** Vercel (frontend), Render (backend)

---

## ✅ Success Criteria (MVP)

* User can sign up and log in
* User can create, update, and delete job applications
* User can generate a basic resume with AI or manual entry
* User can generate a cover letter using job info
* User can track all job applications via dashboard

---

## 🚀 Timeline

10 weeks total (4 hrs/day):

* Weeks 1–2: Planning + UI (Figma)
* Weeks 3–5: Backend API + DB integration
* Weeks 6–7: Frontend integration
* Week 8: AI tools integration
* Week 9: Testing
* Week 10: Deployment + polish
