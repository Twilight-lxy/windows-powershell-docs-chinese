---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/convertfrom-dfsrguid?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: ConvertFrom-DfsrGuid
---

# 将DFSR GUID转换为其他格式

## 摘要
将给定复制组中的GUID转换为友好的名称（即易于理解的字符串）。

## 语法

```
ConvertFrom-DfsrGuid [-GroupName] <String[]> [-Guid] <Guid[]> [[-DomainName] <String>] [<CommonParameters>]
```

## 描述
`ConvertFrom-DfsrGuid` cmdlet 可以将分布式文件系统（DFS）复制中的 GUID 转换为给定复制组内的友好名称。DFS 复制使用 GUID 来表示各种对象和元数据的友好名称。DFS 复制会将这些 GUID 写入 Active Directory、XML 文件、事件日志以及调试日志中。该 cmdlet 可以转换以下类型的 GUID：连接（connid）、复制的文件夹（csid）、复制组（rgid）、卷（volumeid）、成员（memberid）以及数据库（dbguid）。

## 示例

### 示例 1：将 GUID 转换为友好的名称
```
PS C:\> ConvertFrom-DfsrGuid -GroupName RG01 -Guid 9268F23A-7701-4184-8B8B-4BFDBB8AC411

GroupName              : RG01
FolderName             : RF01
DomainName             : corp.contoso.com
Identifier             : 9268f23a-7701-4184-8b8b-4bfdbb8ac411
Description            :
FileNameToExclude      : {~*, *.bak, *.tmp}
DirectoryNameToExclude : {}
DfsnPath               :
IsDfsnPathPublished    : False
```

此命令使用 **ConvertFrom-DfsrGuid** cmdlet 将复制的文件夹的 GUID 转换为其友好的显示形式（即更易于理解的名称或描述）。

### 示例 2：确定哪个服务器进行了文件修改
```
PS C:\> Get-DfsrIdRecord -Path C:\rf01\canary.bmp | Format-List global* GlobalVersionSequenceNumber : {B34A6F21-A20D-402D-9BE1-467309C21CDF}-v20
PS C:\> ConvertFrom-DfsrGuid -GroupName Rg01 -guid B34A6F21-A20D-402D-9BE1-467309C21CDF

ComputerName : SRV01
DomainName   : corp.contoso.com
VolumeGuid   : 9ee0fc3b-a906-11e2-8f95-806e6f6e6963
SerialNumber : 903727946
Path         : \\.\C:
DatabaseGuid : B34A6F21-A20D-402D-9BE1-467309C21CDF
```

这个示例首先查找一个文件的全球版本序列号（GUID），然后再查找发起该更改的服务器名称。

第一个命令使用了 **Get-DfsrIdRecord** cmdlet 来查找文件的全球版本序列号（GUID）。

第二个命令用于查找发起该更改的服务器。

## 参数

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果您不指定此参数，该 cmdlet 将使用当前用户的域。

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
指定一个复制组名称的数组。如果不指定此参数，该cmdlet将会查询所有参与复制的组。您可以使用逗号分隔的列表以及通配符（*）。

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

### -Guid
指定一个 GUID 值数组，将其转换为友好的名称（即易于理解的字符串）。

```yaml
Type: Guid[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

### System.Guid

## 输出

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

### Microsoft.DistributedFileSystemReplication.DfsReplicatedFolder

### Microsoft.DistributedFileSystemReplication.DfsrMember

### Microsoft.DistributedFileSystemReplication.DfsrMembership

### Microsoft.DistributedFileSystemReplication.DfsrConnection

### Microsoft.DistributedFileSystemReplication.DfsrVolume

## 备注

## 相关链接
