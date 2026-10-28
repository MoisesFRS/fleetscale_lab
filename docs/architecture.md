# Arquitetura e requisitos não funcionais

## Domínio
- **Vehicle**: veículo cadastrado e identificador sintético.
- **Position**: latitude, longitude, velocidade, tempo do dispositivo (`recorded_at`) e tempo do servidor (`received_at`).
- Futuros conceitos: Device, Tenant, Geofence, Alert, Journey, DeviceCredential.

## Fluxos
1. Ingestão: dispositivo → validação → persistência → confirmação.
2. Última posição: aplicativo → API → posição de maior tempo do evento.
3. Histórico: consulta por veículo e intervalo.
4. Tempo real (futuro): publicação de novos eventos para assinantes autorizados.

## Decisões
- Começar com monolito modular e evoluir apenas após medir.
- Distinguir tempo do evento e tempo de ingestão.
- Projetar para duplicatas e eventos fora de ordem.
- Em filas, estudar particionamento por `vehicle_id`, idempotência e semântica de entrega.
- Em cache, atualizar última posição de forma condicional por timestamp e ter fallback.
- Não usar dados reais antes de autenticação, autorização por cliente e proteção de privacidade.

## SLOs candidatos (a validar)
| Indicador | Alvo didático |
|---|---|
| Ingestão sustentada | 20.000 eventos/s |
| Pico | 40.000 a 100.000 eventos/s |
| Ingestão p95 | abaixo de 250 ms, após definir semântica do ACK |
| Consulta última posição p95 | abaixo de 200 ms |
| Disponibilidade mensal | 99,9% |

Esses números são **hipóteses, não resultados demonstrados**. A estratégia é gerar baseline, medir gargalos, propor mudanças, repetir testes e documentar trade-offs.

## Evolução pretendida
Banco síncrono → índices e partições → Redis → Kafka/Redpanda → WebSocket → balanceamento e múltiplas réplicas → observabilidade → estratégias de armazenamento distribuído. Cada etapa terá ADR, benchmark e rollback.
