import json
import glob
import sys

def count_producer(path):
    with open(path, 'r') as f:
        data = json.load(f)
        count_producers = 0
        for entry in data:
            for item in entry:
                if item.get("type") == "producer":
                    count_producers += 1
        return count_producers

def count_consumer(path):
    with open(path, 'r') as f:
        data = json.load(f)
        count_consumers = 0
        for entry in data:
            for item in entry:
                if item.get("type") == "consumer":
                    count_consumers += 1
        return count_consumers

def count_services(path):
    with open(path, 'r') as f:
        data = json.load(f)
        count_services = len(data)
        return count_services
    
def count_topics(path):
    with open(path, 'r') as f:
        data = json.load(f)
        count_topics = len(data)
        return count_topics

def main():
    path_producers = glob.glob("outputs/*--search-producers.json")
    path_consumers = glob.glob("outputs/*--search-consumers.json")
    path_services = glob.glob("outputs/*--search-microservices.json")
    path_topics = glob.glob("outputs/*--search-topics.json")

    nom_du_projet = sys.argv[1] if len(sys.argv) > 1 else "Nom_du_projet_inconnu"

    services_number = count_services(path_services[0])
    topics_number = count_topics(path_topics[0])
    producers_number = count_producer(path_producers[0])
    consumers_number = count_consumer(path_consumers[0])
    

    if services_number > 3 and producers_number > 0 and consumers_number > 0:
        with open(f"results.txt", 'a') as file:
            file.write(f"Nom du projet : {nom_du_projet}\n")
            file.write(f"- services : {services_number}\n")
            file.write(f"- producer : {producers_number}\n")
            file.write(f"- consumer : {consumers_number}\n")
            file.write(f"- topics : {topics_number}\n")

if __name__ == "__main__":
    main()