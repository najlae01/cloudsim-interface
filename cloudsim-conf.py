#!/usr/bin/env python

import sys
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class DatacenterPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DatacenterPage, self).__init__(parent)

        ## The First Group
        dcSettingGroup = QtWidgets.QGroupBox("Datacenter Setting")

        #### Architecture
        archLabel = QtWidgets.QLabel("Architecture:")
        self.archCombo = QtWidgets.QComboBox()
        self.archCombo.addItem("X86")
        self.archCombo.addItem("Power")

        archLayout = QtWidgets.QHBoxLayout()
        archLayout.addWidget(archLabel)
        archLayout.addWidget(self.archCombo)

        #### Upper Threshold
        upperThrLabel = QtWidgets.QLabel("Upper Threshold:")
        self.upperThrSpinBox = QtWidgets.QDoubleSpinBox()
        self.upperThrSpinBox.setRange(0.0, 1.0)
        self.upperThrSpinBox.setSingleStep(0.01)
        self.upperThrSpinBox.setValue(0.8)

        upperThrLayout = QtWidgets.QHBoxLayout()
        upperThrLayout.addWidget(upperThrLabel)
        upperThrLayout.addWidget(self.upperThrSpinBox)

        #### Operating System

        osLabel = QtWidgets.QLabel("Operating System:")
        self.osCombo = QtWidgets.QComboBox()
        self.osCombo.addItem("Linux")
        self.osCombo.addItem("Windows")

        osLayout = QtWidgets.QHBoxLayout()
        osLayout.addWidget(osLabel)
        osLayout.addWidget(self.osCombo)

        #### Lower Threshold
        lowerThrLabel = QtWidgets.QLabel("Lower Threshold:")
        self.lowerThrSpinBox = QtWidgets.QDoubleSpinBox()
        self.lowerThrSpinBox.setRange(0.0, 1.0)
        self.lowerThrSpinBox.setSingleStep(0.01)
        self.lowerThrSpinBox.setValue(0.2)

        lowerThrLayout = QtWidgets.QHBoxLayout()
        lowerThrLayout.addWidget(lowerThrLabel)
        lowerThrLayout.addWidget(self.lowerThrSpinBox)

        #### Hypervisor
        hyperLabel = QtWidgets.QLabel("Hypervisor:")
        self.hyperCombo = QtWidgets.QComboBox()
        self.hyperCombo.addItem("Xen")
        self.hyperCombo.addItem("Kvm")

        hyperLayout = QtWidgets.QHBoxLayout()
        hyperLayout.addWidget(hyperLabel)
        hyperLayout.addWidget(self.hyperCombo)

        #### VM Migrations
        vmMigLabel = QtWidgets.QLabel("VM Migrations:")
        self.vmMigCombo = QtWidgets.QComboBox()
        self.vmMigCombo.addItem("Enabled")
        self.vmMigCombo.addItem("Disabled")

        vmMigLayout = QtWidgets.QHBoxLayout()
        vmMigLayout.addWidget(vmMigLabel)
        vmMigLayout.addWidget(self.vmMigCombo)

        #### Sheduling Interval
        shedulingIntervalLabel = QtWidgets.QLabel("Sheduling Interval")
        self.shedulingIntervalSpinBox = QtWidgets.QSpinBox()
        self.shedulingIntervalSpinBox.setRange(300, 600)
        self.shedulingIntervalSpinBox.setSingleStep(300300300)
        self.shedulingIntervalSpinBox.setValue(300)

        shedulingIntervalLayout = QtWidgets.QHBoxLayout()
        shedulingIntervalLayout.addWidget(shedulingIntervalLabel)
        shedulingIntervalLayout.addWidget(self.shedulingIntervalSpinBox)

        #### workload
        workloadLabel = QtWidgets.QLabel("WorkLoad:")
        self.workloadCombo = QtWidgets.QComboBox()
        self.workloadCombo.addItem("20110303")
        self.workloadCombo.addItem("20110306")
        self.workloadCombo.addItem("20110309")
        self.workloadCombo.addItem("20110322")
        self.workloadCombo.addItem("20110325")
        self.workloadCombo.addItem("20110403")
        self.workloadCombo.addItem("20110409")
        self.workloadCombo.addItem("20110411")
        self.workloadCombo.addItem("20110412")
        self.workloadCombo.addItem("20110420")

        workloadLayout = QtWidgets.QHBoxLayout()
        workloadLayout.addWidget(workloadLabel)
        workloadLayout.addWidget(self.workloadCombo)

        #### processing cost

        processCostLabel = QtWidgets.QLabel("Processing Cost(per sec):")
        self.processCostSpinBox = QtWidgets.QDoubleSpinBox()
        # self.processCostSpinBox.setMinimum(0.0)
        self.processCostSpinBox.setRange(0.0, 100.0)
        self.processCostSpinBox.setSingleStep(0.1)
        self.processCostSpinBox.setValue(0.1)

        processCostLayout = QtWidgets.QHBoxLayout()
        processCostLayout.addWidget(processCostLabel)
        processCostLayout.addWidget(self.processCostSpinBox)
        #### memory cost
        memoryCostLabel = QtWidgets.QLabel("Memory Cost(per MB):")
        self.memoryCostSpinBox = QtWidgets.QDoubleSpinBox()
        # self.memoryCostSpinBox.setMinimum(0.0)
        self.memoryCostSpinBox.setRange(0.0, 100.0)
        self.memoryCostSpinBox.setSingleStep(0.01)
        self.memoryCostSpinBox.setValue(0.05)

        memoryCostLayout = QtWidgets.QHBoxLayout()
        memoryCostLayout.addWidget(memoryCostLabel)
        memoryCostLayout.addWidget(self.memoryCostSpinBox)
        #### storage cost
        storageCostLabel = QtWidgets.QLabel("Storage Cost(per MB):")
        self.storageCostSpinBox = QtWidgets.QDoubleSpinBox()
        # self.storageCostSpinBox.setMinimum(0.0)
        self.storageCostSpinBox.setRange(0.0, 100.0)
        self.storageCostSpinBox.setSingleStep(0.01)
        self.storageCostSpinBox.setValue(0.01)

        storageCostLayout = QtWidgets.QHBoxLayout()
        storageCostLayout.addWidget(storageCostLabel)
        storageCostLayout.addWidget(self.storageCostSpinBox)
        #### bandwidth cost
        bandwidthCostLabel = QtWidgets.QLabel("Bandwidth Cost(per MB):")
        self.bandwidthCostSpinBox = QtWidgets.QDoubleSpinBox()
        # self.bandwidthCostSpinBox.setMinimum(0.0)
        self.bandwidthCostSpinBox.setRange(0.0, 100.0)
        self.bandwidthCostSpinBox.setSingleStep(0.1)
        self.bandwidthCostSpinBox.setValue(0.1)

        bandwidthCostLayout = QtWidgets.QHBoxLayout()
        bandwidthCostLayout.addWidget(bandwidthCostLabel)
        bandwidthCostLayout.addWidget(self.bandwidthCostSpinBox)
        ### The dcSetting GridLayout
        dcSettingLayout = QtWidgets.QGridLayout()
        dcSettingLayout.addLayout(archLayout, 0, 0)
        dcSettingLayout.addLayout(upperThrLayout, 0, 1)
        dcSettingLayout.addLayout(osLayout, 1, 0)
        dcSettingLayout.addLayout(lowerThrLayout, 1, 1)
        dcSettingLayout.addLayout(hyperLayout, 2, 0)
        dcSettingLayout.addLayout(vmMigLayout, 2, 1)
        dcSettingLayout.addLayout(shedulingIntervalLayout, 3, 0)
        dcSettingLayout.addLayout(workloadLayout, 3, 1)
        dcSettingLayout.addLayout(processCostLayout, 4, 0)
        dcSettingLayout.addLayout(memoryCostLayout, 4, 1)
        dcSettingLayout.addLayout(storageCostLayout, 5, 0)
        dcSettingLayout.addLayout(bandwidthCostLayout, 5, 1)

        dcSettingGroup.setLayout(dcSettingLayout)

        ## The Second Group
        dcInfoGroup = QtWidgets.QGroupBox("General Information")
        hostLabel = QtWidgets.QLabel("<i>Number of hosts:</i>")
        vmLabel = QtWidgets.QLabel("<i>Number of virtual machines:<i>")
        self.numHostLabel = QtWidgets.QLabel("")
        self.numVmLabel = QtWidgets.QLabel("")

        infoLayout = QtWidgets.QGridLayout()
        infoLayout.addWidget(hostLabel, 0, 0)
        infoLayout.addWidget(self.numHostLabel, 0, 1)
        infoLayout.addWidget(vmLabel, 1, 0)
        infoLayout.addWidget(self.numVmLabel, 1, 1)

        dcInfoGroup.setLayout(infoLayout)

        ## The main layout
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(dcSettingGroup)
        mainLayout.addSpacing(20)
        mainLayout.addStretch(1)
        mainLayout.addWidget(dcInfoGroup)

        self.setLayout(mainLayout)

    def save(self):
        self.archCombo.currentText()


class HostPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(HostPage, self).__init__(parent)
        ## First Group
        hostSettingGroup = QtWidgets.QGroupBox("Host Setting")

        numOfHostLabel = QtWidgets.QLabel("Number of Hosts:")
        self.numOfHostSpinBox = QtWidgets.QSpinBox()
        self.numOfHostSpinBox.setRange(1, 1500)
        self.numOfHostSpinBox.setSingleStep(1)
        self.numOfHostSpinBox.setValue(800)
        self.numOfHostSpinBox.valueChanged.connect(self.updateHostInfoGroup)

        vmSchedulingLabel = QtWidgets.QLabel("Virtual Machine Scheduling:")
        self.vmSchedulingCombo = QtWidgets.QComboBox()
        self.vmSchedulingCombo.addItem("Time Shared")
        self.vmSchedulingCombo.addItem("Space Shared")

        powerModelLabel = QtWidgets.QLabel("Power Model:")
        self.powerModelCombo = QtWidgets.QComboBox()
        self.powerModelCombo.addItem("Spec Power")
        self.powerModelCombo.addItem("Linear")
        self.powerModelCombo.addItem("Square root")
        self.powerModelCombo.addItem("Square")
        self.powerModelCombo.addItem("Clubic")

        ramProvisionerLabel = QtWidgets.QLabel("RAM Provisioner:")
        self.ramProvisionerCombo = QtWidgets.QComboBox()
        self.ramProvisionerCombo.addItem("Dynamic")
        self.ramProvisionerCombo.addItem("Simple")

        bandwidthProvisionerLabel = QtWidgets.QLabel("Bandwidth Provisioner:")
        self.bandwidthProvisionerCombo = QtWidgets.QComboBox()
        self.bandwidthProvisionerCombo.addItem("Simple")
        self.bandwidthProvisionerCombo.addItem("Dynamic")

        peProvisionerLabel = QtWidgets.QLabel("PE Provisioner:")
        self.peProvisionerCombo = QtWidgets.QComboBox()
        self.peProvisionerCombo.addItem("Simple")
        self.peProvisionerCombo.addItem("Dynamic")

        hostSettingLayout = QtWidgets.QGridLayout()
        hostSettingLayout.addWidget(numOfHostLabel, 0, 0)
        hostSettingLayout.addWidget(self.numOfHostSpinBox, 0, 1)
        hostSettingLayout.addWidget(vmSchedulingLabel, 1, 0)
        hostSettingLayout.addWidget(self.vmSchedulingCombo, 1, 1)
        hostSettingLayout.addWidget(powerModelLabel, 2, 0)
        hostSettingLayout.addWidget(self.powerModelCombo, 2, 1)
        hostSettingLayout.addWidget(ramProvisionerLabel, 3, 0)
        hostSettingLayout.addWidget(self.ramProvisionerCombo, 3, 1)
        hostSettingLayout.addWidget(bandwidthProvisionerLabel, 4, 0)
        hostSettingLayout.addWidget(self.bandwidthProvisionerCombo, 4, 1)
        hostSettingLayout.addWidget(peProvisionerLabel, 5, 0)
        hostSettingLayout.addWidget(self.peProvisionerCombo, 5, 1)

        hostSettingGroup.setLayout(hostSettingLayout)

        # Second Group

        hostInfoGroup = QtWidgets.QGroupBox("Information")

        num = self.numOfHostSpinBox.value() / 2
        numberLabel = QtWidgets.QLabel("<b>The Numbers of Hosts</b>")
        describeLabel = QtWidgets.QLabel("<b>Description</b>")
        type1Label = QtWidgets.QLabel(
            "HP ProLiant ML110 G4 (1 x [Xeon 3040 1860 MHz, 2 cores], 4GB)"
        )
        type2Label = QtWidgets.QLabel(
            "HP ProLiant ML110 G5 (1 x [Xeon 3075 2660 MHz, 2 cores], 4GB)"
        )

        self.num1Label = QtWidgets.QLabel(str(num))
        self.num2Label = QtWidgets.QLabel(str(num))

        hostInfoLayout = QtWidgets.QGridLayout()
        hostInfoLayout.addWidget(numberLabel, 0, 0)
        hostInfoLayout.addWidget(describeLabel, 0, 1)
        hostInfoLayout.addWidget(self.num1Label, 1, 0)
        hostInfoLayout.addWidget(type1Label, 1, 1)
        hostInfoLayout.addWidget(self.num2Label, 2, 0)
        hostInfoLayout.addWidget(type2Label, 2, 1)

        hostInfoGroup.setLayout(hostInfoLayout)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(hostSettingGroup)
        mainLayout.addSpacing(20)
        mainLayout.addStretch(1)
        mainLayout.addWidget(hostInfoGroup)

        self.setLayout(mainLayout)

    def updateHostInfoGroup(self):
        num = self.numOfHostSpinBox.value() / 2
        extra = self.numOfHostSpinBox.value() % 2
        num1 = num2 = num

        if extra == 1:
            num1 = num + 1

        self.num1Label.setText(str(num1))
        self.num2Label.setText(str(num2))


class VMPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(VMPage, self).__init__(parent)

        ## The First Group
        vmSettingGroup = QtWidgets.QGroupBox("Virtual Machine Setting")

        numOfVMLabel = QtWidgets.QLabel("Number of Virtual Machines:")
        self.numOfVMSpinBox = QtWidgets.QSpinBox()
        #        self.numOfVMSpinBox.setMinimum(1)
        self.numOfVMSpinBox.setRange(1, 2000)
        self.numOfVMSpinBox.setSingleStep(1)
        self.numOfVMSpinBox.setValue(1500)
        self.numOfVMSpinBox.valueChanged.connect(self.updateVmInfoGroup)

        numOfVMLayout = QtWidgets.QHBoxLayout()
        numOfVMLayout.addWidget(numOfVMLabel)
        numOfVMLayout.addWidget(self.numOfVMSpinBox)

        vmSettingLayout = QtWidgets.QVBoxLayout()
        vmSettingLayout.addLayout(numOfVMLayout)

        vmSettingGroup.setLayout(vmSettingLayout)

        ## The Second Group
        vmInfoGroup = QtWidgets.QGroupBox("Information")

        num = self.numOfVMSpinBox.value() / 4
        num1 = num2 = num3 = num4 = num
        numberLabel = QtWidgets.QLabel("<b>The Numbers of VMs</b>")
        describeLabel = QtWidgets.QLabel("<b>Description</b>")
        type1Label = QtWidgets.QLabel(
            "High-CPU Medium Instance: 2.5 EC2 Compute Units, 0.85 GB"
        )
        type2Label = QtWidgets.QLabel("Large Instance: 2 EC2 Compute Units, 3.75 GB")
        type3Label = QtWidgets.QLabel("Small Instance: 1 EC2 Compute Unit, 1.7 GB")
        type4Label = QtWidgets.QLabel("Micro Instance: 0.5 EC2 Compute Unit, 0.633 GB")

        self.num1Label = QtWidgets.QLabel(str(num1))
        self.num2Label = QtWidgets.QLabel(str(num2))
        self.num3Label = QtWidgets.QLabel(str(num3))
        self.num4Label = QtWidgets.QLabel(str(num4))

        vmInfoLayout = QtWidgets.QGridLayout()
        vmInfoLayout.addWidget(numberLabel, 0, 0)
        vmInfoLayout.addWidget(describeLabel, 0, 1)
        vmInfoLayout.addWidget(self.num1Label, 1, 0)
        vmInfoLayout.addWidget(type1Label, 1, 1)
        vmInfoLayout.addWidget(self.num2Label, 2, 0)
        vmInfoLayout.addWidget(type2Label, 2, 1)
        vmInfoLayout.addWidget(self.num3Label, 3, 0)
        vmInfoLayout.addWidget(type3Label, 3, 1)
        vmInfoLayout.addWidget(self.num4Label, 4, 0)
        vmInfoLayout.addWidget(type4Label, 4, 1)

        vmInfoGroup.setLayout(vmInfoLayout)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(vmSettingGroup)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(30)
        mainLayout.addWidget(vmInfoGroup)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)

    def updateVmInfoGroup(self):
        num = self.numOfVMSpinBox.value() / 4
        extra = self.numOfVMSpinBox.value() % 4
        num1 = num2 = num3 = num4 = num

        if extra == 3:
            num1 = num + 1
            num2 = num + 1
            num3 = num + 1
        elif extra == 2:
            num1 = num + 1
            num2 = num + 1
        elif extra == 1:
            num1 = num + 1

        self.num1Label.setText(str(num1))
        self.num2Label.setText(str(num2))
        self.num3Label.setText(str(num3))
        self.num4Label.setText(str(num4))


class PolicyPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PolicyPage, self).__init__(parent)

        ## First Group
        keySettingGroup = QtWidgets.QGroupBox("Key Policy Setting")

        vmAllocationLabel = QtWidgets.QLabel("Virtual Machine Allocation Policy:")
        self.vmAllocationComboBox = QtWidgets.QComboBox()
        self.vmAllocationComboBox.addItem("IQR")
        self.vmAllocationComboBox.addItem("MAD")
        self.vmAllocationComboBox.addItem("LR")
        self.vmAllocationComboBox.addItem("LRR")
        self.vmAllocationComboBox.addItem("THR")
        self.vmAllocationComboBox.addItem("DVFS")
        self.vmAllocationComboBox.addItem("NPA")

        vmAllocationInfoButton = QtWidgets.QPushButton()
        vmAllocationInfoButton.setIcon(QtGui.QIcon("./images/info.png"))
        vmAllocationInfoButton.setFlat(True)
        vmAllocationInfoButton.clicked.connect(self.vmAllocationMsgBox)

        vmSelectionLabel = QtWidgets.QLabel("Virtual Machine Selection Policy:")
        self.vmSelectionComboBox = QtWidgets.QComboBox()
        self.vmSelectionComboBox.addItem("MC")
        self.vmSelectionComboBox.addItem("MMT")
        self.vmSelectionComboBox.addItem("MU")
        self.vmSelectionComboBox.addItem("RS")
        self.vmSelectionComboBox.addItem("NPA")

        vmSelectionInfoButton = QtWidgets.QPushButton()
        vmSelectionInfoButton.setIcon(QtGui.QIcon("./images/info.png"))
        vmSelectionInfoButton.setFlat(True)
        vmSelectionInfoButton.clicked.connect(self.vmSelectionMsgBox)

        parameterLabel = QtWidgets.QLabel("Parameter:")
        self.parameterEdit = QtWidgets.QLineEdit()

        keySettingLayout = QtWidgets.QGridLayout()
        keySettingLayout.addWidget(vmAllocationLabel, 0, 0)
        keySettingLayout.addWidget(self.vmAllocationComboBox, 0, 1)
        keySettingLayout.addWidget(vmAllocationInfoButton, 0, 2)
        keySettingLayout.addWidget(vmSelectionLabel, 1, 0)
        keySettingLayout.addWidget(self.vmSelectionComboBox, 1, 1)
        keySettingLayout.addWidget(vmSelectionInfoButton, 1, 2)
        keySettingLayout.addWidget(parameterLabel, 2, 0)
        keySettingLayout.addWidget(self.parameterEdit, 2, 1)

        keySettingGroup.setLayout(keySettingLayout)

        ## Second Group
        generalSettingGroup = QtWidgets.QGroupBox("General Setting")

        outputFolderLabel = QtWidgets.QLabel("Output Folder:")
        self.outputFolderEdit = QtWidgets.QLineEdit()
        self.outputFolderEdit.setText("output_test")

        self.outputToFile = QtWidgets.QCheckBox("Output to Files")

        generalLayout = QtWidgets.QGridLayout()
        generalLayout.addWidget(outputFolderLabel, 0, 0)
        generalLayout.addWidget(self.outputFolderEdit, 0, 1)
        generalLayout.addWidget(self.outputToFile, 1, 0, 1, 2)

        generalSettingGroup.setLayout(generalLayout)

        ## Third Information

        policyInfoGroup = QtWidgets.QGroupBox("Information")

        policyInfo1Label = QtWidgets.QLabel(
            "<i>Output Folder</i> : Where the result are placed"
        )
        policyInfo2Label = QtWidgets.QLabel(
            "<i>Output To Files</i> : Indicate whether"
            "the result are output to some csv files"
        )
        policyInfo3Label = QtWidgets.QLabel(
            "<i>Parameter</i> : The value of the Parameter"
            "depends the details of the policy "
        )

        policyInfoLayout = QtWidgets.QGridLayout()

        policyInfoLayout.addWidget(policyInfo1Label)
        policyInfoLayout.addWidget(policyInfo2Label)
        policyInfoLayout.addWidget(policyInfo3Label)

        policyInfoGroup.setLayout(policyInfoLayout)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(keySettingGroup)
        mainLayout.addSpacing(20)
        mainLayout.addWidget(generalSettingGroup)
        mainLayout.addSpacing(20)
        mainLayout.addWidget(policyInfoGroup)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)

    def vmAllocationMsgBox(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Virtual Machine Allocation Policy")
        msgBox.setText(
            "<b>The document has been modified.</b><br>"
            "<hr>the second para<br>"
            "<hr>the second para"
        )
        msgBox.setIcon(1)
        msgBox.exec_()

    def vmSelectionMsgBox(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Virtual Machine Selection Policy")
        msgBox.setText(
            "<b>The document has been modified.</b><br>"
            "<hr>the second para<br>"
            "<hr>the second para"
        )
        msgBox.setIcon(1)
        msgBox.exec_()


class ConfigDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ConfigDialog, self).__init__()

        self.parent = parent
        self.contentsWidget = QtWidgets.QListWidget()
        self.contentsWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.contentsWidget.setIconSize(QtCore.QSize(80, 66))
        self.contentsWidget.setMovement(QtWidgets.QListView.Static)
        self.contentsWidget.setMaximumWidth(128)
        self.contentsWidget.setSpacing(12)

        self.pagesWidget = QtWidgets.QStackedWidget()
        self.pagesWidget.addWidget(DatacenterPage())
        self.pagesWidget.addWidget(HostPage())
        self.pagesWidget.addWidget(VMPage())
        self.pagesWidget.addWidget(PolicyPage())

        self.pagesWidget.widget(1).numOfHostSpinBox.valueChanged.connect(
            self.updateInfoGroup
        )
        self.pagesWidget.widget(2).numOfVMSpinBox.valueChanged.connect(
            self.updateInfoGroup
        )

        closeButton = QtWidgets.QPushButton("Close")

        saveAsButton = QtWidgets.QPushButton("Save As")

        self.createIcons()
        self.contentsWidget.setCurrentRow(0)

        closeButton.clicked.connect(self.parent.close)
        saveAsButton.clicked.connect(self.saveAs)

        horizontalLayout = QtWidgets.QHBoxLayout()
        #    horizontalLayout.addWidget(self.contentsWidget)
        horizontalLayout.addWidget(self.pagesWidget, 1)

        buttonsLayout = QtWidgets.QHBoxLayout()
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(saveAsButton)
        buttonsLayout.addWidget(closeButton)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addLayout(horizontalLayout)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(12)
        mainLayout.addLayout(buttonsLayout)

        self.updateInfoGroup()
        self.setLayout(mainLayout)

        #self.contentsWidget.itemClicked.connect(self.handleItemClick)

    def updateInfoGroup(self):
        numHost = self.pagesWidget.widget(1).numOfHostSpinBox.value()
        numVm = self.pagesWidget.widget(2).numOfVMSpinBox.value()
        self.pagesWidget.widget(0).numHostLabel.setText(str(numHost))
        self.pagesWidget.widget(0).numVmLabel.setText(str(numVm))

    def getConfFilename(self):
        workload = self.pagesWidget.widget(0).workloadCombo.currentText()
        vmAllocation = self.pagesWidget.widget(3).vmAllocationComboBox.currentText()
        vmSelection = self.pagesWidget.widget(3).vmSelectionComboBox.currentText()
        param = self.pagesWidget.widget(3).parameterEdit.text()

        return workload + "_" + vmAllocation + "_" + vmSelection + "_" + param + ".ini"

    def writeDatacenter(self, f):
        dc = self.pagesWidget.widget(0)
        f.write("\nArchitecture=" + dc.archCombo.currentText())
        f.write("\nUpperThreshold=" + str(dc.upperThrSpinBox.value()))
        f.write("\nOperateSystem=" + dc.osCombo.currentText())
        f.write("\nLowerThreshold=" + str(dc.lowerThrSpinBox.value()))
        f.write("\nHypervisor=" + dc.hyperCombo.currentText())
        f.write("\nVMMigrations=" + dc.vmMigCombo.currentText())
        f.write("\nShedulingInterval=" + str(dc.shedulingIntervalSpinBox.value()))
        f.write("\nWorkload=" + dc.workloadCombo.currentText())
        f.write("\nProcessCost=" + str(dc.processCostSpinBox.value()))
        f.write("\nMemoryCost=" + str(dc.memoryCostSpinBox.value()))
        f.write("\nStorageCost=" + str(dc.storageCostSpinBox.value()))
        f.write("\nBandwidthCost=" + str(dc.bandwidthCostSpinBox.value()))

    def writeHost(self, f):
        host = self.pagesWidget.widget(1)
        f.write("\nNumOfHosts=" + str(host.numOfHostSpinBox.value()))
        f.write("\nVMScheduling=" + host.vmSchedulingCombo.currentText())
        f.write("\nPowerModel=" + host.powerModelCombo.currentText())
        f.write("\nRAMProvisioner=" + host.ramProvisionerCombo.currentText())
        f.write(
            "\nBandwidthProvisioner=" + host.bandwidthProvisionerCombo.currentText()
        )
        f.write("\nPeProvisioner=" + host.peProvisionerCombo.currentText())

    def writeVM(self, f):
        vm = self.pagesWidget.widget(2)
        f.write("\nNumOfVMs=" + str(vm.numOfVMSpinBox.value()))

    def writePolicy(self, f):
        policy = self.pagesWidget.widget(3)

        f.write("\nVmAllocationPolicy=" + policy.vmAllocationComboBox.currentText())
        f.write("\nVmSelectionPolicy=" + policy.vmSelectionComboBox.currentText())
        f.write("\nParameter=" + policy.parameterEdit.text())
        f.write("\nOutputFolder=" + policy.outputFolderEdit.text())
        if policy.outputToFile.isChecked():
            f.write("\nOutputToFile=True")
        else:
            f.write("\nOutputToFile=False")

    def saveAs(self):
        date = QDateTime.currentDateTime().toString()
        self.getConfFilename()

        fname = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save IAAS CloudSim Configure File", self.getConfFilename()
        )

        if fname.isNull():
            return 0

        f = open(fname, "w+")
        f.write("# Configure File For IAAS CloudSim")
        f.write("\n#      Date: " + date)
        f.write("\n#      Author: wanglong(wanglong@l-cloud.org)")
        f.write("\n\n# Datacenter Setting")
        self.writeDatacenter(f)
        f.write("\n\n# Host Setting")
        self.writeHost(f)
        f.write("\n\n# Virtual Machine Setting")
        self.writeVM(f)
        f.write("\n\n# Policy Setting")
        self.writePolicy(f)
        f.write("\n")
        f.close()

        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Save Configuue File...")
        msgBox.setText("The Configure File Saved As:<br> <b><i>" + fname + "</i></b>")
        msgBox.setIcon(1)
        msgBox.exec_()

    def changePage(self, current, previous):
        if not current:
            current = previous

        self.pagesWidget.setCurrentIndex(self.contentsWidget.row(current))

    def createIcons(self):
        datacenterButton = QtWidgets.QListWidgetItem(self.contentsWidget)
        datacenterButton.setIcon(QtGui.QIcon("./images/datacenter.png"))
        datacenterButton.setText("Data Center")
        datacenterButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        datacenterButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)


        hostButton = QtWidgets.QListWidgetItem(self.contentsWidget)
        hostButton.setIcon(QtGui.QIcon("./images/config.png"))
        hostButton.setText("Host")
        hostButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        hostButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        vmButton = QtWidgets.QListWidgetItem(self.contentsWidget)
        vmButton.setIcon(QtGui.QIcon("./images/update.png"))
        vmButton.setText("VM")
        vmButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        vmButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        policyButton = QtWidgets.QListWidgetItem(self.contentsWidget)
        policyButton.setIcon(QtGui.QIcon("./images/query.png"))
        policyButton.setText("Policy")
        policyButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        policyButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.contentsWidget.currentItemChanged.connect(self.changePage)


