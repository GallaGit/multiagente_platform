"""CLI: create HubSpot custom properties for lead orchestration."""

from __future__ import annotations

import sys

from api.leads.hubspot import HubSpotClient, HubSpotError


def main() -> int:
    try:
        client = HubSpotClient()
        created = client.ensure_custom_properties()
    except HubSpotError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if created:
        print(f"Propiedades creadas: {', '.join(created)}")
    else:
        print("Todas las propiedades custom ya existen.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
