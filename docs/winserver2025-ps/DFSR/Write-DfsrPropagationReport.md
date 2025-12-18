---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/write-dfsrpropagationreport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Write-DfsrPropagationReport
---

# 编写 DfsrPropagationReport 报告

## 摘要
为复制组中的传播测试文件生成报告。

## 语法

```
Write-DfsrPropagationReport [-GroupName] <String[]> [-FolderName] <String[]> [-ReferenceComputerName] <String>
 [[-Path] <String>] [[-FileCount] <Int32>] [[-DomainName] <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Write-DfsrPropagationReport` cmdlet 用于生成复制组中传播测试文件复制进度的报告。需要指定复制组、被复制的文件夹以及作为参考计算机的成员计算机。

该cmdlet会创建名为`Propagation-\<RG Name\>-\<Date\>-\<Time\>.html`和`Propagation-\<RG Name\>-\<Date\>-\<Time\>.xml`的文件。您可以指定一个文件夹来保存这些文件，或者使用当前的工作目录。

使用 **Start-DfsrPropagationTest** cmdlet 来创建一个传播测试文件。

## 示例

### 示例 1：为特定组和复制的文件夹创建传播报告
```
PS C:\> Write-DfsrPropagationReport -GroupName "RG01" -FolderName "RF22" -ReferenceComputerName "SRV01" -Path "C:\Reports"
```

此命令会在 C:\Reports 文件夹中生成一份传播报告（该报告以 HTML 和 XML 格式保存）。命令指定了 SRV01 作为参考计算机，并指明了组名和文件夹名称。

### 示例 2：使用通配符为所有组和复制的文件夹生成传播报告
```
PS C:\> Write-DfsrPropagationReport -GroupName * -FolderName * -ReferenceComputerName "SRV01" -Verbose
VERBOSE: Performing operation "Write-DfsrPropagationReport" on Target "DFSR membership with domain: corp.contoso.com;
replication group: RG 1; replicated folder: RF 1; computer: SRV01; GUID: {966e2e84-7792-438f-8344-c8f76d214d06}.".
VERBOSE: Successfully saved the propagation report for DFSR membership with domain: corp.contoso.com; replication
group: RG 1; replicated folder: RF 1; computer: SRV01; GUID: {966e2e84-7792-438f-8344-c8f76d214d06}. The XML file is
located here: "C:\Propagation-RG 1-RF 1-04Apr2013-2109.xml". The HTML file is located here: "C:\Propagation-RG 1-RF
1-04Apr2013-2109.html".
VERBOSE: Performing operation "Write-DfsrPropagationReport" on Target "DFSR membership with domain: corp.contoso.com;
replication group: Branch Office 1; replicated folder: Data Distribution 1; computer: SRV01; GUID:
{dbaa3a16-f731-4428-8a4f-8278673e848a}.".
VERBOSE: Successfully saved the propagation report for DFSR membership with domain: corp.contoso.com; replication
group: Branch Office 1; replicated folder: Data Distribution 1; computer: SRV01; GUID:
{dbaa3a16-f731-4428-8a4f-8278673e848a}. The XML file is located here: "C:\Propagation-Branch Office 1-Data Distribution
1-04Apr2013-2109.xml". The HTML file is located here: "C:\Propagation-Branch Office 1-Data Distribution
1-04Apr2013-2109.html".
```

该命令为所有复制组中的所有已复制文件夹生成传播报告，在使用通配符（*）作为**GroupName**和**FolderName**参数时实现了这一功能。该命令指定SRV01作为参考计算机，并通过设置**Verbose**参数将相关信息显示在控制台上。

## 参数

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

### -FileCount
指定用于生成报告的最新生成的传播测试文件的数量。如果您不指定此参数，该 cmdlet 将使用所有文件。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FolderName
用于指定一组已复制文件夹的名称。如果不指定此参数，该 cmdlet 将适用于所有参与复制的文件夹。你可以使用逗号分隔的列表，并使用通配符（*）。

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
指定一个复制组名称的数组。如果您不指定此参数，该cmdlet将应用于所有参与的复制组。您可以使用逗号分隔的列表以及通配符（*）。

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

### -Path
指定报告文件的存储文件夹。如果未指定此参数，cmdlet 将使用当前的工作目录。

```yaml
Type: String
Parameter Sets: (All)
Aliases: FilePath

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReferenceComputerName
指定复制组中参考计算机的名称。该cmdlet会将来自此参考计算机的复制测试文件与复制组中其他所有成员的测试文件进行比较。如果您未指定此参数，cmdlet将使用当前计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ReferenceMember, RefMem

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

### Microsoft.DistributedFileSystemReplication.DfsReplicatedFolder

### 字符串

## 输出

### 无

## 备注

## 相关链接

[Remove-DfsrPropagationTestFile](./Remove-DfsrPropagationTestFile.md)

[Start-DfsrPropagationTest](./Start-DfsrPropagationTest.md)

