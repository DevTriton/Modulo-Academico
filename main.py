import sqlite3
import json
import os
import time
from pathlib import Path

comparacao = 0
escolha = 0
OpGeral = 0
op = 0

     

class ModuloAcademico:
    def __init__(self):
        self.listaAlunos = []
        self.listaProfessor = []
        self.listaDisciplinas = []

    def Insertescolha():
        global escolha
        print("|############################################################|")
        print("|                        OOP PYTHON                          |")
        print("|############################################################|")
        print("Em que modo deseja operar?")
        print("1) SQLite")
        print("2) JSON")
        print("3) SAIR")
        escolha=int(input("digite a opção desejada: "))
        while escolha<1 or escolha>3:
            escolha=int(input("opção invalida tente novamente: "))
        os.system("CLS")    

    def menu_geral():
        print("|############################################################|")
        print("|                        OOP PYTHON                          |")
        print("|############################################################|")
        print("Qual lista deseja manipular?")
        print("1) Aluno")
        print("2) Professor")
        print("3) Disciplinas")
        print("4) sair")
        global OpGeral
        OpGeral=int(input("digite a opção desejada "))
        while OpGeral<1 or OpGeral>4:
            OpGeral=int(input("opção invalida tente novamente: "))    
        os.system("CLS")

    def menuE():
        print("|############################################################|")
        print("|                        OOP PYTHON                          |")
        print("|############################################################|")
        print("Oque deseja fazer?")
        print("1) Cadastrar")
        print("2) Imprimir")
        print("3) atualizar")
        print("4) excluir")
        print("5) Sair")
        global op
        op=int(input("digite a opção que deseja fazer: "))
        while op<1 or op>5:
            op=int(input("opção invalida tente novamente: "))
        os.system("CLS")

    def CriarBD():
        conexao = sqlite3.connect('sistema.db')
        cursor = conexao.cursor()

        script = 'CREATE TABLE PROFESSOR(ID INT,NOME TEXT,IDADE INT, PESO  INT, ALTURA INT, MATRICULA TEXT, PRIMARY KEY(ID));'
        cursor.execute(script)
        script = 'CREATE TABLE ALUNO(ID INT,NOME TEXT,IDADE INT, PESO  INT, ALTURA INT, RGM TEXT, PRIMARY KEY(ID));'
        cursor.execute(script)
        script = 'CREATE TABLE DISCIPLINA(ID INT, CODIGO TEXT, NOME TEXT, CARGAHORARIA INT, TURMA TEXT, NOTAMINIMA INT, PRIMARY KEY(ID));'
        cursor.execute(script)

        conexao.commit()
        conexao.close()

    def Salvar(self, V):
        global OpGeral
        if OpGeral==1:
            self.listaAlunos.append(V)
            lista = []
            arquivo = open("alunos.json", 'w')
            for cont in self.listaAlunos :
                lista.append(cont.serializar())
            json.dump(lista, arquivo) 

        if OpGeral==2:
            self.listaProfessor.append(V)
            lista = []
            arquivo = open("professores.json", 'w')
            for cont in self.listaProfessor :
                lista.append(cont.serializar())
            json.dump(lista, arquivo)

        if OpGeral==3:  
            self.listaDisciplinas.append(V)
            lista = []
            arquivo = open("Disciplinas.json", 'w')
            for cont in self.listaDisciplinas :
                lista.append(cont.serializar())
            json.dump(lista, arquivo)    

    def Recuperar(self):
        global OpGeral
        if OpGeral==1:
            self.listaAlunos.clear()
            arquivo = open("alunos.json", 'r')
            lista_de_jsons_text = json.load(arquivo)
            for text in lista_de_jsons_text:
                V = Aluno()
                V.deserializar(text)
                self.listaAlunos.append(V) 

        if OpGeral==2:
            self.listaProfessor.clear()
            arquivo = open("professores.json", 'r')
            lista_de_jsons_text = json.load(arquivo)
            for text in lista_de_jsons_text:
                V = Professor()
                V.deserializar(text)
                self.listaProfessor.append(V)

        if OpGeral==3:
           
            self.listaDisciplinas.clear()
            arquivo = open("Disciplinas.json", 'r')
            lista_de_jsons_text = json.load(arquivo)
            for text in lista_de_jsons_text:
                V = Disciplina()
                V.deserializar(text)
                self.listaDisciplinas.append(V)

    def imprimir(self):
        global OpGeral
        if OpGeral==1:

            print("----------------------------------------")
            self.Recuperar()
            for cont in self.listaAlunos:
                print(cont.nome, "/", cont.idade, "/", cont.altura, "/", cont.peso, "/", cont.id, "/", cont.rgm)    
            print("----------------------------------------")

        if OpGeral==2:
        
            print("----------------------------------------")
            self.Recuperar()
            for cont in self.listaProfessor:
                print(cont.nome, "/", cont.idade, "/", cont.altura, "/", cont.peso, "/", cont.id, "/", cont.matricula)    
            print("----------------------------------------")     

        if OpGeral==3:


            print("----------------------------------------")
            self.Recuperar()
            for cont in self.listaDisciplinas:
                print(cont.nome, "/", cont.cargahoraria, "/", cont.turma, "/", cont.notaminima, "/", cont.codigo, "/", cont.id)      
            print("----------------------------------------")

    def atualizar(self, resp):  
        global OpGeral
        if OpGeral==1:         
            for cont in self.listaAlunos:
                if resp == cont.id:
                    cont.nome=input("digite o nome do aluno: ")
                    cont.idade=int(input("digite a idade do aluno: "))
                    cont.altura=float(input("digite a altura do aluno:"))
                    cont.peso=float(input("digite o peso do aluno: "))
                    cont.id=int(input("digite o id do aluno"))
                    cont.rgm=input("digite o rgm do aluno")
                    a1=Aluno()
                    self.Salvar(a1)

        if OpGeral==2:      
            for cont in self.listaProfessor:
                if resp == cont.id:
                    cont.nome=input("digite o nome do aluno: ")
                    cont.idade=int(input("digite a idade do aluno: "))
                    cont.altura=float(input("digite a altura do aluno:"))
                    cont.peso=float(input("digite o peso do aluno: "))
                    cont.id=int(input("digite o id do aluno"))
                    cont.matricula=input("digite o rgm do aluno")
                    a1=Professor()
                    self.Salvar(a1)

        if OpGeral==3:                               
            for cont in self.listaDisciplinas:
                if resp == cont.id:
                    cont.nome=input("digite o nome da disciplina: ")
                    cont.cargahoraria=int(input("digite carga horaria da disciplina: "))
                    cont.turma=input("digite a turma da disciplina:")
                    cont.notaminima=float(input("digite a nota minima da disciplina: "))
                    cont.id=int(input("digite o id da disciplina"))
                    cont.codigo=input("digite o codigo da disciplina")
                    a1=Disciplina()
                    self.Salvar(a1)

    def remover(self, resp): 
        global OpGeral
        if OpGeral==1:
            for cont in self.listaAlunos:
                if resp == cont.id:
                    index = cont.id - 1
                    self.listaAlunos.pop(index)
                    a = Aluno()
                    self.Salvar(a)

        if OpGeral==2:
            for cont in self.listaProfessor:
                if resp == cont.id:
                    index = cont.id - 1
                    self.listaProfessor.pop(index)
                    a = Professor()
                    self.Salvar(a)

        if OpGeral==3:                                  
            for cont in self.listaDisciplinas:
                if resp == cont.id:
                    index = cont.id - 1
                    self.listaDisciplinas.pop(index)
                    a = Disciplina()
                    self.Salvar(a)
                                   

