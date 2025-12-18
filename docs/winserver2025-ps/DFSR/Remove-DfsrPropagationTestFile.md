---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/remove-dfsrpropagationtestfile?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DfsrPropagationTestFile
---

# 删除 DfsrPropagationTestFile 文件

## 摘要
删除DFS复制传播测试文件。

## 语法

```
Remove-DfsrPropagationTestFile [-GroupName] <String[]> [-FolderName] <String[]> [[-ComputerName] <String>]
 [-AgeInDays] <UInt32> [-Force] [[-DomainName] <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DfsrPropagationTestFile` cmdlet 用于从分布式文件系统（DFS）复制文件夹中删除测试文件。一旦您从一个复制组中的成员计算机上删除了某个文件，DFS Replication 会自动将该文件从所有其他成员计算机上也删除掉。要创建测试文件，请使用 `Start-DfsrPropagationTest` cmdlet。

测试文件仅包含测试元数据。您可以在任何时候删除它们。

## 示例

### 示例 1：从指定的复制文件夹中删除所有测试文件
```
PS C:\> Remove-DfsrPropagationTestFile -GroupName "RG01" -FolderName "RF07" -ComputerName "SRV01" -AgeInDays 0
This operation will remove the propagation test files from the computer named "SRV01" that are more than 0 days old.
Are you sure you want to continue to remove this propagation test file?
[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):
```

此命令会从名为 SRV01 的计算机上的 RF07 文件夹中删除所有与传播测试相关的文件。该计算机属于名为 RG01 的组。*AgeInDays* 参数的值为 0（零），这意味着无论这些测试文件是何时创建的，该命令都会将它们全部删除。由于此命令没有包含 *Force* 参数，因此您必须确认是否真的要执行删除操作。

## 参数

### -AgeInDays
指定用于删除的传播测试文件的年龄（以天为单位）。如果要删除过去24小时内创建的传播文件，或者要删除所有传播测试文件，请将此值设置为零（0）。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定复制成员计算机的名称。如果您不指定此参数，该 cmdlet 将使用当前的计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Member, Mem

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
```

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果未指定此参数，cmdlet 将使用当前用户的域。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 100
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -FolderName
指定一个包含已复制文件夹名称的数组。你可以使用逗号分隔的列表以及通配符（*）。如果未指定此参数，该cmdlet将从所有已复制的文件夹中删除测试文件。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RF, RfName

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
```

### -Force
强制命令运行，而无需请求用户确认。

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

### -GroupName
指定一个复制组名称的数组。你可以使用逗号分隔的列表以及通配符（*）。如果你不指定此参数，该cmdlet将从指定域内的所有组的复制文件夹中删除测试文件。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RG, RgName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
```

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

### Microsoft.DistributedFileSystemReplication.DfsReplicatedFolder

### 字符串

## 输出

### 无

## 备注

## 相关链接

[Start-DfsrPropagationTest](./Start-DfsrPropagationTest.md)

[Write-DfsrPropagationReport](./Write-DfsrPropagationReport.md)
