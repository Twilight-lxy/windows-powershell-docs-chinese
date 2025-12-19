---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/new-wmsuser?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-WmsUser
---

# New-WmsUser

## 摘要
修改Windows多点服务器用户账户。

## 语法

```
New-WmsUser [-Credential] <PSCredential> [-UserType] <UserTypePS> [[-FullName] <String>]
 [[-Description] <String>] [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-WmsUser` cmdlet 用于更新当前 Windows MultiPoint Server 系统中的本地用户信息。

## 示例

#### 示例 1：修改用户账户
```
PS C:\> Set-WmsUser -Name "Student01" -Description "New Student" -FullName "Patti Fuller"
```

此命令会更新一个用户账户的信息：描述设置为“新学生”，名称为“Student01”，全名为“Patti Fuller”。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个 **PSCredential** 对象。可以使用 **Get-Credential** cmdlet 来获取一个 **PSCredential** 对象。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Description
指定一个描述。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FullName
指定用户的全名。

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

### -Server
指定该命令的目标端——即多点服务器（MultiPoint Server）的完全限定主机名。默认值为“localhost”。

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

### -UserType
指定用户类型。该参数的可接受值包括：

- Administrator
- Standard
- DashboardUser

```yaml
Type: UserTypePS
Parameter Sets: (All)
Aliases:
Accepted values: Administrator, Standard, DashboardUser

Required: True
Position: 1
Default value: None
Accept pipeline input: False
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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[New-WmsUser](New-WmsUser.md)

[Remove-WmsUser](Remove-WmsUser.md)
