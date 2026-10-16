import random, os, json
from datetime import datetime

SYLLABUS = {
 "gk": ["Current Affairs","Indian History","CG Geography - Nadi Jila","Constitution","Science Tech","CG Yojana"],
 "reasoning": ["Analogies","Similarities","Problem Solving","Relationship","Space Visual","Number Series","Arith Reasoning"],
 "hindi": ["Grammar","Vocab","Comprehension","Fill Blanks","Error Detection","Antonyms","Muhavare"],
 "english": ["Synonyms","Antonyms","One Word","Error Detection","Idioms","Passage"],
 "computer": ["Fundamentals","MS Office","Internet","Hardware Software","Abbreviations"],
 "tech": [
  "Basic concepts R L C Power Energy",
  "Kirchhoff Network Theorems",
  "Magnetic Circuit flux mmf reluctance",
  "AC Fundamentals RMS Peak Resonance star delta",
  "Measurement Wattmeter Energy meter CRO CT PT",
  "DC Machines Characteristics Speed Control",
  "Transformers OC SC Tests Regulation",
  "Induction Motors Torque-speed Starting",
  "Single Phase Fractional KW Motors",
  "Synchronous Machines Alternator Regulation",
  "Generation Transmission Distribution Load Factor Tariff Faults",
  "Switchgears Circuit Breakers Relays Buchholz",
  "Estimation Costing IE Rules Earthing",
  "Utilization Illumination Heating Welding Drives",
  "Basic Electronics PN Junction BJT JFET"
 ]
}

def make_set(n):
    q=1; paper=[]
    def add(name, topics, count):
        nonlocal q; sec=[]
        random.shuffle(topics)
        for i in range(count):
            t=topics[i%len(topics)]
            sec.append(f"Q{q}. [{t}] CSPDCL JE Electrical - {name} - Set {n} - Var {random.randint(100,999)}")
            q+=1
        paper.append((name, sec))
    add("GK (10)", SYLLABUS["gk"]*2, 10)
    add("Reasoning (10)", SYLLABUS["reasoning"]*2, 10)
    add("Hindi (5)", SYLLABUS["hindi"], 5)
    add("English (5)", SYLLABUS["english"], 5)
    add("Computer (10)", SYLLABUS["computer"]*2, 10)
    add("Technical Electrical (60)", SYLLABUS["tech"]*4, 60)
    return paper

os.makedirs("cspdcl_output", exist_ok=True)
for set_no in range(1,6):
    p=make_set(set_no)
    fname=f"cspdcl_output/CSPDCL_JE_Electrical_2026_Set_{set_no}.txt"
    with open(fname,"w",encoding="utf-8") as f:
        f.write(f"CSPDCL JE Electrical 2026 - SET {set_no} - 100 Marks\nDate:{datetime.now()}\n"+"="*60+"\n")
        for name, qs in p:
            f.write(f"\n{name}\n"+"-"*40+"\n")
            for qq in qs: f.write(qq+"\n")
    print(f"✅ Set {set_no} ban gaya - {fname}")

print("\n5 SET PURE BAN GAYE! ls cspdcl_output/ se dekho")