class CRUD:
    def __init__(self, tipoDB):
        self.tipoDB = tipoDB
            
    def __executeScript(self, script):
        if self.tipoDB == 1:
            conexao = sqlite3.connect('sistema.db')
            cursor = conexao.cursor()
            print(script)
            cursor.execute(script)
            conexao.commit()
            conexao.close()    

    def __executeSELECT(self, query):
        if self.tipoDB == 1:
            conexao = sqlite3.connect('sistema.db')
            cursor = conexao.cursor()
            retorno = cursor.execute(query)
            listaRetorno = []
            for linha in retorno:
                listaRetorno.append(linha)
            conexao.close()
            return listaRetorno
        
    def _insert(self):
        pass

    def _select(self):
        pass

    def _update(self):
        pass

    def _delete(self):
        pass

    def insert(self):
        script = self._insert()
        self.__executeScript(script)

    def select(self):
        query = self._select()
        retorno = self.__executeSELECT(query)
        return retorno

    def update(self):
        script = self._update()
        self.__executeScript(script)

    def delete(self):
        script = self._delete()
        self.__executeScript(script)   
    

class Aluno(ModuloAcademico):
    def __init__(self, nome="", idade=0, altura=0.0, peso=0.0, rgm="", id=0):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.rgm = rgm
        self.id = id
        self.listaAlunos = []

        try:
            self.Recuperar()
        except:
            pass      
        finally:
            pass

    def serializar(self):
        dic = {}
        dic["nome"] = self.nome
        dic["idade"] = self.idade
        dic["altura"] = self.altura
        dic["peso"] = self.peso
        dic["rgm"] = self.rgm
        dic["id"] = self.id
        texto_json = json.dumps(dic, indent = 3)
        return texto_json

    def deserializar(self, texto_json):
        dic = json.loads(texto_json)
        self.nome = dic["nome"]
        self.idade = dic["idade"]
        self.altura = dic["altura"]
        self.peso = dic["peso"]
        self.rgm = dic["rgm"]
        self.id = dic["id"]                                                                                 

