# Project Plan: Industrial AI Inspection & Intelligence Platform

**Project start:** 24 November 2026\
**Final deadline:** 31 December 2026\
**Duration:** 38 calendar days (including both start and finish dates)\
**Project type:** Flagship portfolio project\
**Primary positioning:** AI/ML Engineer with a Computer Vision
specialisation and production-oriented engineering skills

------------------------------------------------------------------------

## 1. Project objective

Build an end-to-end industrial inspection platform that accepts an image
of a manufactured component, identifies and localises visual defects,
calculates inspection measurements where calibration information is
available, stores inspection results, and lets users query inspection
reports through a retrieval-augmented generation (RAG) assistant.

The project should demonstrate that I can do more than train a model. It
should show that I can:

1.  Prepare and understand a real-world computer-vision dataset.
2.  Train, evaluate and explain a deep-learning model.
3.  Build reusable image-processing and measurement components.
4.  Develop a tested backend and database layer.
5.  integrate a language-model application grounded in stored reports
    and documentation.
6.  Track experiments and model versions.
7.  Package, deploy and document an application.
8.  Make engineering trade-offs and explain limitations.

The project is deliberately based on industrial inspection because it
extends my professional experience in image processing, defect
inspection, calibration, measurement, Python, C++, and AWS without
reusing employer-owned code or data.

> **Data/IP rule:** Use only public datasets, self-generated images, and
> independently written code. Do not use client images, confidential
> information, proprietary algorithms, or employer-owned code from
> Genpact or Zentron Labs.

------------------------------------------------------------------------

### 1.1 Problem statement (in simple terms)

Factories inspect products to find defects such as scratches, dents, cracks,
missing parts or unusual surface patterns. Manual inspection can be slow,
subjective and difficult to keep consistent. Inspection results can also be
scattered across images and reports, making it harder to compare past
inspections or understand recurring problems.

**The problem this project addresses:** Build a software tool that helps an
inspector examine product images, automatically highlights possible defects,
records the inspection results, and makes those results easier to search and
understand.

The tool will also calculate physical measurements when the image includes a
valid scale reference or the user supplies a known reference distance. It will
not claim to know real-world dimensions from an uncalibrated image.

### 1.2 Proposed solution

A user uploads an image. The system analyses it with a computer-vision model,
shows the suspected defect regions and a confidence/anomaly score, optionally
calculates calibrated measurements, and saves the result. The user can later
view inspection history or ask an AI assistant questions about saved reports.
The assistant must base its answers on retrieved records and show which
records support the answer.

## 2. Product scope

### 2.1 User workflow

1.  A user uploads an inspection image.
2.  The backend validates the image and creates an inspection record.
3.  The computer-vision pipeline predicts whether the image contains an
    anomaly/defect and produces a localisation mask or heatmap.
4.  The image-processing module calculates relevant geometric
    measurements when a valid calibration value is supplied.
5.  The system stores the original image, prediction artefacts, model
    version, metrics and inspection metadata.
6.  The user views the result and can retrieve previous inspections.
7.  The user asks the AI assistant questions such as:
    -   "Summarise the defects found in the last inspection."
    -   "Which inspections had the highest anomaly score?"
    -   "Explain the difference between these two inspection reports."
8.  The assistant retrieves relevant records and documentation and
    answers with references to the retrieved records.

### 2.2 Core modules

  -----------------------------------------------------------------------
  Module                  Responsibility          Main technologies
  ----------------------- ----------------------- -----------------------
  Data pipeline           Dataset ingestion,      Python, NumPy, OpenCV,
                          validation,             PyTorch
                          preprocessing, splits   
                          and augmentation        

  CV inference            Defect/anomaly          PyTorch, torchvision or
                          localisation and        segmentation model
                          scoring                 

  Measurement             Calibration and         OpenCV, NumPy
                          pixel-to-metric         
                          conversion              

  Backend                 Upload, inference,      FastAPI, Pydantic
                          inspection history and  
                          report APIs             

  Persistence             Inspection metadata and PostgreSQL, SQLAlchemy
                          report records          

  File storage            Original images and     Local storage for
                          generated artefacts     development; AWS S3 for
                                                  deployment

  Experiment tracking     Parameters, metrics and MLflow
                          model artefacts         

  AI assistant            Search and              Embeddings, RAG, an LLM
                          question-answering over API, pgvector
                          inspection reports      

  Packaging and delivery  Reproducible runtime    Docker, Docker Compose,
                          and automated checks    GitHub Actions

  Observability           Application logs,       Python logging, FastAPI
                          errors and basic health health endpoint, AWS
                          checks                  logs if deployed
  -----------------------------------------------------------------------

