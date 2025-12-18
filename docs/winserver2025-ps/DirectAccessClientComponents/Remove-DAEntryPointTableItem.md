---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DASiteTableEntry.cdxml-help.xml
Module Name: DirectAccessClientComponents
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/directaccessclientcomponents/remove-daentrypointtableitem?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DAEntryPointTableItem
---

# 移除 DA 入口表项

## 摘要
从指定的配置存储中删除一个 DirectAccess 入口点。

## 语法

### ByPolicyStore（默认值）
```
Remove-DAEntryPointTableItem [-EntryPointName <String[]>] -PolicyStore <String> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ByGpoSession
```
Remove-DAEntryPointTableItem [-EntryPointName <String[]>] -GPOSession <String> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Remove-DAEntryPointTableItem -InputObject <CimInstance[]> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DAEntryPointTableItem` cmdlet 用于从指定的配置存储中删除 DirectAccess 入口点。您必须指定配置存储（可以使用 `GPOSession` 或 `PolicyStore`）以及要删除的入口点的名称。

## 示例

### 示例 1：使用管道删除入口点
```
PS C:\> Get-DAEntryPointTableItem -EntryPointName "Redmond" -PolicyStore "Contoso\GPO1" | Remove-DAEntryPointTableItem
```

这个 cmdlet 首先使用 `Get-DAEntryPointTableItem` 获取名为 “Redmond” 的入口点信息，然后将这些信息传递给 `Remove-DA EntryPointTableItem` 来删除该入口点。

### 示例 2：直接删除入口点
```
PS C:\>Remove-DAEntryPointTableItem -EntryPointName "Redmond" -PolicyStore "Contoso\GPO1"
```

此cmdlet通过指定*EntryPointName*和*PolicyStore*参数来删除名为“Redmond”的入口点。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中操作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。您可以输入一台计算机的名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定要删除的入口点的名称。此参数支持通配符。

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
指定用于读取配置信息的组策略会话。您可以将 *GPOSession* 与 *NetGPO* 命令集结合使用，以便汇总对某个组策略对象执行的多个操作。

*GPOSession* 不能与 *PolicyStore* 同时使用。

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

### -InputObject
指定在管道命令中使用的输入对象。

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
该cmdlet会将交互式窗口中的项目作为输入发送到其他cmdlets中。默认情况下，这个cmdlet不会生成任何输出。不过，若要将交互式窗口中的项目发送到其他cmdlets，请先点击以选择这些项目，然后点击“确定”。同时支持使用Shift键或Ctrl键进行选择操作。

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
指定 cmdlet 从哪个策略存储库中检索入口点信息。

要从组策略对象（Group Policy Object）中检索入口点信息，请使用“Domain\GPOName”的格式指定GPO名称。

要从计算机的本地组策略对象（Local Group Policy Object，简称GPO）中检索入口点信息，请以“GPO:\<计算机名称\>”的格式指定该本地GPO的名称。

*PolicyStore* 不能与 *GPOSession* 同时使用。

*PolicyStore* 的默认值是 ActiveStore。

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

### -ThrottleLimit
该参数用于指定可以同时运行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前正在运行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet被运行时会发生什么情况。但实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/StandardCimv2/MSFT_DASiteTableEntry
此cmdlet接受一个CIM对象作为输入，该对象包含一个DA站点表条目。

## 输出

### 无

## 备注

## 相关链接

[Get-DAEntryPointTableItem](./Get-DAEntryPointTableItem.md)

[New-DAEntryPointTableItem](./New-DAEntryPointTableItem.md)

[Rename-DA EntryPointTableItem](./Rename-DAEntryPointTableItem.md)

[Reset-DA EntryPointTableItem](./Reset-DAEntryPointTableItem.md)

[Set-DA EntryPointTableItem](./Set-DAEntryPointTableItem.md)

