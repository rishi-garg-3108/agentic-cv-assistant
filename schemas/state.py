"""

Defines the AgentState object that acts as shared memory
across the entire agentic workflow.

This state tracks:
- raw inputs
- parsed structured data
- retrieved RAG context
- intermediate reasoning results
- final outputs

Agents read from and write to this state, enabling
tool autonomy and multi-step orchestration.
"""


from typing import List, Optional
from pydantic import BaseModel
from schemas.resume import ResumeSchema
from schemas.job import JobSchema

class AgentState(BaseModel):
    raw_cv_text: Optional[str] = None
    raw_job_description: Optional[str] = None

    parsed_cv: Optional[ResumeSchema] = None
    parsed_job: Optional[JobSchema] = None

    retrieved_guidelines: List[str] = []
    skill_gaps: List[str] = []

    optimized_cv: Optional[ResumeSchema] = None
    cover_letter: Optional[str] = None

    errors: List[str] = []
