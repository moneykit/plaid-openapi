# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class JWKPublicKey(BaseModel):
    """A JSON Web Key (JWK) that can be used in conjunction with [JWT libraries](https://jwt.io/#libraries-io) to verify Plaid webhooks"""


    alg: str = Field( description="The alg member identifies the cryptographic algorithm family used with the key.")
    crv: str = Field( description="The crv member identifies the cryptographic curve used with the key.")
    kid: str = Field( description="The kid (Key ID) member can be used to match a specific key. This can be used, for instance, to choose among a set of keys within the JWK during key rollover.")
    kty: str = Field( description="The kty (key type) parameter identifies the cryptographic algorithm family used with the key, such as RSA or EC.")
    use: str = Field( description="The use (public key use) parameter identifies the intended use of the public key.")
    x: str = Field( description="The x member contains the x coordinate for the elliptic curve point, provided as a base64url-encoded string of the coordinate's big endian representation.")
    y: str = Field( description="The y member contains the y coordinate for the elliptic curve point, provided as a base64url-encoded string of the coordinate's big endian representation.")
    created_at: int = Field( description="The timestamp when the key was created, in Unix time.")
    expired_at: Optional[int] = Field(default=None, description="The timestamp when the key expired, in Unix time.")

JWKPublicKey.update_forward_refs()