------------------------------------------------------------------------

### 2.3 Recommended technology stack

This is the **chosen stack for the project**, rather than a list of every
technology that could be used. Keep the number of frameworks small so the
project can be completed by 31 December.

| Layer | Technology | What it will be used for |
|---|---|---|
| Main language | Python 3.11 or 3.12 | Application, data pipeline, model training and inference |
| Numerical/image processing | NumPy, OpenCV, Pillow | Image loading, preprocessing, calibration and measurements |
| Deep learning | PyTorch, torchvision | Training and running the defect-localisation model |
| Model architecture | U-Net with a pretrained encoder | Pixel-level defect localisation using labelled masks |
| Dataset | MVTec AD (two selected categories) | Public industrial anomaly images and defect masks |
| API/backend | FastAPI, Pydantic | Image upload, inference, inspection history and RAG endpoints |
| Database/ORM | PostgreSQL, SQLAlchemy | Inspection metadata, predictions and report records |
| Vector search | pgvector | Store and retrieve document/report embeddings for RAG |
| Embeddings | sentence-transformers | Convert report text into vectors for semantic retrieval |
| LLM integration | One hosted LLM API, accessed through a small provider-independent wrapper | Generate answers using retrieved inspection context |
| Experiment tracking | MLflow | Track training parameters, metrics, runs and model artefacts |
| Testing/quality | pytest, Ruff | Unit/integration tests, linting and basic code-quality checks |
| Containers | Docker, Docker Compose | Reproducible local application and database environment |
| CI | GitHub Actions | Run linting and tests automatically on pushes and pull requests |
| Cloud storage | AWS S3, boto3 | Store uploaded images and generated inspection artefacts in the cloud |
| Cloud hosting | AWS EC2 (optional deployment target) | Host the containerised API if deployment is feasible within time/budget |
| Documentation/API exploration | Markdown, Mermaid, FastAPI Swagger UI | README, architecture diagrams and interactive API documentation |

#### Keep the implementation deliberately simple

- Use **one** deep-learning framework: PyTorch. Do not add TensorFlow.
- Use **one** backend framework: FastAPI.
- Use PostgreSQL with pgvector for both relational records and vector search;
  avoid introducing a second database unless there is a clear need.
- Implement the first RAG pipeline directly with embedding, retrieval and LLM
  API calls. A framework such as LangChain is optional, not a prerequisite.
- Use FastAPI's automatically generated Swagger UI as the initial interface.
  A separate frontend (for example, Streamlit) is a stretch goal, not a
  deadline-critical requirement.
- Run locally with Docker Compose before attempting AWS deployment.
- Keep AWS deployment optional if account access, cost or configuration puts
  the 31 December release at risk. The local Docker deployment remains a
  required deliverable.

#### Skills this stack is intended to demonstrate

Python software engineering, computer vision, deep learning, model
assessment, SQL/database design, backend/API development, NLP/LLM application
development, retrieval-augmented generation, experiment tracking, testing,
containerisation, CI/CD, cloud object storage and technical documentation.

## 3. Scope control: must-have versus stretch

The deadline is fixed. A complete, reliable vertical slice is more
valuable than many half-finished integrations.

### Must-have by 31 December

-   A documented public dataset and reproducible train/validation/test
    split.
-   A trained and evaluated defect/anomaly localisation model.
-   A working OpenCV calibration and measurement module with explicit
    calibration input.
-   FastAPI endpoints for upload, inference, inspection retrieval and
    health checks.
-   PostgreSQL persistence for inspection metadata and results.
-   RAG assistant that retrieves from inspection reports and project
    documentation, and identifies the records used to answer.
