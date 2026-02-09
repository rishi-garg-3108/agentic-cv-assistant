"""

Defines the structured schema for a job description.

This module converts unstructured job postings into a normalized
representation that can be compared against a candidate resume
for ATS-style matching and gap analysis.
"""


from typing import List, Optional
from pydantic import BaseModel, Field

class JobSchema(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    summary: Optional[str] = None
    requirements: List[str] = Field(default_factory=list)
    responsibilities: List[str] = Field(default_factory=list)
    skills: List[str] = Field(default_factory=list) # Explicit skills extracted from JD
