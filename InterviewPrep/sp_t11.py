import json


def find_non_running_pods(filename):
    non_running_pods = []
    pods_missing_info = 0

    with open(filename) as jsonfile:
        pods = json.load(jsonfile)

        for pod in pods["items"]:
            try:
                namespace = pod["metadata"]["namespace"]
                name = pod["metadata"]["name"]
                phase = pod["status"]["phase"]
            except KeyError:
                pods_missing_info += 1
                continue

            if phase != "Running":
                non_running_pods.append((namespace, name, phase))

    return non_running_pods, pods_missing_info


print(find_non_running_pods("pods.json"))
