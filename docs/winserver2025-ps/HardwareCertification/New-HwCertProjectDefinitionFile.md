---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: microsoft.windows.kits.hardware.certification.management.dll-Help.xml
Module Name: HardwareCertification
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hardwarecertification/new-hwcertprojectdefinitionfile?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-HwCertProjectDefinitionFile
---

# New-HwCertProjectDefinitionFile

## 摘要
创建一个HCK项目定义文件。

## 语法

### PdefOverrides
```
New-HwCertProjectDefinitionFile [-ControllerName <String>] [-PdefFilePath <String>]
 [-TestCollectionFilePath <String>] [-EnableIsolateTargets] [-EnableMultiDeviceTest] [-OutputAutomatedPdef]
 [-ProjectName <String>] [-SkipTestStatus <String>] [-CrashDumpCollection <String>] [-MachineList <String[]>]
 [-MachinePool <String>] [-RunSystemTest] [-TestAllDevices] [-HwIdList <String[]>] [-DriverList <String[]>]
 [-ContainerIdList <String[]>] [-ClassIdList <String[]>] [<CommonParameters>]
```

### MachineList
```
New-HwCertProjectDefinitionFile [-ControllerName <String>] [-PdefFilePath <String>]
 [-TestCollectionFilePath <String>] [-EnableIsolateTargets] [-EnableMultiDeviceTest] [-OutputAutomatedPdef]
 [-ProjectName <String>] [-SkipTestStatus <String>] [-CrashDumpCollection <String>] -MachineList <String[]>
 [-RunSystemTest] [-TestAllDevices] [-HwIdList <String[]>] [-DriverList <String[]>]
 [-ContainerIdList <String[]>] [-ClassIdList <String[]>] [<CommonParameters>]
```

### MachinePool
```
New-HwCertProjectDefinitionFile [-ControllerName <String>] [-PdefFilePath <String>]
 [-TestCollectionFilePath <String>] [-EnableIsolateTargets] [-EnableMultiDeviceTest] [-OutputAutomatedPdef]
 [-ProjectName <String>] [-SkipTestStatus <String>] [-CrashDumpCollection <String>] -MachinePool <String>
 [-RunSystemTest] [-TestAllDevices] [-HwIdList <String[]>] [-DriverList <String[]>]
 [-ContainerIdList <String[]>] [-ClassIdList <String[]>] [<CommonParameters>]
```

