# Protocolo de benchmarking

1. Registrar hipótese, métrica principal e sucesso esperado **antes** de alterar código.
2. Fixar máquina, CPU, RAM, rede, versão, banco e volume de dados.
3. Distinguir carga solicitada, recebida e efetivamente persistida.
4. Registrar p50/p95/p99, taxa de erros, throughput real, CPU, RAM, locks, conexões, WAL e IOPS.
5. Executar warm-up; testar cache frio e quente.
6. Repetir testes para não concluir com base em uma execução isolada.
7. Cobrir ramp-up, carga sustentada, picos, recuperação e soak test.
8. Alterar um fator por vez quando possível.
9. Documentar os trade-offs e o plano de rollback.

## Experimento de exemplo
**Hipótese:** índice em `(vehicle_id, recorded_at, id)` melhora consulta de última posição com histórico grande.

**Método:** mesmo dataset, com/sem índice, `EXPLAIN (ANALYZE, BUFFERS)`, benchmark de leitura e medição do overhead de escrita.

## k6
O teste `load/ingestion.js` usa `constant-arrival-rate`. Um `RATE` configurado representa **a taxa desejada**, não um throughput confirmado. Se o gerador saturar ou VUs forem insuficientes, as chegadas não corresponderão à meta.

**Critério para concluir fase:** experimento reprodutível + métricas + explicação técnica + decisão documentada.
