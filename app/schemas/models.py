from enum import Enum
from typing import Literal
from pydantic import BaseModel, Field

class ReqType(str, Enum):
    functional = 'functional'
    non_functional = 'non_functional'

class RequirementInput(BaseModel):
    id: str
    text: str = Field(min_length=3)
    type: ReqType

class SmellFinding(BaseModel):
    requirement_id: str
    smell_type:str
    text:str
    start:int
    end:int
    explanation:str

class DimensionScore(BaseModel):
    dimension: Literal["clarity", "consistency", "completeness", "testability", "traceability", "correctness"]
    score:int = Field(ge=0, le=100)
    justification:str
    suggestion: str = Field(default="", description="Optional suggestion for improvement")

class DimensionResult(BaseModel):
    scores: list[DimensionScore]
    improved_Requirements: str = Field(description="Optional improved requirements text based on the analysis")

class CrossRequirementAnalysis(BaseModel):
    req_id_a: str
    req_id_b: str
    issue_type: Literal["duplicate", "related"]
    similarity_score: float = Field(ge=0, le=1)
    reasoning: str

class RequirementAnalysis(BaseModel):
    id: str
    text: str
    type: ReqType
    smell_findings: list[SmellFinding]
    dimension_results: list[DimensionResult]
    overall_quality_score: float = Field(ge=0, le=100)
    cross_requirement_analysis: list[CrossRequirementAnalysis] = Field(default_factory=list)

class AnalyzeRequest(BaseModel):
    requirements: list[RequirementInput] = Field(min_length=1, description="List of requirements to analyze")

class AnalyzeResponse(BaseModel):
    analysis_results: list[RequirementAnalysis]
    cross_requirement_issues: list[CrossRequirementAnalysis] = Field(default_factory=list, description="List of cross-requirement issues found during analysis")
    average_quality_score: float = Field(ge=0, le=100, description="Average quality score across all analyzed requirements")