-   MLflow experiment tracking.
-   Docker Compose setup for the application and database.
-   Automated unit and API tests.
-   GitHub Actions workflow for linting and tests.
-   A deployed demonstration if cloud setup and cost permit; otherwise a
    fully reproducible local deployment plus deployment instructions.
-   Architecture diagram, README, API documentation, model card and demo
    video.

### Stretch goals (only after must-haves work)

-   A browser-based dashboard.
-   A second model or second dataset category.
-   Asynchronous inference with a task queue.
-   User authentication and role-based access.
-   Advanced monitoring or drift detection.
-   Kubernetes, distributed training, TensorRT or edge optimisation.
-   Fine-tuning an LLM.

**Do not start Kubernetes, a multi-agent framework, or custom LLM
fine-tuning during this project.** They are not necessary to demonstrate
the target competencies.

------------------------------------------------------------------------

## 4. Dataset and modelling strategy

### Recommended starting point

Use the **MVTec AD dataset** (public industrial anomaly-detection
benchmark). Start with only two object/texture categories to keep the
project manageable. Review its licence and download conditions before
use, and cite the dataset in the repository.

Dataset reference:
https://www.mvtec.com/company/research/datasets/mvtec-ad

### Modelling plan

1.  Inspect the dataset structure, image dimensions, masks and category
    distribution.
2.  Create a reproducible split and document any limitations of the
    benchmark's provided split.
3.  Establish a simple baseline before trying a more complex model.
4.  Train a segmentation model using the available defect masks for
    selected categories.
5.  Evaluate image-level and pixel-level performance.
6.  Save predictions, overlays and representative failure cases.
7.  Track parameters, metrics and artefacts in MLflow.

Suggested baseline: a small U-Net-style segmentation model using a
pretrained encoder where practical. Keep the architecture understandable
and training reproducible.

### Metrics to report

-   Image-level: precision, recall, F1 and ROC-AUC where the evaluation
    setup supports them.
-   Pixel-level: precision, recall, Dice score, IoU and pixel ROC-AUC
    where appropriate.
-   Operational: inference latency, model size and memory use on the
    tested machine.

Do not report a metric unless its calculation and evaluation split are
documented. Compare the model with a simple baseline and include false
positives and false negatives in the error analysis.

### Calibration and measurement

The public anomaly dataset may not contain physical scale references.
Therefore, implement calibration as a separate, clearly scoped module:

-   Accept a known physical distance and the corresponding pixel
    distance, or detect a deliberately provided calibration marker.
-   Calculate pixels-per-unit and convert pixel measurements into
    physical units.
-   Reject missing, invalid or ambiguous calibration input.
-   Test using synthetic images with known dimensions and manually
    verified examples.
-   State clearly that physical measurements are valid only when the
    calibration reference is valid and the imaging geometry is
    appropriate.

Do not claim that arbitrary MVTec images provide real-world dimensions.

------------------------------------------------------------------------

## 5. Phase plan and completion dates

Dates are inclusive. Each phase has a concrete exit criterion. The next
phase should not silently absorb unfinished work: reduce optional scope
if a milestone slips.

### Phase 0 --- Project definition and repository setup

**24--25 November 2026**

**Work** - Create the GitHub repository and this project plan. - Define
the two dataset categories and inspect dataset licence/terms. - Create a
clean Python environment and dependency management approach. - Establish
a modular repository layout. - Add README skeleton, `.gitignore`,
configuration handling and logging. - Create a project board with tasks
and priorities.

**Deliverables** - Repository with initial structure. - Dataset decision
and data documentation. - Reproducible environment setup instructions. -
Initial architecture sketch.

**Exit criteria** - A fresh environment can install dependencies. - A
small sample image can be loaded and validated. - No secrets,
credentials or datasets are committed accidentally.

### Phase 1 --- Data pipeline and computer-vision baseline

**26 November--2 December 2026**

**Work** - Download and inspect the selected MVTec AD categories. -
Implement dataset loading and validation. - Document image and mask
formats, class balance and split strategy. - Implement preprocessing and
training-time augmentation. - Create visualisation utilities for images,
masks and overlays. - Build a simple baseline and record initial
metrics. - Add tests for dataset loading, mask alignment and
preprocessing.

