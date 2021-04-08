import pandas as pd
import sys
import pymysql
from Base import *
import variaveis as var
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog,QMessageBox,QLabel
from PyQt5.QtWidgets import QWidget, QAction, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem,QVBoxLayout,QInputDialog

conn = pymysql.connect(host=var.host, port=3306, user=var.user,
                               password=var.password, db=var.db)
cur = conn.cursor()


class ProjSuporte(QMainWindow, Ui_MainWindow):

    print('conexao ok')
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnInserir.clicked.connect(self.inserirForm)
        self.btnAtualizar.clicked.connect(self.updateFomr)
        self.btnBusca.clicked.connect(self.buscaForm)
        self.btnLimpar.clicked.connect(self.limpar)

        # --------------BASE------------------#
        self.btnBaseBusca.clicked.connect(self.buscaBase)

        #-----------Demanda Diaria----------#

        self.btnDDAddDemanda.clicked.connect(self.gravarDemanda)
        self.btnAtDemanda.clicked.connect(self.atualizaDemanda)
        #------------------Constantes---------#
        self.tbBase.setItem(0,0,QTableWidgetItem(''))



        sql_area = "SELECT desc_area FROM tb_area "
        loadArea = pd.read_sql(sql_area, conn).values.tolist()
        for i in loadArea:
            item = i[0]
            self.ddlArea.addItem(item)
            self.ddlBaseArea.addItem(item)

