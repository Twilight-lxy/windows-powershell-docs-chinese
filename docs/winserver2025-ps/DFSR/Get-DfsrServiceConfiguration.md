---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/get-dfsrserviceconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsrServiceConfiguration
---

# Get-DfsrServiceConfiguration

## 摘要
获取群组成员上DFS复制服务的设置信息。

## 语法

```
Get-DfsrServiceConfiguration [[-ComputerName] <String[]>] [<CommonParameters>]
```

## 描述
`Get-DfsrServiceConfiguration` cmdlet 可以获取分布式文件系统（DFS）复制服务在复制组成员上的相关设置。复制组的成员会托管被复制的文件夹。使用此 cmdlet 可以查看与清理操作、调试日志记录以及意外关机时的自动恢复功能相关的设置。

## 示例

### 示例 1：获取本地计算机的 DFS 复制服务设置
```
PS C:\> Get-DfsrServiceConfiguration
ComputerName                      : SRV01
RPCPort                           :
DynamicRPCPort                    : True
DisableDebugLog                   : False
MaximumDebugLogFiles              : 1000
DebugLogPath                      : C:\Windows\debug
DebugLogSeverity                  : 4
MaximumDebugLogMessages           : 200000
UnexpectedAutoRecovery            : False
CleanupStagingFolderAtPercent     : 90
CleanupStagingFolderUntilPercent  : 60
CleanupConflictFolderAtPercent    : 90
CleanupConflictFolderUntilPercent : 60
```

这个命令用于获取本地计算机的DFS复制服务设置。

## 参数

### -ComputerName
指定一组复制成员计算机的名称。您可以使用逗号分隔的列表以及通配符（*）。如果您不指定此参数，该 cmdlet 将使用当前计算机。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: MemberList, MemList

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 字符串

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrServiceConfiguration

## 备注

## 相关链接

[Set-DfsrServiceConfiguration](./Set-DfsrServiceConfiguration.md)

