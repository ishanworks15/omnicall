import streamlit as st
import google.generativeai as genai

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="OmniCall – Live Sales Assistant",
    page_icon="📞",
    layout="wide",
)

# ── API Key ───────────────────────────────────────────────────────────────────
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    api_key = None

if not api_key:
    st.error("⚠️ Gemini API key not found. Add it to `.streamlit/secrets.toml` as `GEMINI_API_KEY = 'your-key'`")
    st.stop()

genai.configure(api_key=api_key)

# ── Knowledge Bases ───────────────────────────────────────────────────────────
SBM_KNOWLEDGE = """
PROGRAMME: Strategic Business Management (SBM) by MasterCamp / Masters' Union

BASICS:
- Duration: 12 months, blended weekend format (keep your job while studying)
- Mode: Online + Optional In-Person weekend classes
- Fee: ₹21,00,000 total (₹50,000 admission + ₹20,50,000 tuition, GST-exempt, NSDC-approved)
- Scholarship: 5–15% standard; 5 named scholarships (profile-based, PD decides amount): Uday Express, Samta Express, Palace on Wheels, Duronto, Vande Bharat
- Commencement: May 2026 (Tentative)
- Eligibility: Working professionals 0–5 yrs, fresh graduates, final-year students

TARGET ARCHETYPES:
- Fresher/Student → knower-vs-doer gap, first CXO exposure, Dropshipping as first business
- Working Professional (1–5 yrs) → plateau, breadth gap, CXO network they'd take 10 yrs to build
- Family Business Successor → professionalize business, modern operator thinking
- Aspiring Founder → Dropshipping Challenge, Investment Camp, Consulting Garage

THE 4 EXPERIENTIAL HOOKS (OutClass Challenges):
1. Consulting Garage (Term 1): Real small business consult — rework their strategy, present to founder's face
2. Creator Challenge (Term 2): Build personal brand on YouTube/Instagram/LinkedIn, compete for traction
3. Investment Camp (Term 3): Manage ₹1 Cr simulated stock portfolio under pressure
4. Dropshipping Challenge (Term 4): Launch real e-commerce business — real products, real revenue

PROGRAMME HIGHLIGHTS:
- 1:1 Mentorship with dedicated industry expert
- 4 In-Person Residencies: Orientation, Campus Immersion 1, Startup Weekend, Campus Immersion 2
- Startup Weekend: 48-hour startup build challenge on campus
- Sharan Hegde (Founder, The 1% Club) exclusive personal finance masterclass
- Leadership Trek: Himalayan trek for experiential leadership
- 6 Learning Domains: MAST, SAMA, FIFI, PRTC, AIML, COMM

FACULTY (use casually — pause before company name):
- Rajat Mathur – Managing Director, Morgan Stanley (Finance/Deals)
- Saurabh Sengupta – Former Sr. VP Sales, Zomato (Consumer internet/Growth)
- Subhonil Ghoshal – Former MD, Accenture (Consulting/Strategy)
- Sharan Hegde – Founder & CEO, The 1% Club (Personal Finance)
- Manoj Kohli – Former CEO, Bharti Airtel; Chairman Board of Governors
- Malthi S S – Former Director Product Management, PayPal
- Sindhu Biswal – Former Head of Growth & Marketing, Betterhalf
- Mukesh Ghuraiya – CMO, Modi Naturals
- Akshay Gurnani – Co-founder & CEO, Schbang

CAREER OUTCOMES:
- Placement target: 6–12 LPA
- 800+ placements in last 8 months
- 600+ hiring partners
- Highest placement: 36 LPA
- Top 10% average: 11.85 LPA
- Median salary hike: 42%+
- Career Advisory: Resume refinement, LinkedIn strategy, 1:1 mentor, mock interviews

SALES PHILOSOPHY (tone to adopt in suggestions):
- Consultative, not pushy. Peer-to-peer tone, not vendor tone
- DO NOT fill silences — pause after key questions
- DO NOT name specific % for named scholarships — defer to PD
- DO NOT trash competitors by name — frame: "they teach you ABOUT business, we teach INSIDE"
- Capture exact words from Discovery Q3 — reference verbatim in close
- 6 ANCHORS: Frame flip → Gap exposure → Faculty authority → Experiential hooks → "What stands out?" → Named scholarship tease + PD hand-off
- GOAL of every call: Schedule the 30–40 min PD video call

OBJECTION HANDLERS:
- "Too expensive (₹21L)": Don't defend ratio — decompose the experience; "Do you want to WATCH business 12 months or DO business 12 months?"
- "Placement?": 800+ placements, 42% median hike, 36 LPA highest; pivot to operators vs employees
- "Need to discuss parents": Validate → suggest PD call first, then PD calls parents directly
- "Already planning MBA": Position as bridge BEFORE MBA — makes them a stronger IIM/ISB candidate
- "No time": Weekend format, keep current job, in-person residencies planned in advance
- "Call me later": 90-second frame — "If after 90 secs you're not interested, I'll hang up myself. Fair?"
"""

