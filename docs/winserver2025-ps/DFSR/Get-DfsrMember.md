---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/get-dfsrmember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsrMember
---

# Get-DfsrMember

## 摘要
获取复制组中的成员计算机。

## 语法

```
Get-DfsrMember [[-GroupName] <String[]>] [[-ComputerName] <String[]>] [[-DomainName] <String>]
 [<CommonParameters>]
```

## 描述
`Get-DfsrMember` cmdlet 可以获取复制组中的成员计算机。复制组的成员计算机会托管被复制的文件夹。

## 示例

#### 示例 1：获取复制组中的一个成员
```
PS C:\> Get-DfsrMember -GroupName "RG07" -ComputerName "SRV01"

GroupName                    : RG07
ComputerName                 : SRV01
DomainName                   : corp.contoso.com
Identifier                   : 5ddc94cd-1602-477d-9e50-a66af5892b67
Description                  : Waukegan Branch Office Server
DnsName                      : SRV01.corp.contoso.com
Site                         : Default-First-Site-Name
NumberOfConnections          : 2
NumberOfInboundConnections   : 1
NumberOfOutboundConnections  : 1
NumberOfInterSiteConnections : -2
NumberOfIntraSiteConnections : 2
IsClusterNode                : False
State                        : Normal
```

这个命令用于获取名为 SRV01 的成员计算机，该计算机属于名为 RG07 的组。

## 参数

### -ComputerName
指定一组成员计算机的名称。您可以使用逗号分隔的列表以及通配符（*）。如果您不指定此参数，该cmdlet将获取通过**DomainName**和**GroupName**参数指定的所有复制组的成员。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: MemberList, MemList

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
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

### -GroupName
指定一个复制组名称的数组。您可以使用逗号分隔的列表以及通配符（*）。如果您不指定此参数，该cmdlet将使用所有参与的复制组。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrMember

## 备注

## 相关链接

[Add-DfsrMember](./Add-DfsrMember.md)

[Remove-DfsrMember](./Remove-DfsrMember.md)

[Set-DfsrMember](./Set-DfsrMember.md)