class CRUD_Aluno(CRUD):
    def __init__(self, Aluno, typoDB):
        self.aluno = Aluno
        super().__init__(typoDB)

    def _insert(self):
        script  = "INSERT INTO ALUNO (ID, NOME, IDADE, PESO, ALTURA, RGM ) VALUES ("
        script +=""+ str(self.aluno.id) + ",'" + self.aluno.nome + "', "+ str(self.aluno.idade) + "," + str(self.aluno.peso) + "," + str(self.aluno.altura) + ", '" + self.aluno.rgm + "');"
        return script

    def _select(self):
        return "SELECT * FROM ALUNO;"

    def _delete(self):
        return "DELETE FROM ALUNO WHERE RGM = '" + comparacao + "';"

    def _update(self):
        return "UPDATE ALUNO SET ID = "+ str(self.aluno.id) + ", NOME = '" + self.aluno.nome + "', IDADE = "+ str(self.aluno.idade) + ", PESO = " + str(self.aluno.peso) + " , ALTURA = " + str(self.aluno.altura) + ", RGM = '" + self.aluno.rgm + "' WHERE RGM = '" + comparacao + "';"

class Professor(ModuloAcademico):
    def __init__(self, nome = "", idade = 0, altura = 0.0, peso = 0, matricula = 0, id = 0):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.matricula = matricula
        self.id = id
        self.listaProfessor = []

        try:
            self.Recuperar()
        except:
            pass      
        finally:
            pass

    def serializar(self):
        dic = {}
        dic["nome"] = self.nome
        dic["idade"] = self.idade
        dic["altura"] = self.altura
        dic["peso"] = self.peso
        dic["matricula"] = self.matricula
        dic["id"] = self.id
        texto_json = json.dumps(dic, indent = 3)
        return texto_json

    def deserializar(self, texto_json):
        dic = json.loads(texto_json)
        self.nome = dic["nome"]
        self.idade = dic["idade"]
        self.altura = dic["altura"]
        self.peso = dic["peso"]
        self.matricula = dic["matricula"]
        self.id = dic["id"]                                       