PGP_KNOWLEDGE = """
PROGRAMME: PGP Bharat by Masters' Union

BASICS:
- Duration: 6 months, full-time immersive
- Structure: 2 months Gurugram campus + 2 months travel + 2 months Gurugram campus
- Fee: ~₹18,00,000 (bundled — includes ALL expenses: flights, stays, food, laundry, insurance)
- Scholarship: 5–15% standard; 5 named scholarships (profile-based, PD decides): Uday Express, Samta Express, Palace on Wheels, Duronto, Vande Bharat
- Target audience: Indian professionals ages 21–28, freshers, working pros, family-business successors, aspiring founders

CORE THESIS:
- "Almost every major Indian industry is GEOGRAPHICALLY native. You cannot understand it remotely."
- 7,000 km across 20 cities, 25+ company immersions, 30+ CXO sessions — all IN PERSON inside their offices
- Everything bundled: "You just show up with your bag"

THE 5 GEOGRAPHICAL HOOKS:
1. Jalandhar (Manufacturing): Sonalika Tractors, Nivia Sports, ITC — factory floor, labour economics, supply chain
2. Mumbai (Supply Chain/Finance): Dabbawalas (Churchgate at 11:45 AM), Kotak Mahindra Bank, Godrej, Swades Foundation, RSVP
3. Jaipur (D2C/Luxury Crafts): Minimalist D2C beauty, Jaipur Rugs, IJYA Jewellery — D2C scaling without metro
4. Bengaluru (Quick-Commerce/Fintech): Swiggy (5M order days), Zerodha, Meesho, Infosys — inside their buildings
5. Darjeeling + Goa (Hospitality/Agribusiness/Industry): Glenburn Tea Estate (60%+ margins), Mayukh Tea, Cordelia Cruises, Zydus, JSW Steel

20-CITY HUB MAP:
Delhi NCR, Jalandhar, Jaipur, Mumbai, Goa, Bengaluru, Darjeeling, Lucknow + more
Key companies: Parliament of India, Addverb, Lenskart, Sonalika Tractors, Minimalist, Dabbawalas, Kotak, Swiggy, Zerodha, Glenburn Tea Estate, Indo-Russian Rifles, Deloitte

PROGRAMME STRUCTURE:
Month 1–2 (Gurugram campus): Dropshipping Challenge — real business, real revenue, real ad spend; Dropshipping Mela showcase
Month 3–4 (Travel across India): Creator Challenge — YouTube/Instagram/LinkedIn personal brand; One-Day Consultancy Challenges at each company visited (8 total, presented to leadership)
Month 5–6 (Gurugram campus): VIP Pre-Seed / Venture Initiation Programme — pitch own startup to Masters Union Investment Fund + investor allies for ACTUAL pre-seed funding

BUNDLED INCLUSIONS (let prospect do mental math — never compute savings for them):
- Residential orientation week on Gurugram campus
- Accommodation + food during campus months
- ALL flights, buses, heritage train (Darjeeling), flagship property stays, meals, laundry, insurance during travel months

FACULTY (name 3 max per call — casually):
- Manoj Kohli – Former CEO, Bharti Airtel (Telecom, leadership at scale)
- Saurabh Sengupta – Ex-Sr. VP, Zomato (Consumer internet, growth)
- Rajat Mathur – Former MD, Morgan Stanley (Investment banking, deals)
- Rajiv Gupta – Ex-VP Sales & Marketing, Honda (Sales strategy)
- Sanjeev Bhasin – Former Director, IIFL (Capital markets)

ARCHETYPE MAPPING:
- Fresher → knower-vs-doer gap, first exposure to real CXOs, Dropshipping as first business, VIP Pre-Seed path to funded startup
- Working Professional → plateau, breadth across verticals, 20-city exposure, CXO network built in 6 months
- Family Business Successor → professionalize it, see 25+ businesses operate, manufacturing immersions, modern operator thinking
- Aspiring Founder → Dropshipping Challenge, VIP Pre-Seed, Masters Union Investment Fund, 30+ CXOs as first customers

KEY SALES FRAME:
- "Is there any classroom in the world — at any price — that can replicate that?" [Let them say no]
- Never mention ₹18L price first — let it come up naturally
- Bundled-cost reveal strips sticker shock without computing math
- GOAL: Schedule 30–40 min PD video call

SCHOLARSHIPS — Named (profile-based, PD decides %):
- Uday Express Grant: Self-made, first-gen, Tier-2/3 city origin
- Samta Express Fellowship: Diverse/remote/underrepresented background
- Palace on Wheels Fellowship: Content creator, filmmaker, storyteller, cultural entrepreneur
- Duronto Fellowship: Founder energy, existing side-project, bootstrapped venture
- Vande Bharat Scholar: Academic topper, competitive exam performer

RULE: Standard 5–15% can be mentioned. Named scholarship % is NEVER disclosed — PD decides.

OBJECTION HANDLERS:
- "₹18L too expensive": Month-for-month comparison is structurally broken. "Do you want to WATCH business for 2 years or DO it for 6 months?" + Bundled cost argument (₹2.5–3L travel/living alone)
- "What's placement?": PGP Bharat isn't placement-first — it's for operators/founders. Dropshipping revenue + VIP Pre-Seed funding = real ROI. Defer specifics to PD.
- "Need to discuss with parents": Validate → PD call first → PD can do separate parent call
- "Planning MBA": "PGP Bharat is a bridge BEFORE MBA. Walk into ISB/IIM with 20-city immersion on your profile — you're not the same candidate."
"""

