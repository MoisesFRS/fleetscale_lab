# FleetScale Lab

Laboratório de arquitetura de software, escalabilidade e sistemas distribuídos aplicado ao rastreamento de veículos.

Meta de referência: 1 milhão de veículos cadastrados, com até 100 mil transmitindo telemetria a cada 5 segundos (20 mil eventos/s em média). Essa é uma meta de estudo, **não** uma capacidade já comprovada.

## Começando

```bash
cp .env.example .env
docker compose up --build -d
curl http://localhost:8000/healthz
```

A documentação da API estará em `http://localhost:8000/docs`.

## Documentação

- [Arquitetura](docs/architecture.md)
- [Roadmap](docs/roadmap.md)
- [Planejamento de capacidade](docs/capacity-planning.md)
- [Testes de desempenho](docs/benchmarking.md)
- [Segurança](docs/security.md)
- [Decisões arquiteturais](docs/adr/0001-modular-monolith.md)

O guia individual de estudos é mantido fora do GitHub.
