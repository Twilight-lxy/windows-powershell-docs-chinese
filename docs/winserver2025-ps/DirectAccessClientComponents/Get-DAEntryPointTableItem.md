---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DASiteTableEntry.cdxml-help.xml
Module Name: DirectAccessClientComponents
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/directaccessclientcomponents/get-daentrypointtableitem?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DAEntryPointTableItem
---

# Get-DAEntryPointTableItem

## 摘要
获取已为 DirectAccess 配置的所有入口点的列表。

## 语法

### ByPolicyStore（默认值）
```
Get-DAEntryPointTableItem [-EntryPointName <String[]>] [-State <State[]>] [-PolicyStore <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByGpoSession
```
Get-DAEntryPointTableItem [-EntryPointName <String[]>] [-State <State[]>] [-GPOSession <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DAEntryPointTableItem` cmdlet 可以获取为 DirectAccess 配置的入口点列表。这些入口点包含有关用于连接的 IP 地址、IP-HTTPs 配置文件以及其他支持多站点 DirectAccess 连接性的元素的信息。

你可以使用 **Get-DA EntryPointTableItem** 来从组策略对象或本地计算机的活动存储中检索该列表。

## 示例

#### 示例 1：获取一组不处于活动状态的入口点列表
```
PS C:\> Get-DAEntryPointTableItem -PolicyStore "ActiveStore" -EntryPointName "Redmond" -State "NotSelected"
```

这个cmdlet从当前激活的存储中获取入口点的列表，并筛选该列表，仅显示那些未处于激活状态的入口点。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，也可以输入会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -EntryPointName
指定入口点的名称。入口点名称通常是该地点的友好称呼，例如“Redmond”（雷德蒙德）或“Paris”（巴黎）。

使用双引号 (“”) 指定入口点的名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -GPOSession
指定用于发送配置信息的组策略会话。您可以将 *GPOSession* 与 **NetGPO** cmdlet 结合使用，以汇总对某个组策略对象执行的多个操作。

*GPOSession* 不能与 *PolicyStore* 同时使用。

```yaml
Type: String
Parameter Sets: ByGpoSession
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PolicyStore
指定该cmdlet将入口点添加到的策略存储位置。

要将入口点添加到组策略对象（Group Policy Object）中，请使用“Domain\GPOName”的格式指定该GPO的名称。

要将入口点信息添加到计算机的本地组策略对象（Local Group Policy Object，简称GPO）中，请以“GPO:\<计算机名称\>”的格式指定该计算机的本地GPO名称。

*PolicyStore* 不能与 *GPOSession* 同时使用。

*PolicyStore* 的默认值是 ActiveStore。

```yaml
Type: String
Parameter Sets: ByPolicyStore
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -State
此参数已过时（不再被推荐使用）。

```yaml
Type: State[]
Parameter Sets: (All)
Aliases:
Accepted values: NotSelected, AutomaticallySelected, ManuallySelected

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值为`0`，那么Windows PowerShell®将根据计算机上正在运行的CIM cmdlet的数量来计算出一个最优的节流限制（即允许同时执行的操作数量）。这个节流限制仅适用于当前的cmdlet，而不适用于整个会话或整台计算机。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance  
Microsoft.Management Infrastructure.CimInstance#root/StandardCimv2/MSFT_DASiteTableEntry
此cmdlet返回一个CIM对象，其中包含DA入口点表项的信息。

## 备注

## 相关链接

[New-DA EntryPointTableItem](./New-DAEntryPointTableItem.md)

[Reset-DA EntryPointTableItem](./Reset-DAEntryPointTableItem.md)

[ Rename-DA EntryPointTableItem](./Rename-DAEntryPointTableItem.md)

[Remove-DAEntryPointTableItem](./Remove-DAEntryPointTableItem.md)

[Set-DAEntryPointTableItem](./Set-DAEntryPointTableItem.md)

