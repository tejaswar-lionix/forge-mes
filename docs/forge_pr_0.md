# ForgeMES Compliance Note 1

## Context
OEE live pipeline for plant head dashboard.

## Changes
- Added WS consumer for OEE streaming (Channels)
- BOM explosion validation for nested qty
- Andon cord stop handling with escalation timeout
- SPC chart 3sigma limits

## Verification
- pytest -q (OEE formula 0.92*0.89*0.96)
- manual WS test: ws://localhost:8001/ws/oee/

## Follow-up
- Pareto report aggregation next
