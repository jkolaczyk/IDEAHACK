import sqlite3
import pandas as pd
import pickle
from ast import literal_eval
from math import sqrt

conn = sqlite3.connect("database.db")
c = conn.cursor()

def get_frequency_map():
    c.execute(' SELECT skills_en.ID, count(skills_en.ID) \
                FROM occupationSkillRelations as osr \
                JOIN skills_en ON skills_en.conceptUri = osr.skillUri \
                GROUP BY skills_en.ID \
                order by skills_en.ID')
    res = c.fetchall()
    freq_map = {row[0]: row[1] for row in res} 
    return freq_map

def label_transform_sql(lbl):
    c.execute('SELECT ID FROM skills_en WHERE preferredLabel=?', (lbl,))
    return c.fetchall()[0][0]

def label_inverse_transform(ID):
    c.execute('SELECT preferredLabel FROM skills_en WHERE ID=?', (ID,))
    return c.fetchall()[0][0]

def person_id_to_skillset(person_id):
    c.execute('SELECT skills FROM skill_profiles WHERE id=?', (str(person_id),))
    skillstr = literal_eval(c.fetchall()[0][0])
    #print(skillstr)
    #return 0
    return str_to_skillset(skillstr)

def str_to_skillset(skills_str):
    return set([label_transform_sql(a) for a in skills_str])

def match_func(person_skills, job_skills):
    return len(person_skills.intersection(job_skills))

def match_func_frequencies(person_skills, job_skills, freq_map):
    match_quality = 0
    for skill_id in person_skills.intersection(job_skills):
        match_quality += 1.0/sqrt(freq_map[skill_id])
    return match_quality


df = pickle.load(open( "df.pickle", "rb" ))
freq_map = get_frequency_map()

def get_results_for_person(person_id):
    ps = person_id_to_skillset(person_id)
    jobs = []

    for index, row in df.iterrows():
        job_skillset = row['skills_set']
        jobs.append([match_func_frequencies(ps, job_skillset, freq_map), row['occupation_name']])
        
        #old matching function
        #jobs.append([ic.match_func(ps, job_skillset), row['occupation_name']])

    #sort by biggest matching score first
    jobs.sort(key=lambda x : x[0], reverse=True)

    return jobs[:10]