**Deliverables** - Reproducible data pipeline. - Dataset exploration
report. - Baseline metrics and visual examples. - Unit tests for data
utilities.

**Exit criteria** - Training and evaluation data are separated
correctly. - Image/mask transformations preserve alignment. - The
baseline can be rerun from documented commands.

### Phase 2 --- Deep-learning model and evaluation

**3--9 December 2026**

**Work** - Implement a segmentation model in PyTorch. - Establish a
training loop with validation, checkpoints and reproducible seeds. -
Track experiments in MLflow. - Evaluate image-level and pixel-level
performance using suitable metrics. - Inspect false positives, false
negatives and category-specific failures. - Export a small set of
prediction overlays. - Implement a stable inference interface
independent of the training code.

**Deliverables** - Trained model checkpoint. - Evaluation script and
results. - MLflow experiment records. - Model card describing intended
use, data, metrics and limitations. - Inference function with
predictable input/output types.

**Exit criteria** - A saved model can be loaded in a clean inference
process. - Evaluation is repeatable. - Results include metrics and
qualitative failure analysis. - The model is not described as
production-validated merely because it performs on a benchmark.

### Phase 3 --- Measurement module and backend

**10--15 December 2026**

**Work** - Implement pixel-to-metric calibration as an independent
module. - Add validation for missing or invalid calibration
information. - Test measurement calculations with synthetic images of
known dimensions. - Create FastAPI endpoints: - `GET /health` -
`POST /inspections` - `GET /inspections/{inspection_id}` -
`GET /inspections` - `GET /inspections/{inspection_id}/report` - Add
request/response schemas with Pydantic. - Persist inspection metadata,
predictions, model version and measurement information in PostgreSQL. -
Store image and output artefacts locally initially; keep a storage
interface that can later use S3. - Add API and database integration
tests.

**Deliverables** - Tested calibration/measurement package. - FastAPI
application. - PostgreSQL schema and persistence layer. - Working
image-upload-to-inference-to-record workflow.

**Exit criteria** - An uploaded image can be processed through the
API. - The result and model version are persisted. - Invalid inputs
return useful errors. - Tests cover successful and failure paths.

### Phase 4 --- RAG inspection assistant

**16--20 December 2026**

**Work** - Prepare a small document collection containing project
documentation, model card, inspection explanations and generated sample
reports. - Chunk and embed the documents. - Store embeddings and
metadata in PostgreSQL with pgvector, or use a simpler vector store if
pgvector setup threatens the deadline. - Retrieve relevant
report/document chunks for a user query. - Generate answers using an LLM
API. - Include retrieved source/inspection identifiers in the
response. - Add guardrails for insufficient evidence: the assistant
should say when the stored information does not answer the question. -
Evaluate a small set of representative questions for retrieval
relevance, groundedness and incorrect claims.

**Deliverables** - Document ingestion and indexing script. - Retrieval
and answer-generation pipeline. - API endpoint for asking questions. -
Small RAG evaluation set and results.

**Exit criteria** - The assistant retrieves relevant stored records for
test questions. - Answers identify supporting records or documents. - It
can abstain when the evidence is insufficient. - API keys are read from
environment variables and never committed.

### Phase 5 --- Packaging, cloud storage and CI/CD

**21--26 December 2026**

**Work** - Containerise the backend and required services. - Create
Docker Compose configuration for local development. - Add persistent
database volumes and environment-based configuration. - Add an S3
storage implementation behind the storage interface. - Add GitHub
Actions for dependency installation, linting and automated tests. - Add
structured logs, request identifiers and useful error messages. - Add
basic health/readiness checks. - Deploy a demonstration to an
appropriate AWS setup if time and budget permit. - Document setup,
deployment, security considerations and cleanup steps.

**Deliverables** - Dockerfile and Docker Compose configuration. - CI
workflow. - S3 storage integration. - Deployment guide and, if
completed, a live demo URL.

**Exit criteria** - A new developer can run the application using
documented steps. - Automated checks run on pushes or pull requests. -
No credentials are stored in the repository. - Cloud resources have
budget limits and a cleanup procedure.

### Phase 6 --- Integration, documentation and portfolio release

