"""AI Candidate Screening & Resume Scoring Agent for Frappe HRMS."""

import re
from typing import Dict, Any, List, Set
from pydantic import BaseModel


class JobOpening(BaseModel):
    job_id: str
    title: str
    min_experience_years: float
    mandatory_skills: List[str]
    preferred_skills: List[str]


class CandidateResume(BaseModel):
    candidate_name: str
    email: str
    phone: str
    resume_text: str


class CandidateMatchReport(BaseModel):
    candidate_name: str
    match_score_pct: float
    experience_matched: bool
    matched_skills: List[str]
    missing_skills: List[str]
    recommendation: str  # Shortlist for Interview, Review Manually, Reject


class AIHRRecruiterEngine:
    """Matches candidate skills against Job Openings using NLP keyword extraction."""

    def evaluate_candidate(self, resume: CandidateResume, job: JobOpening) -> CandidateMatchReport:
        text_lower = resume.resume_text.lower()

        # Extract Experience
        exp_match = re.search(r"(\d+(?:\.\d+)?)\+?\s*(?:years?|yrs?)\s*(?:of)?\s*exp", text_lower)
        cand_exp = float(exp_match.group(1)) if exp_match else 1.0
        exp_ok = cand_exp >= job.min_experience_years

        # Skills Matching
        matched: List[str] = []
        missing: List[str] = []

        for skill in job.mandatory_skills:
            # Word boundary search
            if re.search(r"\b" + re.escape(skill.lower()) + r"\b", text_lower):
                matched.append(skill)
            else:
                missing.append(skill)

        # Score calculation: Mandatory skills weight = 70%, Experience = 30%
        skill_score = (len(matched) / max(len(job.mandatory_skills), 1)) * 70.0
        exp_score = 30.0 if exp_ok else 10.0
        total_score = min(100.0, skill_score + exp_score)

        if total_score >= 75.0:
            rec = "Shortlist for Technical Interview"
        elif total_score >= 50.0:
            rec = "Review Manually by Hiring Manager"
        else:
            rec = "Does Not Meet Minimum Criteria"

        return CandidateMatchReport(
            candidate_name=resume.candidate_name,
            match_score_pct=round(total_score, 1),
            experience_matched=exp_ok,
            matched_skills=matched,
            missing_skills=missing,
            recommendation=rec,
        )
