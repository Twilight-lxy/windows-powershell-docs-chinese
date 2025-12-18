---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/set-dfsrmember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DfsrMember
---

# Set-DfsrMember

## 摘要
修改复制组中成员计算机的信息。

## 语法

```
Set-DfsrMember [-GroupName] <String[]> [-ComputerName] <String[]> [[-Description] <String>]
 [[-DomainName] <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DfsrMember` cmdlet 用于修改复制组中成员计算机的信息。复制组的成员会托管被复制的文件夹，你可以更改这些成员的计算机描述（即相关属性）。

## 示例

#### 示例 1：更新成员的描述
```
PS C:\> Set-DfsrMember -GroupName "RG07" -Member "SRV01" -Description "Waukegan Branch Office Server"
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
IsClusterNode                : True
State                        : Normal
```

此命令用于更新名为RG07的组中名为SRV01的计算机的描述信息。控制台会显示**DfsrMember**对象，其中包含更新后的描述内容。

## 参数

### -ComputerName
指定一组成员计算机的名称。你可以使用逗号分隔的列表以及通配符（*）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: MemberList, MemList

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
```

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

### -Description
为成员计算机指定一个描述信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果不指定此参数，cmdlet 将使用当前用户的域。

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

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

### 字符串（String）

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrMember

## 备注

## 相关链接

[Add-DfsrMember](./Add-DfsrMember.md)

[Get-DfsrMember](./Get-DfsrMember.md)

[Remove-DfsrMember](./Remove-DfsrMember.md)