**27--31 December 2026**

**Work** - Run end-to-end tests from image upload through stored result
and RAG query. - Fix critical bugs and remove unused code. - Verify that
the README instructions work from a clean checkout. - Add architecture
and data-flow diagrams. - Document API routes, configuration, model
evaluation and known limitations. - Add sample requests/responses and
screenshots. - Record a concise demonstration video. - Update resume and
GitHub profile with accurate, measured project outcomes. - Prepare
interview explanations for design decisions and trade-offs.

**Deliverables** - Versioned release (e.g. `v1.0.0`). - Complete README
and architecture diagram. - Model card and evaluation report. - Demo
video and screenshots. - Resume-ready project description.

**Exit criteria** - The must-have features work together. - Setup and
test instructions have been verified. - No confidential data or secrets
are present. - Known limitations are documented honestly. - Repository
is ready to share with recruiters.

------------------------------------------------------------------------

## 6. Suggested repository structure

``` text
industrial-ai-inspection/
├── README.md
├── PROJECT_PLAN.md
├── pyproject.toml
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── configs/
│   ├── data.yaml
│   ├── model.yaml
│   └── app.yaml
├── data/
│   └── README.md
├── artifacts/
│   └── README.md
├── notebooks/
│   └── 01_dataset_exploration.ipynb
├── src/
│   └── inspection/
│       ├── data/
│       ├── models/
│       ├── training/
│       ├── evaluation/
│       ├── inference/
│       ├── imaging/
│       │   ├── calibration.py
│       │   └── measurement.py
│       ├── api/
│       ├── db/
│       ├── storage/
│       ├── rag/
│       └── core/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── scripts/
│   ├── prepare_data.py
│   ├── train.py
│   ├── evaluate.py
│   └── index_documents.py
├── docs/
│   ├── architecture.md
│   ├── dataset.md
│   ├── model_card.md
│   ├── evaluation.md
│   ├── api.md
│   └── deployment.md
└── .github/
    └── workflows/
        └── ci.yml
```

Keep notebooks for exploration. Put reusable code in `src/`. Do not
commit large datasets, model weights, generated images or secrets; use
documented download instructions and an appropriate artefact store.

------------------------------------------------------------------------

## 7. Skill-gap coverage matrix

This matrix maps the gaps identified from my resume review to evidence
that the project should produce.

  -----------------------------------------------------------------------
  Skill / gap             Existing evidence from  Project evidence
                          resume                  required
  ----------------------- ----------------------- -----------------------
  Python engineering      Professional Python     Modular package,
                          experience              typing, configuration,
                                                  logging, error handling

  Software testing        Not clearly             pytest unit,
                          demonstrated            integration and
                                                  end-to-end tests

  SQL                     Not listed              PostgreSQL schema,
                                                  joins, indexes and
                                                  persistence

  Backend development     Not listed              FastAPI REST service
                                                  and Pydantic schemas

  Deep learning           EfficientNet/PyTorch    Reproducible training,
                          experience              validation,
                                                  checkpointing and
                                                  evaluation

  Modern CV               OpenCV and industrial   Segmentation/anomaly
                          image processing        localisation, overlays
                                                  and quantitative
                                                  metrics

  Model evaluation        Accuracy stated for     Precision, recall, F1,
                          prior project           IoU/Dice, ROC-AUC where
                                                  appropriate, error
                                                  analysis

  NLP / LLM               Interest but no stated  Embeddings, retrieval,
                          professional experience RAG endpoint and
                                                  evaluation

  MLOps                   AWS/SageMaker exposure  MLflow runs, model
                                                  artefacts and version
                                                  tracking

  Docker                  Not listed              Reproducible
                                                  containerised
                                                  application

  CI/CD                   Not listed              GitHub Actions workflow
                                                  running tests and
                                                  checks

  Cloud                   S3, Lambda and          S3 integration and
  storage/deployment      SageMaker exposure      documented AWS
                                                  deployment

  Observability           Not clearly             Structured logs, health
                          demonstrated            checks and error
                                                  reporting

  System design           Not clearly             Architecture diagram,
                          demonstrated            storage abstraction and
                                                  documented trade-offs

  C++                     Professional            Retain as an existing
                          vision-library          strength; no need to
                          experience              force C++ into this
                                                  project
  -----------------------------------------------------------------------

