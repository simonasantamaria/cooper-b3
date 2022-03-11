from pydantic import BaseModel, EmailStr


class FrontendVariables(BaseModel):
    name: str
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "name": "Muhammad Hassan",
                "email": "hassan1731996@gmail.com"
            }
        }