# ── Helpers ───────────────────────────────────────────────────────────────────
PROGRAMME_OPTIONS = {
    "🏢 SBM — Strategic Business Management (12 months, Weekend)": "SBM",
    "🇮🇳 PGP Bharat — 6-Month India Immersion": "PGP",
}

ARCHETYPE_OPTIONS = [
    "Select archetype...",
    "🎓 Fresher / Final-year Student",
    "💼 Working Professional (1–5 yrs)",
    "🏭 Family Business Successor",
    "🚀 Aspiring Founder / Has a Side Project",
    "🔄 Career Switcher",
]

def build_prompt(programme_key, client_name, client_age, archetype, edu_goals, family_bg, live_notes):
    knowledge = SBM_KNOWLEDGE if programme_key == "SBM" else PGP_KNOWLEDGE
    prog_name = "Strategic Business Management (SBM)" if programme_key == "SBM" else "PGP Bharat"

    return f"""You are an expert sales coach assisting a live sales call for {prog_name} by MasterCamp / Masters' Union.

=== PROGRAMME KNOWLEDGE BASE ===
{knowledge}

=== LEAD PROFILE ===
Name: {client_name or "Not provided"}
Age: {client_age or "Not provided"}
Archetype: {archetype}
Education/Career Goals: {edu_goals or "Not provided"}
Family Background: {family_bg or "Not provided"}

=== LIVE CALL NOTES (what the lead just said) ===
{live_notes}

=== YOUR TASK ===
Based on the lead's profile AND what they just said in the live notes, generate EXACTLY 3 high-impact suggestions. 

Each suggestion must be ONE of these types:
- 🎯 DISCOVERY QUESTION — a question to ask the lead to deepen the gap or understand their pain
- 💬 TALKING POINT — something to say that connects their situation to the programme
- ⚡ OBJECTION HANDLER — a ready-to-use response to a concern or hesitation they raised

FORMAT YOUR RESPONSE EXACTLY LIKE THIS (use these exact headers):

**Suggestion 1 — [TYPE: DISCOVERY QUESTION / TALKING POINT / OBJECTION HANDLER]**
[Your suggestion — write it as exact words the salesperson should say or ask. Keep it sharp, 2–4 sentences max. Match the consultative, peer-to-peer tone from the sales framework. No filler. No brochure language.]

*Why this works:* [1 sentence explaining the strategic rationale — reference the sales framework]

---

**Suggestion 2 — [TYPE]**
[Your suggestion]

*Why this works:* [1 sentence]

---

**Suggestion 3 — [TYPE]**
[Your suggestion]

*Why this works:* [1 sentence]

---

**🏷️ Scholarship Fit:** Based on this profile, which named scholarship should you tease for the PD hand-off? Name it and give ONE sentence on why.

RULES:
- Never suggest quoting a specific % for named scholarships
- Speak in the salesperson's voice — these are lines to say out loud
- Reference the lead's EXACT situation from the notes
- Match the consultative, non-pushy tone of the sales framework
- Suggestions must be immediately usable mid-call
"""

