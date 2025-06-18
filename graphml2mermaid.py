
import html
import click
import networkx as nx
from networkx.readwrite.graphml import read_graphml

def escape_label(label):
    # Replace newlines with <br> and escape HTML special chars
    return html.escape(label).replace('\n', '<br>')

@click.command()
@click.argument('filename')
def convert(filename):
    result = ['graph TB']
    G = read_graphml(filename)

    for node, label in G.nodes.data('label'):
        if label:
            safe_label = escape_label(str(label))
            result.append(f'    {node}["{safe_label}"]')

    for source, target, data in G.edges(data=True):
        label = escape_label(str(data.get('label', '')))
        if label:
            result.append(f'    {source} -- {label} --> {target}')
        else:
            result.append(f'    {source} --> {target}')

    print('\n'.join(result))

if __name__ == '__main__':
    convert()