#------------Geral---------#
    def inserirForm(self):
        conn = pymysql.connect(host=var.host, port=3306, user=var.user,
                               password=var.password, db=var.db)
        cur = conn.cursor()

        nomeColab = self.txtNomeColaborador.text()
        cpf_rg = self.txtCPF.text()
        email = self.txtEmail.text()
        anydesk = self.txtAnyDesk.text()
        patrimonio = self.txtPatrimonio.text()
        area = self.ddlArea.currentText()
        unidade = self.ddlUnidade.currentText()
        statusColab = self.ddlStatusColab.currentText()
        telefone = self.txtTelefone.text()
        licencaOff = self.txtLicencaOff.text()
        emailOff = self.txtLicencaOff.text()
        chaveOff = self.txtEmailOff.text()
        numOff = self.txtNumOff.text()

        try:
            sql_Insert = (f"INSERT INTO tb_base (nome_colaborador,cpf_rg,email_colab,anydesk,patrimonio,"
                          f"telefone,area_colab,unidade_colab,status_colab,licenca_off,email_off,numero_off,chave_off        )"
                          f" VALUES ('{nomeColab}','{cpf_rg}','{email}','{anydesk}','{patrimonio}','{telefone}',"
                          f"'{area}','{unidade}','{statusColab}','{licencaOff}','{emailOff}','{chaveOff}','{numOff}')")
            cur.execute(sql_Insert)
            conn.commit()
            conn.close()
            QMessageBox.about(self, "Sucesso", "Dados Inseridos")
        except Exception as erro:
            QMessageBox.about(self, "Falha", "Falha ao Gravar")
            print(erro)

    def updateFomr(self):
        conn = pymysql.connect(host=var.host, port=3306, user=var.user,
                               password=var.password, db=var.db)
        cur = conn.cursor()

        nomeColab = self.txtNomeColaborador.text()
        cpf_rg = self.txtCPF.text()
        email = self.txtEmail.text()
        anydesk = self.txtAnyDesk.text()
        patrimonio = self.txtPatrimonio.text()
        area = self.ddlArea.currentText()
        unidade = self.ddlUnidade.currentText()
        statusColab = self.ddlStatusColab.currentText()
        telefone = self.txtTelefone.text()
        licencaOff = self.txtLicencaOff.text()
        emailOff = self.txtLicencaOff.text()
        chaveOff = self.txtEmailOff.text()
        numOff = self.txtNumOff.text()

        try:
            sql_Update = (f"update tb_base  set "
                          f"nome_colaborador = '{nomeColab}', "
                          f"cpf_rg = '{cpf_rg}',"
                          f"email_colab = '{email}',"
                          f"anydesk = '{anydesk}',"
                          f"patrimonio = '{patrimonio}',"
                          f"telefone = '{telefone}',"
                          f"area_colab = '{area}',"
                          f"unidade_colab = '{unidade}',"
                          f"status_colab = '{statusColab}',"
                          f"licenca_off = '{licencaOff}',"
                          f"email_off = '{emailOff}',"
                          f"numero_off = '{chaveOff}',"
                          f"chave_off  = '{numOff}'    where nome_colaborador like = '%{nomeColab}%'" )

            cur.execute(sql_Update)
            conn.commit()
            conn.close()
            QMessageBox.about(self, "Sucesso", "Dados Atualozados")
        except Exception as erro:
            QMessageBox.about(self, "Update", "Dados NãoGravados")
            print(erro)


    def buscaForm(self):
        conn = pymysql.connect(host=var.host, port=3306, user=var.user,
                               password=var.password, db=var.db)
        cur = conn.cursor()

        try:
            nomeColab = self.txtNomeColaborador.text().upper().strip()
            email = self.txtEmailOff.text().strip()
            telefone = self.txtTelefone.text().strip()
            sql_Select = (f"SELECT * from tb_base where  UPPER(nome_colaborador)= '{nomeColab}'")
            tabela =  pd.read_sql(sql_Select,conn)
            lista = tabela.values.tolist()
            id = str(lista[0][0])
            nome_colaborador = lista[0][1]
            cpf_rg = lista[0][2]
            email_colab = lista[0][3]
            anydesk = lista[0][4]
            patrimonio = lista[0][5]
            telefone = lista[0][6]

            area_colab = lista[0][7]
            unidade_colab = lista[0][8]
            status_colab = lista[0][9]

            licenca_off = lista[0][10]
            email_off = lista[0][11]
            numero_off = lista[0][12]
            chave_off = lista[0][13]

            programas = lista[0][14]
            brics = list(programas)

            print(programas)
            print(brics)



            #QMessageBox.about(self, "Sucesso", "Dados Inseridos")
            self.txtNomeColaborador.setText(nome_colaborador)
            self.txtCPF.setText(cpf_rg)
            self.txtEmail.setText(email_colab)
            self.txtAnyDesk.setText(anydesk)
            self.txtPatrimonio.setText(patrimonio)
            # area = self.ddlArea.setText()
            # unidade = self.ddlUnidade.setText()
            # statusColab = self.ddlStatusColab.setText()
            self.txtTelefone.setText(telefone)

            self.txtLicencaOff.setText(licenca_off)
            self.txtEmailOff.setText(email_off)
            self.txtNumOff.setText(numero_off)
            self.txtChaveOff.setText(chave_off)

        except Exception as erro:
            print(sql_Select)
            QMessageBox.about(self, "Read", "Falha ao Recupear")
            print(erro)


    def limpar(self):
        self.txtNomeColaborador.setText('')
        self.txtEmail.setText('')
        self.txtCPF.setText('')
        self.txtTelefone.setText('')
        self.txtAnyDesk.setText('')
        self.txtPatrimonio.setText('')
        self.txtLicencaOff.setText('')
        self.txtEmailOff.setText('')
        self.txtNumOff.setText('')
        self.txtChaveOff.setText('')


