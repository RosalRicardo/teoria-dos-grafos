# Teoria de grafos
## Exemplos de modelos usando teoria dos grafos

coleção de exemplos de implementações de representações de modelos usando teoria dos grafos e redes complexas.

### Redes Complexas

#### Rede livres de escala

Uma rede livre de escala é uma rede cuja distribuição de graus segue uma lei de potência, pelo menos assintoticamente. Ou seja, a fração P de nós na rede tendo k conexões com outros nós vale para grandes valores de k as.

$P(k) ~ k^-\gamma$

modelo com função "gerar_rede(numero de nós, taxa de conexão)" com os seguintes parâmetros:
*numero de nós: quantidade de nós na rede.
*taxa de conexão: taxa de quantos nós serão conectados em relação ao potencial maximo de conexão. (valor entre 0 e 1)

![rede livre de escala](https://raw.githubusercontent.com/RosalRicardo/teoria-dos-grafos/redes-complexas/src/redes%20livre%20de%20escala/exemplos/redelivreescala.png "Exemplo - rede livre de escala")

#### Rede de Barabasi

### Grafos