## 描述
`New-HwCertProjectDefinitionFile` cmdlet 用于创建 Windows 硬件认证套件（HCK）的项目定义文件。该文件中包含了用于认证测试的目标对象（如设备或系统）。HCK 自动化工具会依据此文件中的设置来确定需要测试的目标对象。有关更多信息，请参阅 Microsoft 开发者网络 (MSDN) 文库中的 [Windows 硬件认证套件下载](https://go.microsoft.com/fwlink/?LinkId=614978)。

您可以通过添加任何符合项目定义文件模式的有效更改来更新这个生成的文件。

## 示例

### 示例 1：为驱动程序创建项目定义文件
```
PS C:\> New-HwCertProjectDefinitionFile -MachinePool "Test07" -DriverList "disk.sys"
```

这个命令用于创建一个项目定义文件。该命令会将所有在Test07池中可用的机器上的HCK目标值填充到项目中，其中disk.sys被视为一个设备驱动程序。

## 参数

### -ClassIdList
指定一个由类GUID字符串组成的数组。有关更多信息，请参阅TechNet库中的[Class-GUID](https://technet.microsoft.com/en-us/library/cc957340.aspx)。您可以使用逗号分隔的列表来表示这些类GUID。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: ClassList

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ContainerIdList
指定一个容器ID数组，这些ID采用GUID格式。可以使用逗号分隔的列表来表示这些ID。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: ContainerList

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerName
用于指定控制器或测试服务器的名称。项目定义文件会将控制器名称存储在\<ProjectDefinitionData\>元素的**Controller**属性中。如果您未提供控制器名称，也未指定**OutputAutomatedPdef**参数，该cmdlet将使用当前计算机作为默认设置。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CrashDumpCollection
指定为该项目生成和收集的 Windows 崩溃转储文件的类型。该参数的可接受值为：

- Mini
- Kernel
- Full
- Disable

Default value is Disable.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Mini, Kernel, Full, Disable

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DriverList
指定一组目标驱动程序的名称。可以使用逗号分隔的列表来进行输入。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableIsolateTargets
表示该cmdlet会为每个发现的目标创建一个单独的设备家族。如果您不指定此参数，cmdlet将根据设备类别将目标分组到相应的家族中。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableMultiDeviceTest
表示已启用多设备调度功能。项目定义文件在 `<MultiDeviceTestGroup>` 元素中存储了关于多设备调度的布尔值设置。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: EMDT

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HwIdList
指定一组目标设备的硬件ID数组。您可以使用逗号分隔的列表来表示这些ID。

您可以指定部分的硬件ID。该cmdlet会将部分值识别为硬件ID格式中的子字符串来进行匹配。比较过程使用ASCII字符，并且不区分大小写。如果ID中包含&符号，请将该ID用双引号（" "）括起来。在Windows PowerShell®中，&是一个保留字符。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MachineList
指定一个包含测试计算机名称的数组。可以使用逗号分隔的列表来输入这些名称。如果指定了多台计算机，那么所有这些计算机都必须属于同一个计算机池中。

```yaml
Type: String[]
Parameter Sets: PdefOverrides
Aliases: Machine

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: String[]
Parameter Sets: MachineList
Aliases: Machine

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MachinePool
指定一个现有机器池的名称，该机器池包含用于测试的计算机。

```yaml
Type: String
Parameter Sets: PdefOverrides
Aliases: Pool

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: String
Parameter Sets: MachinePool
Aliases: Pool

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OutputAutomatedPdef
表示该cmdlet会在项目定义文件中生成以下属性：

- **Controller** = "\[MACHINE\]"
- **TestCollectionReadLocation** = "\[FILTERED_TEST_COLLECTION\]"
- **Path** = "\[PACKAGES\]"

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: automate

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PdefFilePath
指定项目定义文件的名称。如果您未指定名称，该cmdlet会按照以下格式创建一个文件名：%UserProfile%\Desktop\PDEF_Files\PDEF_TimeDate\PDEF_OSPlatformName_TimeDate.xml。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProjectName
指定项目的友好名称。项目定义文件将项目名称存储在 `<Project>` 元素的 `Name` 属性中。如果您不指定名称，该 cmdlet 会生成一个包含时间戳的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: PROJ

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RunSystemTest
这表示该cmdlet指定了一个`TargetType`属性，其值为`System`。请使用此参数来测试整个系统。您不能使用其他查询类型来执行针对`System`的测试。

系统测试将目标设备视为一个独立的整体进行检测。这与“TestAllDevices”模式不同——后者虽然会测试系统中的所有设备，但会对每个设备分别进行处理。“TestAllDevices”参数用于选择是否对所有设备进行全面测试。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: System

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SkipTestStatus
指定测试调度时的跳过模式。项目定义文件将此值存储在 `<TestStatusToSkip>` 元素中。该参数的可接受值为：

- Pass
- Fail
- NoData

The default value is Pass.

```yaml
Type: String
Parameter Sets: (All)
Aliases: SkipStatus
Accepted values: Fail, NoData

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TestAllDevices
表示控制器会测试它发现的所有目标设备。控制器会在由 **MachineList** 或 **MachinePool** 参数指定的计算机上查找设备。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: AllDevices

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TestCollectionFilePath
指定测试集合.xml文件的完整路径。项目定义文件将该路径存储在\<Project\>元素的**TestCollectionReadLocation**属性中。如果您未指定路径，该cmdlet将使用空字符串。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[New-HwCertTestCollection](./New-HwCertTestCollection.md)

