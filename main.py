from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route("/")
def all_candidates():
    candidates = utils.load_candidates_from_json("data/candidats.json")
    return render_template("list.html", items=candidates)


@app.route("/candidate/<int:candidat_id>")
def candidate_page(candidat_id):
    candidat = utils.get_candidate_id(candidat_id, "data/candidats.json")
    return render_template("single.html", candidat=candidat)


@app.route("/name/<string:name>")
def candidate_name(name):
    candidats = utils.get_candidates_by_name(name, "data/candidats.json")
    return render_template("search.html", candidats=candidats, candidats_len=len(candidats))


@app.route("/skill/<string:skill>")
def candidates_skill(skill):
    candidats = utils.get_candidates_by_skill(skill, "data/candidats.json")
    return render_template("skill.html", candidats=candidats, candidats_len=len(candidats))


app.run()
