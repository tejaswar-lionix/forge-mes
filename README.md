
# ForgeMES — Digital Twin Factory

Shop-floor MES. Order → BOM → Work Center → QC → Dispatch. Live OEE with Andon.

## Stack
- **Backend:** Django 4.2 + Channels (WebSocket live OEE) + Redis + Celery, PostgreSQL (sqlite fallback)
- **Frontend:** React 18 + Vite + TanStack Query + Chart.js + WebSocket
- **16 Apps:** orders, bom, workcenters, machines, shifts, production, quality, maintenance, inventory, procurement, dispatch, workers, analytics, downtime, traceability, andon

## Install
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
npm install
```

## Build
```bash
make build
docker build -t forgemes .
npm run build
```

## Run
```bash
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000
# WS consumer
daphne forge.asgi:application
celery -A forge worker -l info
npm run dev
docker-compose up
```

## Tests
```bash
pytest -q
pytest --cov=apps --cov-report=xml
npm test
```

## Key Features
- **BOM explosion** nested, routing work-center sequence
- **Shift rostering** + Andon cord stop line
- **SPC quality** charts, MTBF predictive maintenance
- **Lot genealogy** steel coil → finished part
- **OEE = Availability * Performance * Quality** live via Channels WS
- **Plant Head dashboard:** OEE 78.4% gauge, Downtime Pareto, Rejection PPM, On-time dispatch
- **QC:** incoming / in-process / final inspection, CAPA tracker

## Models
Machine, WorkCenter, BOMLine, JobCard, Operation, DowntimeEvent, QCSample, MaintenanceLog, AndonCord

## License
Proprietary — All rights reserved (ForgeMES Labs).

## Changelog 2025-08-25
- Live OEE gauge added
- Andon cord handling fixed
