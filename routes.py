from fastapi import APIRouter
import schemas

router = APIRouter()


@router.post("/print-variables/", description="POST two variables from front-end")
def print_variables_frontend(variables: schemas.FrontendVariables):
    print("variables are here....!!!", variables.name, variables.email)
    return {"response": "XYZ...!!!!", "variables": variables}
