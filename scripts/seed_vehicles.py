"""Cria veiculos sinteticos e grava os UUIDs para uso no k6."""
import argparse
import json
import uuid
from pathlib import Path
from urllib import error, request


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument("--output", type=Path, default=Path("vehicle_ids.txt"))
    args = parser.parse_args()
    if args.count < 1 or args.count > 10000:
        parser.error("--count deve ficar entre 1 e 10000")
    ids = []
    for _ in range(args.count):
        payload = json.dumps({"external_id": f"SIM-{uuid.uuid4().hex[:16]}"}).encode("utf-8")
        req = request.Request(
            f"{args.base_url}/api/v1/vehicles",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with request.urlopen(req, timeout=10) as response:
                ids.append(json.load(response)["id"])
        except error.URLError as exc:
            raise SystemExit(f"Falha no cadastro sintetico: {exc}") from exc
    args.output.write_text("\n".join(ids) + "\n", encoding="utf-8")
    print(f"Criados {len(ids)} veiculos; IDs em {args.output}")


if __name__ == "__main__":
    main()
