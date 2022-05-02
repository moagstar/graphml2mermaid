import click
from networkx.readwrite.graphml import read_graphml


@click.command()
@click.argument('filename')
def convert(filename):

    # TODO: more options, read edge type, node shape etc.

    result = ['graph TB']

    G = read_graphml(filename)

    for node, label in G.nodes.data('label'):
        if label:
            result.append(f'    {node}["{label}]"')

    edge_labels = {
        (source, target): f'- {label} -' if label else ''
        for source, target, label in G.edges.data('label')
    }
    for source, target in G.edges():
        label = edge_labels[(source, target)]
        result.append(f'    {source}-"{label}"->{target}')

    print('\n'.join(result))


if __name__ == '__main__':
    convert()
