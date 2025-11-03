"""
User class to use for realistic datetime example with Polyfactory
"""
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, AwareDatetime


class User(BaseModel):
    """
    User example that does not have an aware datetime
    """
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda dt: dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        }
    )
    first_name: str
    last_name: str
    last_login: datetime = Field(default_factory=datetime.now)

class UserAwareDateTime(User):
    last_login: AwareDatetime