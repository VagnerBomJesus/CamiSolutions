#--------------------Validaçãoes----------------------
from tkinter import PhotoImage


def ValidaISO(ISO):
    import re
    regex = r"[A-Z]{2,2}"
    matches = re.finditer(regex, ISO, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        if len(ISO)==2:
            return True
        else:
            return False
    else:
        return False
def ValidaOpcoes(Opcoes):
    import re
    regex = r"[0-7]{1,1}"
    matches = re.finditer(regex, Opcoes, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        if len(Opcoes)==1:
            return True
        else:
            return False
    else:
        return False
def ValidaISO3(ISO3):
    import re
    regex = r"[A-Z]{3,3}"
    matches = re.finditer(regex, ISO3, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        if len(ISO3)==3:
            return True
        else:
            return False
    else:
        return False


def ValidaISO_Numeric(ISO_Numeric):
    import re
    regex = r"[0-999]{3,3}"
    matches = re.finditer(regex,ISO_Numeric, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        if len(ISO_Numeric) == 3:
            return True
        else:
            return False
    else:
        return False

def ValidaCountry(Country):
    import re
    regex = r"[A-Z][a-z]{2,8}( [a-z]{2,3}){0,1}( [A-Z][a-z]{2,8}){0,4}"
    matches = re.finditer(regex, Country, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False
def ValidaCountryPesquisa(Country):
    import re
    regex = r"[A-Z][a-z]{1,8}( [a-z]{2,3}){0,1}( [A-Z][a-z]{2,8}){0,4}"
    matches = re.finditer(regex, Country, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False
def ValidaArea(Area):
    import re
    regex = r"[0-9]{2,8}"
    matches = re.finditer(regex, Area, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False

def Validatld(tld):
    import re
    regex = r"[a-z]{2,2}"
    matches = re.finditer(regex, tld, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        if len(tld)==2:
            return True
        else:
            return False
    else:
        return False
def ValidaCurrencyName(CurrencyName):
    import re
    regex = r"[A-Z][a-z]{2,8}( [a-z]{2,3}){0,1}( [A-Z][a-z]{2,8}){0,4}"
    matches = re.finditer(regex, CurrencyName, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False

def ValidaContinent(Continent):
    import re
    regex = r"[A-Z]{3,8}([A-Z]{2,8}){0,4}"
    matches = re.finditer(regex, Continent, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False

def ValidaPhone(Phone):
        import re
        regex = r"[0-9]{2,3}"
        matches = re.finditer(regex, Phone, re.MULTILINE)
        matchNum = 0
        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1
        if matchNum == 1:
            if len(Phone) == 3:
                return True
            else:
                return False
        else:
            return False


def ValidaLanguages(Languages):
    import re
    regex = r"[a-z]{2,2}( [A-Z]{2,3}){2,2}"
    matches = re.finditer(regex, Languages, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False
#-------------------------------------------------------------
inserir_Continente = 'pais.txt'
#-------------------------------------------------------------
import os
def Menu(Titulo, Opcoes, np):
    print("\t\t\t\t\t\t\t\t\033[1;33;m---------------------------\033[m")
    print("\t\t\t\t\t\t\t\t\033[1;32;mPrograma do Ubunto Solution\033[m")
    print("\t\t\t\t\t\t\t\t\033[1;33;m---------------------------\033[m")
    from datetime import datetime

    agora = datetime.now()
    #print(agora)
    print("\033[1;30;mData: ", agora.strftime("%Y-%m-%d\033[m"))
    print("\033[1;30;mHora: ", agora.strftime("%X\033[m"))
    print("\n")
    print(Titulo)
    print()
    for i in range(np):
        print(i + 1, "- ", Opcoes[i])
    print("0 -  Terminar")
    while True:
        print("Opção?")

        op = int(input())
        if (op >= 0 and op <= np):
            break
    return op
#-------------------Geografia---------------------------
def Geografia():

    print("\n")
    Titulo = "Tudo sobre Geografia"
    Opcoes = ["Gestão de Continentes", "Gestão de Paises ", "Gestão de Códigos Postais",
              "Gestão de Cidades"]
    np = 4
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            GestaoContinentes()
        elif op == 2:
            GestaoPaises()
        elif op == 3:
            GestaoCodigosPostais()
        elif op == 4:
            GestaoCidades()
        elif op == 0:
            break
        break
#-------------------GestaoContinentes-------------------------
def GestaoContinentes():

    Titulo = "Gestão de Continentes"
    Opcoes = ["Inserir Continentes", "Pesquisar Continentes"]
    np = 2
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            InserirContinente()
        elif op == 2:
            PesquisarContinentePorNome()
        elif op == 0:
            break
def InserirContinente():
    while True:
        ISO = input("Inserir ISO?")
        if ValidaISO(ISO) == True:
            break
    while True:
        ISO3 = input("Inserir ISO3?")
        if ValidaISO3(ISO3) == True:
            break
    while True:
        ISO_Numeric = input("Inserir ISO_Numeric?")
        if ValidaISO_Numeric(ISO_Numeric)== True:
            break
    while True:
        fips = input("Inserir fips?")
        if ValidaISO(fips) == True:
            break
    while True:
        Country = input("Inserir Country?")
        if ValidaCountry(Country)== True:
            break
    while True:
        Capital = input("Inserir Capital?")
        if ValidaCountry(Capital)== True:
            break
    while True:
        Area = input("Inserir Area?")
        if ValidaArea(Area)== True:
            break
    while True:
        Population = input("Inserir população?")
        if ValidaArea(Population)== True:
            break
    while True:
        Continent = input("Inserir Continete?")
        if ValidaContinent(Continent)== True:
            break
    while True:
        tld = input("Inserir tld?")
        if Validatld(tld)==True:
            break
    while True:
        CurrencyCode = input("Inserir CurreacyCode?")
        if ValidaISO3(CurrencyCode) == True:
            break
    while True:
        CurrencyName = input("Inserir CuriacyNome?")
        if ValidaCurrencyName(CurrencyName) == True:
            break
    while True:
        Phone = input("inserir Phone?")
        if ValidaPhone(Phone)==True:
            break
    while True:
        Postal_Code_Format = input("Inserir Postal_Code_Format?")
        if Postal_Code_Format != "":
            break
    while True:
        Postal_Code_Regex = input("Inserir Postal_Code_Regex?")
        if Postal_Code_Regex != "":
            break
    while True:
        Languages = input("Inserir Language?")
        if Languages != "":
            break
    while True:
        geonameid = input("Inserir geonameid?")
        if geonameid != "":
            break
    while True:
        neighbours = input("Inserir neighbours?")
        if ValidaArea(neighbours) == True:
            break
    while True:
        EquivalentFipsCode = input("inserir EquivalentFipsCode?")
        if ValidaISO(EquivalentFipsCode)== True:
            break

    f  = open(inserir_Continente,"at")
    print("%s" % ISO, file=f, end='\t', sep='\n')
    print("%s" % ISO3, file=f, end='\t', sep='')
    print("%s" % ISO_Numeric, file=f, end='\t', sep='')
    print("%s" % fips, file=f, end='\t', sep='')
    print("%s" % Country, file=f, end='\t', sep='')
    print("%s" % Capital, file=f, end='\t', sep='')
    print("%s" % Area,    file=f, end='\t', sep='')
    print("%s" % Population, file=f, end='\t', sep='')
    print("%s" % Continent, file=f, end='\t', sep='')
    print("%s" % tld, file=f, end='\t', sep='')
    print("%s" % CurrencyCode, file=f, end='\t', sep='')
    print("%s" % CurrencyName, file=f, end='\t', sep='')
    print("%s" % Phone, file=f, end='\t', sep='')
    print("%s" % Postal_Code_Format, file=f, end='\t', sep='')
    print("%s" % Postal_Code_Regex, file=f, end='\t', sep='')
    print("%s" % Languages, file=f, end='\t', sep='')
    print("%s" % geonameid, file=f, end='\t', sep='')
    print("%s" % neighbours, file=f, end='\t', sep='')
    print("%s" % EquivalentFipsCode, file=f)
    f.close()
    print("\n")
    print("Fim da Inserção!")
    input("Prima enter para continuar")
    


def PesquisarContinentePorNome():
    print("\n")
    print("Pesquisar Continente Por Nome")
    f = open("pais.txt", "rt")
    linhas = f.readlines()  # vector
    f.close()
    np = 0
    while True:
        nome_procurar = input("Nome do Continente que desejas procurar? ")
        if ValidaContinent(nome_procurar) == True:
            break
    print("\n")
    print("%3s %4s %6s \t%-13s %29s"
                  "%18s %11s %21s"
          % ("\033[1;34;mContinent", "ISO", "ISO3", "Country", "Capital",
             "Area", "Phone",
             "Languages\033[m"))
    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        if len(colunas) < 18:
            continue
        ISO = colunas[0]
        ISO3 = colunas[1]
        Country = colunas[5]
        Capital = colunas[6]
        Area = colunas[7]
        Continent = colunas[9]
        Phone = colunas[13]
        Languages = colunas[16]
        # if  Languages.find (nome_procurar.) >=0:
        if Continent.find(nome_procurar) >= 0:
            print("%2s \t%5s %6s \t%-35s %-20s %-10s"
                  "\t%-15s %s "
                  % (Continent, ISO, ISO3, Country, Capital
                     , Area,  Phone, Languages))
            np = np + 1
    print("\n")
    print("Total de Paises Contidos na %2s: %d" % (nome_procurar, np))
    input("Prima enter para continuar")
#----------------GestaoPaises------------------
def GestaoPaises():

    Titulo = "Gestão de Paises"
    Opcoes = ["Inserir Paises", "Pesquisar Paises","Caminho entre Paises"]
    np = 3
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            InserirPaises()
        elif op == 2:
            PesquisarPaises()
        elif op ==3:
            Caminho()
        elif op == 0:
            break
def InserirPaises():
    while True:
        ISO = input("Inserir ISO?")
        if ValidaISO(ISO) == True:
            break
    while True:
        ISO3 = input("Inserir ISO3?")
        if ValidaISO3(ISO3) == True:
            break
    while True:
        ISO_Numeric = input("Inserir ISO_Numeric?")
        if ValidaISO_Numeric(ISO_Numeric) == True:
            break
    while True:
        fips = input("Inserir fips?")
        if ValidaISO(fips) == True:
            break
    while True:
        Country = input("Inserir Country?")
        if ValidaCountry(Country) == True:
            break
    while True:
        Capital = input("Inserir Capital?")
        if ValidaCountry(Capital) == True:
            break
    while True:
        Area = input("Inserir Area?")
        if ValidaArea(Area) == True:
            break
    while True:
        Population = input("Inserir população?")
        if ValidaArea(Population) == True:
            break
    while True:
        Continent = input("Inserir Continete?")
        if ValidaCountry(Continent) == True:
            break
    while True:
        tld = input("Inserir tld?")
        if Validatld(tld) == True:
            break
    while True:
        CurrencyCode = input("Inserir CurreacyCode?")
        if ValidaISO3(CurrencyCode) == True:
            break
    while True:
        CurrencyName = input("Inserir CuriacyNome?")
        if ValidaCurrencyName(CurrencyName) == True:
            break
    while True:
        Phone = input("inserir Phone?")
        if ValidaPhone(Phone) == True:
            break
    while True:
        Postal_Code_Format = input("Inserir Postal_Code_Format?")
        if Postal_Code_Format != "":
            break
    while True:
        Postal_Code_Regex = input("Inserir Postal_Code_Regex?")
        if Postal_Code_Regex != "":
            break
    while True:
        Languages = input("Inserir Language?")
        if Languages != "":
            break
    while True:
        geonameid = input("Inserir geonameid?")
        if geonameid != "":
            break
    while True:
        neighbours = input("Inserir neighbours?")
        if ValidaArea(neighbours) == True:
            break
    while True:
        EquivalentFipsCode = input("inserir EquivalentFipsCode?")
        if ValidaISO(EquivalentFipsCode) == True:
            break

    f = open(inserir_Continente, "at")
    print("%s" % ISO, file=f, end='\t', sep='\n')
    print("%s" % ISO3, file=f, end='\t', sep='')
    print("%s" % ISO_Numeric, file=f, end='\t', sep='')
    print("%s" % fips, file=f, end='\t', sep='')
    print("%s" % Country, file=f, end='\t', sep='')
    print("%s" % Capital, file=f, end='\t', sep='')
    print("%s" % Area, file=f, end='\t', sep='')
    print("%s" % Population, file=f, end='\t', sep='')
    print("%s" % Continent, file=f, end='\t', sep='')
    print("%s" % tld, file=f, end='\t', sep='')
    print("%s" % CurrencyCode, file=f, end='\t', sep='')
    print("%s" % CurrencyName, file=f, end='\t', sep='')
    print("%s" % Phone, file=f, end='\t', sep='')
    print("%s" % Postal_Code_Format, file=f, end='\t', sep='')
    print("%s" % Postal_Code_Regex, file=f, end='\t', sep='')
    print("%s" % Languages, file=f, end='\t', sep='')
    print("%s" % geonameid, file=f, end='\t', sep='')
    print("%s" % neighbours, file=f, end='\t', sep='')
    print("%s" % EquivalentFipsCode, file=f)
    f.close()
    print("Fim da Inserção")
    input("Prima enter para continuar")
def PesquisarPaises():
    print("\n")
    print("Pesquisar Paises Por Nome")
    f = open("pais.txt", "rt")
    linhas = f.readlines()  # vector
    np = 0
    f.close()
    while True:
        nome_procurar = input("Nome do Pais que desejas procurar?")
        if ValidaCountryPesquisa(nome_procurar) == True:
            break
    np=0
    print("%3s %4s %6s \t%-13s %29s"
          "%18s %11s %20s %30s"
          % ("Continent", "ISO", "ISO3", "Country", "Capital",
             "Area", "Phone",
              "neighbours","Languages"))

    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        if len(colunas) < 18:
            continue
        ISO = colunas[0]
        ISO3 = colunas[1]
        Country = colunas[5]
        Capital = colunas[6]
        Area = colunas[7]
        Continent = colunas[9]
        Phone = colunas[13]
        Languages = colunas[16]
        neighbours = colunas[18]
        # if  Languages.find (nome_procurar.) >=0:
        if Country.find(nome_procurar) >= 0:
            print("%2s \t%5s %6s \t%-35s %-20s %-10s"
                  "\t%-15s %-20s %20s"
                  % (Continent, ISO, ISO3, Country, Capital
                     , Area, Phone, neighbours,Languages))

            np = np + 1
    print("\n")
    print("Total de Paises encontrados: %d" % np)
    input("Prima enter para continuar")
def PesquusPaisVetor(paises,pais):
    for p in paises:
        if p[0]==pais:
            return p
def PesquusPaisNome(paises,pais):
    for p in paises:
        if p[1]==pais:
            return p
def Caminho():
    from Djikstra.Djikstra import LerPaisesParaVetor
    paises = LerPaisesParaVetor()
    from Djikstra.Djikstra import Graph
    graph = Graph()
    for i in range(1, len(paises)):
        p = paises[i]
        pais = p[0]
        vizinhos_string = p[2]
        # print(pais, vizinhos)
        if vizinhos_string == "":
            continue
        vizinhos = vizinhos_string.split(',')
        for v in vizinhos:
            # print(pais, v)
            graph.add_edge(pais, v, 1)
    from Djikstra.Djikstra import dijsktra
    #caminho = dijsktra(graph, 'DE', 'PT');
    print("Exemplo de paises")
    for i in range(1, len(paises)):
        print(paises[i][0], " - ", paises[i][1])
    while True:
        origem = input("Pais de Origem?")
        if ValidaCountry(origem) == True:
            break
    while True:
        destino = input("Pais de Destino?")
        if ValidaCountry(destino)== True:
            break
    iso_origem = PesquusPaisNome(paises, origem)[0]
    iso_destino = PesquusPaisNome(paises, destino)[0]
    caminho = dijsktra(graph, iso_origem, iso_destino)
    x=""
    for iso in caminho:
        pais=PesquusPaisVetor(paises,iso)
        x=x+pais[1] + " -> "
    print(origem+"->"+ destino + " : " + x.rstrip(" -> "))
    #print()
    #print(caminho)
    input("Prima enter para continuar")

def GestaoCodigosPostais():

    Titulo = "Gestão de Códigos Postais"
    Opcoes = ["Inserir Códigos Postais", "Pesquisar Códigos Postais"]
    np = 2
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            InserirCodigosPostais()
        elif op == 2:
            PesquisarCodigosPostais()
        elif op == 0:
            break
def InserirCodigosPostais():
    while True:
        ISO = input("Inserir ISO?")
        if ValidaISO(ISO) == True:
            break
    while True:
        ISO3 = input("Inserir ISO3?")
        if ValidaISO3(ISO3) == True:
            break
    while True:
        ISO_Numeric = input("Inserir ISO_Numeric?")
        if ValidaISO_Numeric(ISO_Numeric) == True:
            break
    while True:
        fips = input("Inserir fips?")
        if ValidaISO(fips) == True:
            break
    while True:
        Country = input("Inserir Country?")
        if ValidaCountry(Country) == True:
            break
    while True:
        Capital = input("Inserir Capital?")
        if ValidaCountry(Capital) == True:
            break
    while True:
        Area = input("Inserir Area?")
        if ValidaArea(Area) == True:
            break
    while True:
        Population = input("Inserir população?")
        if ValidaArea(Population) == True:
            break
    while True:
        Continent = input("Inserir Continete?")
        if ValidaCountry(Continent) == True:
            break
    while True:
        tld = input("Inserir tld?")
        if Validatld(tld) == True:
            break
    while True:
        CurrencyCode = input("Inserir CurreacyCode?")
        if ValidaISO3(CurrencyCode) == True:
            break
    while True:
        CurrencyName = input("Inserir CuriacyNome?")
        if ValidaCurrencyName(CurrencyName) == True:
            break
    while True:
        Phone = input("inserir Phone?")
        if ValidaPhone(Phone) == True:
            break
    while True:
        Postal_Code_Format = input("Inserir Postal_Code_Format?")
        if Postal_Code_Format != "":
            break
    while True:
        Postal_Code_Regex = input("Inserir Postal_Code_Regex?")
        if Postal_Code_Regex != "":
            break
    while True:
        Languages = input("Inserir Language?")
        if Languages != "":
            break
    while True:
        geonameid = input("Inserir geonameid?")
        if geonameid != "":
            break
    while True:
        neighbours = input("Inserir neighbours?")
        if ValidaArea(neighbours) == True:
            break
    while True:
        EquivalentFipsCode = input("inserir EquivalentFipsCode?")
        if ValidaISO(EquivalentFipsCode) == True:
            break

    f = open(inserir_Continente, "at")
    print("%s" % ISO, file=f, end='\t', sep='\n')
    print("%s" % ISO3, file=f, end='\t', sep='')
    print("%s" % ISO_Numeric, file=f, end='\t', sep='')
    print("%s" % fips, file=f, end='\t', sep='')
    print("%s" % Country, file=f, end='\t', sep='')
    print("%s" % Capital, file=f, end='\t', sep='')
    print("%s" % Area, file=f, end='\t', sep='')
    print("%s" % Population, file=f, end='\t', sep='')
    print("%s" % Continent, file=f, end='\t', sep='')
    print("%s" % tld, file=f, end='\t', sep='')
    print("%s" % CurrencyCode, file=f, end='\t', sep='')
    print("%s" % CurrencyName, file=f, end='\t', sep='')
    print("%s" % Phone, file=f, end='\t', sep='')
    print("%s" % Postal_Code_Format, file=f, end='\t', sep='')
    print("%s" % Postal_Code_Regex, file=f, end='\t', sep='')
    print("%s" % Languages, file=f, end='\t', sep='')
    print("%s" % geonameid, file=f, end='\t', sep='')
    print("%s" % neighbours, file=f, end='\t', sep='')
    print("%s" % EquivalentFipsCode, file=f)
    f.close()
    print("Fim da Inserção")
    input("Prima enter para continuar!")
def PesquisarCodigosPostais():
    print("\n")
    print("Pesquisar Codigos Postais!")
    f = open("pais.txt", "rt")
    linhas = f.readlines()  # vector
    f.close()
    nome_procurar = input("Formato do Codigo Postal?"
                          "\tEx(####-###).")
    np = 0
    print("%-15s \t%5s %6s \t%-35s %-20s %-10s"
            "\t%-15s %-20s %20s"
          % ("Continent", "ISO", "ISO3", "Country", "Capital",
             "Area", "Phone",
             "Postal_Code_Format", "Postal_Code_Regex"))

    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        if len(colunas) < 18:
            continue
        ISO = colunas[0]
        ISO3 = colunas[1]
        Country = colunas[5]
        Capital = colunas[6]
        Area = colunas[7]
        Continent = colunas[9]
        Phone = colunas[13]
        Postal_Code_Format = colunas[14]
        Postal_Code_Regex = colunas[15]
        # if  Languages.find (nome_procurar.) >=0:
        if Postal_Code_Format.find(nome_procurar) >= 0:
            print("%-15s \t%5s %6s \t%-35s %-20s %-10s"
                  "\t%-15s %-20s %20s"
                  % (Continent, ISO, ISO3, Country, Capital
                     , Area, Phone, Postal_Code_Format, Postal_Code_Regex))
            np = np + 1
    print("\n")
    print("Total de Paises Contidos neste Continent: %d" % np)
    input("Prima enter para continuar")
#----------------GestaoCidades----------------------
def GestaoCidades():

    Titulo = "Gestão de Cidades"
    Opcoes = ["Inserir Cidades", "Pesquisar Cidades"]
    np = 2
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            InserirCidades()
        elif op == 2:
            PesquisarCidades()
        elif op == 0:
            break
def InserirCidades():
    while True:
        ISO = input("Inserir ISO?")
        if ValidaISO(ISO) == True:
            break
    while True:
        ISO3 = input("Inserir ISO3?")
        if ValidaISO3(ISO3) == True:
            break
    while True:
        ISO_Numeric = input("Inserir ISO_Numeric?")
        if ValidaISO_Numeric(ISO_Numeric) == True:
            break
    while True:
        fips = input("Inserir fips?")
        if ValidaISO(fips) == True:
            break
    while True:
        Country = input("Inserir Country?")
        if ValidaCountry(Country) == True:
            break
    while True:
        Capital = input("Inserir Capital?")
        if ValidaCountry(Capital) == True:
            break
    while True:
        Area = input("Inserir Area?")
        if ValidaArea(Area) == True:
            break
    while True:
        Population = input("Inserir população?")
        if ValidaArea(Population) == True:
            break
    while True:
        Continent = input("Inserir Continete?")
        if ValidaCountry(Continent) == True:
            break
    while True:
        tld = input("Inserir tld?")
        if Validatld(tld) == True:
            break
    while True:
        CurrencyCode = input("Inserir CurreacyCode?")
        if ValidaISO3(CurrencyCode) == True:
            break
    while True:
        CurrencyName = input("Inserir CuriacyNome?")
        if ValidaCurrencyName(CurrencyName) == True:
            break
    while True:
        Phone = input("inserir Phone?")
        if ValidaPhone(Phone) == True:
            break
    while True:
        Postal_Code_Format = input("Inserir Postal_Code_Format?")
        if Postal_Code_Format != "":
            break
    while True:
        Postal_Code_Regex = input("Inserir Postal_Code_Regex?")
        if Postal_Code_Regex != "":
            break
    while True:
        Languages = input("Inserir Language?")
        if Languages != "":
            break
    while True:
        geonameid = input("Inserir geonameid?")
        if geonameid != "":
            break
    while True:
        neighbours = input("Inserir neighbours?")
        if ValidaArea(neighbours) == True:
            break
    while True:
        EquivalentFipsCode = input("inserir EquivalentFipsCode?")
        if ValidaISO(EquivalentFipsCode) == True:
            break
    f = open(inserir_Continente, "at")
    print("%s" % ISO, file=f, end='\t', sep='\n')
    print("%s" % ISO3, file=f, end='\t', sep='')
    print("%s" % ISO_Numeric, file=f, end='\t', sep='')
    print("%s" % fips, file=f, end='\t', sep='')
    print("%s" % Country, file=f, end='\t', sep='')
    print("%s" % Capital, file=f, end='\t', sep='')
    print("%s" % Area, file=f, end='\t', sep='')
    print("%s" % Population, file=f, end='\t', sep='')
    print("%s" % Continent, file=f, end='\t', sep='')
    print("%s" % tld, file=f, end='\t', sep='')
    print("%s" % CurrencyCode, file=f, end='\t', sep='')
    print("%s" % CurrencyName, file=f, end='\t', sep='')
    print("%s" % Phone, file=f, end='\t', sep='')
    print("%s" % Postal_Code_Format, file=f, end='\t', sep='')
    print("%s" % Postal_Code_Regex, file=f, end='\t', sep='')
    print("%s" % Languages, file=f, end='\t', sep='')
    print("%s" % geonameid, file=f, end='\t', sep='')
    print("%s" % neighbours, file=f, end='\t', sep='')
    print("%s" % EquivalentFipsCode, file=f)
    f.close()
    print("Fim de Inserção")
    input("Prima enter para continuar")
def PesquisarCidades():
    print("\n")
    print("Pesquisar Por Cidades")
    f = open("pais.txt", "rt")
    linhas = f.readlines()  # vector
    f.close()
    while True:
        nome_procurar = input("Nome da Cidade que desejas procurar?")
        if ValidaCountryPesquisa(nome_procurar) == True:
            break
    np=0
    print("%3s %4s %6s \t%-13s %29s %18s %11s %20s %33s"
          % ("Continent", "ISO", "ISO3", "Country", "Capital",
             "Area", "Phone", "neighbours", "Languages"))

    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        if len(colunas) < 18:
            continue
        ISO = colunas[0]
        ISO3 = colunas[1]
        Country = colunas[5]
        Capital = colunas[6]
        Area = colunas[7]
        Continent = colunas[9]
        Phone = colunas[13]
        Languages = colunas[16]
        neighbours = colunas[18]
        # if  Languages.find (nome_procurar.) >=0:
        if Capital.find(nome_procurar) >= 0:
            print("%2s \t%5s %6s \t%-35s %-20s %-10s"
                  "\t%-15s %-20s %20s"
                  % (Continent, ISO, ISO3, Country, Capital
                     , Area, Phone, neighbours, Languages))
            np = np + 1
    print("\n")
    print("Total de Cidades encontradas: %d " % np)
    input("Prima enter para continuar")


import os
# -----------Ficheiros de testos-------------
nome_ficheiro_clubes = "clubes.txt"
nome_ficheiro_jogadores = "jogadores.txt"
nome_ficheiro_Estadios = "estadios.txt"
nome_ficheiro_Equipas = "equipas.txt"
nome_ficheiro_Jogos = "jogos.txt"
# -----------Validaçãoes-------------
def ValidaSigla(Sigla):
    import re
    regex = r"[A-Z]{3,5}"
    matches = re.finditer(regex, Sigla, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False

def ValidaNome(Nome):
    import re
    regex = r"[A-Z][a-z]{2,8}( [a-z]{1,4}){0,1}( [A-Z][a-z]{2,8}){1,4}"
    matches = re.finditer(regex, Nome, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False

def ValidarNomeCampo(nome):
    import re
    regex = r"[A-Z][a-z]{1,8}([a-z]{1,4}){0,1}( [A-Z][a-z]{2,8}){0,4}"
    matches = re.finditer(regex, nome, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False

def ValidaSocios(VM):
    import re
    regex = r"[0-9]{2,8}"
    matches = re.finditer(regex, VM, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False

def ValidarNumero(PP):

    import re
    regex = r"[0-9]{1,2}"
    matches = re.finditer(regex, PP, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        return True
    else:
        return False

def ValidarSexo(sexo):

    import re
    regex = r"[A-Z]{1,2}"
    matches = re.finditer(regex, sexo, re.MULTILINE)
    matchNum = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
    if matchNum == 1:
        if len(sexo) == 1:
            return True
        else:
            return False
    else:
        return False

def LerData(msg, min=None, max=None):
    from datetime import datetime
    while True:
        data_texto = input(msg)
        try:
            data = datetime.strptime(data_texto, '%Y-%m-%d')
        except ValueError:
            print("Data inválida")
            continue
        if data >= min and data <= max:
            break
        else:
            print("Data fora do intervalo %s e %s"
                  % (min.strftime("%Y-%m-%d"),
                     max.strftime("%Y-%m-%d")))
    return data_texto

from datetime import datetime
data_min = datetime.strptime("1000-01-01", '%Y-%m-%d')
data_max = datetime.strptime("2019-12-31", '%Y-%m-%d')
##----Futebol-Jogo---------------------

def Futebol():
    print("\n")
    Titulo = "Menu principal"
    Opcoes = ["Gestão de Clubes", "Gestão de Jogadores ", "Gestão de Equipas",
              "Gestão de  Estádios", "Gestão de Jogos"]
    np = 5
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            GestaoClubes()
        elif op == 2:
            GestaoJogadores()
        elif op == 3:
            GestaoEquipas()
        elif op == 4:
            GestaoEstadios()
        elif op == 5:
            GestaoJogos()
        elif op == 0:
            break

# --------------------GestaoClubes------------------------------------------
def GestaoClubes():
    print("\n")
    Titulo = "Gestão de Clubes"
    Opcoes = ["Inserir Clubes", "Alterar Clubes",
              "Eliminar Clubes", "Listar todos os Clubes"]
    np = 4
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            InserirClubes()
        elif op == 2:
            AlterarClubes()
        elif op == 3:
            EliminarClubes()
        elif op == 4:
            ListarTodosClubes()
        elif op == 0:
            break

def InserirClubes():
    while True:
        Sigla = input("Inserir Sigla do Clube?")
        if ValidaSigla(Sigla) == True:
            break
    while True:
        NomeClube = input("Inserir Nome do Clube?")
        if ValidaNome(NomeClube) == True:
            break
    while True:
        Data_Fundacao = LerData("Data de Fundação do Clube?", data_min, data_max)
        if Data_Fundacao != "":
            break
    while True:
        Nome_Presidente = input("Nome do Presidente do %2s?" % (NomeClube))
        if ValidaNome(Nome_Presidente) == True:
            break
    while True:
        Numero_Socios = input("Inserir Numeros de Socios?")
        if ValidaSocios(Numero_Socios) == True:
            break
    while True:
        Numero_Modalidades = input("Numero de Modalidade deste Clube?")
        if ValidaSocios(Numero_Modalidades) == True:
            break
    f = open(nome_ficheiro_clubes, "at")
    print("%s" % Sigla, file=f, end='\t', sep='\n')
    print("%2s" % NomeClube, file=f, end='\t', sep='')
    print("%2s" % Data_Fundacao, file=f, end='\t', sep='')
    print("%2s" % Nome_Presidente, file=f, end='\t', sep='')
    print("%2s" % Numero_Socios, file=f, end='\t', sep='')
    print("%2s" % Numero_Modalidades, file=f)
    f.close()
    print("Fim da Inserção!")
    input("Prima enter para continuar!")

def AlterarClubes():
    f = open("clubes.txt", "rt")
    cabecalho = f.readline()
    jogadores = f.readlines()
    f.close()
    nome = input("Nome?")
    for i in range(len(jogadores)):
        j = jogadores[i]
        if len(j) < 5:
            continue
        # Jogador	Equipa	Posição	JJ	G
        Sigla, NomeClube, Data_Fundacao, Nome_Presidente, Numero_Socios, Numero_Modalidades = j.split("\t")
        if (NomeClube.find(nome)) >= 0:  # encontrado um jogador, escrever dados
            # print(j)
            print("Clube com'%s'no Nome encontrado" % nome)
            print("Sigla...................: %s" % Sigla)
            print("NomeClube...............: %s" % NomeClube)
            print("Data Fundacao...........: %s" % Data_Fundacao)
            print("Nome Presidente.........: %s" % Nome_Presidente)
            print("Numero Socios...........: %s" % Numero_Socios)
            print("Numero Modalidades......: %s" % Numero_Modalidades)
            o = input("Quer alterar ?(s/n)")
            if o == "s":  # novos dados
                while True:
                    NomeClube = input("Inserir novo Nome do Clube?")
                    if ValidaNome(NomeClube) == True:
                        break
                f = open("clubes.txt", "wt")  # gravar novos dados no ficheiro
                print(cabecalho, file=f, end='')
                for k in range(len(jogadores)):
                    if k == i:
                        print(Sigla, NomeClube, Data_Fundacao, Nome_Presidente,
                              Numero_Socios, Numero_Modalidades,
                              sep='\t', file=f, end='')
                    else:
                        print(jogadores[k], file=f, end='')
                f.close()
            elif o != 's':
                break
    print("Fim da Alteração!")
    input("Prima enter para continuar!")

def EliminarClubes():
    f = open("clubes.txt", "rt")
    cabecalho = f.readline()
    jogadores = f.readlines()
    f.close()
    nome = input("Nome?")
    for i in range(len(jogadores)):
        j = jogadores[i]
        if len(j) < 5:
            continue
        # Jogador	Equipa	Posição	JJ	G
        Sigla, NomeClube, Data_Fundacao, Nome_Presidente, \
        Numero_Socios, Numero_Modalidades = j.split("\t")
        if (NomeClube.find(nome)) >= 0:  # encontrado um jogador, escrever dados
            # print(j)
            print("Clube com'%s'no Nome encontrado" % nome)
            print("Sigla...................: %s" % Sigla)
            print("NomeClube...............: %s" % NomeClube)
            print("Data Fundacao...........: %s" % Data_Fundacao)
            print("Nome Presidente.........: %s" % Nome_Presidente)
            print("Numero Socios...........: %s" % Numero_Socios)
            print("Numero Modalidades......: %s" % Numero_Modalidades)

            o = input("Confirma eliminar Clubes?(s/n)")
            if o == "s":  # Confirma?
                f = open("clubes.txt", "wt")  # gravar novos dados no ficheiro
                print(cabecalho, file=f, end='')
                for k in range(len(jogadores)):
                    if k != i:
                        print(jogadores[k], file=f, end='')
                f.close()
                f = open("log_clubes.txt", "at")
                print("Operação:" "eliminar" + " Clubes")
                print("\n")
                f.close()
            elif o != 's':
                break
    print("Fim da Eliminação de Clube!")
    input("Prima enter para continuar!")

def ListarTodosClubes():
    print("\n")
    Titulo = "Gestão de Clubes"
    Opcoes = ["Listar Clubes", "Pesquisar Clubes",
              "Contar  Clubes", "Agrupar os Clubes"]
    np = 4
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            ListarClubes()
        elif op == 2:
            PesquisarClubes()
        elif op == 3:
            ContarClubes()
        elif op == 4:
            AgruparClubes()
        elif op == 0:
            break

def ListarClubes():
    print("Listas de Todos os Clubes!")
    f = open("clubes.txt", "rt")
    linhas = f.readlines()  # vector
    f.close()
    #print("\n\033[1;mListagem de todos os Clubes\n")
    print("%4s %21s %35s %22s \t\t\t%10s" % (
    "Siglas", "Nomes dos Clubes", "Data Fundação", "Nome Presidente", "Numero Socios"))
    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        Sigla = colunas[0]
        Nome = colunas[1]
        Data_Fundacao = colunas[2]
        Nome_Presidente = colunas[3]
        Numero_Socios = colunas[4]
        # Numero_Modalidades = colunas[5]
        print("%4s \t\t%-40s %s \t\t%-30s %-20s" % (Sigla, Nome, Data_Fundacao,
                                                    Nome_Presidente, Numero_Socios))
    input("Prima enter para continuar!")

def PesquisarClubes():
    # pedir o nome a procurar
    # Ler o ficheiro para um vetor
    # comparar o nome de cada elemento do
    # vetor com o nome_procurar
    # nome_procurar = LerNome()
    nome_procurar = input("Nome a procurar?")
    f = open(nome_ficheiro_clubes, "rt")
    linhas = f.readlines()  # vetor
    f.close()
    enc = False
    for linha in linhas:
        nome = linha[0:49]
        data = linha[50:50 + 10]
        if nome.find(nome_procurar) >= 0:
            print(linha)
            enc = True
    if not enc:
        print("O nome %s não existe." % nome_procurar)
    print("Fim da Pesquisa!")
    input("Prima Enter pra Continuar!")
def ContarClubes():
    print("Contargens dos Clubes!")
    f = open("clubes.txt", "rt")
    linhas = f.readlines()  # vector
    np = 0
    f.close()
    # print("%4s %21s %35s %22s \t\t\t%10s" % (
    # "\033[1;32;mSiglas", "Nomes dos Clubes",
    # "Data Fundação", "Nome Presidente", "Numero Socios\033[m"))
    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        Sigla = colunas[0]
        Nome = colunas[1]
        Data_Fundacao = colunas[2]
        Nome_Presidente = colunas[3]
        Numero_Socios = colunas[4]
        # Numero_Modalidades = colunas[5]
        # print("%4s \t\t%-40s %s \t\t%-30s %-20s" %
        # (Sigla, Nome, Data_Fundacao, Nome_Presidente, Numero_Socios))
        np = np + 1
    print("Numero Total de Clubes %2s!" % (np))
    input("Prima enter para continuar")

def AgruparClubes():
    os.system("cls")
    print("Alterar Jogadores")
    print("Em desenvolvimento")
    input("Prima enter para continuar")

# ---------------------GestaoJogadores-----------------------------------------
def GestaoJogadores():
    print("\n")
    Titulo = "Gestão de Jogadores"
    Opcoes = ["Inserir Jogadores", "Alterar Jogadores",
              "Eliminar Jogadores", "Listar Todos Jogadores"]
    np = 4
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            InserirJogadores()
        elif op == 2:
            AlterarJogadores()
        elif op == 3:
            EliminarJogadores()
        elif op == 4:
            ListarTodosJogadores()
        elif op == 0:
            break;

def InserirJogadores():

    while True:
        Nome_jogador = input("Nome  Completo do Jogador?")
        if ValidaNome(Nome_jogador) == True:
            break
    while True:
        Nome_Em_Campo = input("Nome do Jogador em Campo?")
        if ValidarNomeCampo(Nome_Em_Campo) == True:
            break
    while True:
        PosisaoEmCampo = input("Posisão do %2s em Campo?" % (Nome_Em_Campo))
        if ValidarNomeCampo(PosisaoEmCampo) == True:
            break
    while True:
        Numero_em_Campo = input("Número do %2s em Campo?" % (Nome_Em_Campo))
        if ValidarNumero(Numero_em_Campo) == True:
            break
    while True:
        Data_Nascimento = LerData("Data Nascimento do jogador?", data_min, data_max)
        if Data_Nascimento != "":
            break
    while True:
        sexoJogador = input("Introduz o Sexo do %2s?(M/F)" % (Nome_jogador))
        if ValidarSexo(sexoJogador) == True:
            break
    f = open(nome_ficheiro_jogadores, "at")
    print("%s" % Nome_jogador, file=f, sep='\n', end='\t')
    print("%2s" % Nome_Em_Campo, file=f, end='\t', sep='')
    print("%2s" % PosisaoEmCampo, file=f, end='\t', sep='')
    print("%2s" % Numero_em_Campo, file=f, end='\t', sep='')
    print("%2s" % Data_Nascimento, file=f, end='\t', sep='')
    print("%2s" % sexoJogador, file=f, sep='')
    f.close()
    print("\n")
    print("Fim da Inserção!")
    input("Prima enter para continuar!")

def AlterarJogadores():
    f = open("jogadores.txt", "rt")
    cabecalho = f.readline()
    jogadores = f.readlines()
    f.close()
    nome = input("Nome?")
    for i in range(len(jogadores)):
        j = jogadores[i]
        if len(j) < 5:
            continue
        # Nome_jogador, Nome_Em_Campo, PosisaoEmCampo, Numero_em_Campo, Data_Nascimento, sexoJogador
        Nome_jogador, Nome_Em_Campo, PosisaoEmCampo, Numero_em_Campo, Data_Nascimento, sexoJogador = j.split("\t")
        if (Nome_jogador.find(nome)) >= 0:  # encontrado um jogador, escrever dados
            print(j)
            print("Jogadores com'%s'no Nome encontrado" % nome)
            print("Nome jogador............: %s" % Nome_jogador)
            print("NomeClube...............: %s" % Nome_Em_Campo)
            print("Data Fundacao...........: %s" % PosisaoEmCampo)
            print("Nome Presidente.........: %s" % Numero_em_Campo)
            print("Data Nascimento.........: %s" % Data_Nascimento)
            print("Sexo do Jogador.........: %s" % sexoJogador)
            o = input("Quer alterar ?(s/n)")
            if o == "s":  # novos dados
                while True:
                    Nome_jogador = input("Inserir novo Nome do Clube?")
                    if ValidaNome(Nome_jogador) == True:
                        break
                f = open("jogadores.txt", "wt")  # gravar novos dados no ficheiro
                print(cabecalho, file=f, end='')
                for k in range(len(jogadores)):
                    if k == i:
                        print(Nome_jogador, Nome_Em_Campo, PosisaoEmCampo, Numero_em_Campo, Data_Nascimento,
                              sexoJogador, sep='\t', file=f, end='')
                    else:
                        print(jogadores[k], file=f, end='')
                f.close()
            elif o != 's':
                break
    print("Fim da Alteração!")
    input("Prima enter para continuar!")
def EliminarJogadores():
    f = open("jogadores.txt", "rt")
    cabecalho = f.readline()
    jogadores = f.readlines()
    f.close()
    nome = input("Nome?")
    for i in range(len(jogadores)):
        j = jogadores[i]
        if len(j) < 5:
            continue
        # Jogador	Equipa	Posição	JJ	G
        Nome_jogador, Nome_Em_Campo, PosisaoEmCampo, Numero_em_Campo, Data_Nascimento, sexoJogador = j.split("\t")
        if (Nome_jogador.find(nome)) >= 0:  # encontrado um jogador, escrever dados
            #print(linha)
            print("Jogadores com'%s'no Nome encontrado" % nome)
            print("Nome jogador............: %s" % Nome_jogador)
            print("NomeClube...............: %s" % Nome_Em_Campo)
            print("Data Fundacao...........: %s" % PosisaoEmCampo)
            print("Nome Presidente.........: %s" % Numero_em_Campo)
            print("Data Nascimento.........: %s" % Data_Nascimento)
            print("Sexo do Jogador.........: %s" % sexoJogador)
            o = input("Confirma eliminar Clubes?(s/n)")
            if o == "s":  # Confirma?
                f = open("equipas.txt", "wt")  # gravar novos dados no ficheiro
                print(cabecalho, file=f, end='')
                for k in range(len(jogadores)):
                    if k != i:
                        print(jogadores[k], file=f, end='')
                f.close()
                f = open("log_jogadores.txt", "at")
                print("Operação:" "eliminar" + " Jogadores")
                print("\n")
                f.close()
            elif o != 's':
                break
    print("Fim da Eliminação de Jogadores!")
    input("Prima enter para continuar!")

def ListarTodosJogadores():
    print("\n")
    Titulo = "Gestão de Jogadores"
    Opcoes = ["Listar Jogadores", "Pesquisar Jogadores",
              "Contar  Jogadores", "Agrupar os Jogadores"]
    np = 4
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            ListarJogadores()
        elif op == 2:
            PesquisarJogadores()
        elif op == 3:
            ContarJogadores()
        elif op == 4:
            AgruparJogadores()
        elif op == 0:
            break
def ListarJogadores():
    print("ListarPaises")
    f = open("jogadores.txt", "rt")
    linhas = f.readlines()  # vector
    f.close()
    print("\n Listagem de todos os países\n")
    print("%-20s %21s %15s %15s %20s %11s" % (
    "Nome jogador", "Nome em Campo", "Posição", "Numero", "Data Nascimento", "Sexo"))
    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        Nome_jogador = colunas[0]
        Nome_Em_Campo = colunas[1]
        PosisaoEmCampo = colunas[2]
        Numero_em_Campo = colunas[3]
        Data_Nascimento = colunas[4]
        sexoJogador = colunas[5]
        # Numero_Modalidades  = colunas[6]
        print("%-20s %-10s %15s %16s %19s %10s"
              % (Nome_jogador, Nome_Em_Campo, PosisaoEmCampo,
                 Numero_em_Campo, Data_Nascimento, sexoJogador))
    print("Fim da Lista dos Jogadores")
    input("Prima enter para continuar!")

def PesquisarJogadores():
    # pedir o nome a procurar
    # Ler o ficheiro para um vetor
    # comparar o nome de cada elemento do
    # vetor com o nome_procurar
    # nome_procurar = LerNome()
    nome_procurar = input("Nome a procurar?")
    f = open(nome_ficheiro_jogadores, "rt")
    linhas = f.readlines()  # vetor
    f.close()
    enc = False
    for linha in linhas:
        nome = linha[0:49]
        data = linha[50:50 + 10]
        if nome.find(nome_procurar) >= 0:
            # print("Nome encontrado")
            print(linha)
            enc = True
    if not enc:
        print("O nome %s não existe." % nome_procurar)
    input("Prima enter para continuar!")

def ContarJogadores():
    print("ListarPaises")
    f = open("jogadores.txt", "rt")
    linhas = f.readlines()  # vector
    np = 0
    f.close()
    print("\n Contar  todos os Jogadores\n")
    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        Nome_jogador = colunas[0]
        Nome_Em_Campo = colunas[1]
        PosisaoEmCampo = colunas[2]
        Numero_em_Campo = colunas[3]
        Data_Nascimento = colunas[4]
        sexoJogador = colunas[5]
        # Numero_Modalidades  = colunas[6]

        np = np + 1
    print("Numero Total de Jogadores %2s!" % (np))
    input("Prima enter para continuar")

def AgruparJogadores():
    os.system("cls")
    print("Alterar Jogadores")
    print("Em desenvolvimento")
    input("Prima enter para continuar")

# ---------------------------GestaoEquipas------------------------------
def GestaoEquipas():
    print("\n")
    Titulo = "Gestão de Equipas"
    Opcoes = ["Inserir Equipas", "Alterar Equipas",
              "Eliminar Equipas", "Listar Todas as Equipas"]
    np = 4
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            InserirEquipas()
        elif op == 2:
            AlterarEquipas()
        elif op == 3:
            EliminarEquipas()
        elif op == 4:
            ListarTodasEquipas()
        elif op == 0:
            break

def InserirEquipas():
    while True:
        SiglaEquipa = input("Inserir Sigla da Equipa?")
        if ValidaSigla(SiglaEquipa) == True:
            break
    while True:
        NomeEquipa = input("Inserir Nome do Equipa?")
        if ValidaNome(NomeEquipa) == True:
            break
    while True:
        DataFundacaoEquipa = LerData("Data de Fundação do Equipa?", data_min, data_max)
        if DataFundacaoEquipa != "":
            break
    while True:
        NomePresidenteEquipa = input("Nome do Presidente do %2s?" % (NomeEquipa))
        if ValidaNome(NomePresidenteEquipa) == True:
            break
    f = open(nome_ficheiro_Equipas, "at")
    print("%s" % SiglaEquipa, file=f, end='\t', sep='\n')
    print("%2s" % NomeEquipa, file=f, end='\t', sep='')
    print("%2s" % DataFundacaoEquipa, file=f, end='\t', sep='')
    print("%2s" % NomePresidenteEquipa, file=f)
    f.close()
    print("Fim da Inserção!")
    input("Prima enter para continuar!")

def AlterarEquipas():
    f = open("equipas.txt", "rt")
    cabecalho = f.readline()
    jogadores = f.readlines()
    f.close()
    nome = input("Nome da Equipa?")
    for i in range(len(jogadores)):
        j = jogadores[i]
        if len(j) < 5:
            continue
        # Jogador	Equipa	Posição	JJ	G
        SiglaEquipa, NomeEquipa, DataFundacaoEquipa, NomePresidenteEquipa = j.split("\t")
        if (NomeEquipa.find(nome)) >= 0:  # encontrado um jogador, escrever dados
            print(j)
            ###
            print("Clube com'%s'no Nome encontrado" % nome)
            print("Sigla da Equipa...........: %s" % SiglaEquipa)
            print("Nome Equipa...............: %s" % NomeEquipa)
            print("Data Fundacao.............: %s" % DataFundacaoEquipa)
            print("Nome Presidente...........: %s" % NomePresidenteEquipa)
            ###
            o = input("Quer alterar ?(s/n)")
            if o == "s":  # novos dados
                while True:
                    NomeEquipa = input("Inserir novo Nome do Clube?")
                    if ValidaNome(NomeEquipa) == True:
                        break
                f = open("equipas.txt", "wt")  # gravar novos dados no ficheiro
                print(cabecalho, file=f, end='')
                for k in range(len(jogadores)):
                    if k == i:
                        print(SiglaEquipa, NomeEquipa, DataFundacaoEquipa, NomePresidenteEquipa,
                              sep='\t', file=f, end='')
                    else:
                        print(jogadores[k], file=f, end='')
                f.close()
            elif o != 's':
                break
    print("Fim da Alteração!")
    input("Prima enter para continuar!")
def EliminarEquipas():
    f = open("equipas.txt", "rt")
    cabecalho = f.readline()
    jogadores = f.readlines()
    f.close()
    nome = input("Nome Equipa?")
    for i in range(len(jogadores)):
        j = jogadores[i]
        if len(j) < 5:
            continue# Jogador	Equipa	Posição	JJ	G
        SiglaEquipa, NomeEquipa, DataFundacaoEquipa, NomePresidenteEquipa = j.split("\t")
        if (NomeEquipa.find(nome)) >= 0:  # encontrado um jogador, escrever dados # print(linha)
            print("Clube com'%s'no Nome encontrado" % nome)
            print("Sigla da Equipa...........: %s" % SiglaEquipa)
            print("Nome Equipa...............: %s" % NomeEquipa)
            print("Data Fundacao.............: %s" % DataFundacaoEquipa)
            print("Nome Presidente...........: %s" % NomePresidenteEquipa)
            o = input("Confirma eliminar Clubes?(s/n)")
            if o == "s":  # Confirma?
                f = open("equipas.txt", "wt")  # gravar novos dados no ficheiro
                print(cabecalho, file=f, end='')
                for k in range(len(jogadores)):
                    if k != i:
                        print(jogadores[k], file=f, end='')
                f.close()
                f = open("log_equipas.txt", "at")
                print("Operação:" "eliminar" + " Equipas")
                print("\n")
                f.close()
            elif o != 's':

                break
    print("Fim da Eliminação de Jogadores!")
    input("Prima enter para continuar!")

def ListarTodasEquipas():
    print("\n")
    Titulo = "Gestão de Jogadores"
    Opcoes = ["Listar Equipas", "Pesquisar Equipas",
              "Contar  Equipas", "Agrupar os Equipas"]
    np = 4
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            ListarEquipas()
        elif op == 2:
            PesquisarEquipas()
        elif op == 3:
            ContarEquipas()
        elif op == 4:
            AgruparEquipas()
        elif op == 0:
            break;

def ListarEquipas():
    f = open("equipas.txt", "rt")
    linhas = f.readlines()  # vector
    f.close()
    print("\n Listagem de todos as Equipas\n")
    print("%4s %16s %37s %22s" % ("Sigla", "Nome da Equipa",
                                  "Data Fundação", "Nome do Presidente"))
    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        SiglaEquipa = colunas[0]
        NomeEquipa = colunas[1]
        DataFundacaoEquipa = colunas[2]
        NomePresidenteEquipa = colunas[3]
        print("%4s \t%-40s %s \t\t%-30s"
              % (SiglaEquipa, NomeEquipa, DataFundacaoEquipa,
                 NomePresidenteEquipa))
    print("Fim da Lista das Equipas")
    input("Prima enter para continuar!")

def PesquisarEquipas():
    nome_procurar = input("Nome a procurar?")
    f = open(nome_ficheiro_Equipas, "rt")
    linhas = f.readlines()  # vetor
    f.close()
    enc = False
    for linha in linhas:
        nome = linha[0:49]
        data = linha[50:50 + 10]
        if nome.find(nome_procurar) >= 0:
            # print("Nome encontrado")
            print(linha)
            enc = True
    if not enc:
        print("O nome %s não existe." % nome_procurar)

    input("Prima enter para continuar!")

def ContarEquipas():
    print("Contargens dos EQuipas!")
    f = open("equipas.txt", "rt")
    linhas = f.readlines()  # vector
    np = 0
    f.close()
    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        Nome = colunas[0]
        Data_Fundacao = colunas[1]
        Nome_Presidente = colunas[2]
        Numero_Socios = colunas[3]
        # Numero_Modalidades = colunas[4]
        np = np + 1
    print("Numero Total de Clubes %2s!" % (np))
    input("Prima enter para continuar")

def AgruparEquipas():
    os.system("cls")
    print("Alterar Jogadores")
    print("Em desenvolvimento")
    input("Prima enter para continuar")

# --------------------------GestaoEstadios------------------------------
def GestaoEstadios():
    print("\n")
    Titulo = "Gestão de Estadios"
    Opcoes = ["Inserir Estadios", "Alterar Estadios",
              "Eliminar Estadios", "Listar Todos os Estadios"]
    np = 4
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            InserirEstadios()
        elif op == 2:
            AlterarEstadios()
        elif op == 3:
            EliminarEstadios()
        elif op == 4:
            ListarTodosEstadios()
        elif op == 0:
            break

def InserirEstadios():
    while True:
        NomeEstadio = input("Inserir Nome do Estádio?")
        if ValidaNome(NomeEstadio) == True:
            break
    while True:
        NomeClubeEstadio = input("Nome do Clube que %2s pertence?" % (NomeEstadio))
        if ValidaNome(NomeClubeEstadio) == True:
            break
    while True:
        Data_Fundacao = LerData("Data de Inauguração do Estádio?", data_min, data_max)
        if Data_Fundacao != "":
            break
    while True:
        Capacidade = input("Inserir Lotação maxima do Estádio?")
        if ValidaSocios(Capacidade) == True:
            break
    while True:
        Modalidades = input("Modalidade Praticada em %2s?" % (NomeEstadio))
        if ValidarNomeCampo(Modalidades) == True:
            break
    f = open(nome_ficheiro_Estadios, "at")
    print("%s" % NomeEstadio, file=f, end='\t', sep='\n')
    print("%2s" % NomeClubeEstadio, file=f, end='\t', sep='')
    print("%2s" % Data_Fundacao, file=f, end='\t', sep='')
    print("%2s" % Capacidade, file=f, end='\t', sep='')
    print("%2s" % Modalidades, file=f)
    f.close()
    print("Fim da Inserção!")
    input("Prima enter para continuar!")

def AlterarEstadios():
    f = open("estadios.txt", "rt")
    cabecalho = f.readline()
    jogadores = f.readlines()
    f.close()
    nome = input("Nome do Estádio?")
    for i in range(len(jogadores)):
        j = jogadores[i]
        if len(j) < 5:
            continue
        # Jogador	Equipa	Posição	JJ	G
        NomeEstadio, NomeClubeEstadio, Data_Fundacao, Capacidade, Modalidades = j.split("\t")
        if (NomeEstadio.find(nome)) >= 0:  # encontrado um jogador, escrever dados
            # print(j)
            print("Clube com'%s'no Nome encontrado" % nome)
            print("Nome do Estadio.........: %s" % NomeEstadio)
            print("Nome Clube Estadio......: %s" % NomeClubeEstadio)
            print("Data Fundação...........: %s" % Data_Fundacao)
            print("Nome Presidente.........: %s" % Capacidade)
            print("Modalidades.............: %s" % Modalidades)
            # print("Numero Modalidades......: %s" % Numero_Modalidades)
            o = input("Quer alterar ?(s/n)")
            if o == "s":  # novos dados
                while True:
                    NomeEstadio = input("Inserir novo Nome do Estádio?")
                    if ValidaNome(NomeEstadio) == True:
                        break
                f = open("estadios.txt", "wt")  # gravar novos dados no ficheiro
                print(cabecalho, file=f, end='')
                for k in range(len(jogadores)):
                    if k == i:
                        print(NomeEstadio, NomeClubeEstadio, Data_Fundacao,
                              Capacidade, Modalidades, sep='\t',
                              file=f, end='')
                    else:
                        print(jogadores[k], file=f, end='')
                f.close()
            elif o != 's':
                break
    print("Fim da Alteração!")
    input("Prima enter para continuar!")

def EliminarEstadios():
    f = open("estadios.txt", "rt")
    cabecalho = f.readline()
    jogadores = f.readlines()
    f.close()
    nome = input("Nome do Estádio?")
    for i in range(len(jogadores)):
        j = jogadores[i]
        if len(j) < 5: continue
        NomeEstadio, NomeClubeEstadio, Data_Fundacao, Capacidade, Modalidades = j.split("\t")
        if (NomeEstadio.find(nome)) >= 0:  # encontrado um jogador, escrever dados # print(j)
            print("Clube com'%s'no Nome encontrado" % nome)
            print("Nome do Estadio.........: %s" % NomeEstadio)
            print("Nome Clube Estadio......: %s" % NomeClubeEstadio)
            print("Data Fundação...........: %s" % Data_Fundacao)
            print("Nome Presidente.........: %s" % Capacidade)
            print("Modalidades.............: %s" % Modalidades)
            o = input("Confirma eliminação do Estádio %2s?(s/n)" % (NomeEstadio))
            if o == "s":  # Confirma?
                f = open("estadios.txt", "wt")  # gravar novos dados no ficheiro
                print(cabecalho, file=f, end='')
                for k in range(len(jogadores)):
                    if k != i:
                        print(jogadores[k], file=f, end='')
                f.close()
                f = open("log_estadios.txt", "at")
                print("Operação:" "eliminar" + "Estádio")
                print("\n")
                f.close()
            elif o != 's':
                break
    print("Fim da Eliminação!")
    input("Prima enter para continuar!")

def ListarTodosEstadios():
    print("\n")
    Titulo = "Gestão de Jogadores"
    Opcoes = ["Listar Estadios", "Pesquisar Estadios",
              "Contar  Estadios", "Agrupar os Estadios"]
    np = 4
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            ListarEstadios()
        elif op == 2:
            PesquisarEstadios()
        elif op == 3:
            ContarEstadios()
        elif op == 4:
            AgruparEstadios()
        elif op == 0:
            break

def ListarEstadios():
    print("Listas de Todos os Estádios!")
    f = open("estadios.txt", "rt")
    linhas = f.readlines()  # vector
    f.close()
    # print("\n\033[1;mListagem de todos os Clubes\033[m\n")
    print("%-30s \t\t\t%-40s %10s \t%-15s \t%5s" % (
        "Nome do Estadio", "Nome Clube Estadio", "Data Fundacao",
        "   Capacidade", "Modalidades"))
    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        NomeEstadio = colunas[0]
        NomeClubeEstadio = colunas[1]
        Data_Fundacao = colunas[2]
        Capacidade = colunas[3]
        Modalidades = colunas[4]
        # Numero_Modalidades = colunas[5]
        print("%-30s \t%-40s  %10s      \t%-15s %-s" % (
        NomeEstadio, NomeClubeEstadio, Data_Fundacao, Capacidade, Modalidades))
    input("Prima enter para continuar!")

def PesquisarEstadios():
    nome_procurar = input("Estádio a procurar?")
    f = open(nome_ficheiro_Estadios, "rt")
    linhas = f.readlines()  # vetor
    f.close()
    enc = False
    for linha in linhas:
        nome = linha[0:49]
        data = linha[50:50 + 10]
        if nome.find(nome_procurar) >= 0:
            # print("Nome encontrado")
            print(linha)
            enc = True
    if not enc:
        print("O nome %s não existe." % nome_procurar)
    input("Prima enter para continuar!")

def ContarEstadios():
    print("Contagem de Todos os Estádios!")
    f = open("estadios.txt", "rt")
    linhas = f.readlines()  # vector
    f.close()
    np = 0
    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        NomeEstadio = colunas[0]
        NomeClubeEstadio = colunas[1]
        Data_Fundacao = colunas[2]
        Capacidade = colunas[3]
        Modalidades = colunas[4]
        # Numero_Modalidades = colunas[5]
        # print("%-30s \t%-40s  %10s      \t%-15s %-s" % (
        # NomeEstadio, NomeClubeEstadio, Data_Fundacao, Capacidade, Modalidades))
        np = np + 1
    print("Exintem %2s Estádios Incritos!" % (np))
    input("Prima enter para continuar!")

def AgruparEstadios():
    os.system("cls")
    print("Alterar Jogadores")
    print("Em desenvolvimento")
    input("Prima enter para continuar")

# --------------------------GestaoJogos---------------------------------
# obs:
def GestaoJogos():
    print("\n")
    Titulo = "Gestão de Jogos"
    Opcoes = ["Inserir Jogos", "Alterar Jogos",
              "Eliminar Jogos", "Listar Todos os Jogos"]
    np = 4
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            InserirJogos()
        elif op == 2:
            AlterarJogos()
        elif op == 3:
            EliminarJogos()
        elif op == 4:
            ListarTodosJogos()
        elif op == 0:
            break
def InserirJogos():
    while True:
        NomeEquipaJogo = input("Inserir Nome da Equipa")
        if ValidaNome(NomeEquipaJogo) == True:
            break
    while True:
        JogosVencidos = input("Inserir Numero Jogos vencido?")
        if ValidaSocios(JogosVencidos) == True:
            break
    while True:
        JogosPerdidos = input("Inserir Numero Jogos perdidos?")
        if ValidaSocios(JogosPerdidos) == True:
            break
    while True:
        Data_InicioJogo = LerData("Data do Primeiro Jogo?", data_min, data_max)
        if Data_InicioJogo != "":
            break
    while True:
        Data_FimJogo = LerData("Data do Ultimo Jogo?", data_min, data_max)
        if Data_FimJogo != "":
            break

    f = open(nome_ficheiro_Jogos, "at")
    print("%s" % NomeEquipaJogo, file=f, end='\t', sep='\n')
    print("%2s" % JogosVencidos, file=f, end='\t', sep='')
    print("%2s" % JogosPerdidos, file=f, end='\t', sep='')
    print("%2s" % Data_InicioJogo, file=f, end='\t', sep='')
    print("%2s" % Data_FimJogo, file=f)
    f.close()
    print("Fim da Inserção!")
    input("Prima enter para continuar!")

def AlterarJogos():
    f = open("jogos.txt", "rt")
    cabecalho = f.readline()
    jogadores = f.readlines()
    f.close()
    nome = input("Nome Equipa?")
    for i in range(len(jogadores)):
        j = jogadores[i]
        if len(j) < 5:
            continue# Jogador	Equipa	Posição	JJ	G
        NomeEquipaJogo, JogosVencidos, JogosPerdidos,\
        Data_InicioJogo, Data_FimJogo = j.split("\t")
        if (NomeEquipaJogo.find(nome)) >= 0:  # encontrado um jogador, escrever dados
            # print(j)
            print("Clube com'%s'no Nome encontrado" % nome)
            print("Nomeda Equipa....................: %s" % NomeEquipaJogo)
            print("Jogos vencidos...................: %s" % JogosVencidos)
            print("Jogos perdidos...................: %s" % JogosPerdidos)
            print("Data de inicio dos jogos.........: %s" % Data_InicioJogo)
            print("Data do fim dos jogos............: %s" % Data_FimJogo)
            # print("Numero Modalidades......: %s" % Numero_Modalidades)
            o = input("Quer alterar ?(s/n)")
            if o == "s":  # novos dados
                while True:
                    NomeEquipaJogo = input("Inserir novo Nome do Clube?")
                    if ValidaNome(NomeEquipaJogo) == True:
                        break
                f = open("jogos.txt", "wt")  # gravar novos dados no ficheiro
                print(cabecalho, file=f, end='')
                for k in range(len(jogadores)):
                    if k == i:
                        print(NomeEquipaJogo, JogosVencidos, JogosPerdidos,
                              Data_InicioJogo, Data_FimJogo,
                              sep='\t', file=f, end='')
                    else:
                        print(jogadores[k], file=f, end='')
                f.close()
            elif o != 's':
                break
    print("Fim da Alteração!")
    input("Prima enter para continuar!")
def EliminarJogos():
    f = open("clubes.txt", "rt")
    cabecalho = f.readline()
    jogadores = f.readlines()
    f.close()
    nome = input("Nome?")
    for i in range(len(jogadores)):
        j = jogadores[i]
        if len(j) < 5:
            continue# Jogador	Equipa	Posição	JJ	G
        NomeEquipaJogo, JogosVencidos, JogosPerdidos, Data_InicioJogo, Data_FimJogo = j.split("\t")
        if (NomeEquipaJogo.find(nome)) >= 0:  # encontrado um jogador, escrever dados# print(j)
            print("Clube com'%s'no Nome encontrado" % nome)
            print("Nomeda Equipa....................: %s" % NomeEquipaJogo)
            print("Jogos vencidos...................: %s" % JogosVencidos)
            print("Jogos perdidos...................: %s" % JogosPerdidos)
            print("Data de inicio dos jogos.........: %s" % Data_InicioJogo)
            print("Data do fim dos jogos............: %s" % Data_FimJogo)
            o = input("Confirma eliminar?(s/n)")
            if o == "s":  # Confirma?
                f = open("jogos.txt", "wt")  # gravar novos dados no ficheiro
                print(cabecalho, file=f, end='')
                for k in range(len(jogadores)):
                    if k != i:
                        print(jogadores[k], file=f, end='')
                f.close()
                f = open("log_jogos.txt", "at") # print("Operação:" "eliminar" + " Clubes")
                print("\n")
                f.close()
            elif o != 's':
                break
    print("Fim da Eliminação!")
    input("Prima enter para continuar!")

def ListarTodosJogos():
    print("\n")
    Titulo = "Gestão de Jogadores"
    Opcoes = ["Listar Jogos", "Pesquisar Jogos",
              "Contar  Jogos", "Agrupar os Jogos"]
    np = 4
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            ListarJogos()
        elif op == 2:
            PesquisarJogos()
        elif op == 3:
            ContarJogos()
        elif op == 4:
            AgruparJogos()
        elif op == 0:
            break
def ListarJogos():
    print("Listas de Todos os Jogos e os seus respertivos Clubes!")
    f = open("jogos.txt", "rt")
    linhas = f.readlines()  # vector
    f.close()
    # print("\n\033[1;mListagem de todos os Clubes\033[m\n")
    print("%-30s %s  %10s     %-15s %-s" %
          ("Nome Equipa", "Vitórias", "Derotas", "Data Inicio", "Data Fim"))
    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        NomeEquipaJogo = colunas[0]
        JogosVencidos = colunas[1]
        JogosPerdidos = colunas[2]
        Data_InicioJogo = colunas[3]
        Data_FimJogo = colunas[4]
        # Numero_Modalidades = colunas[5]
        print("%-30s   %s \t%9s      \t%-15s %-s" %
              (NomeEquipaJogo, JogosVencidos, JogosPerdidos,
               Data_InicioJogo, Data_FimJogo))
    input("Prima enter para continuar!")

def PesquisarJogos():
    nome_procurar = input("Nome a procurar?")
    f = open(nome_ficheiro_Jogos, "rt")
    linhas = f.readlines()  # vetor
    f.close()
    enc = False
    for linha in linhas:
        nome = linha[0:49]
        data = linha[50:50 + 10]
        if nome.find(nome_procurar) >= 0:
            print(linha)
            enc = True
    if not enc:
        print("O nome %2s não existe." % nome_procurar)
    print("Fim da Pesquisa!")
    input("Prima enter para continuar!")

def ContarJogos():
    print("Listas de Todos os Jogos e os seus respertivos Clubes!")
    f = open("jogos.txt", "rt")
    linhas = f.readlines()  # vector
    f.close()
    np = 0
    # print("\n\033[1;mListagem de todos os Clubes\033[m\n")

    for i in range(1, len(linhas)):
        r = linhas[i]
        r = r.rstrip('\n')
        colunas = r.split('\t')  # vetor
        NomeEquipaJogo = colunas[0]
        JogosVencidos = colunas[1]
        JogosPerdidos = colunas[2]
        Data_InicioJogo = colunas[3]
        Data_FimJogo = colunas[4]
        # Numero_Modalidades = colunas[5]
        np = np + 1
        # print("%-30s   %s \t%9s      \t%-15s %-s" %
        # (NomeEquipaJogo, JogosVencidos, JogosPerdidos, Data_InicioJogo, Data_FimJogo))
    print("Existe %2s equipas com Jogos agendados" % (np))
    input("Prima enter para continuar!")

def AgruparJogos():
    os.system("cls")
    print("Alterar Jogadores")
    print("Em desenvolvimento")
    input("Prima enter para continuar")
def UbuntoSolution():
    print("\n")
    print("\033[1;34;mInformações Sobre Ubunto Solution\033[m")
    print("\033[1;34;m\033[m")
    print("\033[1;33;mUbunto Solution\033[m"
          "->é uma empresa de desenvovimento de Algoritmos simples e lógicos.\n"
          "E tambem e Elaboração de programas em Python")
    print("Com base num conjunto de dados sobre: "
          "\nContinentes, Países, Códigos Postais, "
          "Cidades entre outros elaborar algoritmos e respetivo programa."
          "\nPython que permita gerir dados de "
          "Clubes, Jogadores, Equipas, Estádios e Jogos \n(isto é: inserir, alterar, eliminar, listar, pesquisar,"
          "ordenar, contar, etc.)"
          "\nNeste trabalho será inventar um algoritmo que permita determinar "
          "caminhos entre dois países."
          "\nExemplos: Portugal -> Alemanha: Portugal -> Espanha -> França -> Alemanha")
    input("Prima enter para continuar")
def MenuPrincipal():

    print("\n")
    Titulo = "Menu Principal"
    Opcoes = ["Tudo sobre Geografia",
              "Tudo sobre Futebol","Ubunto Solutionr"]
    np = 3
    while True:
        op = Menu(Titulo, Opcoes, np)
        if   op == 1:
            Geografia()
        elif op == 2:
            Futebol()
        elif op == 3:
            UbuntoSolution()
        elif op == 0:
            break
MenuPrincipal()
