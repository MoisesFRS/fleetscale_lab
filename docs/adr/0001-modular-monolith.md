# ADR 0001 — Monolito modular

**Status:** aceito para baseline.

**Contexto:** ainda não existe carga real nem gargalo medido; o objetivo é comparar evoluções reproduzíveis.

**Decisão:** iniciar com uma API FastAPI, um PostgreSQL e código modular, mantendo contratos HTTP explícitos.

**Alternativas:** microsserviços desde o começo, Kafka obrigatório, Kubernetes no MVP.

**Justificativa:** distribuir cedo adicionaria overhead, rede, observabilidade, transações e custo operacional sem evidência de melhora.

**Consequências:** desenvolvimento e depuração mais simples no começo; poderá exigir separação quando forem medidos limites entre ingestão, leitura e consumidores.

**Revisar quando:** resultados demonstráveis indicarem contenda de recursos ou requisitos independentes de disponibilidade.
