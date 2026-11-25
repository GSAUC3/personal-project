
industrial-inspection/
│
├── pyproject.toml
├── poetry.lock
├── README.md
├── PROJECT_PLAN.md
├── .gitignore
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── Makefile
│
├── configs/
│   ├── default.yaml
│   ├── model.yaml
│   └── logging.yaml
│
├── data/
│   ├── README.md
│   ├── raw/
│   ├── processed/
│   └── samples/
│
├── models/
│   └── README.md
│
├── src/
│   └── industrial_inspection/
│       │
│       ├── __init__.py
│       ├── main.py
│       │
│       ├── api/
│       │   ├── __init__.py
│       │   ├── dependencies.py
│       │   ├── routes/
│       │   │   ├── __init__.py
│       │   │   ├── health.py
│       │   │   ├── inspection.py
│       │   │   └── reports.py
│       │   └── schemas/
│       │       ├── __init__.py
│       │       ├── inspection.py
│       │       └── common.py
│       │
│       ├── core/
│       │   ├── __init__.py
│       │   ├── config.py
│       │   ├── logging.py
│       │   ├── exceptions.py
│       │   └── constants.py
│       │
│       ├── vision/
│       │   ├── __init__.py
│       │   ├── preprocessing.py
│       │   ├── inference.py
│       │   ├── postprocessing.py
│       │   ├── model_loader.py
│       │   └── visualization.py
│       │
│       ├── measurement/
│       │   ├── __init__.py
│       │   ├── calibration.py
│       │   ├── geometry.py
│       │   └── measurements.py
│       │
│       ├── services/
│       │   ├── __init__.py
│       │   ├── inspection_service.py
│       │   └── report_service.py
│       │
│       ├── database/
│       │   ├── __init__.py
│       │   ├── connection.py
│       │   ├── models.py
│       │   └── repositories/
│       │       ├── __init__.py
│       │       └── inspection_repository.py
│       │
│       ├── storage/
│       │   ├── __init__.py
│       │   └── image_storage.py
│       │
│       └── rag/
│           ├── __init__.py
│           ├── embeddings.py
│           ├── retriever.py
│           └── qa.py
│
├── scripts/
│   ├── validate_dataset.py
│   ├── train.py
│   └── evaluate.py
│
├── notebooks/
│   └── README.md
│
├── tests/
│   ├── conftest.py
│   ├── unit/
│   │   ├── test_preprocessing.py
│   │   ├── test_inference.py
│   │   ├── test_measurements.py
│   │   └── test_visualization.py
│   ├── integration/
│   │   ├── test_inspection_api.py
│   │   └── test_database.py
│   └── fixtures/
│       └── README.md
│
├── docs/
│   ├── architecture.md
│   ├── dataset_documentation.md
│   ├── api_documentation.md
│   └── model_card.md
│
└── .github/
    └── workflows/
        └── ci.yml
