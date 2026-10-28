# Roadmap técnico — FleetScale Lab

## Método
Cada fase segue **estudar → hipótese → experimento → medição → comparação → documentação**. Não declarar fase concluída só porque o código foi escrito.

| Fase | Semanas indicativas | Entrega |
|---|---|---|
| 00 | 1–2 | Requisitos, SLOs, matemática de capacidade |
| 01 | 3–4 | MVP FastAPI, PostgreSQL, Docker, testes |
| 02 | 5–6 | Baseline k6, profiling, EXPLAIN |
| 03 | 7–8 | Concorrência, async, pools e backpressure |
| 04 | 9–10 | PostgreSQL: índices, WAL, partições |
| 05 | 11–12 | Redis: última localização e cache consistente |
| 06 | 13–14 | Kafka/Redpanda, consumidores, DLQ, replay |
| 07 | 15–16 | WebSocket e mapa React |
| 08 | 17–18 | Escala horizontal, Nginx, réplicas stateless |
| 09 | 19–20 | Resiliência, retries, circuit breaker, caos |
| 10 | 21–22 | OpenTelemetry, Prometheus, Grafana |
| 11 | 23–24 | Replicação, retenção, arquivamento, sharding |
| 12 | 25–26 | Segurança, identidade, tenant, LGPD |
| 13 | 27–30 | CI/CD, Kubernetes opcional, capstone |

## Backlog
### M0 — Capacity planning
- [ ] Estimar 1 mil, 10 mil e 100 mil dispositivos ativos.
- [ ] Calcular eventos/s, volume/dia e custo de retenção.
- [ ] Definir SLIs/SLOs e contrato de posição.

### M1 — MVP
- [x] Scaffold FastAPI, PostgreSQL e Docker Compose.
- [x] Cadastro, ingestão e consulta de última posição.
- [x] Testes unitários, simulador e script inicial k6.
- [ ] Testes de integração, migrações Alembic e validação end-to-end.

### M2 — Benchmark
- [ ] Medir 10, 50, 100 e 500 RPS.
- [ ] Habilitar pg_stat_statements e profiling.
- [ ] Reportar p50, p95, p99, erros, CPU e I/O.

### M3 — Concorrência
- [ ] Comparar sync/async; configurar pool e limites.
- [ ] Simular saturação, timeouts e backpressure.

### M4 — Banco
- [ ] EXPLAIN (ANALYZE, BUFFERS), índices e impacto em escrita.
- [ ] Partições, autovacuum, retenção e Alembic.

### M5 — Cache
- [ ] Redis última posição, invalidação por timestamp e fallback.
- [ ] Comparar latência com/sem cache.

### M6 — Eventos
- [ ] Broker e consumidor idempotente.
- [ ] Definir durabilidade do ACK, DLQ, retry, replay e lag.

### M7 — Tempo real
- [ ] WebSocket autorizado por veículo; mapa React sintético.
- [ ] Reconexão, heartbeat, fan-out e medição evento→tela.

### M8 — Escala horizontal
- [ ] Load balancer e no mínimo duas réplicas.
- [ ] Avaliar sticky sessions e distribuição WebSocket.

### M9 — Resiliência
- [ ] Circuit breaker, retries com jitter, quotas, bulkheads.
- [ ] Falhas de banco, broker, duplicatas e eventos fora de ordem.

### M10 — Observabilidade
- [ ] Traces, logs estruturados, métricas e alertas.
- [ ] Postmortem de incidente simulado.

### M11 — Volume
- [ ] Partição temporal, réplica, arquivamento e sharding simulado.
- [ ] RPO/RTO e recuperação de falhas.

### M12 — Segurança
- [ ] Autenticação de dispositivo e isolamento por tenant.
- [ ] Rate limit, antirreplay, auditoria e LGPD.

### M13 — Capstone
- [ ] Benchmark replicável, arquitetura final e custos estimados.
- [ ] Publicar **somente métricas realmente medidas**.

## Regra de qualidade
Cada PR relevante: hipótese, ambiente, dataset, métricas antes/depois, trade-offs, rollback e testes. Correção e consistência vêm antes da velocidade.
