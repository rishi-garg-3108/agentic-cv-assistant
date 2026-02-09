"""
resume.py

Defines the structured schema for a candidate's resume (CV).

This module converts unstructured resume text into a strongly-typed
domain object that can be reliably used by agents for:
- skill matching
- gap analysis
- resume optimization
- formatting (LaTeX / PDF)

The schema is intentionally detailed to mirror how ATS systems
internally represent candidate profiles.
"""


from typing import List, Optional
from pydantic import BaseModel, Field

# Represents a single work experience entry in the resume
# Each entry corresponds to a role held by the candidate
class Experience(BaseModel):
    company: Optional[str] = None
    title: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    location: Optional[str] = None
    job_details: List[str] = Field(default_factory=list) # Flat list for ATS keyword matching
    

# Represents an education record such as a degree or certification program
class Education(BaseModel):
    school: Optional[str] = None
    degree: Optional[str] = None
    field: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

# Top-level resume schema
# Acts as the canonical representation of a candidate's CV
# used throughout the agentic pipeline

class Project(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    links: List[str] = Field(default_factory=list)
    tech: List[str] = Field(default_factory=list)

class ResumeSchema(BaseModel):
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    links: List[str] = Field(default_factory=list)
    summary: Optional[str] = None
    skills: List[str] = Field(default_factory=list)
    experience: List[Experience] = Field(default_factory=list)
    education: List[Education] = Field(default_factory=list)
    certifications: List[str] = Field(default_factory=list)
    projects: List[Project] = Field(default_factory=list)
