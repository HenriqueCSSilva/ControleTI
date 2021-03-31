import os
import pandas as pd
import sys
import pymysql
from Base import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog,QMessageBox,QLabel
from PyQt5.QtWidgets import QWidget, QAction, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem,QVBoxLayout,QInputDialog

conn = pymysql.connect(host="satelpjceara.com", port=3306, user="satelp03_marcosh",
                       password="12345678", db="satelp03_db_suporte")
cur = conn.cursor()

class ProjSuporte(QMainWindow, Ui_MainWindow):

    print('conexao ok')
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnInserir.clicked.connect(self.inserirForm)
        self.btnAtualizar.clicked.connect(self.updateFomr)
        self.btnBusca.clicked.connect(self.buscaForm)



    def inserirForm(self):
        nomeColab = self.txtNomeColaborador.text()
        cpf_rg = self.txtCPF.text()
        email = self.txtEmail.text()
        anydesk = self.txtAnyDesk.text()
        patrimonio = self.txtPatrimonio.text()
        area = self.ddlArea.currentText()
        unidade = self.ddlUnidade.currentText()
        statusColab = self.ddlStatusColab.currentText()
        telefone = self.txtTelefone.text()
        licencaOff =  self.txtLicencaOff.text()
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
            print(erro)


    def updateFomr(self):
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

        try:
            nomeColab = self.txtNomeColaborador.text().upper().split()
            sql_Select = (f"SELECT * from tb_base where   nome_colaborador =  UPPER('{nomeColab[0]}')")
            tabela =  pd.read_sql(sql_Select,conn)
            lista = tabela.values.tolist()
            print(lista)
            id = str(lista[0][0])
            nome_colaborador = lista[0][1]
            cpf_rg = lista[0][2]
            email_colab = lista[0][3]
            anydesk = lista[0][4]
            patrimonio = lista[0][5]
            telefone = lista[0][6]
            '''
            area_colab = lista[0][7]
            unidade_colab = lista[0][8]
            status_colab = lista[0][9]
            '''
            licenca_off = lista[0][10]
            email_off = lista[0][11]
            numero_off = lista[0][12]
            chave_off =  lista[0][13]

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





if __name__ == '__main__':
    qt = QApplication(sys.argv)
    setupSuporte = ProjSuporte()
    setupSuporte.show()
    qt.exec_()