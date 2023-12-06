"""
@Author: Team C
@Created: 04/12/2023 16:58
@Desc: Ce script permet de récupérer le projet github passé en paramètre, de le cloner, et de parcourir ses fichiers
pour en extraire les connexions à un bus kafka. Ce script se concentre sur les producer kafka des langages Java,
Kotlin, Javascript, Python, Typescript, Go, C#. Ces connexions sont ensuite stockées dans un fichier json où chaque
connexion est représentée par un objet de la forme :
{
    "name": "nom_du_projet",
    "kafka": "nom_du_bus_kafka",
    "topic": "nom_du_topic",
    "type": "producer"
}
"""
import uuid
import os
import json
import shutil
import subprocess
import re
import stat
import time
import argparse
from common.utils import BCOLORS


def delete_folder(project_name):
    """
    Supprimer un dossier
    :param path: chemin du dossier à supprimer
    """
    path = f'./projects/{project_name}'
    # Is the error an access error?
    os.chmod(path, stat.S_IWUSR)
    for r, _, ff in os.walk(path):
        for momo in dirs:
            os.chmod(os.path.join(r, momo), stat.S_IWUSR)
        for momo in ff:
            os.chmod(os.path.join(r, momo), stat.S_IWUSR)
    print(f"{BCOLORS.OKBLUE}Permissions changed{BCOLORS.ENDC}")
    if os.path.exists(path):
        print(f"{BCOLORS.OKBLUE}Deleting project {project_name}...{BCOLORS.ENDC}")
        # Delete using absolute path
        shutil.rmtree(f'{os.getcwd()}\\projects\\{project_name}')
        print(f"{BCOLORS.OKBLUE}Project {project_name} deleted{BCOLORS.ENDC}")
    else:
        print(f"{BCOLORS.WARNING}Project {project_name} does not exist{BCOLORS.ENDC}")


def clone_project(project_name):
    """
    Cloner un projet github
    :param project_name: nom du projet à cloner
    """
    # Vérifier si le dossier ./projects existe, sinon le créer
    if not os.path.exists('./projects'):
        print(f"{BCOLORS.WARNING}Folder ./projects does not exist{BCOLORS.ENDC}")
        os.makedirs('./projects')
        print(f"{BCOLORS.OKBLUE}Folder ./projects created{BCOLORS.ENDC}")

    # Cloner le projet s'il n'existe pas
    if os.path.exists(f'./projects/{project_name}'):
        print(f"{BCOLORS.WARNING}Project {project_name} already exists{BCOLORS.ENDC}")
        return
    os.chdir('./projects')
    print(f"{BCOLORS.OKBLUE}Cloning project {project_name}...{BCOLORS.ENDC}")
    subprocess.run(['git', 'clone', f'https://github.com/{project}'])
    os.chdir('..')
    print(f"{BCOLORS.OKBLUE}Project {project_name} cloned{BCOLORS.ENDC}")


if __name__ == '__main__':

    # Générer un identifiant du run
    run_id = str(uuid.uuid4())

    parser = argparse.ArgumentParser(description='Extract kafka producers from a github project')
    parser.add_argument('-p', '--project', metavar='project', type=str, help='github project to analyze')
    parser.add_argument('-o', '--output', metavar='output', type=str, help='output file',
                        default=f'./outputs/output-{run_id}.json')
    args = parser.parse_args()

    # Récupérer le projet github passé en paramètre
    project = args.project
    project_name = project.split('/')[1]
    project_folder = f"./projects/{project_name}"
    output = args.output if args.output else f'./outputs/{project_name}-{run_id}.json'
    print(f"{BCOLORS.HEADER}Analyzing project {project}...{BCOLORS.ENDC}")

    # Cloner le projet
    clone_project(project)

    # Parcourir les fichiers du projet
    os.chdir(project_folder)
    producers = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.java') or file.endswith('.kt') or file.endswith('.js') or file.endswith(
                    '.py') or file.endswith('.ts') or file.endswith('.go') or file.endswith('.cs'):
                # Lire le fichier
                with open(os.path.join(root, file), 'r') as f:
                    content = f.read()
                    # print(f'{content}')
                    # Extraire les connexions à un bus kafka
                    matches = re.findall(r'topic', content)
                    print(f'{content}') if matches else None
                    # if matches:
                    #     # Récupérer le nom du bus kafka et du topic
                    #     kafka = re.findall(r'bootstrap.servers\s*=\s*"(.*)"', content)
                    #     topic = re.findall(r'topic\s*=\s*"(.*)"', content)
                    #     if kafka and topic:
                    #         # Ajouter la connexion à la liste des connexions
                    #         producer = {
                    #             "name": project_name,
                    #             "kafka": kafka[0],
                    #             "topic": topic[0],
                    #             "type": "producer"
                    #         }
                    #         producers.append(producer)
                    #         print(f"Producer found in {os.path.join(root, file)}")
    os.chdir('../..')
    print(f"{BCOLORS.OKGREEN}Project {project_name} analyzed{BCOLORS.ENDC}")

    # Supprimer le projet
    # delete_folder(project_name)

    # Créer le dossier ./outputs s'il n'existe pas
    if not os.path.exists('./outputs'):
        print(f"{BCOLORS.WARNING}Folder ./outputs does not exist{BCOLORS.ENDC}")
        os.makedirs('./outputs')
        print(f"{BCOLORS.OKBLUE}Folder ./outputs created{BCOLORS.ENDC}")

    # Ecrire les connexions dans un fichier json
    if len(producers) == 0:
        print(f"{BCOLORS.WARNING}No producers found{BCOLORS.ENDC}")
        exit(0)
    with open(output, 'w') as f:
        json.dump(producers, f)
        print(f"{BCOLORS.OKGREEN}Producers written in {output}{BCOLORS.ENDC}")