class CRUD_Professor(CRUD):
    def __init__(self, Professor, typoDB):
        self.professor = Professor
        super().__init__(typoDB)

    def _insert(self):
        script  = "INSERT INTO PROFESSOR (ID, NOME ,IDADE , PESO  , ALTURA , MATRICULA ) VALUES ("
        script +=""+ str(self.professor.id) + ",'" + self.professor.nome + "', "+ str(self.professor.idade) + "," + str(self.professor.peso) + "," + str(self.professor.altura) + ", '" + self.professor.matricula + "');"
        return script

    def _select(self):
        return "SELECT * FROM PROFESSOR;"

    def _delete(self):
        return "DELETE FROM PROFESSOR WHERE MATRICULA = '" + comparacao + "';"

    def _update(self):
        return "UPDATE PROFESSOR SET ID = "+ str(self.professor.id) + ", NOME = '" + self.professor.nome + "', IDADE = "+ str(self.professor.idade) + ", PESO = " + str(self.professor.peso) + " , ALTURA = " + str(self.professor.altura) + ", MATRICULA = '" + self.professor.matricula + "' WHERE MATRICULA = '" + comparacao + "';"

class Disciplina(ModuloAcademico):
    def __init__(self, nome = "", cargahoraria = 0, turma = "", notaminima = 0.0, codigo = 0, id = 0):
        self.nome = nome
        self.cargahoraria = cargahoraria
        self.turma = turma
        self.notaminima = notaminima
        self.codigo = codigo
        self.id = id
        self.listaDisciplinas = []

        try:
            self.Recuperar()
        except:
            pass      
        finally:
            pass

    def serializar(self):
        dic = {}
        dic["nome"] = self.nome
        dic["cargahoraria"] = self.cargahoraria
        dic["turma"] = self.turma
        dic["notaminima"] = self.notaminima
        dic["id"] = self.id
        dic["codigo"] = self.codigo
        texto_json = json.dumps(dic, indent = 3)
        return texto_json

    def deserializar(self, texto_json):
        dic = json.loads(texto_json)
        self.nome = dic["nome"]
        self.cargahoraria = dic["cargahoraria"]
        self.turma = dic["turma"]
        self.notaminima = dic["notaminima"]
        self.id = dic["id"]
        self.codigo = dic["codigo"]                                 

class CRUD_Disciplina(CRUD):
    def __init__(self, Disciplina, typoDB):
        self.disciplina = Disciplina
        super().__init__(typoDB)

    def _insert(self):
        script  = "INSERT INTO DISCIPLINA (ID, NOME,CARGAHORARIA , TURMA , NOTAMINIMA , CODIGO ) VALUES ("
        script +=""+ str(self.disciplina.id) + ",'" + self.disciplina.nome + "', "+ str(self.disciplina.cargahoraria) + ",'" + self.disciplina.turma + "'," + str(self.disciplina.notaminima) + ", '" + self.disciplina.codigo + "');"
        return script

    def _select(self):
        return "SELECT * FROM DISCIPLINA;"

    def _delete(self):
        return "DELETE FROM DISCIPLINA WHERE CODIGO = '" +  comparacao + "';"

    def _update(self):
        return "UPDATE DISCIPLINA SET ID = "+ str(self.disciplina.id) + ", NOME = '" + self.disciplina.nome + "', CARGAHORARIA = "+ str(self.disciplina.cargahoraria) + ", TURMA = '" + self.disciplina.turma + "' , NOTAMINIMA = " + str(self.disciplina.notaminima) + ", CODIGO = '" + self.disciplina.codigo + "' WHERE CODIGO = '" + comparacao + "';"    

