import navegacao, aplicativo, YoutubeComments
from tkinter import filedialog
import csv


def salvarCsv():
    YoutubeComments.menuInicial.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(
        ('csv files', '*.csv'), ('text files', '*.txt'), ("jpeg files", "*.jpg"), ("all files", "*.*")),
                                                                   defaultextension='.txt')

    csv.register_dialect('myDialect', delimiter=';')
    with open(YoutubeComments.menuInicial.filename, 'w', newline='', encoding='windows-1252', errors='ignore') as saida:  # iso-8859-1  windows-1252  utf-8
        escrever = csv.writer(saida, dialect='myDialect')
        escrever.writerow(['ID', 'Nome', 'Data', 'Comentário'])
        for id, item in enumerate(navegacao.infoDados):
            escrever.writerow([id, item['authorDisplayName'], item['publishedAt'][:10], item['textDisplay']])