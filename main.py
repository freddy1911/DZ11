from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidates_by_name, get_candidates_by_skill, get_candidate

PATH_CANDIDATES = 'candidates.json'
candidates = load_candidates_from_json(PATH_CANDIDATES)
app = Flask(__name__)

@app.route('/')
def get_all_user():
    return render_template('file.html', candidates=candidates)

@app.route('/candidate/<int:x>')
def get_one_user(x):
    item = get_candidate(x, candidates)
    if item:
        return render_template('single.html', item=item)
    return 'NOT FOUND'

@app.route('/search/<candidate_name>')
def get_one_by_name(candidate_name):
    items = get_candidates_by_name(candidate_name, candidates)
    if items:
        return render_template('single.html', candidates=items)
    return 'NOT FOUND'


@app.route('/skill/<skill_name>')
def get_one_by_skills(skill_name):
    items = get_candidates_by_skill(skill_name, candidates)
    if items:
        return render_template('skills.html', skills=skill_name, candidates=items)
    return 'NOT FOUND'

app.run()