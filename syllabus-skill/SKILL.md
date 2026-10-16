---
name: cspdcl-je-electrical
description: Generate 5 FULL CSPDCL JE Electrical 2026 papers - 100Q, 100 Marks, 100% syllabus. Fixes 2-4 model question problem.
version: 2.0
author: hemantkumar30590-tech
---

# CSPDCL JE Electrical 2026 - 5 Set Generator

## Problem:
User says "5 set banao" - LLM gives 2-4 sample. This skill gives FULL 5 sets.

## Official Syllabus Pattern 2026:
- Total: 100 Q, 100 Marks, MCQ
- GK 10% (CG GK special) - 10 Q
- Reasoning 10% - 10 Q  
- Hindi 5% - 5 Q
- English 5% - 5 Q
- Computer 10% - 10 Q
- Technical Electrical 60% - 60 Q
    - Basic concepts, Circuit law, Magnetic Circuit, AC Fundamentals, Measurement, DC Machines, Transformers, Induction Motors, Single Phase, Synchronous, Generation Transmission Distribution, Switchgears, Estimation Costing, Utilization, Basic Electronics

## Rules for Generation:
1. MUST generate 100 questions per set, not sample
2. Each chapter MUST appear
3. Each of 5 sets must have DIFFERENT variant numbers
4. Output to cspdcl_output/ as txt + pdf
5. Validate coverage = 100%

## Usage:
When user says "CSPDCL JE" -> run cspdcl_je.py
