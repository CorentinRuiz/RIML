import json
import glob
import sys
import os

def counter_prod_cons(path):
      with open(path, 'r') as f:
        data = json.load(f)
        count = 0
        for entry in data:
            for item in entry:
                if item.get("type") == "consumer" or item.get("type") == "producer":
                    count += 1
        return count

def counter_ser_top(path):
    with open(path, 'r') as f:
        data = json.load(f)
        count = len(data)
        return count
    
def calculate_topics_diversity(topics_number,services_number):
    return topics_number/services_number

def count_services_comm_w_bus(paths):
    map_services_uses_buses = {}
    for path in paths:
        with open(path, 'r') as f:
            data = json.load(f)
            for entry in data:
                for item in entry:
                    if item.get("type") == "consumer" or item.get("type") == "producer":
                        service = item.get("service")
                        if service is not None:
                            if service not in map_services_uses_buses:
                                map_services_uses_buses[service] = 1
                            else:
                                map_services_uses_buses[service] += 1
    return map_services_uses_buses

def create_metrics(path_producers, path_consumers, path_services, path_topics):
    services_number = counter_ser_top(path_services)
    topics_number = counter_ser_top(path_topics)
    producers_number = counter_prod_cons(path_producers)
    consumers_number = counter_prod_cons(path_consumers)
    topics_diversity=calculate_topics_diversity(topics_number,services_number)
    number_services_comm_w_bus=count_services_comm_w_bus([path_producers,path_consumers])
    
    data = {
    "producers_number": producers_number,
    "consumers_number": consumers_number,
    "services_number": services_number,
    "topics_number": topics_number,
    "topics_diversity": topics_diversity,
    "communication_rate_map": number_services_comm_w_bus
    }
    
    return data
    
def save_metrics(data, path):
    with open(path, 'w') as ofile:
        json.dump(data, ofile, indent=4)
        print(f"Metrics written in {path}")
    
def main():
    path_producers = glob.glob("outputs/*--search-producers.json")
    path_consumers = glob.glob("outputs/*--search-consumers.json")
    path_services = glob.glob("outputs/*--search-microservices.json")
    path_topics = glob.glob("outputs/*--search-topics.json")
    
    nom_du_projet = sys.argv[1] if len(sys.argv) > 1 else "Nom_du_projet_inconnu"
    
    path_metrics = f'./metrics/{nom_du_projet.split("/")[1]}--metrics.json'
    

    metrics = create_metrics(path_producers[0], path_consumers[0], path_services[0], path_topics[0])
    
    if not os.path.exists('./metrics'):
        os.makedirs('./metrics')
    
    save_metrics(metrics, path_metrics)

if __name__ == "__main__":
    main()