The project does not need to prove expert-level proficiency in every
technology. It needs to demonstrate sound working knowledge and the
ability to explain the implementation.

------------------------------------------------------------------------

## 8. Definition of done

The project is complete only when the following are true:

### Product

-   [ ] A user can submit an image through the API.
-   [ ] The model returns an anomaly/defect score and localisation
    output.
-   [ ] The system records the prediction and model version.
-   [ ] Measurements are calculated only when valid calibration is
    supplied.
-   [ ] Inspection history can be retrieved.
-   [ ] The RAG assistant can answer questions using retrieved
    inspection information.

### Engineering

-   [ ] Code is modular and configuration is not hardcoded.
-   [ ] Unit and integration tests cover critical paths.
-   [ ] API errors are handled predictably.
-   [ ] PostgreSQL persistence works.
-   [ ] Docker Compose starts the local application.
-   [ ] CI runs tests and quality checks.
-   [ ] Secrets are not committed.
-   [ ] Logs and health checks are available.

### ML quality

-   [ ] Dataset source, licence and split are documented.
-   [ ] Baseline and final metrics are recorded.
-   [ ] Model limitations and failure cases are documented.
-   [ ] Inference is reproducible from a saved checkpoint.
-   [ ] RAG answers expose supporting records and can abstain.

### Portfolio

-   [ ] README includes problem, architecture, setup, usage and results.
-   [ ] Architecture diagram is included.
-   [ ] Model card and evaluation report are included.
-   [ ] Demo video or walkthrough is available.
-   [ ] Resume claims match what is actually implemented.

------------------------------------------------------------------------

## 9. Risk management

  -----------------------------------------------------------------------
  Risk                                Mitigation
  ----------------------------------- -----------------------------------
  Dataset/model training takes longer Limit the project to two
  than expected                       categories; establish a simple
                                      baseline early

  Segmentation performance is weak    Report honest results, inspect
                                      failures and compare with the
                                      baseline

  Dataset has no physical scale       Keep calibration independent and
  reference                           validate with synthetic known-scale
                                      images

  RAG integration becomes a time sink Use a simple retrieval pipeline and
                                      one LLM API; avoid agent frameworks

  AWS deployment introduces cost or   Complete Docker-based local
  configuration issues                deployment first; set a budget and
                                      clean up resources

  Too many technologies reduce        Treat the must-have list as the
  quality                             scope boundary; defer stretch goals

  Public dataset terms are unsuitable Review terms before committing;
                                      choose another appropriately
                                      licensed public dataset if
                                      necessary
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 10. Weekly operating rhythm

Use a repeatable routine rather than spending the entire day watching
tutorials.

Suggested daily allocation (approximately 4--5 hours):

-   **60--90 minutes:** Learn the concept needed for the current
    milestone.
-   **2--2.5 hours:** Implement it in the project.
-   **30--45 minutes:** Tests, debugging and code review.
-   **30 minutes:** Notes, documentation and interview revision.

At the end of each week:

1.  Demonstrate the working feature to yourself.
2.  Run the tests from a clean state.
3.  Update the README and project board.
4.  Record what remains unfinished.
5.  Cut optional work before moving the deadline.

Reserve at least one lighter/rest day each week. If fewer than four
hours are available on a given day, prioritise implementation and tests
over additional tutorials.

------------------------------------------------------------------------

## 11. Final release target: 31 December 2026

By the deadline, the repository should tell a coherent story:

> I built an industrial AI inspection platform that uses deep learning
> and image processing to localise defects, performs calibrated
> measurements when reference information is available, exposes
> inspection workflows through a tested API, stores inspection data, and
> supports evidence-grounded querying of inspection reports. I tracked
> model experiments, containerised the application, automated checks and
> documented deployment.

That is the target---not a claim that every module is enterprise-scale
or production-certified.

**Primary success measure:** a recruiter or engineer can clone the
repository, follow the instructions, run the application, inspect the
model evaluation, test the API, and understand the engineering decisions
without needing a personal explanation from me.
