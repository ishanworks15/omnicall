# OmniCall — Live Sales Assistant
Built for MasterCamp by Masters' Union.

## Local Setup
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Cloud
1. Push this repo to GitHub (secrets.toml is gitignored — keep it local)
2. Go to share.streamlit.io → New App → select this repo
3. In Advanced Settings → Secrets, paste:
   ```
   GEMINI_API_KEY = "your-key-here"
   ```
4. Deploy ✅
