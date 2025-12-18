---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DASiteTableEntry.cdxml-help.xml
Module Name: DirectAccessClientComponents
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/directaccessclientcomponents/reset-daentrypointtableitem?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Reset-DAEntryPointTableItem
---

# 重置 DAEntryPointTableItem

## 摘要
将指定的 DirectAccess 入口点配置重置为默认配置。

## 语法

### ByPolicyStore（默认值）
```
Reset-DAEntryPointTableItem [-EntryPointName <String[]>] -PolicyStore <String> [-TeredoServerIP]
 [-IPHttpsProfile] [-GslbIP] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ByGpoSession
```
Reset-DAEntryPointTableItem [-EntryPointName <String[]>] -GPOSession <String> [-TeredoServerIP]
 [-IPHttpsProfile] [-GslbIP] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject（cdxml）
```
Reset-DAEntryPointTableItem -InputObject <CimInstance[]> [-TeredoServerIP] [-IPHttpsProfile] [-GslbIP]
 [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Reset-DA EntryPointTableItem` cmdlet 将由 `EntryPointName` 指定的入口点的配置重置为默认配置。您可以使用可选参数将特定的配置设置重置为默认值。

## 示例

#### 示例 1：重置入口点属性
```
PS C:\> Reset-DAEntryPointTableItem -GslbIP -EntryPointName "Paris" -PolicyStore "Contoso\GPO1"
```

此cmdlet将巴黎（Paris）入口点的GslbIP属性重置为“未配置”状态。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用该参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -EntryPointName
指定要修改的入口点的名称。入口点名称通常是该位置的友好名称，例如“Redmond”或“Paris”。

使用双引号（“”）来指定入口点的名称。

```yaml
Type: String[]
Parameter Sets: ByPolicyStore, ByGpoSession
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -GPOSession
指定用于发送配置信息的组策略会话。您可以使用 *GPOSession* 与 **NetGPO** 命令集，来汇总对某个组策略对象执行的多个操作。

*GPOSession* 不能与 **PolicyStore** 同时使用。

```yaml
Type: String
Parameter Sets: ByGpoSession
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -GslbIP
将指定网站的全局服务器负载均衡（GSLB）IP地址重置为未配置的状态。

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

### -IPHttpsProfile
将指定网站的 `IpHTTPsProfile` 属性重置为未配置的状态。有关 IPHTTPs 配置文件的更多信息，请参阅 **NetworkTransition** 模块中的 **NetIPHTTPsConfiguration** cmdlet。

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

### -InputObject
指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给此 cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PassThru
该cmdlet会将交互式窗口中的项目作为输入数据传递给其他cmdlet。默认情况下，此cmdlet不会生成任何输出结果。不过，若要将这些项目传递到其他cmdlet中，请先单击以选中这些项目，然后再点击“确定”。同时支持使用Shift键或Ctrl键进行选择操作。

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

### -PolicyStore
指定该 cmdlet 将入口点添加到的策略存储库。

要将入口点添加到组策略对象（Group Policy Object）中，请使用“Domain\GPOName”格式指定该GPO的名称。

要将入口点信息添加到计算机的本地组策略对象（GPO）中，请以“GPO:\<计算机名称\>”的格式指定该计算机的本地GPO名称。

*PolicyStore* 不能与 *GPOSession* 同时使用。

```yaml
Type: String
Parameter Sets: ByPolicyStore
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TeredoServerIP
将指定网站的 `TeredoServerIP` 属性重置为未配置的状态。

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

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/StandardCimv2/MSFT_DASiteTableEntry
此cmdlet接受一个CIM对象作为输入，该对象包含一个DA站点表条目。

## 输出

### 无

## 备注

## 相关链接

[Get-DAEntryPointTableItem](./Get-DA EntryPointTableItem.md)

[New-DAEntryPointTableItem](./New-DA EntryPointTableItem.md)

[Remove-DAEntryPointTableItem](./Remove-DAEntryPointTableItem.md)

[ Rename-DA EntryPointTableItem](./Rename-DAEntryPointTableItem.md)

[Set-DAEntryPointTableItem](./Set-DAEntryPointTableItem.md)

