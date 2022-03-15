from fastapi import APIRouter
import schemas

router = APIRouter()


@router.post("/print-variables/", description="POST two variables from front-end")
def print_variables_frontend(variables: schemas.FrontendVariables):
    print("variables are here....!!!", variables.name, variables.email)
    return {"submitted_variables": variables, "modified_variable_name": variables.name + " !!!----", }


#@router.get("/{name}")
#def root(name: str):
#    print('its here...')
#    return {"variable": name}
@router.get("/")
def root():
    return "Welcome Here..!!"
