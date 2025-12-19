---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterVPort.cmdletDefinition.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadaptervport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapterVPort
---

# Get-NetAdapterVPort

## 摘要
显示SR-IOV或VMQ VPort的网络适配器VPort设置。

## 语法

### 按名称排序（默认方式）
```
Get-NetAdapterVPort [[-Name] <String[]>] [-VPortID <UInt32[]>] [-SwitchID <UInt32[]>] [-FunctionID <UInt16[]>]
 [-PhysicalFunction] [-IncludeHidden] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ByInstanceID
```
Get-NetAdapterVPort -InterfaceDescription <String[]> [-VPortID <UInt32[]>] [-SwitchID <UInt32[]>]
 [-FunctionID <UInt16[]>] [-PhysicalFunction] [-IncludeHidden] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-NetAdapterVPort` cmdlet 可以显示单根 I/O 虚拟化（SR-IOV）或虚拟机队列（VMQ）相关的网络适配器虚拟端口（VPort）的设置信息。

如果没有指定 VPort，此 cmdlet 会显示网络适配器上的所有 VPort 的名称、编号和状态。

提供一个特定的VPort ID后，该特定的VPort会以长格式显示出来。

可选地，如果提供了虚拟功能ID，此cmdlet会显示SR-IOV虚拟功能的设置信息。

## 示例

### 示例 1：显示指定网络适配器上的所有虚拟端口（VPorts）
```
PS C:\> Get-NetAdapterVPort -Name "Ethernet 2"
```

此命令会显示名为“Ethernet 2”的网络适配器上的所有VPort（虚拟端口）。

### 示例 2：显示指定网络适配器的指定端口号的 VPort 摘要信息
```
PS C:\> Get-NetAdapterVPort -Name "Ethernet Connection 2" -VPortID 3
```

此命令会显示名为“Ethernet Connection 2”的网络适配器上VPort 3的VPort摘要信息。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行耗时较长的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job` cmdlets系列命令；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FunctionID
指定要显示为数组的 SR-IOV 虚拟函数设置的 ID。

```yaml
Type: UInt16[]
Parameter Sets: (All)
Aliases: VfID

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeHidden
表示该cmdlet在操作中会同时包含可见的网络适配器和隐藏的网络适配器。默认情况下，仅包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将会与所有（无论是隐藏的还是可见的）网络适配器进行匹配。

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

### -InterfaceDescription
指定一个网络适配器接口描述的数组。对于物理网络适配器来说，这通常是网络适配器的供应商名称后跟型号和描述，例如“Contoso 12345 千兆网络设备”。

```yaml
Type: String[]
Parameter Sets: ByInstanceID
Aliases: ifDesc, InstanceID

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定一个网络适配器名称数组。

```yaml
Type: String[]
Parameter Sets: ByName
Aliases: ifAlias, InterfaceAlias

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PhysicalFunction
指定该物理功能作为VPort的网络适配器。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: PF

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SwitchID
指定虚拟交换机的ID，以便识别一个或多个VPort所对应的网络适配器。

```yaml
Type: UInt32[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值为`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值（即并发操作的最大数量）。此限制仅适用于当前运行的cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VPortID
指定以长格式显示的虚拟交换机端口号。如果不提供此参数，则会显示所有V端口或指定的端口范围；如果指定了某个具体的V端口，那么仅该V端口会以长格式显示。

```yaml
Type: UInt32[]
Parameter Sets: (All)
Aliases: Id

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterVPortSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-NetAdapterSriov](./Get-NetAdapterSriov.md)

[Get-NetAdapterVmq](./Get-NetAdapterVmq.md)