def get_ai_suggestions(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# ── UI ─────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 1.5rem 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        color: white;
    }
    .section-card {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 10px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }
    .suggestion-box {
        background: #ffffff;
        border-left: 4px solid #0f3460;
        border-radius: 8px;
        padding: 1rem 1.2rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    .scholarship-box {
        background: #fff8e1;
        border: 1px solid #ffc107;
        border-radius: 8px;
        padding: 1rem;
        margin-top: 0.5rem;
    }
    .live-badge {
        display: inline-block;
        background: #e53e3e;
        color: white;
        font-size: 0.7rem;
        font-weight: bold;
        padding: 2px 8px;
        border-radius: 20px;
        margin-left: 8px;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.5} }
    .stTextArea textarea { font-size: 0.95rem !important; }
    .prog-selector label { font-weight: 600 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h2 style="margin:0; font-size:1.6rem;">📞 OmniCall <span style="font-size:0.9rem; opacity:0.7; font-weight:400;">Live Sales Assistant</span></h2>
    <p style="margin:0.3rem 0 0; opacity:0.8; font-size:0.85rem;">MasterCamp by Masters' Union · Real-time AI coaching during sales calls</p>
</div>
""", unsafe_allow_html=True)

# ── Programme Selector ────────────────────────────────────────────────────────
prog_label = st.selectbox(
    "**Select Programme**",
    options=list(PROGRAMME_OPTIONS.keys()),
    key="programme",
)
programme_key = PROGRAMME_OPTIONS[prog_label]

st.divider()

# ── Layout: Left = Lead Profile | Right = Live Notes + AI ────────────────────
col_left, col_right = st.columns([1, 1.4], gap="large")

with col_left:
    st.markdown("### 👤 Lead Profile")

    client_name = st.text_input("Client Name", placeholder="e.g. Rahul Sharma", key="name")
    client_age = st.text_input("Age", placeholder="e.g. 24", key="age")
    archetype = st.selectbox("Current Situation (Archetype)", ARCHETYPE_OPTIONS, key="archetype")

    edu_goals = st.text_area(
        "Education & Career Goals",
        placeholder="e.g. Wants to move from IT into business strategy, considering MBA but unsure...",
        height=90,
        key="edu_goals",
    )
    family_bg = st.text_area(
        "Family Background",
        placeholder="e.g. Father runs a textile business in Surat, first in family to pursue corporate career...",
        height=90,
        key="family_bg",
    )

    st.markdown("---")
    st.markdown("##### 🎯 Quick Anchor Tracker")
    st.markdown("Check off anchors landed:")
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        a1 = st.checkbox("Frame Flip done", key="a1")
        a2 = st.checkbox("Gap exposed (Q3 captured)", key="a2")
        a3 = st.checkbox("Faculty names dropped", key="a3")
    with col_a2:
        a4 = st.checkbox("Hooks delivered", key="a4")
        a5 = st.checkbox('"What stands out?" asked', key="a5")
        a6 = st.checkbox("Scholarship tease + PD ask", key="a6")

    anchors_done = sum([a1, a2, a3, a4, a5, a6])
    st.progress(anchors_done / 6, text=f"{anchors_done}/6 anchors completed")

with col_right:
    st.markdown(f'### 📝 Live Notes <span class="live-badge">LIVE</span>', unsafe_allow_html=True)
    st.caption("Type what the lead says. Hit **Get AI Suggestions** after each key moment.")

    live_notes = st.text_area(
        "What's happening on the call right now?",
        placeholder=(
            "e.g. He said he's been watching a lot of entrepreneurship content on YouTube but hasn't "
            "actually tried starting anything. Mentioned his dad has a small manufacturing unit but he "
            "doesn't want to just inherit it — wants to 'prove himself first'. Seems interested in the "
            "Dropshipping challenge but worried about the fee..."
        ),
        height=200,
        key="live_notes",
        label_visibility="collapsed",
    )

    ready = (
        live_notes.strip() != ""
        and archetype != "Select archetype..."
    )

    if not ready:
        st.info("💡 Fill in the archetype + live notes to unlock AI suggestions.")

    get_btn = st.button(
        "⚡ Get AI Suggestions",
        type="primary",
        disabled=not ready,
        use_container_width=True,
    )

    # ── AI Output ─────────────────────────────────────────────────────────────
    if get_btn:
        with st.spinner("🤖 Thinking mid-call..."):
            try:
                prompt = build_prompt(
                    programme_key,
                    client_name,
                    client_age,
                    archetype,
                    edu_goals,
                    family_bg,
                    live_notes,
                )
                result = get_ai_suggestions(prompt)

                st.markdown("---")
                st.markdown("### 🎯 AI Suggestions")
                st.markdown(result)

            except Exception as e:
                st.error(f"API Error: {e}")

    # ── Objection Quick-Ref ───────────────────────────────────────────────────
    st.markdown("---")
    with st.expander("🛡️ Quick Objection Reference", expanded=False):
        if programme_key == "SBM":
            st.markdown("""
**💸 '₹21L too expensive'**
> "Do you want to WATCH business for 12 months, or DO business for 12 months?"

**📊 'What's the placement?'**
> "800+ placements, 42% median hike, 36 LPA highest. But SBM isn't for employees — it's for operators."

**👨‍👩‍👧 'Need to ask parents'**
> "Totally. Get on the PD call first — understand it yourself. PD can call your parents separately."

**🎓 'Planning MBA/ISB/IIM'**
> "SBM is a bridge BEFORE your MBA. Walk in with a real portfolio — you're a different candidate."

**⏰ 'No time'**
> "Weekend format. Keep your job. In-person residencies planned well in advance."
            """)
        else:
            st.markdown("""
**💸 '₹18L too expensive'**
> "Month-for-month comparison is broken. The travel + stays alone are ₹2.5–3L. And: Do you want to WATCH business for 2 years or DO it for 6 months?"

**📊 'What's placement?'**
> "PGP Bharat isn't placement-first — it's for founders and operators. Some graduate with funded startups, not job offers."

**👨‍👩‍👧 'Need to ask parents'**
> "Totally. Get on the PD call first — PD can do a separate call with your parents."

**🎓 'Planning MBA'**
> "Walk into ISB/IIM after 20-city immersion on your profile. You're not the same candidate."

**🏙️ 'What cities do you visit?'**
> Jalandhar (Sonalika, Nivia), Mumbai (Dabbawalas, Kotak), Jaipur (Minimalist, Jaipur Rugs), Bengaluru (Swiggy, Zerodha), Darjeeling (Glenburn Tea Estate), Goa (Cordelia Cruises, JSW)
            """)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("OmniCall · Built for MasterCamp Sales Team · Powered by Gemini 1.5 Flash · admissions@mastercamp.org")
