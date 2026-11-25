# Project Plan: Industrial AI Inspection and Intelligence Platform

| Project detail | Value |
| --- | --- |
| Start | 24 November 2026 |
| Deadline | 31 December 2026 |
| Duration | 38 calendar days, including both start and finish dates |
| Project type | Flagship portfolio project |
| Primary positioning | AI/ML Engineer specialising in computer vision, with production-oriented engineering skills |

## Contents

1. [Project objective](#1-project-objective)
2. [Product scope](#2-product-scope)
3. [Scope control](#3-scope-control)
4. [Dataset and modelling strategy](#4-dataset-and-modelling-strategy)
5. [Delivery plan](#5-delivery-plan)
6. [Repository structure](#6-repository-structure)
7. [Skill evidence](#7-skill-evidence)
8. [Definition of done](#8-definition-of-done)
9. [Risk management](#9-risk-management)
10. [Operating rhythm](#10-operating-rhythm)
11. [Final release target](#11-final-release-target)

---

## 1. Project objective

Build an end-to-end industrial inspection platform that:

- accepts an image of a manufactured component;
- identifies and localises visual defects;
- calculates inspection measurements when valid calibration information is available;
- stores inspection results and artefacts; and
- allows users to query inspection reports through a retrieval-augmented generation (RAG) assistant.

The project must demonstrate engineering beyond model training. The repository should provide evidence of:

- real-world computer-vision dataset preparation;
- reproducible deep-learning training, evaluation and explanation;
- reusable image-processing and measurement components;
- a tested backend and database layer;
- a language-model application grounded in stored reports and documentation;
- experiment and model-version tracking;
- packaging, deployment and technical documentation; and
- clear engineering trade-offs and limitations.

This project is deliberately industrial in scope because it builds on professional experience with image processing, defect inspection, calibration, measurement, Python, C++, and AWS without reusing employer-owned code or data.

> **Data and IP rule:** Use only public datasets, generated images and independently written code. Do not use client images, confidential information, proprietary algorithms or employer-owned code from Genpact or Zentron Labs.

### 1.1 Problem statement

Factories inspect products for defects such as scratches, dents, cracks, missing parts and unusual surface patterns. Manual inspection can be slow and subjective, and inspection records may be scattered across images and reports.

The platform should help an inspector:

1. analyse a product image;
2. highlight likely defect regions;
3. record the result and model version; and
4. search and understand previous inspection reports.

### 1.2 Proposed solution

A user uploads an image. The system:

1. validates the image and creates an inspection record;
2. predicts whether a defect or anomaly is present;
3. produces a localisation mask or heatmap;
4. calculates physical measurements only when calibration is valid;
5. stores the original image, prediction artefacts, metrics and metadata; and
6. provides retrieval-grounded answers with source references.

The system must not claim to know real-world dimensions from an uncalibrated image.

---

## 2. Product scope

### 2.1 User workflow

1. The user uploads an inspection image.
2. The backend validates the input and creates an inspection record.
3. The computer-vision pipeline predicts an anomaly score and produces a mask or heatmap.
4. The measurement module converts pixel distances to physical units when calibration is valid.
5. The system stores the image, prediction artefacts, model version and inspection metadata.
6. The user views the result and retrieves previous inspections.
7. The user asks questions such as:
   - “Summarise the defects found in the last inspection.”
   - “Which inspections had the highest anomaly score?”
   - “Explain the difference between these two inspection reports.”
8. The RAG assistant retrieves relevant records and returns an answer with supporting references.

### 2.2 Core modules

| Module | Responsibility | Main technologies |
| --- | --- | --- |
| Data pipeline | Dataset ingestion, validation, preprocessing, splits and augmentation | Python, NumPy, PyTorch, OpenCV |
| CV inference | Defect/anomaly scoring and localisation | PyTorch, torchvision |
| Measurement | Calibration and pixel-to-metric conversion | OpenCV, NumPy |
| Backend | Upload, inference, report and history APIs | FastAPI, Pydantic |
| Persistence | Inspection metadata and report records | PostgreSQL, SQLAlchemy |
| File storage | Original images and generated artefacts | Local storage; AWS S3 for deployment |
| Experiment tracking | Parameters, metrics and model artefacts | MLflow |
| AI assistant | Search and question answering over stored reports | Embeddings, RAG, LLM API, pgvector |
| Packaging | Reproducible runtime and automated checks | Docker, Docker Compose, GitHub Actions |
| Observability | Application logs, errors and health checks | Python logging, FastAPI health endpoint, AWS logs |

### 2.3 Recommended technology stack

The following stack is a fixed implementation choice rather than a catalogue of possible alternatives.

| Layer | Technology | Use |
| --- | --- | --- |
| Main language | Python 3.13 | Application, data pipeline, training and inference |
| Numerical/image processing | NumPy, OpenCV, Pillow | Loading, preprocessing, calibration and measurement |
| Deep learning | PyTorch, torchvision | Defect-localisation training and inference |
| Model architecture | U-Net with a pretrained encoder | Pixel-level defect localisation with labelled masks |
| Dataset | MVTec AD, two selected categories | Public industrial anomaly images and defect masks |
| API/backend | FastAPI, Pydantic | Upload, inference, history and RAG endpoints |
| Database/ORM | PostgreSQL, SQLAlchemy | Metadata, predictions and report records |
| Vector search | pgvector | Store and retrieve report/document embeddings |
| Embeddings | sentence-transformers | Convert report text into vectors |
| LLM integration | One hosted LLM API with a small provider-independent wrapper | Answer generation with retrieved context |
| Experiment tracking | MLflow | Parameters, metrics, runs and model artefacts |
| Testing/quality | pytest, Ruff | Tests and basic code-quality checks |
| Containers | Docker, Docker Compose | Local application and database environment |
| CI | GitHub Actions | Tests and checks on pushes and pull requests |
| Cloud storage | AWS S3, boto3 | Uploaded images and inspection artefacts |
| Cloud hosting | AWS EC2, optional | Containerised API deployment |
| Documentation | Markdown, Mermaid, FastAPI Swagger UI | Project, architecture and API documentation |

### 2.4 Implementation principles

- Use one deep-learning framework: PyTorch.
- Use one backend framework: FastAPI.
- Use PostgreSQL for relational records and pgvector for vector search.
- Implement the initial RAG pipeline directly with embedding, retrieval and LLM calls.
- Use FastAPI Swagger UI initially; a separate dashboard is optional.
- Run locally with Docker Compose before attempting AWS deployment.
- Keep AWS deployment optional if cost or configuration threatens the deadline.

---

## 3. Scope control

The deadline is fixed. A reliable vertical slice is more valuable than many unfinished integrations.

### 3.1 Must-have scope

- [ ] Documented public dataset and reproducible train/validation/test split
- [ ] Trained and evaluated defect or anomaly-localisation model
- [ ] Working OpenCV calibration and measurement module with explicit calibration input
- [ ] FastAPI endpoints for upload, inference, inspection retrieval and health checks
- [ ] PostgreSQL persistence for inspection metadata and results
- [ ] RAG assistant grounded in inspection reports and project documentation
- [ ] MLflow experiment tracking
- [ ] Docker Compose setup for the application and database
- [ ] Automated unit and API tests
- [ ] GitHub Actions workflow for linting and tests
- [ ] Live deployment if feasible; otherwise a fully reproducible local deployment
- [ ] Architecture diagram, README, API documentation, model card and demo video

### 3.2 Stretch goals

Treat these as optional after every must-have item is working:

- Browser-based dashboard
- Second model or dataset category
- Asynchronous inference with a task queue
- Authentication and role-based access
- Monitoring or drift detection
- Kubernetes or distributed training
- TensorRT or edge optimisation
- Fine-tuning an LLM

Do not begin Kubernetes, multi-agent orchestration or custom LLM fine-tuning during this project; they do not materially improve the target outcome within the deadline.

---

## 4. Dataset and modelling strategy

### 4.1 Dataset

Use DsPCBSD+, a public PCB anomaly-detection benchmark. Start with two object or texture categories to keep the project manageable.

- Dataset: https://doi.org/10.6084/m9.figshare.24970329
- Review licence and download terms before use.
- Record the selected categories and licence terms in the repository.
- Use the public benchmark without adding proprietary or confidential data.

### 4.2 Modelling plan

1. Inspect image dimensions, masks and category distributions.
2. Create a reproducible split and document any limitations of the benchmark split.
3. Establish a simple baseline before increasing model complexity.
4. Train a segmentation model using the available defect masks.
5. Evaluate image-level and pixel-level performance.
6. Save predictions, overlays and representative failure cases.
7. Track parameters, metrics and artefacts in MLflow.

Suggested baseline: a small U-Net-style segmentation model with a pretrained encoder where practical. Keep the architecture understandable and reproducible.

### 4.3 Metrics

| Level | Metrics |
| --- | --- |
| Image | Precision, recall, F1 and ROC-AUC when supported by the evaluation setup |
| Pixel | Precision, recall, Dice, IoU and pixel ROC-AUC |
| Operational | Inference latency, model size and memory use |

Do not report a metric unless the calculation and evaluation split are documented. Compare with a simple baseline and include false positives and false negatives in the error analysis.

### 4.4 Calibration and measurement

The public anomaly dataset may not contain physical scale references. Keep calibration as a separate, clearly scoped module:

- accept a known physical distance and corresponding pixel distance;
- optionally detect a deliberately provided calibration marker;
- calculate pixels-per-unit and convert pixel measurements to physical units;
- reject missing, invalid or ambiguous calibration input;
- test with synthetic images of known dimensions and manually verified examples; and
- state clearly that measurements are valid only with a valid reference and appropriate imaging geometry.

Do not claim that arbitrary MVTec AD images provide real-world dimensions.

---

## 5. Delivery plan

Dates are inclusive. Each phase has an exit criterion; unfinished work must be reduced or deferred rather than silently inherited by the next phase.

### Phase 0 — Project definition and repository setup

**Dates:** 24–25 November 2026

| Area | Work |
| --- | --- |
| Repository | Create the GitHub repository and project plan |
| Dataset | Define two dataset categories and inspect licence and terms |
| Environment | Create a clean Python environment and dependency-management approach |
| Structure | Establish a modular repository layout |
| Foundations | Add README skeleton, `.gitignore`, configuration handling and logging |
| Planning | Create a project board with tasks and priorities |

**Deliverables**

- Repository with an initial structure
- Dataset decision and data documentation
- Reproducible environment setup
- Initial architecture sketch

**Exit criteria**

- A fresh environment installs dependencies successfully.
- A small sample image loads and passes validation.
- No secrets, credentials or datasets are committed.

### Phase 1 — Data pipeline and computer-vision baseline

**Dates:** 26 November–2 December 2026

| Area | Work |
| --- | --- |
| Data | Download and inspect MVTec AD categories; implement loading and validation |
| Documentation | Document formats, class balance and the split strategy |
| Processing | Implement preprocessing and training-time augmentation |
| Visualisation | Add utilities for images, masks and overlays |
| Baseline | Build a simple baseline and record initial metrics |
| Tests | Test loading, mask alignment and preprocessing |

**Deliverables**

- Reproducible data pipeline
- Dataset exploration report
- Baseline metrics and visual examples
- Unit tests for data utilities

**Exit criteria**

- Training and evaluation data are separated correctly.
- Image and mask transformations preserve alignment.
- The baseline runs using documented commands.

### Phase 2 — Deep-learning model and evaluation

**Dates:** 3–9 December 2026

| Area | Work |
| --- | --- |
| Model | Implement a segmentation model in PyTorch |
| Training | Add validation, checkpoints, reproducible seeds and a documented training loop |
| Tracking | Record experiments in MLflow |
| Evaluation | Measure image-level and pixel-level performance |
| Analysis | Inspect false positives, false negatives and category-specific failures |
| Inference | Export overlays and implement a stable interface independent of training code |

**Deliverables**

- Trained model checkpoint
- Evaluation script and results
- MLflow experiment records
- Model card covering intended use, data, metrics and limitations
- Predictable inference input and output types

**Exit criteria**

- A saved model loads in a clean inference process.
- Evaluation is repeatable.
- Metrics and qualitative failure analysis are available.
- Results are not described as production-validated solely because they perform on a benchmark.

### Phase 3 — Measurement module and backend

**Dates:** 10–15 December 2026

| Area | Work |
| --- | --- |
| Measurement | Implement and validate the independent pixel-to-metric module |
| Testing | Test known dimensions using synthetic images |
| API | Add health, inspection upload, retrieval, history and report endpoints |
| Schemas | Define request and response models with Pydantic |
| Persistence | Store metadata, predictions, model version and measurement data in PostgreSQL |
| Storage | Store artefacts locally; retain an interface suitable for S3 |
| Integration | Add API and database integration tests |

**API endpoints**

- `GET /health`
- `POST /inspections`
- `GET /inspections/{inspection_id}`
- `GET /inspections`
- `GET /inspections/{inspection_id}/report`

**Deliverables**

- Tested calibration package
- FastAPI application
- PostgreSQL schema and persistence layer
- Working image-upload-to-inference-to-record workflow

**Exit criteria**

- An uploaded image can be processed through the API.
- Results and model versions are persisted.
- Invalid inputs return useful errors.
- Tests cover success and failure paths.

### Phase 4 — RAG inspection assistant

**Dates:** 16–20 December 2026

| Area | Work |
| --- | --- |
| Documents | Prepare documentation, model-card text and sample reports |
| Indexing | Chunk and embed documents |
| Storage | Use PostgreSQL with pgvector, or a simpler vector store if setup threatens the deadline |
| Retrieval | Retrieve relevant report and document chunks |
| Generation | Generate answers through one hosted LLM API |
| Grounding | Include source and inspection identifiers |
| Guardrails | Abstain when the available evidence is insufficient |
| Evaluation | Test retrieval relevance, grounding and incorrect claims |

**Deliverables**

- Document-ingestion and indexing script
- Retrieval and answer-generation pipeline
- RAG query API endpoint
- Small evaluation set and results

**Exit criteria**

- Test queries retrieve relevant records.
- Answers identify supporting records or documents.
- Insufficient evidence produces an abstention.
- API keys come from environment variables and are never committed.

### Phase 5 — Packaging, cloud storage and CI/CD

**Dates:** 21–26 December 2026

| Area | Work |
| --- | --- |
| Containers | Create Dockerfile, Docker Compose and persistent database configuration |
| Storage | Implement the S3 storage adapter behind the storage interface |
| CI | Add GitHub Actions for installation, linting and tests |
| Operations | Add structured logs, request identifiers and health/readiness checks |
| Deployment | Deploy to AWS if feasible within time and budget |
| Documentation | Document setup, deployment, security and cleanup |

**Deliverables**

- Dockerfile and Docker Compose configuration
- CI workflow
- S3 storage integration
- Deployment guide and, if completed, a live demo URL

**Exit criteria**

- A new developer can run the application from documented steps.
- Automated checks run on pushes or pull requests.
- No credentials are stored in the repository.
- Cloud resources have budget limits and a cleanup procedure.

### Phase 6 — Integration, documentation and portfolio release

**Dates:** 27–31 December 2026

| Area | Work |
| --- | --- |
| Integration | Run end-to-end upload, storage and RAG tests |
| Cleanup | Fix critical bugs and remove unused code |
| Verification | Run setup and tests from a clean checkout |
| Documentation | Add architecture/data-flow diagrams, API docs and known limitations |
| Portfolio | Add sample requests, responses and screenshots |
| Presentation | Record a concise demonstration video |
| Career | Update the resume and GitHub profile with measured outcomes |
| Interview | Prepare explanations for design decisions and trade-offs |

**Deliverables**

- Versioned release, for example `v1.0.0`
- Complete README and architecture diagram
- Model card and evaluation report
- Demo video and screenshots
- Resume-ready project description

**Exit criteria**

- Must-have features work together.
- Setup and test instructions are verified.
- No confidential data or secrets are present.
- Known limitations are documented honestly.
- The repository is ready to share with recruiters.

---

## 6. Repository structure

```text
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

Keep notebooks for exploration and put reusable code in `src/`. Do not commit large datasets, model weights, generated images or secrets. Use documented download instructions and an appropriate artefact store.

---

## 7. Skill evidence

The project should map each portfolio gap to concrete repository evidence.

| Skill or gap | Existing evidence | Project evidence |
| --- | --- | --- |
| Python engineering | Professional Python experience | Modular package, typing, configuration, logging and error handling |
| Software testing | Not clearly demonstrated | pytest unit, integration and end-to-end tests |
| SQL | Not listed | PostgreSQL schema, joins, indexes and persistence |
| Backend development | Not listed | FastAPI REST service and Pydantic schemas |
| Deep learning | EfficientNet/PyTorch experience | Reproducible training, validation, checkpointing and evaluation |
| Modern CV | OpenCV and industrial image processing | Segmentation/anomaly localisation, overlays and quantitative metrics |
| Model evaluation | Accuracy stated in prior projects | Precision, recall, F1, IoU/Dice, ROC-AUC and error analysis |
| NLP/LLM | Interest but no stated professional experience | Embeddings, retrieval, RAG endpoint and evaluation |
| MLOps | AWS/SageMaker exposure | MLflow runs, model artefacts and version tracking |
| Docker | Not listed | Reproducible containerised application |
| CI/CD | Not listed | GitHub Actions for tests and checks |
| Cloud | S3, Lambda and SageMaker exposure | S3 integration and documented AWS deployment |
| Observability | Not clearly demonstrated | Structured logs, health checks and error reporting |
| System design | Not clearly demonstrated | Architecture diagram, storage abstraction and documented trade-offs |
| C++ | Professional experience | Existing strength; no need to force C++ into this project |

The project does not need expert-level proficiency in every technology. It needs sound working knowledge and the ability to explain implementation decisions.

---

## 8. Definition of done

### Product

- [ ] A user can submit an image through the API.
- [ ] The model returns an anomaly or defect score and localisation output.
- [ ] The system records the prediction and model version.
- [ ] Measurements are calculated only with valid calibration.
- [ ] Inspection history can be retrieved.
- [ ] The RAG assistant answers questions using retrieved inspection information.

### Engineering

- [ ] Code is modular and configuration is not hardcoded.
- [ ] Unit and integration tests cover critical paths.
- [ ] API errors are handled predictably.
- [ ] PostgreSQL persistence works.
- [ ] Docker Compose starts the local application.
- [ ] CI runs tests and quality checks.
- [ ] Secrets are not committed.
- [ ] Logs and health checks are available.

### Machine learning

- [ ] Dataset source, licence and split are documented.
- [ ] Baseline and final metrics are recorded.
- [ ] Model limitations and failure cases are documented.
- [ ] Inference is reproducible from a saved checkpoint.
- [ ] RAG answers expose supporting records and can abstain.

### Portfolio

- [ ] README includes the problem, architecture, setup, usage and results.
- [ ] Architecture diagram is included.
- [ ] Model card and evaluation report are included.
- [ ] Demo video or walkthrough is available.
- [ ] Resume claims match the implemented work.

---

## 9. Risk management

| Risk | Mitigation |
| --- | --- |
| Dataset or model training takes longer than expected | Limit scope to two categories and establish a baseline early |
| Segmentation performance is weak | Report honest results, inspect failures and compare against the baseline |
| The dataset has no physical scale reference | Keep calibration independent and validate with synthetic known-scale images |
| RAG integration becomes a time sink | Use direct retrieval and one LLM API; avoid agent frameworks |
| AWS deployment introduces cost or configuration issues | Complete local Docker deployment first; set budgets and clean up resources |
| Too many technologies reduce quality | Treat must-have scope as a boundary and defer stretch goals |
| Public dataset terms are unsuitable | Review terms before use and choose another appropriately licensed dataset |

---

## 10. Operating rhythm

Use a repeatable routine rather than spending the day watching tutorials.

### Daily allocation

Recommended for 4–5 hour project days:

| Activity | Time |
| --- | --- |
| Learn the concept needed for the current milestone | 60–90 minutes |
| Implement the project | 2–2.5 hours |
| Tests, debugging and code review | 30–45 minutes |
| Notes, documentation and interview revision | 30 minutes |

### End-of-week checklist

1. Demonstrate the working feature.
2. Run tests from a clean state.
3. Update the README and project board.
4. Record unfinished work.
5. Cut optional work before moving the deadline.

Reserve at least one lighter or rest day each week. If fewer than four hours are available, prioritise implementation and tests over additional tutorials.

---

## 11. Final release target

By 31 December 2026, the repository should tell this coherent story:

> I built an industrial AI inspection platform that uses deep learning and image processing to localise defects, performs calibrated measurements when reference information is available, exposes inspection workflows through a tested API, stores inspection data and supports evidence-grounded querying of inspection reports. I tracked model experiments, containerised the application, automated checks and documented deployment.

This is a target for a working portfolio project—not a claim that every module is enterprise-scale or production-certified.

**Primary success measure:** A recruiter or engineer should be able to clone the repository, follow the instructions, run the application, inspect the model evaluation, test the API and understand the engineering decisions without a personal explanation.
