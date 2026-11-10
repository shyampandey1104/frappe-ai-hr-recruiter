"""Unit tests for AIHRRecruiterEngine."""

from recruiter.engine import AIHRRecruiterEngine, JobOpening, CandidateResume


def test_candidate_screening_evaluation():
    engine = AIHRRecruiterEngine()

    job = JobOpening(
        job_id="JOB-PY-01",
        title="Senior Python & ERPNext Developer",
        min_experience_years=3.0,
        mandatory_skills=["Python", "Frappe", "ERPNext", "FastAPI"],
        preferred_skills=["Docker", "PostgreSQL"],
    )

    resume = CandidateResume(
        candidate_name="Rohit Sharma",
        email="rohit@example.com",
        phone="9876543210",
        resume_text="""
        Software Engineer with 4 years of experience building web applications.
        Proficient in Python, Frappe Framework, ERPNext customization, and FastAPI microservices.
        Experienced with Docker containers and MySQL databases.
        """,
    )

    report = engine.evaluate_candidate(resume, job)
    assert report.candidate_name == "Rohit Sharma"
    assert report.match_score_pct >= 90.0
    assert report.experience_matched is True
    assert "Shortlist" in report.recommendation
    assert len(report.missing_skills) == 0
