import galai as gal
import torch
import baseAnalysis as ba

# Init is ran on server startup
# Load your model to GPU as a global variable here.
def init():
    global model

    model = gal.load_model("base",num_gpus=1)


# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    global model

    # Parse out your arguments
    resume = model_inputs.get('resume', None)
    max_length = model_inputs.get('max_length', 60)
    top_p = model_inputs.get('top_p', None)
    new_doc = model_inputs.get('new_doc', False)
    if resume == None:
        return {'message': "No resume provided"}
    
    # Run the model
    #output = model.generate(prompt,max_length=max_length,top_p=top_p,new_doc=new_doc)
    output = ba.extract_datamap(model,resume,max_length)

    result = {"output": output}

    # Return the results as a dictionary
    return result
