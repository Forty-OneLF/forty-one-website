"""Turn the hub's meetings into availability.json for the website's call booking.

Usage: python3 tools/build_availability.py <meetings_dir> [availability.json]

<meetings_dir> holds one JSON file per meeting, as saved by the ArtifactData tool with
out_dir (each file is {"id":..., "data": {...}} or just the meeting fields).

Only busy slot times are written. No titles, names or locations ever leave the hub.
"""
import json, os, sys
from datetime import datetime, timedelta, date
from zoneinfo import ZoneInfo

LONDON = ZoneInfo("Europe/London")
SLOTS = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:30', '13:00', '13:30',
         '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00']
CALL_MIN = 15        # length of a website call
BUFFER_MIN = 15      # breathing space either side of a diary entry
DEFAULT_MIN = 60     # assumed length when a meeting has no end time
DAYS_AHEAD = 21


def minutes(hhmm):
    h, m = hhmm.split(':')[:2]
    return int(h) * 60 + int(m)


def load(meetings_dir):
    out = []
    for root, _, files in os.walk(meetings_dir):
        for f in files:
            if f.endswith('.json'):
                doc = json.load(open(os.path.join(root, f)))
                out.append(doc.get('data', doc))
    return out


def build(meetings):
    today = datetime.now(LONDON).date()
    last = today + timedelta(days=DAYS_AHEAD)
    busy = {}
    for m in meetings:
        if (m.get('status') or '').lower() == 'cancelled' or m.get('deletedAt'):
            continue
        d, t = m.get('date'), m.get('time')
        if not d:
            continue
        try:
            day = date.fromisoformat(d)
            if t:
                start = minutes(t)
                end = minutes(m['endTime']) if m.get('endTime') else start + DEFAULT_MIN
            else:                         # a meeting with no time (e.g. a day in London) blocks the whole day
                start, end = minutes(SLOTS[0]), minutes(SLOTS[-1]) + CALL_MIN
        except (ValueError, KeyError):
            continue
        if not (today <= day <= last):
            continue
        if end <= start:
            end = start + DEFAULT_MIN
        lo, hi = start - BUFFER_MIN, end + BUFFER_MIN
        for s in SLOTS:
            a = minutes(s)
            if a < hi and a + CALL_MIN > lo:
                busy.setdefault(d, set()).add(s)
    return {
        'generated': datetime.now(LONDON).isoformat(timespec='minutes'),
        'busy': {k: sorted(v) for k, v in sorted(busy.items())},
    }


if __name__ == '__main__':
    result = build(load(sys.argv[1]))
    dst = sys.argv[2] if len(sys.argv) > 2 else 'availability.json'
    with open(dst, 'w') as fh:
        json.dump(result, fh, indent=1)
        fh.write('\n')
    print(f"{dst}: {sum(len(v) for v in result['busy'].values())} busy slots over {len(result['busy'])} days")
