import modelo
import plotly.graph_objs as go

Grafo,node_trace,edge_trace = modelo.gera_rede(100,0.125)

node_adjacencies = []
node_text = []
for node, adjacencies in enumerate(Grafo.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))
    node_text.append('# of connections: '+str(len(adjacencies[1])))

node_trace.marker.color = node_adjacencies
node_trace.text = node_text

#plot da rede livre de escala - Barabasi
fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='Rede feita aleatóriamente para estudo',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Rede feita por estudo - Ricardo Rosal",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
fig.show()