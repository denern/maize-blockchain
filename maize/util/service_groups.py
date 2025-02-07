from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "maize_harvester maize_timelord_launcher maize_timelord maize_farmer maize_full_node maize_wallet".split(),
    "node": "maize_full_node".split(),
    "harvester": "maize_harvester".split(),
    "farmer": "maize_harvester maize_farmer maize_full_node maize_wallet".split(),
    "farmer-no-wallet": "maize_harvester maize_farmer maize_full_node".split(),
    "farmer-only": "maize_farmer".split(),
    "timelord": "maize_timelord_launcher maize_timelord maize_full_node".split(),
    "timelord-only": "maize_timelord".split(),
    "timelord-launcher-only": "maize_timelord_launcher".split(),
    "wallet": "maize_wallet maize_full_node".split(),
    "wallet-only": "maize_wallet".split(),
    "introducer": "maize_introducer".split(),
    "simulator": "maize_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
