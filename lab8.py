import psycopg2
import sys

from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._connect_to_db()

        self.setWindowTitle("SСЃhedule")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        # РЎРѕР·РґР°РµРј РѕР±СЉРµРєС‚ QScrollArea Рё РґРѕР±Р°РІР»СЏРµРј РІ РЅРµРіРѕ РІРёРґР¶РµС‚
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.tabs)

        # РЈСЃС‚Р°РЅР°РІР»РёРІР°РµРј РІРёРґР¶РµС‚ СЃ РїСЂРѕРєСЂСѓС‚РєРѕР№ РІ РєР°С‡РµСЃС‚РІРµ РіР»Р°РІРЅРѕРіРѕ РІРёРґР¶РµС‚Р° РѕРєРЅР°
        self.setLayout(QVBoxLayout(self))
        self.layout().addWidget(scroll_area)

        # self._create_shedule_tab("schedule")
        self._create_shedule_tab("schedule")
        # self._update_table()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="lab8",
                                     user="postgres",
                                     password="123",
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()


    def _create_shedule_tab(self, tab_name):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, tab_name)

        self.table_gbox1 = QGroupBox("Monday")
        self.table_gbox2 = QGroupBox("Tuesday")
        self.table_gbox3 = QGroupBox("Wednesday")
        self.table_gbox4 = QGroupBox("Thursday")
        self.table_gbox5 = QGroupBox("Friday")
        self.table_gbox6 = QGroupBox("Saturday")
        self.table_gbox7 = QGroupBox("Sunday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()
        self.shbox4 = QHBoxLayout()
        self.shbox5 = QHBoxLayout()
        self.shbox6 = QHBoxLayout()
        self.shbox7 = QHBoxLayout()
        self.shboxupdate = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)
        self.svbox.addLayout(self.shbox4)
        self.svbox.addLayout(self.shbox5)
        self.svbox.addLayout(self.shbox6)
        self.svbox.addLayout(self.shbox7)
        self.svbox.addLayout(self.shboxupdate)

        self.shbox1.addWidget(self.table_gbox1)
        self.shbox2.addWidget(self.table_gbox2)
        self.shbox3.addWidget(self.table_gbox3)
        self.shbox4.addWidget(self.table_gbox4)
        self.shbox5.addWidget(self.table_gbox5)
        self.shbox6.addWidget(self.table_gbox6)
        self.shbox7.addWidget(self.table_gbox7)

        self._create_day_table()

        self.update_shedule_button = QPushButton("Update")
        self.shboxupdate.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule_tab.setLayout(self.svbox)



    def _create_day_table(self):
        self.table1 = QTableWidget()
        self.table1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table1.setColumnCount(2)
        self.table1.setHorizontalHeaderLabels(["Subject", "Time"])


        self.table2 = QTableWidget()
        self.table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table2.setColumnCount(2)
        self.table2.setHorizontalHeaderLabels(["Subject", "Time"])

        self.table3 = QTableWidget()
        self.table3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table3.setColumnCount(2)
        self.table3.setHorizontalHeaderLabels(["Subject", "Time"])

        self.table4 = QTableWidget()
        self.table4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table4.setColumnCount(2)
        self.table4.setHorizontalHeaderLabels(["Subject", "Time"])

        self.table5 = QTableWidget()
        self.table5.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table5.setColumnCount(2)
        self.table5.setHorizontalHeaderLabels(["Subject", "Time"])


        self.table6 = QTableWidget()
        self.table6.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table6.setColumnCount(2)
        self.table6.setHorizontalHeaderLabels(["Subject", "Time"])

        self.table7 = QTableWidget()
        self.table7.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.table7.setColumnCount(2)
        self.table7.setHorizontalHeaderLabels(["Subject", "Time"])



        self._update_table()

        self.mvbox1 = QVBoxLayout()
        self.mvbox1.addWidget(self.table1)
        self.table_gbox1.setLayout(self.mvbox1)

        self.mvbox2 = QVBoxLayout()
        self.mvbox2.addWidget(self.table2)
        self.table_gbox2.setLayout(self.mvbox2)

        self.mvbox3 = QVBoxLayout()
        self.mvbox3.addWidget(self.table3)
        self.table_gbox3.setLayout(self.mvbox3)

        self.mvbox4 = QVBoxLayout()
        self.mvbox4.addWidget(self.table4)
        self.table_gbox4.setLayout(self.mvbox4)

        self.mvbox5 = QVBoxLayout()
        self.mvbox5.addWidget(self.table5)
        self.table_gbox5.setLayout(self.mvbox5)

        self.add_record_button = QPushButton("Add Record")
        self.mvbox5.addWidget(self.add_record_button)
        self.add_record_button.clicked.connect(self._add_record)


        self.mvbox6 = QVBoxLayout()
        self.mvbox6.addWidget(self.table6)
        self.table_gbox6.setLayout(self.mvbox6)

        self.mvbox7 = QVBoxLayout()
        self.mvbox7.addWidget(self.table7)
        self.table_gbox7.setLayout(self.mvbox7)

    def _add_record(self):
        row_count = self.table5.rowCount()

        self.table5.insertRow(row_count)

        subject_item = QTableWidgetItem("")
        time_item = QTableWidgetItem("")

        self.table5.setItem(row_count, 0, subject_item)
        self.table5.setItem(row_count, 1, time_item)

        self.table5.resizeRowsToContents()

    def _update_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='wednesday'")
        records = list(self.cursor.fetchall())

        self.table1.setRowCount(len(records) + 1)
        self.table2.setRowCount(len(records) + 1)
        self.table3.setRowCount(len(records) + 1)
        self.table4.setRowCount(len(records) + 1)
        self.table5.setRowCount(len(records) + 1)
        self.table6.setRowCount(len(records) + 1)
        self.table7.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.table1.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.table1.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.table1.setItem(i, 2,
                                      QTableWidgetItem(str(r[4])))
            self.table1.setCellWidget(i, 3, joinButton)
            #
            self.table2.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.table2.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.table2.setItem(i, 2,
                                      QTableWidgetItem(str(r[4])))
            self.table2.setCellWidget(i, 3, joinButton)
            #
            self.table3.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.table3.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.table3.setItem(i, 2,
                                      QTableWidgetItem(str(r[4])))
            self.table3.setCellWidget(i, 3, joinButton)
            #
            self.table4.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.table4.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.table4.setItem(i, 2,
                                      QTableWidgetItem(str(r[4])))
            self.table4.setCellWidget(i, 3, joinButton)
            #
            self.table5.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.table5.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.table5.setItem(i, 2,
                                      QTableWidgetItem(str(r[4])))
            self.table5.setCellWidget(i, 3, joinButton)
            #
            self.table6.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.table6.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.table6.setItem(i, 2,
                                      QTableWidgetItem(str(r[4])))
            self.table6.setCellWidget(i, 3, joinButton)
            #
            self.table7.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.table7.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.table7.setItem(i, 2,
                                      QTableWidgetItem(str(r[4])))
            self.table7.setCellWidget(i, 3, joinButton)


            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num))

        self.table1.resizeRowsToContents()
        self.table2.resizeRowsToContents()
        self.table3.resizeRowsToContents()
        self.table4.resizeRowsToContents()
        self.table5.resizeRowsToContents()
        self.table6.resizeRowsToContents()
        self.table7.resizeRowsToContents()

    def _change_day_from_table(self, rowNum, day):
        row = list()
        for i in range(self.mtable.columnCount()):
            try:
                row.append(self.table.item(rowNum, i).text())
            except:
                row.append(None)
            try:
                self.cursor.execute("UPDATE timetable set subject  = %s WHERE day = %s ",\
                                    (row[0],))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _update_shedule(self):
        self._update_table()
        ...


app = QApplication(sys.argv)
print(app)
win = MainWindow()
win.show()
sys.exit(app.exec_())
