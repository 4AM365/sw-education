1) Core Python thinking (not syntax)

“Effective Python” – Brett Slatkin
Read items selectively. Focus on:

Items on functions, generators, context managers

Mutability, default args, dataclasses
This fixes 80% of “why is this behaving weirdly?” problems.

Official Python Tutorial (sections, not cover-to-cover)
Skim:

Modules & Packages

Virtual environments

Standard library overview

2) Package & project structure (this is what you’re missing)

“Python Packaging User Guide” (packaging.python.org)
Read once, slowly:

pyproject.toml

src-layout vs flat layout

dependency groups

versioning
This directly answers “how should this repo be shaped?”

“The Hitchhiker’s Guide to Python”
Skim chapters on:

Project structure

Testing

Logging

Style
Old, but still good mental models.

3) Design & architecture (Python-specific, not CS theory)

“Architecture Patterns with Python” – Percival & Gregory
This is the bridge from scripts → systems.
Read:

Chapters on boundaries, services, adapters

Ignore the DDD religious parts if they annoy you
You’ll immediately see how to separate CV logic, IO, models, and orchestration.

“Clean Code” (selectively)
Ignore Java-isms. Focus on:

Function size

Naming

Dependency direction
Apply mentally, not literally.

4) CV-adjacent, pragmatic

OpenCV Python examples repo (read structure, not code)
Ask: where is state? where is IO? where are transforms?

FastAPI source (skim)
Not to copy, but to see:

Dependency injection

Clear boundaries

Explicit contracts

5) Testing & sanity

pytest docs (intro + fixtures)
If your code isn’t testable, your architecture is lying to you.