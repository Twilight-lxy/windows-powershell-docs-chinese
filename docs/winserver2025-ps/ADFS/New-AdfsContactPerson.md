---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/new-adfscontactperson?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-AdfsContactPerson
---

# 新的 AdFS 联系人信息

## 摘要
创建一个联系人对象。

## 语法

```
New-AdfsContactPerson [-Company <String>] [-EmailAddress <String[]>] [-GivenName <String>]
 [-TelephoneNumber <String[]>] [-Surname <String>] [<CommonParameters>]
```

## 描述
`New-AdfsContactPerson` cmdlet 用于在 ADFS 中创建一个联系人对象。

## 示例

### 示例 1：创建并发布联系人对象
```
PS C:\> $CP = New-AdfsContactPerson -EmailAddress "support@fabrikam.com"
PS C:\> Set-AdfsProperties -ContactPerson $CP
```

第一个命令创建了一个具有指定地址的联系人，并将其赋值给 $CP 变量。

第二个命令使用 **Set-AdfsProperties** cmdlet 将联系人对象发布到联邦服务（Federation Service）中。

## 参数

### -Company
指定联系人的公司名称。

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

### -EmailAddress
指定联系人的电子邮件地址数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GivenName
指定联系人的姓名。

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

### -Surname
指定联系人的姓氏。

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

### -TelephoneNumber
指定联系人的电话号码数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### MicrosoftIdentityServer POWERShell.Resources.ContactPerson
此cmdlet生成一个类结构，用于表示联邦服务中的联系人对象。

## 备注
* You can publish this contact person in the federation metadata of the Federation Service by using the **Set-AdfsProperties** cmdlet.

## 相关链接

[Get-AdfsProperties](./Get-AdfsProperties.md)

[Set-AdfsProperties](./Set-AdfsProperties.md)

