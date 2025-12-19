---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/get-wmsuser?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WmsUser
---

# Get-WmsUser

## 摘要
获取本地用户账户信息。

## 语法

### getUsers
```
Get-WmsUser -Name <String> [-Server <String>] [<CommonParameters>]
```

### getAllUsers
```
Get-WmsUser [-All] [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-WmsUser` cmdlet 可以获取指定用户或所有用户的本地用户账户信息。

## 示例

### 示例 1：获取所有本地用户账户信息
```
PS C:\> Get-WmsUser -All
Name         : Administrator
Password     :
FullName     :
Description  : Built-in account for administering the computer/domain
UserType     : Administrator
ComputerName : Test1
Name         : Guest
Password     :
FullName     :
Description  : Built-in account for guest access to the computer/domain
UserType     : Standard
ComputerName : Test1
```

这个命令可以获取所有本地用户账户的信息。

## 参数

### -All
表示此操作适用于目标主机上的所有会话。

```yaml
Type: SwitchParameter
Parameter Sets: GetAllUsers
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要获取的用户名称。

```yaml
Type: String
Parameter Sets: GetUser
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定该命令的目标（即MultiPoint Server）的完全限定主机名。默认值为localhost。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ComputerName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### WmsUser

这个cmdlet将一个**WmsUser**集合作为**PSObject**集合返回。

## 备注

## 相关链接

[New-WmsUser](New-WmsUser.md)

[Remove-WmsUser](Remove-WmsUser.md)

[Set-WmsUser](Set-WmsUser.md)
