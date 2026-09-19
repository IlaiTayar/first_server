first_serverA
------------------------------------------------------------------------------------------
lightweight FastAPI service with aiomysql for async MySQL access,
Redis as a cache layer, all containerized with Docker and orchestrated via docker‑compose.
------------------------------------------------------------------------------------------
Features:
- FastAPI: Building blocks for async REST endpoints.
- aiomysql + databases: Async MySQL driver.
- Redis: Simple key‑value cache (e.g., customer lookup).
- Docker / docker‑compose: Reproducible environment, zero‑config deployment.
- Layered architecture: controller, repository, service – keeps business logic testable.
