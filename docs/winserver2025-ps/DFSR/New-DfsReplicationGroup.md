---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/new-dfsreplicationgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-DfsReplicationGroup
---

# 新DFS复制组

## 摘要
创建一个复制组。

## 语法

```
New-DfsReplicationGroup [-GroupName] <String[]> [[-Description] <String>] [[-DomainName] <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`New-DfsReplicationGroup` cmdlet 用于创建一个复制组。复制组是由一组服务器组成的集合，这些服务器参与一个或多个文件夹的复制过程。被复制的文件夹会在复制组的成员之间保持同步状态。此 cmdlet 无法修改资源组的带宽或调度设置。

## 示例

### 示例 1：创建一个复制组
```
PS C:\> New-DfsReplicationGroup -GroupName "RG01"

GroupName              : RG01
DomainName             : corp.contoso.com
Identifier             : 81251362-e30f-4c1e-b6b0-23906c1ebdd7
Description            :
State                  : Normal
```

该命令创建了一个名为RG01的复制组。

#### 示例 2：创建复制拓扑结构
```
PS C:\> New-DfsReplicationGroup -GroupName "Branch Office 1" | New-DfsReplicatedFolder -FolderName "Data Distribution 1" | Add-DfsrMember -ComputerName "SRV01","SRV02","SRV03" | Format-Table dnsname,groupname -auto -wrap

DnsName               GroupName
-------               ---------
SRV01.corp.contoso.com Branch Office 1
SRV02.corp.contoso.com Branch Office 1
SRV03.corp.contoso.com Branch Office 1

PS C:\> Add-DfsrConnection -GroupName "Branch Office 1" -SourceComputerName "SRV01" -DestinationComputerName "SRV02" | Format-Table *name -wrap -autosize

GroupName       SourceComputerName DestinationComputerName
---------       ------------------ -----------------------
Branch Office 1 SRV01               SRV02
Branch Office 1 SRV02               SRV01

PS C:\> Add-DfsrConnection -GroupName "Branch Office 1" -SourceComputerName "SRV01" -DestinationComputerName "SRV03" | Format-Table *name -wrap -autosize

GroupName       SourceComputerName DestinationComputerName
---------       ------------------ -----------------------
Branch Office 1 SRV01               SRV03
Branch Office 1 SRV03               SRV01

PS C:\> Set-DfsrMembership -GroupName "Branch Office 1" -FolderName "Data Distribution 1" -ContentPath "C:\Rf01" -ComputerName "SRV01" -PrimaryMember $True -StagingPathQuotaInMB 16384 -Force | Format-Table *name,*path,primary* -autosize -wrap

DomainName       GroupName       FolderName          ComputerName ContentPath StagingPath                PrimaryMember
----------       ---------       ----------          ------------ ----------- -----------                -------------
corp.contoso.com Branch Office 1 Data Distribution 1 SRV01         c:\Rf01      c:\Rf01\DfsrPrivate\Staging          True

PS C:\> Set-DfsrMembership -GroupName "Branch Office 1" -FolderName "Data Distribution 1" -ContentPath "C:\Rf01" -ComputerName "SRV02","SRV03" -StagingPathQuotaInMB 16384 -Force | Format-Table *name,*path,primary* -autosize -wrap

DomainName       GroupName       FolderName          ComputerName ContentPath StagingPath                PrimaryMember
----------       ---------       ----------          ------------ ----------- -----------                -------------
corp.contoso.com Branch Office 1 Data Distribution 1 SRV02         c:\Rf01      c:\Rf01\DfsrPrivate\Staging         False
corp.contoso.com Branch Office 1 Data Distribution 1 SRV03         c:\Rf01      c:\Rf01\DfsrPrivate\Staging         False
```

这个示例创建了一个复制拓扑结构，其中包含一个上游服务器和两个下游服务器。

第一个命令使用 **New-DfsReplicationGroup** cmdlet 创建一个名为 “Branch Office 1” 的复制组。该命令将输出结果传递给 **New-DfsReplicatedFolder** cmdlet，以创建一个名为 “Data Distribution 1” 的复制备份文件夹。接着，该命令将输出结果再次传递给 **Add-DfsrMember** cmdlet，用于添加成员服务器 SRV01、SRV02 和 SRV03。最后，该命令将整个处理流程的输出结果格式化为表格形式。

第二个命令使用了 **Add-DfsrConnection** cmdlet，在服务器 SRV01 和 SRV02 之间建立双向连接。

第三个命令使用了 **Add-DfsrConnection** cmdlet 来在 SRV01 和 SRV03 服务器之间建立双向连接。

第四条命令使用 **Set-DfsrMembership** cmdlet 将 SRV01 设置为主要成员。

第五条命令使用了 **Set-DfsrMembership** cmdlet 来设置 SRV02 和 SRV03 服务器的成员身份。

## 参数

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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

### -Description
为复制组指定一个描述。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果不指定此参数，cmdlet 将使用当前域。

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

### -GroupName
指定一个复制组名称的数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RG, RgName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 输出

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 备注

## 相关链接

[Get-DfsReplicationGroup](./Get-DfsReplicationGroup.md)

[Remove-DfsReplicationGroup](./Remove-DfsReplicationGroup.md)

[Set-DfsReplicationGroup](./Set-DfsReplicationGroup.md)

[Suspend-DfsReplicationGroup](./Suspend-DfsReplicationGroup.md)

[Sync-DfsReplicationGroup](./Sync-DfsReplicationGroup.md)

