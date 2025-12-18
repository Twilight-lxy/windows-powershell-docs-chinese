---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/get-dfsrstate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsrState
---

# Get-DfsrState

## 摘要
获取某个成员的DFS复制状态。

## 语法

```
Get-DfsrState [[-ComputerName] <String>] [<CommonParameters>]
```

## 描述
`Get-DfsrState` cmdlet 可以获取计算机在其复制组伙伴方面的分布式文件系统（DFS）复制状态。该 cmdlet 会返回传入和传出的文件复制信息，例如当前正在复制的文件以及接下来即将被复制的文件。

## 示例

### 示例 1：获取某个成员的 DFS 复制状态
```
PS C:\> Get-DfsrState -ComputerName "SRV02" | Format-Table FileName,UpdateState,Inbound,Source* -Auto -Wrap


FileName                   UpdateState Inbound SourceComputerName
--------                   ----------- ------- ------------------
ntfrs - Copy.exe             Scheduled    True SRV02
ntdsai - Copy.dll            Scheduled    True SRV02
NlsLexicons0046 - Copy.dll   Scheduled    True SRV02
NlsLexicons000a - Copy.dll Downloading    True SRV02
occache - Copy.dll           Scheduled    True SRV02
NlsModels0011 - Copy.dll     Scheduled    True SRV02
NlsLexicons0007 - Copy.dll   Scheduled    True SRV02
NlsLexicons000f - Copy.dll Downloading    True SRV02
NlsLexicons003e - Copy.dll   Scheduled    True SRV02
NlsLexicons0045 - Copy.dll   Scheduled    True SRV02
NlsData001a - Copy.dll     Downloading    True SRV02
ntlanui2 - Copy.dll          Scheduled    True SRV02
```

这个命令可以获取当前正在从名为SRV02的计算机复制文件或排队进行入站/出站复制的文件列表。

## 参数

### -ComputerName
指定复制成员计算机的名称。如果您不指定此参数，该cmdlet将使用当前计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Member, Mem

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 字符串

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrUpdate

## 备注

## 相关链接

[Get-DfsReplicationGroup](./Get-DfsReplicationGroup.md)

