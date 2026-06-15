from flask import Flask, jsonify, render_template, send_from_directory
import sys
import os

# Add the main_file directory to path so imports work
sys.path.insert(0, os.path.dirname(__file__))

from pathways.primary_sch import primary_school_pathways
from pathways.secondary_sch import secondary_sch_pathways
from pathways.junior_college import junior_college_pathways
from pathways.polytechnic import polytechnic_school_pathways
from pathways.millennia_institute import millennia_institute_pathways

app = Flask(__name__)

# ── Serve the HTML frontend ────────────────────────────────────────────────────

@app.route('/')
def index():
    return open(os.path.join(os.path.dirname(__file__), 'index.html'), encoding='utf-8').read()

# ── API route — returns all pathway data as JSON ───────────────────────────────

@app.route('/api/pathways')
def get_pathways():
    """Returns all pathway data structured by level."""
    data = {
        "Primary School": {
            "icon": "📚",
            "hint": "Pathways available during or after primary school",
            "pathways": primary_school_pathways
        },
        "Secondary School": {
            "icon": "🏫",
            "hint": "Pathways available during or after secondary school",
            "pathways": secondary_sch_pathways
        },
        "Junior College": {
            "icon": "🎓",
            "hint": "Pathways available at junior college",
            "pathways": junior_college_pathways
        },
        "Polytechnic": {
            "icon": "🔧",
            "hint": "Pathways available after polytechnic",
            "pathways": polytechnic_school_pathways
        },
        "Millennia Institute": {
            "icon": "📖",
            "hint": "Pathways available at Millennia Institute",
            "pathways": millennia_institute_pathways
        }
    }
    return jsonify(data)

# ── API route — returns pathways for a specific level ─────────────────────────

@app.route('/api/pathways/<level>')
def get_level_pathways(level):
    """Returns pathways for a specific level."""
    level_map = {
        "primary": primary_school_pathways,
        "secondary": secondary_sch_pathways,
        "junior_college": junior_college_pathways,
        "polytechnic": polytechnic_school_pathways,
        "millennia_institute": millennia_institute_pathways
    }
    if level.lower() in level_map:
        return jsonify(level_map[level.lower()])
    return jsonify({"error": "Level not found"}), 404

# ── Run ────────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("Starting Educational Pathway Navigator...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)
