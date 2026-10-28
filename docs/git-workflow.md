# Fluxo de trabalho

1. Abrir issue por experimento: teoria, hipótese, métrica e critérios.
2. Criar branch `feat/<tema>`, `perf/<tema>` ou `docs/<tema>`.
3. PR pequeno com testes e resultados antes/depois.
4. Não ocultar resultados negativos: registrar por que a hipótese falhou.
5. Fazer merge com CI verde. Evitar misturar refatoração e otimização no mesmo experimento.

## Modelo de experimento
```md
Hipótese:
Ambiente / commit:
Dataset:
Carga:
Métricas antes (RPS, p50, p95, p99, erros, CPU, IO):
Métricas depois:
Trade-offs:
Conclusão:
Rollback:
```
