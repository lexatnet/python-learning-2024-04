import argparse

parser = argparse.ArgumentParser(description='Анализирует данные и создает отчет')

parser.add_argument('input')
parser.add_argument('sheet')

parser.add_argument('output') 

args = parser.parse_args()