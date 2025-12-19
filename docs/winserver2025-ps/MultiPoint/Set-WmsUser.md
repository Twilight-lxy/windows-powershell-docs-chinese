---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/set-wmsuser?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WmsUser
---

# Set-WmsUser

## 摘要
修改Windows多点服务器用户账户的信息。

## 语法

### 使用用户名（UseUserName）
```
Set-WmsUser [-Name] <String> [-FullName <String>] [-Description <String>] [-UserType <UserTypePS>]
 [-Server <String>] [<CommonParameters>]
```

### UseCreds
```
Set-WmsUser [-Credential] <PSCredential> [-FullName <String>] [-Description <String>] [-UserType <UserTypePS>]
 [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-WmsUser` cmdlet 用于更新当前 Windows MultiPoint Server 系统中的本地用户信息。

## 示例

### 示例 1
```
PS C:\> Set-WmsUser -Name "Student01" -Description "New Student" -FullName "Patti Fuller"
```

该命令用于更新用户账户的信息：将账户描述设置为“新学生”，用户名设置为“Student01”，全名设置为“Patti Fuller”。

## 参数

### -Credential
指定一个 **PSCredential** 对象。可以使用 **Get-Credential** cmdlet 来获取一个 **PSCredential** 对象。

```yaml
Type: PSCredential
Parameter Sets: UseCreds
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Description
指定一个描述（description）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
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
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
为用户指定一个名称。

```yaml
Type: String
Parameter Sets: UseUserName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定该命令的目标（即MultiPoint Server）的完全限定主机名。默认值为“localhost”。

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

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Get-WmsUser](Get-WmsUser.md)

[New-WmsUser](New-WmsUser.md)

[Remove-WmsUser](Remove-WmsUser.md)
