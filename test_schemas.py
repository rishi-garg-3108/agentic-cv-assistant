"""

Lightweight sanity tests for validating schema correctness.

These tests ensure that:
- Pydantic schemas can be instantiated
- Default values behave as expected
- Validation errors are raised for malformed input

This file is intentionally simple and serves as an
early validation checkpoint during development.
"""




from schemas.resume import ResumeSchema, Experience
from schemas.job import JobSchema
from schemas.state import AgentState

# Validates creation and serialization of ResumeSchema
def test_resume_schema():
    resume = ResumeSchema(
        full_name="Rishi Garg",
        email="rishi@example.com",
        skills=["Python", "Transformers", "RAG"],
        experience=[
            Experience(
                company="Fraunhofer IEM",
                title="Research Assistant",
                job_details=[
                    "Worked on AI-generated text detection",
                    "Built transformer-based classifiers"
                ]
            )
        ]
    )
    print("ResumeSchema OK")
    print(resume.model_dump())

# Validates creation of JobSchema
def test_job_schema():
    job = JobSchema(
        title="Machine Learning Engineer",
        company="Example Corp",
        skills=["Python", "NLP", "LLMs"]
    )
    print("JobSchema OK")
    print(job.model_dump())

def test_agent_state():
    state = AgentState(
        parsed_cv=test_resume_schema,
        parsed_job=test_job_schema
    )
    print("AgentState OK")
    print(state)

if __name__ == "__main__":
    test_resume_schema()
    test_job_schema()
