# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\GitHub\Muskrat_RPG\NPC_generator\NPC_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NPC_Widget(object):
    def setupUi(self, NPC_Widget):
        NPC_Widget.setObjectName("NPC_Widget")
        NPC_Widget.resize(370, 320)
        self.groupBox_incoming_damage = QtWidgets.QGroupBox(NPC_Widget)
        self.groupBox_incoming_damage.setGeometry(QtCore.QRect(190, 120, 171, 41))
        self.groupBox_incoming_damage.setTitle("")
        self.groupBox_incoming_damage.setObjectName("groupBox_incoming_damage")
        self.lineEdit_incoming_damage_magic = QtWidgets.QLineEdit(self.groupBox_incoming_damage)
        self.lineEdit_incoming_damage_magic.setGeometry(QtCore.QRect(90, 2, 21, 20))
        self.lineEdit_incoming_damage_magic.setStyleSheet("background-color: rgb(190, 190, 255);")
        self.lineEdit_incoming_damage_magic.setText("")
        self.lineEdit_incoming_damage_magic.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_incoming_damage_magic.setObjectName("lineEdit_incoming_damage_magic")
        self.lineEdit_incoming_damage_armor = QtWidgets.QLineEdit(self.groupBox_incoming_damage)
        self.lineEdit_incoming_damage_armor.setGeometry(QtCore.QRect(110, 2, 21, 20))
        self.lineEdit_incoming_damage_armor.setStyleSheet("background-color: rgb(186, 190, 202);")
        self.lineEdit_incoming_damage_armor.setText("")
        self.lineEdit_incoming_damage_armor.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_incoming_damage_armor.setObjectName("lineEdit_incoming_damage_armor")
        self.lineEdit_incoming_damage_health = QtWidgets.QLineEdit(self.groupBox_incoming_damage)
        self.lineEdit_incoming_damage_health.setGeometry(QtCore.QRect(150, 2, 21, 20))
        self.lineEdit_incoming_damage_health.setStyleSheet("background-color: rgb(255, 199, 200);")
        self.lineEdit_incoming_damage_health.setText("")
        self.lineEdit_incoming_damage_health.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_incoming_damage_health.setObjectName("lineEdit_incoming_damage_health")
        self.lineEdit_incoming_damage_penetration_damage = QtWidgets.QLineEdit(self.groupBox_incoming_damage)
        self.lineEdit_incoming_damage_penetration_damage.setGeometry(QtCore.QRect(130, 2, 21, 20))
        self.lineEdit_incoming_damage_penetration_damage.setStyleSheet("background-color: rgb(195, 166, 166);")
        self.lineEdit_incoming_damage_penetration_damage.setText("")
        self.lineEdit_incoming_damage_penetration_damage.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_incoming_damage_penetration_damage.setObjectName("lineEdit_incoming_damage_penetration_damage")
        self.lineEdit_periodic_damage_magic = QtWidgets.QLineEdit(self.groupBox_incoming_damage)
        self.lineEdit_periodic_damage_magic.setGeometry(QtCore.QRect(0, 5, 21, 20))
        self.lineEdit_periodic_damage_magic.setStyleSheet("background-color: rgb(190, 190, 255);")
        self.lineEdit_periodic_damage_magic.setText("")
        self.lineEdit_periodic_damage_magic.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_periodic_damage_magic.setObjectName("lineEdit_periodic_damage_magic")
        self.lineEdit_periodic_damage_armor = QtWidgets.QLineEdit(self.groupBox_incoming_damage)
        self.lineEdit_periodic_damage_armor.setGeometry(QtCore.QRect(20, 5, 21, 20))
        self.lineEdit_periodic_damage_armor.setStyleSheet("background-color: rgb(186, 190, 202);")
        self.lineEdit_periodic_damage_armor.setText("")
        self.lineEdit_periodic_damage_armor.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_periodic_damage_armor.setObjectName("lineEdit_periodic_damage_armor")
        self.lineEdit_periodic_damage_penetration_damage = QtWidgets.QLineEdit(self.groupBox_incoming_damage)
        self.lineEdit_periodic_damage_penetration_damage.setGeometry(QtCore.QRect(40, 5, 21, 20))
        self.lineEdit_periodic_damage_penetration_damage.setStyleSheet("background-color: rgb(195, 166, 166);")
        self.lineEdit_periodic_damage_penetration_damage.setText("")
        self.lineEdit_periodic_damage_penetration_damage.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_periodic_damage_penetration_damage.setObjectName("lineEdit_periodic_damage_penetration_damage")
        self.lineEdit_periodic_damage_health = QtWidgets.QLineEdit(self.groupBox_incoming_damage)
        self.lineEdit_periodic_damage_health.setGeometry(QtCore.QRect(60, 5, 21, 20))
        self.lineEdit_periodic_damage_health.setStyleSheet("background-color: rgb(255, 199, 200);")
        self.lineEdit_periodic_damage_health.setText("")
        self.lineEdit_periodic_damage_health.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_periodic_damage_health.setObjectName("lineEdit_periodic_damage_health")
        self.label_periodic = QtWidgets.QLabel(self.groupBox_incoming_damage)
        self.label_periodic.setGeometry(QtCore.QRect(0, 20, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setItalic(True)
        self.label_periodic.setFont(font)
        self.label_periodic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_periodic.setObjectName("label_periodic")
        self.pushButton_incoming_damage_enter = QtWidgets.QPushButton(self.groupBox_incoming_damage)
        self.pushButton_incoming_damage_enter.setGeometry(QtCore.QRect(130, 21, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_incoming_damage_enter.setFont(font)
        self.pushButton_incoming_damage_enter.setObjectName("pushButton_incoming_damage_enter")
        self.radioButton_crit = QtWidgets.QRadioButton(self.groupBox_incoming_damage)
        self.radioButton_crit.setGeometry(QtCore.QRect(90, 20, 41, 21))
        self.radioButton_crit.setObjectName("radioButton_crit")
        self.groupBox = QtWidgets.QGroupBox(NPC_Widget)
        self.groupBox.setGeometry(QtCore.QRect(190, 30, 171, 61))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.comboBox_type = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_type.setGeometry(QtCore.QRect(0, 20, 171, 20))
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.setItemText(0, "")
        self.comboBox_trash_elite_legend = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_trash_elite_legend.setGeometry(QtCore.QRect(20, 0, 61, 21))
        self.comboBox_trash_elite_legend.setObjectName("comboBox_trash_elite_legend")
        self.comboBox_trash_elite_legend.addItem("")
        self.comboBox_trash_elite_legend.setItemText(0, "")
        self.comboBox_trash_elite_legend.addItem("")
        self.comboBox_trash_elite_legend.addItem("")
        self.comboBox_trash_elite_legend.addItem("")
        self.lineEdit_lvl = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_lvl.setGeometry(QtCore.QRect(0, 0, 21, 21))
        self.lineEdit_lvl.setText("")
        self.lineEdit_lvl.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_lvl.setObjectName("lineEdit_lvl")
        self.comboBox_gender = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_gender.setGeometry(QtCore.QRect(80, 0, 41, 21))
        self.comboBox_gender.setObjectName("comboBox_gender")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.setItemText(0, "")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.pushButton_generation = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_generation.setGeometry(QtCore.QRect(120, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_generation.setFont(font)
        self.pushButton_generation.setObjectName("pushButton_generation")
        self.pushButton_load = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_load.setGeometry(QtCore.QRect(40, 40, 41, 21))
        self.pushButton_load.setObjectName("pushButton_load")
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_save.setGeometry(QtCore.QRect(0, 40, 41, 21))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_info = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_info.setGeometry(QtCore.QRect(130, 0, 31, 20))
        self.pushButton_info.setObjectName("pushButton_info")
        self.pushButton_reset = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_reset.setGeometry(QtCore.QRect(80, 40, 41, 21))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.groupBox_physique_mastery_intelligence = QtWidgets.QGroupBox(NPC_Widget)
        self.groupBox_physique_mastery_intelligence.setGeometry(QtCore.QRect(10, 30, 171, 281))
        self.groupBox_physique_mastery_intelligence.setTitle("")
        self.groupBox_physique_mastery_intelligence.setObjectName("groupBox_physique_mastery_intelligence")
        self.pushButton_d20_mastery = QtWidgets.QPushButton(self.groupBox_physique_mastery_intelligence)
        self.pushButton_d20_mastery.setGeometry(QtCore.QRect(151, 60, 20, 21))
        self.pushButton_d20_mastery.setText("")
        self.pushButton_d20_mastery.setObjectName("pushButton_d20_mastery")
        self.comboBox_skill_1 = QtWidgets.QComboBox(self.groupBox_physique_mastery_intelligence)
        self.comboBox_skill_1.setGeometry(QtCore.QRect(0, 80, 131, 22))
        self.comboBox_skill_1.setObjectName("comboBox_skill_1")
        self.comboBox_skill_1.addItem("")
        self.comboBox_skill_1.setItemText(0, "")
        self.pushButton_d20_skill_1 = QtWidgets.QPushButton(self.groupBox_physique_mastery_intelligence)
        self.pushButton_d20_skill_1.setGeometry(QtCore.QRect(151, 80, 20, 21))
        self.pushButton_d20_skill_1.setText("")
        self.pushButton_d20_skill_1.setObjectName("pushButton_d20_skill_1")
        self.comboBox_skill_2 = QtWidgets.QComboBox(self.groupBox_physique_mastery_intelligence)
        self.comboBox_skill_2.setGeometry(QtCore.QRect(0, 100, 131, 22))
        self.comboBox_skill_2.setObjectName("comboBox_skill_2")
        self.comboBox_skill_2.addItem("")
        self.comboBox_skill_2.setItemText(0, "")
        self.pushButton_d20_skill_2 = QtWidgets.QPushButton(self.groupBox_physique_mastery_intelligence)
        self.pushButton_d20_skill_2.setGeometry(QtCore.QRect(151, 100, 20, 21))
        self.pushButton_d20_skill_2.setText("")
        self.pushButton_d20_skill_2.setObjectName("pushButton_d20_skill_2")
        self.comboBox_skill_3 = QtWidgets.QComboBox(self.groupBox_physique_mastery_intelligence)
        self.comboBox_skill_3.setGeometry(QtCore.QRect(0, 120, 131, 22))
        self.comboBox_skill_3.setObjectName("comboBox_skill_3")
        self.comboBox_skill_3.addItem("")
        self.comboBox_skill_3.setItemText(0, "")
        self.pushButton_d20_skill_3 = QtWidgets.QPushButton(self.groupBox_physique_mastery_intelligence)
        self.pushButton_d20_skill_3.setGeometry(QtCore.QRect(151, 120, 20, 21))
        self.pushButton_d20_skill_3.setText("")
        self.pushButton_d20_skill_3.setObjectName("pushButton_d20_skill_3")
        self.comboBox_skill_4 = QtWidgets.QComboBox(self.groupBox_physique_mastery_intelligence)
        self.comboBox_skill_4.setGeometry(QtCore.QRect(0, 140, 131, 21))
        self.comboBox_skill_4.setObjectName("comboBox_skill_4")
        self.comboBox_skill_4.addItem("")
        self.comboBox_skill_4.setItemText(0, "")
        self.pushButton_d20_skill_4 = QtWidgets.QPushButton(self.groupBox_physique_mastery_intelligence)
        self.pushButton_d20_skill_4.setGeometry(QtCore.QRect(151, 140, 20, 21))
        self.pushButton_d20_skill_4.setText("")
        self.pushButton_d20_skill_4.setObjectName("pushButton_d20_skill_4")
        self.comboBox_spell_1 = QtWidgets.QComboBox(self.groupBox_physique_mastery_intelligence)
        self.comboBox_spell_1.setGeometry(QtCore.QRect(0, 180, 131, 22))
        self.comboBox_spell_1.setObjectName("comboBox_spell_1")
        self.comboBox_spell_1.addItem("")
        self.comboBox_spell_1.setItemText(0, "")
        self.pushButton_d20_intelligence = QtWidgets.QPushButton(self.groupBox_physique_mastery_intelligence)
        self.pushButton_d20_intelligence.setGeometry(QtCore.QRect(151, 160, 20, 21))
        self.pushButton_d20_intelligence.setText("")
        self.pushButton_d20_intelligence.setObjectName("pushButton_d20_intelligence")
        self.pushButton_d20_spell_1 = QtWidgets.QPushButton(self.groupBox_physique_mastery_intelligence)
        self.pushButton_d20_spell_1.setGeometry(QtCore.QRect(151, 180, 20, 21))
        self.pushButton_d20_spell_1.setText("")
        self.pushButton_d20_spell_1.setObjectName("pushButton_d20_spell_1")
        self.pushButton_d20_spell_2 = QtWidgets.QPushButton(self.groupBox_physique_mastery_intelligence)
        self.pushButton_d20_spell_2.setGeometry(QtCore.QRect(151, 200, 20, 21))
        self.pushButton_d20_spell_2.setText("")
        self.pushButton_d20_spell_2.setObjectName("pushButton_d20_spell_2")
        self.pushButton_d20_spell_3 = QtWidgets.QPushButton(self.groupBox_physique_mastery_intelligence)
        self.pushButton_d20_spell_3.setGeometry(QtCore.QRect(151, 220, 20, 21))
        self.pushButton_d20_spell_3.setText("")
        self.pushButton_d20_spell_3.setObjectName("pushButton_d20_spell_3")
        self.pushButton_d20_spell_4 = QtWidgets.QPushButton(self.groupBox_physique_mastery_intelligence)
        self.pushButton_d20_spell_4.setGeometry(QtCore.QRect(151, 240, 20, 21))
        self.pushButton_d20_spell_4.setText("")
        self.pushButton_d20_spell_4.setObjectName("pushButton_d20_spell_4")
        self.pushButton_d20_spell_5 = QtWidgets.QPushButton(self.groupBox_physique_mastery_intelligence)
        self.pushButton_d20_spell_5.setGeometry(QtCore.QRect(151, 260, 20, 21))
        self.pushButton_d20_spell_5.setText("")
        self.pushButton_d20_spell_5.setObjectName("pushButton_d20_spell_5")
        self.comboBox_spell_2 = QtWidgets.QComboBox(self.groupBox_physique_mastery_intelligence)
        self.comboBox_spell_2.setGeometry(QtCore.QRect(0, 200, 131, 22))
        self.comboBox_spell_2.setObjectName("comboBox_spell_2")
        self.comboBox_spell_2.addItem("")
        self.comboBox_spell_2.setItemText(0, "")
        self.comboBox_spell_3 = QtWidgets.QComboBox(self.groupBox_physique_mastery_intelligence)
        self.comboBox_spell_3.setGeometry(QtCore.QRect(0, 220, 131, 22))
        self.comboBox_spell_3.setObjectName("comboBox_spell_3")
        self.comboBox_spell_3.addItem("")
        self.comboBox_spell_3.setItemText(0, "")
        self.comboBox_spell_4 = QtWidgets.QComboBox(self.groupBox_physique_mastery_intelligence)
        self.comboBox_spell_4.setGeometry(QtCore.QRect(0, 240, 131, 22))
        self.comboBox_spell_4.setObjectName("comboBox_spell_4")
        self.comboBox_spell_4.addItem("")
        self.comboBox_spell_4.setItemText(0, "")
        self.comboBox_spell_5 = QtWidgets.QComboBox(self.groupBox_physique_mastery_intelligence)
        self.comboBox_spell_5.setGeometry(QtCore.QRect(0, 260, 131, 21))
        self.comboBox_spell_5.setObjectName("comboBox_spell_5")
        self.comboBox_spell_5.addItem("")
        self.comboBox_spell_5.setItemText(0, "")
        self.label_mastery = QtWidgets.QLabel(self.groupBox_physique_mastery_intelligence)
        self.label_mastery.setGeometry(QtCore.QRect(50, 60, 71, 20))
        self.label_mastery.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_mastery.setObjectName("label_mastery")
        self.label__intelligence = QtWidgets.QLabel(self.groupBox_physique_mastery_intelligence)
        self.label__intelligence.setGeometry(QtCore.QRect(60, 160, 61, 20))
        self.label__intelligence.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label__intelligence.setObjectName("label__intelligence")
        self.lineEdit_mastery = QtWidgets.QLineEdit(self.groupBox_physique_mastery_intelligence)
        self.lineEdit_mastery.setGeometry(QtCore.QRect(130, 61, 21, 20))
        self.lineEdit_mastery.setStyleSheet("background-color: rgb(221, 255, 219);")
        self.lineEdit_mastery.setText("")
        self.lineEdit_mastery.setObjectName("lineEdit_mastery")
        self.lineEdit_skill_1 = QtWidgets.QLineEdit(self.groupBox_physique_mastery_intelligence)
        self.lineEdit_skill_1.setGeometry(QtCore.QRect(130, 80, 21, 21))
        self.lineEdit_skill_1.setText("")
        self.lineEdit_skill_1.setObjectName("lineEdit_skill_1")
        self.lineEdit_skill_2 = QtWidgets.QLineEdit(self.groupBox_physique_mastery_intelligence)
        self.lineEdit_skill_2.setGeometry(QtCore.QRect(130, 100, 21, 21))
        self.lineEdit_skill_2.setText("")
        self.lineEdit_skill_2.setObjectName("lineEdit_skill_2")
        self.lineEdit_skill_3 = QtWidgets.QLineEdit(self.groupBox_physique_mastery_intelligence)
        self.lineEdit_skill_3.setGeometry(QtCore.QRect(130, 120, 21, 21))
        self.lineEdit_skill_3.setText("")
        self.lineEdit_skill_3.setObjectName("lineEdit_skill_3")
        self.lineEdit_skill_4 = QtWidgets.QLineEdit(self.groupBox_physique_mastery_intelligence)
        self.lineEdit_skill_4.setGeometry(QtCore.QRect(130, 140, 21, 21))
        self.lineEdit_skill_4.setText("")
        self.lineEdit_skill_4.setObjectName("lineEdit_skill_4")
        self.lineEdit_intelligence = QtWidgets.QLineEdit(self.groupBox_physique_mastery_intelligence)
        self.lineEdit_intelligence.setGeometry(QtCore.QRect(130, 160, 21, 21))
        self.lineEdit_intelligence.setStyleSheet("background-color: rgb(207, 224, 255);")
        self.lineEdit_intelligence.setText("")
        self.lineEdit_intelligence.setObjectName("lineEdit_intelligence")
        self.lineEdit_spell_1 = QtWidgets.QLineEdit(self.groupBox_physique_mastery_intelligence)
        self.lineEdit_spell_1.setGeometry(QtCore.QRect(130, 180, 21, 21))
        self.lineEdit_spell_1.setText("")
        self.lineEdit_spell_1.setObjectName("lineEdit_spell_1")
        self.lineEdit_spell_2 = QtWidgets.QLineEdit(self.groupBox_physique_mastery_intelligence)
        self.lineEdit_spell_2.setGeometry(QtCore.QRect(130, 200, 21, 21))
        self.lineEdit_spell_2.setText("")
        self.lineEdit_spell_2.setObjectName("lineEdit_spell_2")
        self.lineEdit_spell_3 = QtWidgets.QLineEdit(self.groupBox_physique_mastery_intelligence)
        self.lineEdit_spell_3.setGeometry(QtCore.QRect(130, 220, 21, 21))
        self.lineEdit_spell_3.setText("")
        self.lineEdit_spell_3.setObjectName("lineEdit_spell_3")
        self.lineEdit_spell_4 = QtWidgets.QLineEdit(self.groupBox_physique_mastery_intelligence)
        self.lineEdit_spell_4.setGeometry(QtCore.QRect(130, 240, 21, 21))
        self.lineEdit_spell_4.setText("")
        self.lineEdit_spell_4.setObjectName("lineEdit_spell_4")
        self.lineEdit_spell_5 = QtWidgets.QLineEdit(self.groupBox_physique_mastery_intelligence)
        self.lineEdit_spell_5.setGeometry(QtCore.QRect(130, 260, 21, 21))
        self.lineEdit_spell_5.setText("")
        self.lineEdit_spell_5.setObjectName("lineEdit_spell_5")
        self.pushButton_d20_physique = QtWidgets.QPushButton(self.groupBox_physique_mastery_intelligence)
        self.pushButton_d20_physique.setGeometry(QtCore.QRect(150, 1, 20, 20))
        self.pushButton_d20_physique.setText("")
        self.pushButton_d20_physique.setObjectName("pushButton_d20_physique")
        self.lineEdit_physique = QtWidgets.QLineEdit(self.groupBox_physique_mastery_intelligence)
        self.lineEdit_physique.setGeometry(QtCore.QRect(129, 1, 21, 20))
        self.lineEdit_physique.setStyleSheet("background-color: rgb(235, 219, 219);")
        self.lineEdit_physique.setText("")
        self.lineEdit_physique.setObjectName("lineEdit_physique")
        self.label_physique = QtWidgets.QLabel(self.groupBox_physique_mastery_intelligence)
        self.label_physique.setGeometry(QtCore.QRect(39, 0, 81, 21))
        self.label_physique.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_physique.setObjectName("label_physique")
        self.comboBox_talent_2 = QtWidgets.QComboBox(self.groupBox_physique_mastery_intelligence)
        self.comboBox_talent_2.setGeometry(QtCore.QRect(0, 40, 171, 20))
        self.comboBox_talent_2.setObjectName("comboBox_talent_2")
        self.comboBox_talent_2.addItem("")
        self.comboBox_talent_2.setItemText(0, "")
        self.comboBox_talent_1 = QtWidgets.QComboBox(self.groupBox_physique_mastery_intelligence)
        self.comboBox_talent_1.setGeometry(QtCore.QRect(0, 21, 171, 20))
        self.comboBox_talent_1.setObjectName("comboBox_talent_1")
        self.comboBox_talent_1.addItem("")
        self.comboBox_talent_1.setItemText(0, "")
        self.radioButton_magic = QtWidgets.QRadioButton(self.groupBox_physique_mastery_intelligence)
        self.radioButton_magic.setGeometry(QtCore.QRect(0, 160, 51, 21))
        self.radioButton_magic.setObjectName("radioButton_magic")
        self.radioButton_might = QtWidgets.QRadioButton(self.groupBox_physique_mastery_intelligence)
        self.radioButton_might.setGeometry(QtCore.QRect(0, 60, 51, 21))
        self.radioButton_might.setObjectName("radioButton_might")
        self.pushButton_d20_mastery.raise_()
        self.comboBox_skill_1.raise_()
        self.pushButton_d20_skill_1.raise_()
        self.comboBox_skill_2.raise_()
        self.pushButton_d20_skill_2.raise_()
        self.comboBox_skill_3.raise_()
        self.pushButton_d20_skill_3.raise_()
        self.comboBox_skill_4.raise_()
        self.pushButton_d20_skill_4.raise_()
        self.comboBox_spell_1.raise_()
        self.pushButton_d20_intelligence.raise_()
        self.pushButton_d20_spell_1.raise_()
        self.pushButton_d20_spell_2.raise_()
        self.pushButton_d20_spell_3.raise_()
        self.pushButton_d20_spell_4.raise_()
        self.pushButton_d20_spell_5.raise_()
        self.comboBox_spell_2.raise_()
        self.comboBox_spell_3.raise_()
        self.comboBox_spell_4.raise_()
        self.comboBox_spell_5.raise_()
        self.label_mastery.raise_()
        self.label__intelligence.raise_()
        self.lineEdit_mastery.raise_()
        self.lineEdit_skill_1.raise_()
        self.lineEdit_skill_2.raise_()
        self.lineEdit_skill_3.raise_()
        self.lineEdit_skill_4.raise_()
        self.lineEdit_intelligence.raise_()
        self.lineEdit_spell_1.raise_()
        self.lineEdit_spell_2.raise_()
        self.lineEdit_spell_3.raise_()
        self.lineEdit_spell_4.raise_()
        self.lineEdit_spell_5.raise_()
        self.pushButton_d20_physique.raise_()
        self.label_physique.raise_()
        self.comboBox_talent_2.raise_()
        self.lineEdit_physique.raise_()
        self.comboBox_talent_1.raise_()
        self.radioButton_magic.raise_()
        self.radioButton_might.raise_()
        self.groupBox_weapons_battle = QtWidgets.QGroupBox(NPC_Widget)
        self.groupBox_weapons_battle.setGeometry(QtCore.QRect(190, 190, 171, 121))
        self.groupBox_weapons_battle.setTitle("")
        self.groupBox_weapons_battle.setObjectName("groupBox_weapons_battle")
        self.lineEdit_weapon2_armor_damage = QtWidgets.QLineEdit(self.groupBox_weapons_battle)
        self.lineEdit_weapon2_armor_damage.setGeometry(QtCore.QRect(110, 59, 21, 20))
        self.lineEdit_weapon2_armor_damage.setStyleSheet("background-color: rgb(186, 190, 202);")
        self.lineEdit_weapon2_armor_damage.setText("")
        self.lineEdit_weapon2_armor_damage.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_weapon2_armor_damage.setObjectName("lineEdit_weapon2_armor_damage")
        self.lineEdit_weapon2_penetration_damage = QtWidgets.QLineEdit(self.groupBox_weapons_battle)
        self.lineEdit_weapon2_penetration_damage.setGeometry(QtCore.QRect(130, 59, 21, 20))
        self.lineEdit_weapon2_penetration_damage.setStyleSheet("background-color: rgb(195, 166, 166);")
        self.lineEdit_weapon2_penetration_damage.setText("")
        self.lineEdit_weapon2_penetration_damage.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_weapon2_penetration_damage.setObjectName("lineEdit_weapon2_penetration_damage")
        self.lineEdit_weapon1_penetration_damage = QtWidgets.QLineEdit(self.groupBox_weapons_battle)
        self.lineEdit_weapon1_penetration_damage.setGeometry(QtCore.QRect(130, 20, 21, 21))
        self.lineEdit_weapon1_penetration_damage.setStyleSheet("background-color: rgb(195, 166, 166);")
        self.lineEdit_weapon1_penetration_damage.setText("")
        self.lineEdit_weapon1_penetration_damage.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_weapon1_penetration_damage.setObjectName("lineEdit_weapon1_penetration_damage")
        self.lineEdit_weapon1_health_damage = QtWidgets.QLineEdit(self.groupBox_weapons_battle)
        self.lineEdit_weapon1_health_damage.setGeometry(QtCore.QRect(150, 20, 21, 21))
        self.lineEdit_weapon1_health_damage.setStyleSheet("background-color: rgb(255, 199, 200);")
        self.lineEdit_weapon1_health_damage.setText("")
        self.lineEdit_weapon1_health_damage.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_weapon1_health_damage.setObjectName("lineEdit_weapon1_health_damage")
        self.lineEdit_weapon1_armor_damage = QtWidgets.QLineEdit(self.groupBox_weapons_battle)
        self.lineEdit_weapon1_armor_damage.setGeometry(QtCore.QRect(110, 20, 21, 21))
        self.lineEdit_weapon1_armor_damage.setStyleSheet("background-color: rgb(186, 190, 202);")
        self.lineEdit_weapon1_armor_damage.setText("")
        self.lineEdit_weapon1_armor_damage.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_weapon1_armor_damage.setObjectName("lineEdit_weapon1_armor_damage")
        self.comboBox_weapon_1 = QtWidgets.QComboBox(self.groupBox_weapons_battle)
        self.comboBox_weapon_1.setGeometry(QtCore.QRect(0, 20, 91, 21))
        self.comboBox_weapon_1.setStyleSheet("")
        self.comboBox_weapon_1.setObjectName("comboBox_weapon_1")
        self.comboBox_weapon_1.addItem("")
        self.comboBox_weapon_1.setItemText(0, "")
        self.comboBox_weapon_1.addItem("")
        self.lineEdit_weapon2_health_damage = QtWidgets.QLineEdit(self.groupBox_weapons_battle)
        self.lineEdit_weapon2_health_damage.setGeometry(QtCore.QRect(150, 59, 21, 20))
        self.lineEdit_weapon2_health_damage.setStyleSheet("background-color: rgb(255, 199, 200);")
        self.lineEdit_weapon2_health_damage.setText("")
        self.lineEdit_weapon2_health_damage.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_weapon2_health_damage.setObjectName("lineEdit_weapon2_health_damage")
        self.lineEdit_health = QtWidgets.QLineEdit(self.groupBox_weapons_battle)
        self.lineEdit_health.setGeometry(QtCore.QRect(40, 101, 20, 20))
        self.lineEdit_health.setStyleSheet("background-color: rgb(255, 199, 200);")
        self.lineEdit_health.setText("")
        self.lineEdit_health.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_health.setObjectName("lineEdit_health")
        self.lineEdit_armor = QtWidgets.QLineEdit(self.groupBox_weapons_battle)
        self.lineEdit_armor.setGeometry(QtCore.QRect(20, 101, 21, 20))
        self.lineEdit_armor.setStyleSheet("background-color: rgb(186, 190, 202);")
        self.lineEdit_armor.setText("")
        self.lineEdit_armor.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_armor.setObjectName("lineEdit_armor")
        self.lineEdit_magic_barrier = QtWidgets.QLineEdit(self.groupBox_weapons_battle)
        self.lineEdit_magic_barrier.setGeometry(QtCore.QRect(0, 101, 21, 20))
        self.lineEdit_magic_barrier.setAutoFillBackground(False)
        self.lineEdit_magic_barrier.setStyleSheet("background-color: rgb(190, 190, 255);")
        self.lineEdit_magic_barrier.setText("")
        self.lineEdit_magic_barrier.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_magic_barrier.setObjectName("lineEdit_magic_barrier")
        self.radioButton_defense = QtWidgets.QRadioButton(self.groupBox_weapons_battle)
        self.radioButton_defense.setGeometry(QtCore.QRect(70, 101, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_defense.setFont(font)
        self.radioButton_defense.setObjectName("radioButton_defense")
        self.pushButton_attack = QtWidgets.QPushButton(self.groupBox_weapons_battle)
        self.pushButton_attack.setGeometry(QtCore.QRect(130, 102, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_attack.setFont(font)
        self.pushButton_attack.setObjectName("pushButton_attack")
        self.comboBox_plate = QtWidgets.QComboBox(self.groupBox_weapons_battle)
        self.comboBox_plate.setGeometry(QtCore.QRect(0, 81, 171, 21))
        self.comboBox_plate.setStyleSheet("")
        self.comboBox_plate.setObjectName("comboBox_plate")
        self.comboBox_plate.addItem("")
        self.comboBox_plate.setItemText(0, "")
        self.lineEdit_weapon1_magic_damage = QtWidgets.QLineEdit(self.groupBox_weapons_battle)
        self.lineEdit_weapon1_magic_damage.setGeometry(QtCore.QRect(90, 20, 21, 21))
        self.lineEdit_weapon1_magic_damage.setStyleSheet("background-color: rgb(190, 190, 255);")
        self.lineEdit_weapon1_magic_damage.setText("")
        self.lineEdit_weapon1_magic_damage.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_weapon1_magic_damage.setObjectName("lineEdit_weapon1_magic_damage")
        self.lineEdit_weapon2_magic_damage = QtWidgets.QLineEdit(self.groupBox_weapons_battle)
        self.lineEdit_weapon2_magic_damage.setGeometry(QtCore.QRect(90, 59, 21, 20))
        self.lineEdit_weapon2_magic_damage.setStyleSheet("background-color: rgb(190, 190, 255);")
        self.lineEdit_weapon2_magic_damage.setText("")
        self.lineEdit_weapon2_magic_damage.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_weapon2_magic_damage.setObjectName("lineEdit_weapon2_magic_damage")
        self.comboBox_weapon_2 = QtWidgets.QComboBox(self.groupBox_weapons_battle)
        self.comboBox_weapon_2.setGeometry(QtCore.QRect(0, 59, 91, 20))
        self.comboBox_weapon_2.setStyleSheet("")
        self.comboBox_weapon_2.setObjectName("comboBox_weapon_2")
        self.comboBox_weapon_2.addItem("")
        self.comboBox_weapon_2.setItemText(0, "")
        self.comboBox_weapon_2.addItem("")
        self.lineEdit_weapon1 = QtWidgets.QLineEdit(self.groupBox_weapons_battle)
        self.lineEdit_weapon1.setGeometry(QtCore.QRect(0, 1, 171, 20))
        self.lineEdit_weapon1.setText("")
        self.lineEdit_weapon1.setObjectName("lineEdit_weapon1")
        self.lineEdit_weapon2 = QtWidgets.QLineEdit(self.groupBox_weapons_battle)
        self.lineEdit_weapon2.setGeometry(QtCore.QRect(0, 40, 171, 20))
        self.lineEdit_weapon2.setText("")
        self.lineEdit_weapon2.setObjectName("lineEdit_weapon2")
        self.comboBox_weapon_2.raise_()
        self.comboBox_weapon_1.raise_()
        self.lineEdit_weapon2_health_damage.raise_()
        self.lineEdit_weapon2_penetration_damage.raise_()
        self.lineEdit_weapon2_armor_damage.raise_()
        self.lineEdit_weapon2_magic_damage.raise_()
        self.lineEdit_weapon1_health_damage.raise_()
        self.lineEdit_weapon1_penetration_damage.raise_()
        self.lineEdit_weapon1_armor_damage.raise_()
        self.lineEdit_weapon1_magic_damage.raise_()
        self.lineEdit_health.raise_()
        self.lineEdit_armor.raise_()
        self.lineEdit_magic_barrier.raise_()
        self.radioButton_defense.raise_()
        self.pushButton_attack.raise_()
        self.lineEdit_weapon1.raise_()
        self.lineEdit_weapon2.raise_()
        self.comboBox_plate.raise_()
        self.lineEdit_name = QtWidgets.QLineEdit(NPC_Widget)
        self.lineEdit_name.setGeometry(QtCore.QRect(10, 7, 351, 21))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setToolTipDuration(1)
        self.lineEdit_name.setText("")
        self.lineEdit_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_name.setObjectName("lineEdit_name")

        self.retranslateUi(NPC_Widget)
        QtCore.QMetaObject.connectSlotsByName(NPC_Widget)

    def retranslateUi(self, NPC_Widget):
        _translate = QtCore.QCoreApplication.translate
        NPC_Widget.setWindowTitle(_translate("NPC_Widget", "Form"))
        self.label_periodic.setText(_translate("NPC_Widget", " ~~ periodic ~~"))
        self.pushButton_incoming_damage_enter.setText(_translate("NPC_Widget", "Damage"))
        self.radioButton_crit.setText(_translate("NPC_Widget", "Crit"))
        self.comboBox_trash_elite_legend.setItemText(1, _translate("NPC_Widget", "Trash"))
        self.comboBox_trash_elite_legend.setItemText(2, _translate("NPC_Widget", "Elite"))
        self.comboBox_trash_elite_legend.setItemText(3, _translate("NPC_Widget", "Legend"))
        self.comboBox_gender.setItemText(1, _translate("NPC_Widget", "Ж"))
        self.comboBox_gender.setItemText(2, _translate("NPC_Widget", "М"))
        self.comboBox_gender.setItemText(3, _translate("NPC_Widget", "Н"))
        self.pushButton_generation.setText(_translate("NPC_Widget", "Generate"))
        self.pushButton_load.setText(_translate("NPC_Widget", "Load"))
        self.pushButton_save.setText(_translate("NPC_Widget", "Save"))
        self.pushButton_info.setText(_translate("NPC_Widget", "Info"))
        self.pushButton_reset.setText(_translate("NPC_Widget", "Reset"))
        self.label_mastery.setText(_translate("NPC_Widget", "Мастерство"))
        self.label__intelligence.setText(_translate("NPC_Widget", "Интеллект"))
        self.label_physique.setText(_translate("NPC_Widget", "Телосложение"))
        self.radioButton_magic.setText(_translate("NPC_Widget", "Magic"))
        self.radioButton_might.setText(_translate("NPC_Widget", "Might"))
        self.comboBox_weapon_1.setItemText(1, _translate("NPC_Widget", "Занято"))
        self.radioButton_defense.setText(_translate("NPC_Widget", "Защита"))
        self.pushButton_attack.setText(_translate("NPC_Widget", "Attack"))
        self.comboBox_weapon_2.setItemText(1, _translate("NPC_Widget", "Занято"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NPC_Widget = QtWidgets.QWidget()
    ui = Ui_NPC_Widget()
    ui.setupUi(NPC_Widget)
    NPC_Widget.show()
    sys.exit(app.exec_())
