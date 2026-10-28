import http from 'k6/http';
import { check } from 'k6';

const BASE_URL = __ENV.BASE_URL || 'http://localhost:8000';
const VEHICLES = (__ENV.VEHICLE_IDS || '').split(',').filter(Boolean);
const RATE = Number(__ENV.RATE || 10);

export const options = {
  scenarios: {
    ingestion: {
      executor: 'constant-arrival-rate',
      rate: RATE,
      timeUnit: '1s',
      duration: __ENV.DURATION || '1m',
      preAllocatedVUs: 20,
      maxVUs: 200,
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};

export default function () {
  if (VEHICLES.length === 0) {
    throw new Error('Configure VEHICLE_IDS separado por virgulas (scripts/seed_vehicles.py).');
  }
  const idx = Math.floor(Math.random() * VEHICLES.length);
  const body = JSON.stringify({
    vehicle_id: VEHICLES[idx],
    latitude: -23.0 + (Math.random() - 0.5) * 0.04,
    longitude: -46.84 + (Math.random() - 0.5) * 0.04,
    speed_kmh: Math.random() * 100,
    recorded_at: new Date().toISOString(),
  });
  const response = http.post(`${BASE_URL}/api/v1/positions`, body, {
    headers: { 'Content-Type': 'application/json' },
  });
  check(response, { '201 Created': (r) => r.status === 201 });
}
