class Mapa:
    def __init__ (self, ini, fim, tam, velo):
        self.inicio = ini
        self.final = fim
        self.distancia = tam
        self.velocidade = velo
        
    def procura_no (self, ini, fim, velo):
        if (self.inicio == ini and self.final == fim):
            self.velocidade = velo
    
    def calcula_tempo (self):
        if (self.velocidade == 0):
            self.tempo = 9999999
        else:
            self.tempo = self.distancia / self.velocidade
            
    def checa_origem(self, origem):
        if self.inicio == origem:
            return 0
        else:
            return 1
        
    def checa_destino(self, fim):
        if self.final == fim:
            return 0
        else:
            return 1
        
def main():
    dijsktra = []
    velocidade_maxima = input()
    velocidade_maxima = float (velocidade_maxima)
    
    linha = input()
    try:
        flag = linha[0]
        flag = 1
    except:
        flag = 0
    while flag == 1:
        dividido = linha.split(" ")
        try:
            x = Mapa(dividido[0], dividido[1], float(dividido[2]), float(dividido[3]))
            dijsktra.append(x)
            linha = input()
        except:
            x = Mapa(dividido[0], dividido[1], float(dividido[2]), velocidade_maxima)
            linha = input()
            dijsktra.append(x)
        try:
            flag = linha[0]
            flag = 1
        except:
            flag = 0
    
    linha = input()
    flag = 1
    while flag == 1:
        dividido = linha.split(" ")
        try:
            for x in dijsktra:
                x.procura_no(dividido[0], dividido[1], float(dividido[2]))
            linha = input()
        except:
            ini = dividido[0]
            fim = input()
            flag = 0
            
    flag = 1
    for x in dijsktra:
        if flag == 1:
            flag = x.checa_origem(ini)
    if(flag == 1):
        print("Origem nao existe")
        return
    
    flag = 1
    for x in dijsktra:
        if flag == 1:
            flag = x.checa_destino(fim)
    if(flag == 1):
        print("Destino nao existe")
        return
    
    for no in dijsktra:
        no.calcula_tempo()
            
    vertices = []
    for no in dijsktra:
        if not(no.inicio in vertices):
            vertices.append(no.inicio)
        if not(no.final in vertices):
            vertices.append(no.final)
                        
    custo = {}
    caminhos = {}
    for v in vertices:
        custo[v] = 9999999
        caminhos[v] = -1
    custo[ini] = 0
    vertices_nao_visitados = custo.copy();
    while len(vertices_nao_visitados) > 0:
        menor = min(vertices_nao_visitados, key = vertices_nao_visitados.get)
        vertice_menor = vertices_nao_visitados[menor]
        del vertices_nao_visitados[menor]
        for no in dijsktra:
            if no.inicio == menor:
                if custo[no.final] > custo[no.inicio] + no.tempo:
                    custo[no.final] = custo[no.inicio] + no.tempo
                    caminhos[no.final] = no.inicio
                    vertices_nao_visitados[no.final] = custo[no.final]
    
    final_parcial = fim
    caminho_mais_curto = [fim]
    while final_parcial != ini and final_parcial != -1:
        final_parcial = caminhos[final_parcial]
        caminho_mais_curto = caminho_mais_curto + [final_parcial]
        
    if(final_parcial == -1):
        print('Nao existe caminho de '+ini+' para '+fim)
        return
    
    print(int(custo[fim]*60), end='')
    print(" minutos")
    caminho_mais_curto.reverse()
    print(caminho_mais_curto)
    
                
if __name__ == "__main__":
    main()