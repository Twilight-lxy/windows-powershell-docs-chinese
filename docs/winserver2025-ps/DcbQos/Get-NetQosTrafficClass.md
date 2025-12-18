---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetQosTrafficClass.cdxml-help.xml
Module Name: DcbQos
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/dcbqos/get-netqostrafficclass?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetQosTrafficClass
---

# Get-NetQosTrafficClass

## 摘要
获取流量类别设置信息。

## 语法

### 使用 IfAlias（默认设置）
```
Get-NetQosTrafficClass [[-Name] <String[]>] [[-InterfaceAlias] <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 作者：ByIfIndex
```
Get-NetQosTrafficClass [[-Name] <String[]>] [[-InterfaceIndex] <UInt32>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-NetQosTrafficClass` cmdlet 可以检索在 Windows Server® 2012 及更高版本中配置的网络流量类别。一个流量类别包含一种或多种类型的流量，每种流量类型都通过 IEEE 802.1p 优先级来区分。

有关流量类的更多信息，请参阅 **New-NetQosTrafficClass** cmdlet。

此 cmdlet 仅用于检索在 Windows Server 2012 及更高版本中配置的流量类别。这些流量类别并不一定会在计算机的网络适配器上按原样进行配置。要查看网络适配器上的流量类别配置，请运行 **Get-NetAdapterQos** cmdlet。

## 示例

### 示例 1：显示所有流量类别
```
PS C:\> Get-NetQosTrafficClass

Name                      Algorithm Bandwidth(%) Priority
----                      --------- ------------ --------
[Default]                 ETS       40           0-2,4-7
SMB                       ETS       60           3
```

这个命令会显示所有的流量类别。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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

### -InterfaceAlias
```yaml
Type: String
Parameter Sets: ByIfAlias
Aliases: IfAlias

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InterfaceIndex
```yaml
Type: UInt32
Parameter Sets: ByIfIndex
Aliases: IfIndex

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.UInt32

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetQosTrafficClassSettingData

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（#）后面的路径表示底层 WMI 对象的命名空间和类名。此 cmdlet 返回一个 **MSFT_NetQosTrafficClassSettingData** 对象，其中包含网络流量类别的相关信息。

## 备注

## 相关链接

[New-NetQosTrafficClass](./New-NetQosTrafficClass.md)

[Set-NetQosTrafficClass](./Set-NetQosTrafficClass.md)

