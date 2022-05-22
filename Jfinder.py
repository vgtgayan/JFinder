#!/remote/vgrnd21/asitha/python/venv/bin/python
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWebEngineWidgets
from JfinderModelTfid import JfinderModel
import webbrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(784, 472)
        MainWindow.setGeometry(200, 150, 784, 472)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.le_jiraID = QLineEdit(self.centralwidget)
        self.le_jiraID.setObjectName(u"le_jiraID")
        self.le_jiraID.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.le_jiraID, 0, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.le_numOfResults = QLineEdit(self.centralwidget)
        self.le_numOfResults.setObjectName(u"le_numOfResults")
        self.le_numOfResults.setText("10")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_numOfResults.sizePolicy().hasHeightForWidth())
        self.le_numOfResults.setSizePolicy(sizePolicy)
        self.le_numOfResults.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.le_numOfResults, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_3.addWidget(self.checkBox)

        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_3.addWidget(self.checkBox_3)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_3.addWidget(self.checkBox_2)

        self.checkBox_4 = QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_3.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout_3.addWidget(self.checkBox_5)


        self.verticalLayout.addWidget(self.groupBox)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(3, -1, 3, -1)
        self.lw_results = QListWidget(self.centralwidget)
        self.lw_results.setObjectName(u"lw_results")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lw_results.sizePolicy().hasHeightForWidth())
        self.lw_results.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.lw_results)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setZoomFactor(0.5)
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.webEngineView)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.vs_zoomInOut = QSlider(self.centralwidget)
        self.vs_zoomInOut.setObjectName(u"vs_zoomInOut")
        self.vs_zoomInOut.setOrientation(Qt.Vertical)
        self.vs_zoomInOut.setMaximum(4)
        self.vs_zoomInOut.setMinimum(1)
        self.vs_zoomInOut.setValue(2)

        self.verticalLayout_2.addWidget(self.vs_zoomInOut)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, -1, 3, 3)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pb_find = QPushButton(self.centralwidget)
        self.pb_find.setObjectName(u"pb_find")

        self.horizontalLayout_2.addWidget(self.pb_find)
        
        self.pb_browse = QPushButton(self.centralwidget)
        self.pb_browse.setObjectName(u"pb_browse")

        self.horizontalLayout_2.addWidget(self.pb_browse)


        self.pb_close = QPushButton(self.centralwidget)
        self.pb_close.setObjectName(u"pb_close")

        self.horizontalLayout_2.addWidget(self.pb_close)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 784, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.le_jiraID)
        self.label_2.setBuddy(self.le_numOfResults)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"JFinder", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"&Keywords", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"&Number of Results:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Similarity Checks", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"&Title", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Typ&e", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"De&scription", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Pro&duct L1", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Prod&uct L2", None))
        self.pb_find.setText(QCoreApplication.translate("MainWindow", u"&Find", None))
        self.pb_close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pb_browse.setText(QCoreApplication.translate("MainWindow", u"Open in Browser", None))
    # retranslateUi

class JFinder(QMainWindow):
    def __init__(self):
        super(JFinder, self).__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.gui.pb_find.clicked.connect(self.on_findClick)
        self.gui.pb_close.clicked.connect(self.on_closeClick)
        self.gui.pb_browse.clicked.connect(self.on_browseClick)
        self.gui.vs_zoomInOut.valueChanged.connect(self.on_sliderValuechange)
        self.gui.lw_results.itemSelectionChanged.connect(self.on_selectionChange)
        self.jfmodel  = JfinderModel("test-data-54000")


    def AddResults(self):
        if jiraId:
            self.AddResults()
        else:
            print("Please enter Jira ID")

        jiraId = self.gui.le_jiraID.text()
        numOfResults = int(self.gui.le_numOfResults.text())
        jiraList = GetJiraListFromMLModel(numOfResults)
        for jiraID in jiraList:
            self.gui.lw_results.addItem(jiraID)
    
    def LoadJiraWebPage(self, jiraID):
        url = "https://jira.internal.synopsys.com/browse/" + jiraID
        self.gui.webEngineView.load(url)


    def on_findClick(self):
        self.gui.lw_results.clear()
        jiraId = self.gui.le_jiraID.text()
        if not jiraId:
            print("Please enter Jira ID")
            return
        numOfResults = int(self.gui.le_numOfResults.text())
        results = self.jfmodel.getresult(numOfResults, jiraId)
        jiraList = [x['key'] for x in results]
        for jiraId in jiraList:
            self.gui.lw_results.addItem(jiraId)
        #select first item
        if self.gui.lw_results.count() > 0:
            firstItem  = self.gui.lw_results.item(0)
            self.gui.lw_results.setItemSelected(firstItem, True)
            self.LoadJiraWebPage(firstItem.text())
        self.link = "https://jira.internal.synopsys.com/issues/?jql=key%20in%20("+"%2C%20".join(jiraList) +")"

    def on_sliderValuechange(self):
        sliderVal = self.gui.vs_zoomInOut.value()
        self.gui.webEngineView.setZoomFactor(sliderVal*0.25)
        
    def on_selectionChange(self):
        currentItem = self.gui.lw_results.currentItem()
        if currentItem:
            self.LoadJiraWebPage(currentItem.text())

    def on_closeClick(self):
        self.close()

    def on_browseClick(self):
        webbrowser.open(self.link)


def main():       
    app = QApplication(sys.argv)
    jFinder = JFinder()
    jFinder.show()
    sys.exit(app.exec_())

main()

