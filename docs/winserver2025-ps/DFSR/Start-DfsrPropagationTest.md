---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/start-dfsrpropagationtest?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-DfsrPropagationTest
---

# 启动 DfsrPropagationTest

## 摘要
在复制的文件夹中创建一个用于测试数据传播的文件。

## 语法

```
Start-DfsrPropagationTest [[-GroupName] <String[]>] [-FolderName] <String[]> [-ReferenceComputerName] <String>
 [[-DomainName] <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Start-DfsrPropagationTest` cmdlet 会在分布式文件系统（DFS）的复制文件夹中创建一个用于测试文件传播功能的文件。该测试文件包含元数据，例如时间和日期戳。DFS 复制服务会将此文件传播到复制组中的其他计算机上。您可以使用 `Write-DfsrPropagationReport` cmdlet 来生成相关的文件传播报告。

此cmdlet会在一个隐藏的、只读的系统文件夹（名为__DFSR_DIAGNOSTICS_TEST_FOLDER__）中，于复制的文件夹内创建测试文件。这些测试文件的名称格式为\<参考计算机名\>@\<GUID\>@\<RG名称\>-\<RF名称\>.xml。可以使用**Remove-DfsrPropagationTestFile** cmdlet来删除旧的测试文件。

## 示例

### 示例 1：在指定的参考计算机上创建一个测试文件
```
PS C:\> Start-DfsrPropagationTest -GroupName "ReplicationGroup07" -FolderName "ReplicatedFolder19" -ReferenceComputerName "SRV01.Contoso.com"
```

此命令为名为“ReplicatedFolder19”的复制文件夹创建一个用于测试传播功能的文件，该文件夹属于名为“ReplicationGroup07”的组。同时，该命令指定了参考计算机的名称。

### 示例 2：为所有复制的文件夹创建测试文件
```
PS C:\> Start-DfsrPropagationTest -GroupName * -FolderName * -ReferenceComputerName "SRV01.corp.Contoso.com" -Verbose
VERBOSE: Performing operation "Start-DfsrPropagationTest" on Target "DFSR membership with domain: corp.contoso.com;
replication group: RG 1; replicated folder: RF 1; computer: SRV01; GUID: {966e2e84-7792-438f-8344-c8f76d214d06}.".
VERBOSE: Successfully started the propagation test for DFSR membership with domain: corp.contoso.com; replication
group: RG 1; replicated folder: RF 1; computer: SRV01; GUID: {966e2e84-7792-438f-8344-c8f76d214d06}.
VERBOSE: Performing operation "Start-DfsrPropagationTest" on Target "DFSR membership with domain: corp.contoso.com;
replication group: Branch Office 1; replicated folder: Data Distribution 1; computer: SRV01; GUID:
{dbaa3a16-f731-4428-8a4f-8278673e848a}.".
VERBOSE: Successfully started the propagation test for DFSR membership with domain: corp.contoso.com; replication
group: Branch Office 1; replicated folder: Data Distribution 1; computer: SRV01; GUID:
{dbaa3a16-f731-4428-8a4f-8278673e848a}.
```

此命令会在参考计算机 SRV01.corp.Contoso.com 上的所有复制文件夹中创建测试文件。该命令使用通配符 (*) 作为 **GroupName** 和 **FolderName** 参数的值，因此它会在计算机的任何复制文件夹中创建测试文件，而不管这台计算机属于哪个或多个复制组。

## 参数

### -Confirm
在运行cmdlet之前会提示您进行确认。

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
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果未指定此参数，cmdlet 将使用当前用户的所在域。

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
指定一个包含已复制文件夹名称的数组。您可以使用逗号分隔的列表以及通配符（*）。如果您不指定此参数，该 cmdlet 将为指定组域内的所有已复制文件夹创建测试文件。

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

### -GroupName
指定一个复制组名称的数组。您可以使用逗号分隔的列表以及通配符（*）。如果您不指定此参数，该cmdlet将为所有在指定域内且名称与*FolderName*参数值匹配的已复制文件夹创建测试文件。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RG, RgName

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
```

### -ReferenceComputerName
指定复制组中参考计算机的名称。该cmdlet会在参考计算机上创建用于测试数据传播的文件。如果未指定此参数，cmdlet会使用本地计算机作为参考计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ReferenceMember, RefMem

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

### 字符串（String）

## 输出

### 无

## 备注

## 相关链接

[Remove-DfsrPropagationTestFile](./Remove-DfsrPropagationTestFile.md)

[Write-DfsrPropagationReport](./Write-DfsrPropagationReport.md)
