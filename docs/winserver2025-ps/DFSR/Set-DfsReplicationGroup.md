---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/set-dfsreplicationgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DfsReplicationGroup
---

# Set-DfsReplicationGroup

## 摘要
修改一个复制组。

## 语法

```
Set-DfsReplicationGroup [-GroupName] <String[]> [[-Description] <String>] [[-DomainName] <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DfsReplicationGroup` cmdlet 用于修改现有复制组的配置。

复制组是一组服务器或成员，它们共同参与一个或多个文件夹的复制过程。被复制的文件夹会在复制组的各个成员之间保持同步状态。此命令无法修改资源组的带宽设置或调度计划。

## 示例

### 示例 1：修改复制组配置
```
PS C:\> Set-DfsReplicationGroup -GroupName "RG01" -Description "Contoso Branch Office Data Collection for Backups"

GroupName              : RG01
DomainName             : corp.contoso.com
Identifier             : 1f06f8d4-a0ae-4221-99d2-0bd1bb27882b
UseScheduleInLocalTime : True
UseScheduleInUtc       : False
Description            : Contoso Branch Office Data Collection for Backups
```

此命令用于修改名为 RG01 的复制组的描述信息。

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
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果未指定此参数，cmdlet 将使用当前域。

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
指定一个复制组名称的数组。如果不指定此参数，该cmdlet将查询所有参与的复制组。您可以使用逗号分隔的列表以及通配符（*）。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 输出

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 备注

## 相关链接

[Get-DfsReplicationGroup](./Get-DfsReplicationGroup.md)

[New-DfsReplicationGroup](./New-DfsReplicationGroup.md)

[Remove-DfsReplicationGroup](./Remove-DfsReplicationGroup.md)