while escolha!=3:
    ModuloAcademico.Insertescolha() 
    if escolha==1:
        caminho_arquivo = Path("sistema.db")

        if caminho_arquivo.exists():
            print("O arquivo existe!")
        else:
            ModuloAcademico.CriarBD()
            print("BD criado")

        ModuloAcademico.menu_geral()   
        while OpGeral!=4:
            if OpGeral==1:
                ModuloAcademico.menuE()
                while op!=5:
                    if op==1:
                        a1 = Aluno(id=int(input("digite o id do aluno: ")), nome=input("digite o nome do aluno: "), idade=int(input("digite a idade do aluno: ")), altura=float(input("digite a altura do aluno: ")), peso=float(input("digite o peso do aluno: ")), rgm=input("digite o rgm do aluno: "))
                        CRUD_Aluno(a1, escolha).insert()
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                    elif op==2:
                        a1= Aluno(id="ficticio")
                        resultado = CRUD_Aluno(a1, escolha).select()
                        lista = []
                        for linha in resultado:
                            lista.append(linha[:])
                        for cont in range (len(lista)):
                            print(lista[cont])
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                    elif op==3:
                        comparacao=input("digite o Rgm do aluno que deseja alterar: ")
                        a1 = Aluno(id=int(input("digite o id do aluno: ")), nome=input("digite o nome do aluno: "), idade=int(input("digite a idade do aluno: ")), altura=float(input("digite a altura do aluno: ")), peso=float(input("digite o peso do aluno: ")), rgm=input("digite o rgm do aluno: "))
                        CRUD_Aluno(a1, escolha).update()
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                    elif op==4:
                        a1 = Aluno(nome="ficticio")
                        comparacao=input("digite o Rgm do aluno que deseja alterar: ")
                        CRUD_Aluno(a1, escolha).delete()
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                if op==5:
                    break 

            if OpGeral==2:
                op = 0
                ModuloAcademico.menuE()   
                while op!=5: 
                    if op==1:
                        a1 = Professor(id=int(input("digite o id do professor: ")), nome=input("digite o nome do professor: "), idade=int(input("digite a idade do professor: ")), altura=float(input("digite a altura do professor: ")), peso=float(input("digite o peso do professor: ")), matricula=input("digite a matricula do professor: "))
                        CRUD_Professor(a1, escolha).insert()
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                    elif op==2:
                        a1= Professor(id="ficticio")
                        resultado = CRUD_Professor(a1, escolha).select()
                        lista = []
                        for linha in resultado:
                            lista.append(linha[:])
                        for cont in range (len(lista)):
                            print(lista[cont])
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                    elif op==3:
                        comparacao=input("digite a matricula do professor que deseja alterar: ")
                        a1 = Professor(id=int(input("digite o id do professor: ")), nome=input("digite o nome do professor: "), idade=int(input("digite a idade do professor: ")), altura=float(input("digite a altura do professor: ")), peso=float(input("digite o peso do professor: ")), matricula=input("digite a matricula do professor: "))
                        CRUD_Professor(a1, escolha).update()
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                    elif op==4:
                        a1 = Professor(nome="ficticio")
                        comparacao=input("digite a matricula do professor que deseja alterar: ")
                        CRUD_Professor(a1, escolha).delete()
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE() 
                if op==5:
                    break          
            elif OpGeral==3:
                op=0
                ModuloAcademico.menuE()
                while op!=5:
                    if op==1:
                        a1 = Disciplina(id=int(input("digite o id da disciplina: ")), nome=input("digite o nome do disciplina: "), turma=input("digite a turma: "), notaminima=float(input("digite a notaminima: ")), cargahoraria=int(input("digite a carga horaria: ")), codigo=input("digite o codigo da disciplina: "))
                        CRUD_Disciplina(a1, escolha).insert()
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                    if op==2:
                        a1= Disciplina(id="ficticio")
                        resultado = CRUD_Disciplina(a1, escolha).select()
                        lista = []
                        for linha in resultado:
                            lista.append(linha[:])
                        for cont in range (len(lista)):
                            print(lista[cont])
                        time.sleep(1)
                        os.system("CLS")    
                        ModuloAcademico.menuE()    
                    if op==3:
                        comparacao=input("digite o codigo da disciplina que deseja altera: ")
                        a1 = Disciplina(id=int(input("digite o id da disciplina: ")), nome=input("digite o nome do disciplina: "), turma=input("digite a turma: "), notaminima=float(input("digite a nota minima: ")), cargahoraria=int(input("digite a carga horaria: ")), codigo=input("digite o codigo da disciplina: "))
                        CRUD_Disciplina(a1, escolha).update()
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                    if op==4:
                        a1 = Disciplina(nome="ficticio")
                        comparacao=input("digite o codigo da disciplina que deseja altera: ")
                        CRUD_Disciplina(a1, escolha).delete()
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                if op==5:
                    break             
            elif OpGeral==4:
                break 
    if escolha==2:
        ModuloAcademico.menu_geral()
        while OpGeral!=4:
            if OpGeral==1:

                op = 0
                ModuloAcademico.menuE()
                while op!=5:
                    if op==1:
                        a1 = Aluno(nome=input("digite o nome do aluno: "), idade=int(input("digite a idade do aluno: ")), altura=float(input("digite a altura do aluno: ")), peso=int(input("digite o peso do aluno: ")), rgm=input("digite o rgm do aluno: "), id=int(input("digite o id do aluno: ")))
                        a=ModuloAcademico()
                        a.Salvar(a1)
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()   
                    elif op==2:
                        a1 =Aluno()
                        a1.imprimir()
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                    elif op==3:
                        resp=int(input("digite o id do aluno que deseja alterar: "))
                        a1 = Aluno()
                        a1.atualizar(resp)
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE() 
                    elif op==4:
                        resp=int(input("digite o id do aluno que deseja alterar: "))
                        a1 = Aluno(nome="ficticio")
                        a1.remover(resp)
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                if op==5:
                    break
            if OpGeral==2:
                op = 0
                ModuloAcademico.menuE()
                while op!=5:
                    if op==1:
                        a1 = Professor(nome=input("digite o nome do professor: "), idade=int(input("digite a idade do professor: ")), altura=float(input("digite a altura do professor: ")), peso=int(input("digite o peso do professor: ")), matricula=input("digite a matricula do professor: "), id=int(input("digite o id do professor: ")))
                        a1.Salvar(a1)
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()  
                    elif op==2:
                        a1 =Professor()
                        a1.imprimir()
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                    elif op==3:
                        resp=int(input("digite o id do professor que deseja alterar: "))
                        a1 = Professor()
                        a1.atualizar(resp)
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE() 
                    elif op==4:
                        resp=int(input("digite o id do professor que deseja alterar: "))
                        a1 = Professor(nome="ficticio")
                        a1.remover(resp)
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                if op==5:
                    break
            if OpGeral==3:
                op = 0
                ModuloAcademico.menuE()
                while op!=5:
                    if op==1:
                        a1 = Disciplina(id=int(input("digite o id da disciplina: ")), nome=input("digite o nome da disciplina: "), turma=input("digite a turma: "), notaminima=float(input("digite a notaminima: ")), cargahoraria=int(input("digite a carga horaria: ")), codigo=input("digite o codigo da disciplina: "))
                        a1.Salvar(a1)
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()   
                    elif op==2:
                        a1 =Disciplina()
                        a1.imprimir()
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                    elif op==3:
                        resp=int(input("digite o id da disciplina que deseja alterar: "))
                        a1 = Disciplina()
                        a1.atualizar(resp)
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE() 
                    elif op==4:
                        resp=int(input("digite o id da disciplina que deseja alterar: "))
                        a1 = Disciplina(nome="ficticio")
                        a1.remover(resp)
                        time.sleep(1)
                        os.system("CLS")
                        ModuloAcademico.menuE()
                if op==5:
                    break        
        

    if escolha==3:
        break