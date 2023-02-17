
tech_extr = '\n\nQ: What software technologies are mentioned in the abstract above?\n\nA:'
pgrm_extr = '\n\nQ: What programming languages are mentioned in the abstract above?\n\nA:'
dtbs_extr = '\n\nQ: What databases are mentioned in the abstract above?\n\nA:'
edu_extr  = '\n\nQ: What education institutes are mentioned in the abstract above?\n\nA:'

startup_fit  = '\n\nQ: Is the resume above a good fit to startups?\n\nA:'
profile_extr = '\n\nQ: Among Developer, Tester, Back End, Front End, BlockChain Developer, DataScience, Manager What is the best classification for the resume above?\n\nA:'
str_of_work_yr = '\n\nQ: What year did start work the candidate of the abstract above?\n\nA:'

EMPTY = ''

'''
query_map = {"technologies":tech_extr , "programming-languages":pgrm_extr,
             "databases" : dtbs_extr , "education": edu_extr, "fit-to-startups": startup_fit,
            "profile":profile_extr,"years-of-work":str_of_work_yr}
'''
query_map = {"technologies":tech_extr , 
             "programming-languages":pgrm_extr,
             "databases" : dtbs_extr , 
             "fit-to-startups": startup_fit,
             "profile":profile_extr}

def parse_answer(s):
  try:
     lidx = s.rindex('A:')
  except ValueError:
    return EMPTY

  return s[lidx+2:]

def extract_datamap(model,resume,max_length=400):
    response = {} 

    # extract all relevant information from the current resume
    for key,value in query_map.items():
        prompt = resume + value
        generated_text = model.generate(prompt,max_length=max_length)
        answer = parse_answer(generated_text)
        response[key] = answer.strip()

    return response