class CloudConf(QtWidgets.QMainWindow):
    def __init__(self):
        super(CloudConf, self).__init__()

        self.initUI()

    def save(self):
        self.centralWidget().saveAs()

    def configure_datacenter(self):
        print("datacenter")
        self.centralWidget().contentsWidget.setCurrentRow(0)

    def configure_host(self):
        print("host")
        self.centralWidget().contentsWidget.setCurrentRow(1)

    def configure_vm(self):
        print("virtual machine")
        self.centralWidget().contentsWidget.setCurrentRow(2)

    def configure_policy(self):
        print("policy")
        self.centralWidget().contentsWidget.setCurrentRow(3)

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        self.mainWidget = ConfigDialog(self)
        self.setCentralWidget(self.mainWidget)

        self.exitAction = QtWidgets.QAction(
            QtGui.QIcon("./images/exit.png"), "&Exit", self
        )
        self.exitAction.setShortcut("Ctrl+Q")
        self.exitAction.setStatusTip("Exit application")
        self.exitAction.triggered.connect(self.close)

        self.saveAction = QtWidgets.QAction(
            QtGui.QIcon("./images/save.png"), "&Save", self
        )
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.setStatusTip("Save Configuration")
        self.saveAction.triggered.connect(self.save)

        self.showDatacenterAction = QtWidgets.QAction(
            QtGui.QIcon("./images/datacenter.png"), "&Data Center", self
        )
        self.showDatacenterAction.setStatusTip("Show Datacenter Configuration")
        self.showDatacenterAction.setShortcut("Ctrl+D")
        self.showDatacenterAction.triggered.connect(self.configure_datacenter)

        self.showHostAction = QtWidgets.QAction(
            QtGui.QIcon("./images/host.png"), "&Host", self
        )
        self.showHostAction.setStatusTip("Show Host Configuration")
        self.showHostAction.setShortcut("Ctrl+H")
        self.showHostAction.triggered.connect(self.configure_host)

        self.showVMAction = QtWidgets.QAction(
            QtGui.QIcon("./images/vm.png"), "&VM", self
        )
        self.showVMAction.setStatusTip("Show Virtual Machine Configuration")
        self.showVMAction.setShortcut("Ctrl+M")
        self.showVMAction.triggered.connect(self.configure_vm)

        self.showPolicyAction = QtWidgets.QAction(
            QtGui.QIcon("./images/policy.png"), "&Policy", self
        )
        self.showPolicyAction.setStatusTip("Show Policy Configuration")
        self.showPolicyAction.setShortcut("Ctrl+P")
        self.showPolicyAction.triggered.connect(self.configure_policy)

        self.mainMenuBar = self.menuBar()
        self.fileMenu = self.mainMenuBar.addMenu("&File")
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.exitAction)

        self.confMenu = self.mainMenuBar.addMenu("&Configure")
        self.confMenu.addAction(self.showDatacenterAction)
        self.confMenu.addAction(self.showHostAction)
        self.confMenu.addAction(self.showVMAction)
        self.confMenu.addAction(self.showPolicyAction)

        self.toolbar = self.addToolBar("File")
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolbar.setIconSize(QtCore.QSize(36, 36))
        self.toolbar.addAction(self.saveAction)

        self.toolbar = self.addToolBar("Configure")
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolbar.setIconSize(QtCore.QSize(36, 36))
        self.toolbar.addAction(self.showDatacenterAction)
        self.toolbar.addAction(self.showHostAction)
        self.toolbar.addAction(self.showVMAction)
        self.toolbar.addAction(self.showPolicyAction)

        self.toolbar = self.addToolBar("Exit")
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolbar.setIconSize(QtCore.QSize(36, 36))
        self.toolbar.addAction(self.exitAction)
        #        self.statusBar().showMessage('Ready')

        self.resize(1000, 600)
        self.center()
        self.setWindowIcon(QtGui.QIcon("./images/icon.png"))
        self.setWindowTitle("CloudSim")
        self.show()
        self.saveAction.triggered.connect(
            self.save
        )  # Use self.saveAction.triggered.connect



def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = CloudConf()
    sys.exit(app.exec_())



main()