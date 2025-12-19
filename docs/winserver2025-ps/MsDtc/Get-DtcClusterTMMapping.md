---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DtcClusterTMMappingTask_v1.0.cdxml-help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/get-dtcclustertmmapping?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DtcClusterTMMapping
---

# Get-DtcClusterTMMapping

## 摘要
获取集群DTC映射数据。

## 语法

```
Get-DtcClusterTMMapping [-Name <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-DtcClusterTMMapping` cmdlet 用于获取集群的分布式事务协调器（DTC）映射数据。如果您没有指定 `Name` 参数，该 cmdlet 将获取所有集群事务管理器（TM）的映射数据。此 cmdlet 仅支持在集群计算机上使用。

## 示例

### 示例 1：获取集群映射信息
```
PS C:\> Get-DtcClusterTMMapping -Name "TestMapping"
```

这个示例获取了名为 **MappingName** 的 TestMapping 的集群 DTC（数据传输控制）到 TM（转换模块）的映射关系。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个代表该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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

### -Name
指定 **MappingName**。如果您不指定此参数，该 cmdlet 将获取所有的 TM 映射关系。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### DtcClusterTMMapping
此cmdlet返回一个**DtcClusterTMMapping**对象，其中包含指定的**MappingName**值。如果您没有指定**MappingName**，则此cmdlet会获取所有映射信息。

## 备注

## 相关链接

[Add-DtcClusterTMMapping](./Add-DtcClusterTMmapping.md)

[Remove-DtcClusterTMMapping](./Remove-DtcClusterTMMapping.md)

[Set-DtcClusterTMMapping](./Set-DtcClusterTMMapping.md)

