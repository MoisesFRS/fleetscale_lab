"""Simulador didatico sequencial, NAO um gerador de alta carga."""
import argparse
import json
import random
import time
import uuid
from datetime import datetime, timezone
from urllib import error, request


def post_json(base_url, path, payload):
    req = request.Request(
        f"{base_url}{path}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with request.urlopen(req, timeout=10) as response:
        return json.load(response)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--vehicles", type=int, default=10)
    parser.add_argument("--interval", type=float, default=5)
    parser.add_argument("--rounds", type=int, default=3)
    args = parser.parse_args()
    if not 1 <= args.vehicles <= 500 or args.interval <= 0 or args.rounds <= 0:
        parser.error("Use 1-500 veiculos, intervalo positivo e rounds positivos")
    vehicles = []
    for _ in range(args.vehicles):
        external_id = f"SIM-{uuid.uuid4().hex[:12]}"
        try:
            vehicle = post_json(args.base_url, "/api/v1/vehicles", {"external_id": external_id})
            vehicles.append(vehicle["id"])
        except error.URLError as exc:
            raise SystemExit(f"API indisponivel: {exc}") from exc
    print(f"Simulando {len(vehicles)} veiculos por {args.rounds} rodadas")
    for round_number in range(args.rounds):
        start = time.monotonic()
        successes = 0
        for vehicle_id in vehicles:
            point = {
                "vehicle_id": vehicle_id,
                "latitude": round(-23.0021 + random.uniform(-0.02, 0.02), 6),
                "longitude": round(-46.8465 + random.uniform(-0.02, 0.02), 6),
                "speed_kmh": round(random.uniform(0, 90), 1),
                "recorded_at": datetime.now(timezone.utc).isoformat(),
            }
            try:
                post_json(args.base_url, "/api/v1/positions", point)
                successes += 1
            except error.URLError as exc:
                print(f"Erro no envio: {exc}")
        print(f"Rodada {round_number + 1}: {successes}/{len(vehicles)} posicoes gravadas")
        remaining = args.interval - (time.monotonic() - start)
        if round_number + 1 < args.rounds and remaining > 0:
            time.sleep(remaining)


if __name__ == "__main__":
    main()