#-----------------------------Base--------------------#




    def buscaBase(self):
        conn = pymysql.connect(host=var.host, port=3306, user=var.user,
                               password=var.password, db=var.db)
        cur = conn.cursor()

        try:
            nome = self.txtBaseNomeColaborador.text().upper()
            sql_Select = (f"SELECT * from tb_base where   nome_colaborador like  UPPER('%{nome[0]}%')")
            tabela = pd.read_sql(sql_Select, conn)
            lista = tabela.values.tolist()

            '''id = str(tabela.iloc[:,0])
            nome_colaborador = tabela.iloc[:,1]
            cpf_rg = tabela.iloc[:,2]
            email_colab = tabela.iloc[:,3]
            anydesk = tabela.iloc[:,4]
            patrimonio = tabela.iloc[:,5]
            telefone = tabela.iloc[:,6]'''

            id = str(lista[0][0])
            nome_colaborador = lista[0][1]
            cpf_rg = lista[0][2]
            email_colab = lista[0][3]
            anydesk = lista[0][4]
            patrimonio = lista[0][5]
            telefone = lista[0][6]

            '''area_colab = lista[0][7]
            unidade_colab = lista[0][8]
            status_colab = lista[0][9]'''
            ''' licenca_off = lista[0][10]
            email_off = lista[0][11]
            numero_off = lista[0][12]
            chave_off =  lista[0][13]'''


            '''if self.addCheckDB.isChecked():
                self.addCheck.setChecked(False)'''

            row = 0
            for i in lista:
                self.tbBase.insertRow(row)
                self.tbBase.setItem(row, 0, QTableWidgetItem(str(i[0])))
                self.tbBase.setItem(row, 1, QTableWidgetItem(i[1]))
                self.tbBase.setItem(row, 2, QTableWidgetItem(i[7]))
                self.tbBase.setItem(row, 3, QTableWidgetItem(i[8]))
                self.tbBase.setItem(row, 4, QTableWidgetItem(i[9]))
                self.tbBase.setItem(row, 5, QTableWidgetItem(i[3]))

                row = row+1
        except Exception as erro:
            print(erro)



#------------------------------Tarefas----------------------------#
    def gravarDemanda(self):

        conn = pymysql.connect(host=var.host, port=3306, user=var.user,
                               password=var.password, db=var.db)
        cur = conn.cursor()

        categoria = self.ddlDDCategoria.currentText()
        prioridade = self.ddlDDPrioridade.currentText()
        assunto = self.ddlDDAssunto.currentText()
        beneficiado = self.ddlDDBeneficiado.currentText()
        descricao = self.txtDDDescricao.toPlainText()
        prazo = self.dteDDPrazo.text()
        print(prazo)
        try:
            sql_Insert = (f"INSERT INTO tb_demanda_diaria (cod,data_ingresso,categoria,prioridade,"
                          f"assunto,beneficiado,descricao,status_atividade)"
                          f" VALUES (right(RAND(),4),now(), '{categoria}','{prioridade}',"
                          f"'{assunto}','{beneficiado}','{descricao}','Em Aberto' )")
            cur.execute(sql_Insert)

            QMessageBox.about(self, "Sucesso", "Dados Inseridos")
        except Exception as erro:
            print(erro)
            print(sql_Insert)
            QMessageBox.about(self, "Falha", "Falha")
        conn.commit()
        conn.close()

    def atualizaDemanda(self):
        conn = pymysql.connect(host=var.host, port=3306, user=var.user,
                               password=var.password, db=var.db)
        cur = conn.cursor()
        try:
            nome = self.txtBaseNomeColaborador.text().upper().split()
            sql_Select = (f"SELECT * from tb_demanda_diaria where  status_atividade like '%Em Aberto%' ")
            tabela = pd.read_sql(sql_Select, conn)
            lista = tabela.values.tolist()

            row = 0
            for i in lista:
                cod = str(i[1])
                categoria = i[3]
                data_ingresso = i[2]
                prioridade = i[3]
                assunto = i[5]
                beneficiado = i[6]
                prazo = i[7]
                descricao = i[8]
                self.tbDemanda.insertRow(row)
                self.tbDemanda.setItem(row, 0, QTableWidgetItem(cod ))
                self.tbDemanda.setItem(row, 1, QTableWidgetItem(categoria))
                self.tbDemanda.setItem(row, 2, QTableWidgetItem(data_ingresso))
                self.tbDemanda.setItem(row, 3, QTableWidgetItem(prioridade))
                self.tbDemanda.setItem(row, 4, QTableWidgetItem(assunto))
                self.tbDemanda.setItem(row, 5, QTableWidgetItem(beneficiado))
                self.tbDemanda.setItem(row, 6, QTableWidgetItem(prazo))
                self.tbDemanda.setItem(row, 7, QTableWidgetItem(descricao))

            row = row + 1

        except Exception as erro:
            print(erro)
        conn.commit()
        conn.close()







if __name__ == '__main__':
    qt = QApplication(sys.argv)
    setupSuporte = ProjSuporte()
    setupSuporte.show()
    qt.exec_()