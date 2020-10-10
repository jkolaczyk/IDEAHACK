import sqlite3
import pandas as pd
import pickle
from ast import literal_eval
from math import sqrt
from io import StringIO



def load_db_to_memory():
    con = sqlite3.connect("database.db")
    tempfile = StringIO()
    for line in con.iterdump():
        tempfile.write('%s\n' % line)
    con.close()
    tempfile.seek(0)

    # Create a database in memory and import from tempfile
    conn = sqlite3.connect(":memory:")
    conn.cursor().executescript(tempfile.read())
    conn.commit()
    return conn

def get_skill_names_map():
    c.execute('SELECT skills_en.ID, skills_en.preferredLabel FROM skills_en')
    res = c.fetchall()
    names_map = {row[0]: row[1] for row in res} 
    return names_map

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

def skill_id_to_name(ID):
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

def get_results_for_person(person_id):
    ps = person_id_to_skillset(person_id)
    jobs = []

    for index, row in df.iterrows():

        #if index % (df.shape[0]//100) == 0:
        #    print (index//(df.shape[0]//100))

        job_skillset = row['skills_set']

        match_quality = 0
        matching_skills = []

        for skill_id in ps.intersection(job_skillset):
            mq = 1.0/sqrt(freq_map[skill_id])
            matching_skills.append([mq, skill_id])
            match_quality += mq
        
        matching_skills.sort(key=lambda x : x[0], reverse=True)
        matching_skills = [skill_names_map[a[1]] for a in matching_skills]

        #lacking_skills = []
        lacking_skills = [[1.0/sqrt(freq_map[skill_id]), skill_names_map[skill_id]] for skill_id in job_skillset - ps if skill_id in freq_map]
        lacking_skills.sort(key=lambda x : x[0], reverse=True)
        lacking_skills = [a[1] for a in lacking_skills]
        

        jobs.append([match_func_frequencies(ps, job_skillset, freq_map), row['occupation_name'], matching_skills[:5], lacking_skills[:5]])
        
        #old matching function
        #jobs.append([ic.match_func(ps, job_skillset), row['occupation_name']])

    #sort by biggest matching score first
    jobs.sort(key=lambda x : x[0], reverse=True)

    return jobs[:10]

conn = load_db_to_memory()
c = conn.cursor()
df = pickle.load(open( "df.pickle", "rb" ))
freq_map = get_frequency_map()
skill_names_map = get_skill_names_map()

if __name__ == "__main__":
    print(get_results_for_person(10)[0])