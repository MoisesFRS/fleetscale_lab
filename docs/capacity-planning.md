# Planejamento de capacidade

Cenário hipotético: **1 milhão** de veículos cadastrados, **100 mil** ativos, uma posição a cada **5 s**.

- 100.000 / 5 = **20.000 eventos/s**
- 20.000 × 86.400 = **1.728.000.000 eventos/dia**
- Em 7 dias, **12.096.000.000 eventos**
- Assumindo 150–300 bytes efetivos/evento (hipótese simplificada): **259,2–518,4 GB/dia**, antes de índices, WAL, réplicas, backups e variações de armazenamento.
- Pico de 2–5× exigiria capacidade momentânea de 40 mil–100 mil eventos/s ou absorção por fila.

## Exercícios
1. Recalcular para frota ativa de 10%, 30%, 60%.
2. Intervalos de 1, 5 e 30 segundos.
3. Modelar picos sincronizados e dispositivos offline enviando backlog.
4. Projetar retenção quente de 7 dias, morna de 90 dias e arquivo anual.
5. Distinguir RPS, concorrência e conexões persistentes; estudar Lei de Little `L = λW`.
6. Medir tamanho real de linha, WAL e índices no PostgreSQL.

| Data | Commit | Hardware | Cenário | RPS realizado | p95/p99 | Erros | CPU/IO | Evidência |
|---|---|---|---|---|---|---|---|---|
| A medir | A medir | A medir | Baseline 10/s | — | — | — | — | — |
